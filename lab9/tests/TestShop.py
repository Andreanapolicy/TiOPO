import unittest

from lab9.controller.ProductController import ProductController


class TestShop(unittest.TestCase):
    def setUp(self):
        self.productController = ProductController()
        self.createdProducts = []

    def tearDown(self):
        if len(self.createdProducts) > 0:
            for createdProduct in self.createdProducts:
                self.productController.deleteById(createdProduct)
        self.productController = None

    def test_CreateProduct(self):
        assert len(self.createdProducts) == 0

    def test_deleteProductById(self):
        assert 1 == 1
