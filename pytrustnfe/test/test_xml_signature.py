# coding=utf-8
'''
Created on Jun 14, 2015

@author: danimar
'''
import os
import os.path
import unittest
from lxml import etree
from pytrustnfe.nfse.assinatura import Assinatura
from pytrustnfe.nfe.assinatura import Assinatura as SignxmlSignature


class test_xml_signature(unittest.TestCase):

    caminho = os.path.dirname(__file__)

    def test_assinar_xml_valido_pyxmlsec(self):
        path = os.path.join(os.path.dirname(__file__), 'xml-nfse')
        xml_to_sign = open(os.path.join(
            path, 'nfse-paulistana.xml'), 'r').read()

        pfx_path = os.path.join(self.caminho, 'teste.pfx')
        signer = Assinatura(pfx_path, '123456')

        xml = signer.assina_xml(xml_to_sign, '')

        fw = open(os.path.join(
            path, 'nfse-paulistana-signed-xmlsec.xml'), 'w')
        fw.write(xml)
        fw.close()

    def test_assinar_xml_valido_signxml(self):
        path = os.path.join(os.path.dirname(__file__), 'xml-nfse')
        xml_to_sign = open(os.path.join(
            path, 'nfse-paulistana.xml'), 'r').read()

        pfx = open(os.path.join(self.caminho, 'teste.pfx')).read()
        signer = SignxmlSignature(pfx, '123456')

        xml = signer.assina_xml(etree.fromstring(xml_to_sign), None)

        fw = open(os.path.join(
            path, 'nfse-paulistana-signed-signxml.xml'), 'w')
        fw.write(xml)
        fw.close()
