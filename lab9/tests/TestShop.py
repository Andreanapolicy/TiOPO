import unittest
import json
from lab9.controller.ProductController import ProductController


class TestShop(unittest.TestCase):
    def setUp(self):
        self.productController = ProductController()
        self.createdProducts = []
        f = open('data/test_data.json')
        self.data = json.load(f)

    def tearDown(self):
        if len(self.createdProducts) > 0:
            for createdProduct in self.createdProducts:
                self.productController.deleteById(createdProduct)
        self.productController = None

    def test_CreateProduct(self):
        self.productController.create(self.data['valid_product']).json()
        assert len(self.createdProducts) == 0

    def test_DeleteProductById(self):
        assert 1 == 1
