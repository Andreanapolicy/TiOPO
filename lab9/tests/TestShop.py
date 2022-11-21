import unittest
import json
from lab9.controller.ProductController import ProductController
from lab9.validator.Validator import Validator
from slugify import slugify
import unidecode

def loadJSON(url):
    f = open(url)
    return json.load(f)


def GetItemById(items, id):
    createdProduct = None
    for item in items:
        if item['id'] == str(id):
            createdProduct = item

    return createdProduct


class TestShop(unittest.TestCase):
    def setUp(self):
        self.productController = ProductController()
        self.createdProducts = []
        self.data = loadJSON('data/test_data.json')
        self.defaultResponseScheme = loadJSON('schemes/common_response_scheme.json')
        self.productListResponseScheme = loadJSON('schemes/product_list.json')

    def tearDown(self):
        if len(self.createdProducts) > 0:
            for createdProduct in self.createdProducts:
                self.productController.deleteById(createdProduct['id'])
        self.productController = None

    def test_GetAllProducts_ProductListHaveToBeNotEmpty_Success(self):
        response = self.productController.getAll()

        assert Validator.validate(response, self.productListResponseScheme)
        assert len(response) > 0

    def test_DeleteProduct_Success(self):
        product = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(product)

        self.productController.deleteById(product['id'])
        response = self.productController.getAll()
        createdProduct = GetItemById(response, product['id'])

        assert createdProduct is None

    def test_DeleteProduct_Fail(self):
        response = self.productController.deleteById(0)

        print("\nWrong id to delete product\n")
        assert response['status'] == 1

    def test_CreateProduct_ProductCreated_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        assert Validator.validate(response, self.defaultResponseScheme)

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        assert createdProduct is not None
        assert createdProduct['id'] == str(self.createdProducts[0]['id'])

    def test_CreateProduct_ProductNotCreated_Fail(self):
        print("\nWrong product data to create product entity\n")
        response = self.productController.create(self.data['invalid_product'])
        self.createdProducts.append(response)
        assert Validator.validate(response, self.defaultResponseScheme)

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        assert createdProduct is not None
        assert createdProduct['id'] == str(self.createdProducts[0]['id'])

    def test_EditProduct_ProductEdited_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        assert Validator.validate(response, self.defaultResponseScheme)

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['another_one_valid_product'])

        response = self.productController.edit(newProduct)
        assert Validator.validate(response, self.defaultResponseScheme)

        createdProduct = GetItemById(self.productController.getAll(), self.createdProducts[0]['id'])

        createdProduct.pop('cat', None)
        createdProduct.pop('alias', None)
        newProduct.pop('cat', None)
        newProduct.pop('alias', None)
        assert response['status'] == 1
        assert newProduct == createdProduct

    def test_EditProduct_EditByInvalidProduct_Fail(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        assert Validator.validate(response, self.defaultResponseScheme)

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['invalid_product'])

        try:
            self.productController.edit(newProduct)
        except Exception as exception:
            print("\nWrong product data to edit product entity\n")
            self.fail('Caught this error: ' + repr(exception))

    def test_EditProduct_EditByEmptyProductData_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        assert Validator.validate(response, self.defaultResponseScheme)

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['null_product'])

        response = self.productController.edit(newProduct)
        updatedProduct = GetItemById(self.productController.getAll(), self.createdProducts[0]['id'])

        createdProduct.pop('alias', None)
        updatedProduct.pop('alias', None)
        assert response['status'] == 1
        assert updatedProduct == createdProduct

    def test_GenerateAlias_NewProduct_Success(self):
        self.createdProducts.append(self.productController.create(self.data['valid_product']))
        self.createdProducts.append(self.productController.create(self.data['valid_product']))

        response = self.productController.getAll()

        firstProduct = GetItemById(response, self.createdProducts[0]['id'])
        secondProduct = GetItemById(response, self.createdProducts[1]['id'])

        assert firstProduct['alias'] == slugify(self.data['valid_product']['title'])
        assert secondProduct['alias'] == slugify(self.data['valid_product']['title']) + '-0'

    def test_EditAliasByEditingProductTitle_NewProduct_Success(self):
        self.createdProducts.append(self.productController.create(self.data['valid_product']))
        self.createdProducts.append(self.productController.create(self.data['valid_product']))

        response = self.productController.getAll()

        firstProduct = GetItemById(response, self.createdProducts[0]['id'])
        secondProduct = GetItemById(response, self.createdProducts[1]['id'])

        firstProduct.update(self.data['another_one_valid_product'])
        secondProduct.update(self.data['another_one_valid_product'])

        self.productController.edit(firstProduct)
        self.productController.edit(secondProduct)

        response = self.productController.getAll()

        firstProduct = GetItemById(response, self.createdProducts[0]['id'])
        secondProduct = GetItemById(response, self.createdProducts[1]['id'])

        assert firstProduct['alias'] == slugify(self.data['another_one_valid_product']['title'])
        assert secondProduct['alias'] == slugify(self.data['another_one_valid_product']['title']) + '-' + secondProduct['id']
