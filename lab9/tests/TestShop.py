import unittest

from lab9.controller.ProductController import ProductController


class TestShop(unittest.TestCase):
    # def __init__(self):
    #     self.productController = ProductController()
    #     self.createdProducts = []

    # @pytest.fixture(autouse=True)
    # def beforeAndAfter(self):
    #     print('just beforeAndAfter')
    #     if len(self.createdProducts) > 0:
    #         for createdProduct in self.createdProducts:
    #             self.productController.deleteById(createdProduct)

    def setUp(self):
        self.productController = ProductController()
        self.createdProducts = []

    def test_CreateProduct(self):
        assert len(self.createdProducts) == 0

    def test_deleteProductById(self):
        assert 1 == 1
        #create priduct
        #delete product
