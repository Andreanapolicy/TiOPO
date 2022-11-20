import unittest
import json
from lab9.controller.ProductController import ProductController
from lab9.validator.Validator import Validator


def loadJSON(url):
    f = open(url)
    return json.load(f)


class TestShop(unittest.TestCase):
    def setUp(self):
        self.productController = ProductController()
        self.createdProducts = []
        self.data = loadJSON('data/test_data.json')
        self.defaultResponseScheme = loadJSON('schemes/default_response_scheme.json')
        self.productListResponseScheme = loadJSON('schemes/product_list.json')

    def tearDown(self):
        if len(self.createdProducts) > 0:
            for createdProduct in self.createdProducts:
                self.productController.deleteById(createdProduct)
        self.productController = None

    def test_GetAllProducts_Success(self):
        response = self.productController.getAll()
        print(response[0])

        assert Validator.validate(response, self.productListResponseScheme)
        assert len(response) > 0

    def test_CreateProduct_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)

        assert Validator.validate(response, self.defaultResponseScheme)

        assert len(self.createdProducts) == 1

    def test_DeleteProductById(self):
        assert len(self.createdProducts) == 0
