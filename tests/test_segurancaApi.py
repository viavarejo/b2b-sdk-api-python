import unittest
from lib.models.SegurancaDTO import SegurancaDTO
from lib.api import segurancaApi
import datetime


class TestSegurancaMethods(unittest.TestCase):

    def test_getchave_sucess(self) -> SegurancaDTO:
        dto = segurancaApi.SegurancaApi().getchave();
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(datetime.datetime(2018, 11, 28, 13, 56, 6), dto.data.dataCadastro)
