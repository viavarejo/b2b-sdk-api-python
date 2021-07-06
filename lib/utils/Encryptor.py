from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode, b64encode
from lib.api import segurancaApi


class Encryptor(object):

    chave = ''

    def encript(self, inputData: str):
        keyDER = b64decode(self.chave)
        keyPub = RSA.importKey(keyDER)
        cipher = Cipher_PKCS1_v1_5.new(keyPub)
        cipher_text = cipher.encrypt(inputData.encode())
        emsg = b64encode(cipher_text)
        return emsg

    def set_chave(self, chave: str):
        self.chave = chave

    # def encrypt_private_key(a_message, private_key):
    #     encryptor = PKCS1_OAEP.new(private_key)
    #     encrypted_msg = encryptor.encrypt(a_message)
    #     encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    #     return encoded_encrypted_msg
