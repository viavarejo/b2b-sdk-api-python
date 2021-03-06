import json
import urllib.request

import httplib2
import sys
import requests
import logging
import configparser
from urllib.parse import urlparse, parse_qsl, urlunparse, urljoin
import os
from urllib.request import Request, urlopen
import urllib3

try:
    from multidimensional_urlencode import urlencode
except ImportError:
    try:
        from urllib.parse import urlencode
    except ImportError:
        from urllib import urlencode



logger = logging.getLogger(__name__)

# you can set the log level to debug to see every url request
#   logger.setLevel(logging.DEBUG)

# if you want to see the log on your terminal you can use the StreamHandler:
#   sh = logging.StreamHandler()
#   logger.addHandler(sh)


class sapi(object):
    baseurl = ''
    token = ''
    mockurl = ''
    validmethods = ['GET', 'PUT', 'POST', 'DELETE', 'PATCH']
    config = configparser.ConfigParser()

    def __init__(self):
        self.connection = httplib2.Http(disable_ssl_certificate_validation=True)
        ini_path = os.path.join(os.getcwd(), 'config.ini')
        self.config.read(ini_path)
        self.baseurl = self.config.get('BASE', 'baseurl')
        self.token = self.config.get('BASE', 'token')
        self.mockurl = self.config.get('BASE', 'mockurl')



    def call(self, taxonomy, method='GET', data={}, parameters={}):

        if (method not in self.validmethods):
            self.error('Invalid HTTP-Method ' + str(method), exit=True)
        url = self.buildHttpQuery(taxonomy, parameters)
        body = json.dumps(data)
        response, content = self.connection.request(url, method, body=body, headers={'Authorization': self.token, 'Content-Type':'application/json'})
        self.connection.close()
        logger.debug('request: {}'.format(url))
        logger.debug(' * method: {}'.format(method))
        logger.debug(' * body: {}'.format(json.dumps(data, indent=2)))

        if (response['status'] == '404'):
            raise Exception("Status 404 on: " + url)

        try:
            data = json.loads(content.decode('utf-8'))
        except:
            if logger.level > logging.DEBUG:
                logger.info('request: {}'.format(url))
                logger.info(' * response: {}'.format(response))
                logger.info(' * content: {}'.format(content))
                self.error('could not load data', False)

        # Error handling
        if 'data' not in data:
            logger.info('data: {}'.format(json.dumps(data, indent=2)))
            self.error('Invalid response', exit=True)
        else:
            if 'data' in data:
                return data
            else:
                return True

    def get(self, url, data={}, params={}):
        return self.call(url, 'GET', parameters=params, data=data)

    def post(self, url, data={}, params={}):
        return self.call(url, 'POST', data, params)

    def put(self, url, data={}, params={}):
        return self.call(url, 'PUT', data, params)

    def delete(self, url, params={}):
        return self.call(url, 'DELETE', {}, params)

    def patch(self, url, data={}, params={}):
        return self.call(url, 'PATCH', data, params)

    def error(self, message, exit=False):
        logger.error(message)
        if (exit):
            sys.exit(1)

    def getFile(self, path):
        url = self.buildHttpQuery(path, {})
        if self.mockurl != '':
            url = self.mockurl + path
        return requests.get(url, allow_redirects=True, headers={'Authorization': self.token, 'Content-Type':'application/json'})



    def buildHttpQuery(self, taxonomy, parameters):
        if taxonomy.startswith('/'):
            taxonomy = taxonomy[1:]
        if not self.baseurl.endswith('/'):
            self.baseurl += '/'
        url = urljoin(self.baseurl, taxonomy)
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(parameters)

        url_parts[4] = urlencode(query)

        url = urlunparse(url_parts)
        return url