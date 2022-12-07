import unittest
import json
from lab9.controller.ProductController import ProductController
from lab9.validator.Validator import Validator
from slugify import slugify
from parameterized import parameterized

def loadJSON(url):
    f = open(url)
    return json.load(f)


def GetItemById(items, id):
    createdProduct = None
    for item in items:
        if item['id'] == str(id):
            createdProduct = item

    return createdProduct

DEFAULT_COMPARER_KEYS = [
    'category_id',
    'title',
    'content',
    'price',
    'old_price',
    'status',
    'keywords',
    'description',
    'hit',
]

def AreProductsEqual(firstItem, secondItem, keys = None):
    if keys is None:
        keys = DEFAULT_COMPARER_KEYS

    for key in keys:
        if firstItem[key] != secondItem[key]:
            return False

    return True


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

        self.assertTrue(Validator.validate(response, self.productListResponseScheme), "error, response from get all method is not valid")
        self.assertTrue(len(response) > 0, "error, there are no products")

    def test_DeleteProduct_Success(self):
        product = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(product)

        self.productController.deleteById(product['id'])
        response = self.productController.getAll()
        createdProduct = GetItemById(response, product['id'])

        self.assertTrue(createdProduct is None, "error, product was not deleted")

    def test_DeleteProduct_Fail(self):
        response = self.productController.deleteById(0)

        self.assertTrue(response['status'] == 1, "error, response status is not success")

    @parameterized.expand([
        ("valid_product_Success", "valid_product"),
        ("valid_product_with_category_14_Success", "valid_product_with_category_14"),
        ("invalid_product_with_category_15_Fail", "invalid_product_with_category_15"),
        ("valid_product_with_hit_1_Success", "valid_product_with_hit_1"),
        ("invalid_product_with_hit_2_Fail", "invalid_product_with_hit_2"),
        ("valid_product_with_status_1_Success", "valid_product_with_status_1"),
        ("invalid_product_with_status_2_Fail", "invalid_product_with_status_2")
    ])
    def test_CreateProduct(self, description, product):
        response = self.productController.create(self.data[product])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, product does not created")
        self.assertTrue(AreProductsEqual(createdProduct, self.data[product]), "error, product was created with not input data")

    @parameterized.expand([
        ("valid_product_Success", "valid_product", "valid_product", True),
        ("invalid_product_with_category_15_Success", "valid_product", "invalid_product_with_category_15", False),
        ("invalid_product_with_hit_2_Success", "valid_product", "invalid_product_with_hit_2", False),
        ("null_product_Success", "null_product", "invalid_product_with_status_2", False),
    ])
    def test_EditProduct(self, description, startingData, updatingData, willUpdate):
        try:
            response = self.productController.create(self.data[startingData])
            self.createdProducts.append(response)
            self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")

        except Exception as exception:
            self.fail('Wrong product data to create product entity')
        try:
            self.productController.edit(self.data[updatingData])

            response = self.productController.getAll()
            createdProduct = GetItemById(response, self.createdProducts[0]['id'])

            self.assertTrue(
                AreProductsEqual(createdProduct, self.data[updatingData if willUpdate else startingData]),
                "error, created product data is not equal to update-data")
        except Exception as exception:
            self.fail('Wrong product data to edit product entity')

    # def test_EditProduct_ProductEditedBySameProduct_Success(self):
    #     response = self.productController.create(self.data['valid_product'])
    #     self.createdProducts.append(response)
    #     self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")
    #
    #     response = self.productController.getAll()
    #     createdProduct = GetItemById(response, self.createdProducts[0]['id'])
    #
    #     newProduct = createdProduct
    #     newProduct.update(self.data['valid_product'])
    #
    #     response = self.productController.edit(newProduct)
    #     self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, edit response is invalid")
    #
    #     createdProduct = GetItemById(self.productController.getAll(), self.createdProducts[0]['id'])
    #
    #     createdAlias = createdProduct.pop('alias', None)
    #     newAlias = newProduct.pop('alias', None)
    #
    #     self.assertTrue(response['status'] == 1, "error, response status is fail")
    #     self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product']), "error, created product data is not equal to update-data")
    #     self.assertTrue(createdAlias == (newAlias + '-' + str(self.createdProducts[0]['id'])), "error, alias generated invalid")

    # def test_GenerateAlias_NewProduct_Success(self):
    #     self.createdProducts.append(self.productController.create(self.data['valid_product']))
    #     self.createdProducts.append(self.productController.create(self.data['valid_product']))
    #
    #     response = self.productController.getAll()
    #
    #     firstProduct = GetItemById(response, self.createdProducts[0]['id'])
    #     secondProduct = GetItemById(response, self.createdProducts[1]['id'])
    #
    #     self.assertTrue(firstProduct['alias'] == slugify(self.data['valid_product']['title']), 'error, alias was equal to slugify title')
    #     self.assertTrue(secondProduct['alias'] == slugify(self.data['valid_product']['title']) + '-0', 'error, alias was equal to slugify title and -0')
    #
    # def test_EditAliasByEditingProductTitle_NewProduct_Success(self):
    #     self.createdProducts.append(self.productController.create(self.data['valid_product']))
    #     self.createdProducts.append(self.productController.create(self.data['valid_product']))
    #
    #     response = self.productController.getAll()
    #
    #     firstProduct = GetItemById(response, self.createdProducts[0]['id'])
    #     secondProduct = GetItemById(response, self.createdProducts[1]['id'])
    #
    #     firstProduct.update(self.data['another_one_valid_product'])
    #     secondProduct.update(self.data['another_one_valid_product'])
    #
    #     self.productController.edit(firstProduct)
    #     self.productController.edit(secondProduct)
    #
    #     response = self.productController.getAll()
    #
    #     firstProduct = GetItemById(response, self.createdProducts[0]['id'])
    #     secondProduct = GetItemById(response, self.createdProducts[1]['id'])
    #
    #     self.assertTrue(firstProduct['alias'] == slugify(self.data['another_one_valid_product']['title']), 'error, alias was equal to slugify title')
    #     self.assertTrue(secondProduct['alias'] == slugify(self.data['another_one_valid_product']['title']) + '-' + secondProduct['id'], 'error, alias was equal to slugify title and -id')
    #
    # def test_EditAliasBySameTitle_SameProduct_Success(self):
    #     self.createdProducts.append(self.productController.create(self.data['valid_product']))
    #
    #     response = self.productController.getAll()
    #
    #     firstProduct = GetItemById(response, self.createdProducts[0]['id'])
    #
    #     firstProduct.update(self.data['valid_product'])
    #
    #     self.productController.edit(firstProduct)
    #
    #     response = self.productController.getAll()
    #
    #     firstProduct = GetItemById(response, self.createdProducts[0]['id'])
    #
    #     self.assertTrue(firstProduct['alias'] == slugify(self.data['valid_product']['title']) + '-' + str(self.createdProducts[0]['id']), 'error, alias was invalid created after editing')
