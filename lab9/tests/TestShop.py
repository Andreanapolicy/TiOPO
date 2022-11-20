import pytest

from lab9.controller.ProductController import ProductController


class TestShop:
    def __init__(self):
        self.productController = ProductController()
        self.createdProducts = []

    @pytest.fixture(autouse=True)
    def beforeAndAfter(self):
        if len(self.createdProducts) > 0:
            for createdProduct in self.createdProducts:
                self.productController.deleteById(createdProduct)

    def testCreateProduct(self):
        assert 1 == 1

    def deleteProductById(self):
        #create priduct
        #delete product
