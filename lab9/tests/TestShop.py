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

    def test_CreateProduct_ProductCreated_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, product does not created")
        self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product']), "error, created product data is not equal to create-data")

    def test_CreateProduct_ProductCreatedWithCategoryId14_Success(self):
        response = self.productController.create(self.data['valid_product_with_category_14'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, product does not created")
        self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product_with_category_14']), "error, created product data is not equal to create-data")

    def test_CreateProduct_ProductCreatedWithCategoryId15_Fail(self):
        response = self.productController.create(self.data['invalid_product_with_category_15'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, wrong category id to create product entity")

    def test_CreateProduct_ProductCreatedWithHit1_Success(self):
        response = self.productController.create(self.data['valid_product_with_hit_1'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, product does not created")
        self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product_with_hit_1']), "error, created product data is not equal to create-data")

    def test_CreateProduct_ProductCreatedWithHit2_Fail(self):
        response = self.productController.create(self.data['invalid_product_with_hit_2'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, wrong hit id to create product entity")

    def test_CreateProduct_ProductCreatedWithStatus1_Success(self):
        response = self.productController.create(self.data['valid_product_with_status_1'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, product does not created")
        self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product_with_status_1']), "error, created product data is not equal to create-data")

    def test_CreateProduct_ProductCreatedWithStatus2_Fail(self):
        response = self.productController.create(self.data['invalid_product_with_status_2'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, response from create method is not valid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(createdProduct is not None, "error, wrong status to create product entity")

    def test_EditProduct_ProductEditedBySameProduct_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['valid_product'])

        response = self.productController.edit(newProduct)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, edit response is invalid")

        createdProduct = GetItemById(self.productController.getAll(), self.createdProducts[0]['id'])

        createdAlias = createdProduct.pop('alias', None)
        newAlias = newProduct.pop('alias', None)

        self.assertTrue(response['status'] == 1, "error, response status is fail")
        self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product']), "error, created product data is not equal to update-data")
        self.assertTrue(createdAlias == (newAlias + '-' + str(self.createdProducts[0]['id'])), "error, alias generated invalid")

    def test_EditProduct_EditByInvalidProductWithInvalidCategory_ProductDoesNotChanged_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['invalid_product_with_category_15'])
        try:
            self.productController.edit(self.data['invalid_product_with_category_15'])

            response = self.productController.getAll()
            createdProduct = GetItemById(response, self.createdProducts[0]['id'])

            self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product']), "error, created product data is not equal to update-data")
        except Exception as exception:
            self.fail('Wrong product data to edit product entity')

    def test_EditProduct_EditByInvalidProductWithInvalidHit_ProductDoesNotChanged_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['invalid_product_with_hit_2'])
        try:
            self.productController.edit(self.data['invalid_product_with_hit_2'])

            response = self.productController.getAll()
            createdProduct = GetItemById(response, self.createdProducts[0]['id'])

            self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product']), "error, created product data is not equal to update-data")
        except Exception as exception:
            self.fail('Wrong product data to edit product entity')

    def test_EditProduct_EditByInvalidProductWithInvalidStatus_ProductDoesNotChanged_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['invalid_product_with_status_2'])
        try:
            self.productController.edit(self.data['invalid_product_with_status_2'])

            response = self.productController.getAll()
            createdProduct = GetItemById(response, self.createdProducts[0]['id'])

            self.assertTrue(AreProductsEqual(createdProduct, self.data['valid_product']), "error, created product data is not equal to update-data")
        except Exception as exception:
            self.fail('Wrong product data to edit product entity')

    def test_EditProduct_EditByEmptyProductData_Success(self):
        response = self.productController.create(self.data['valid_product'])
        self.createdProducts.append(response)
        self.assertTrue(Validator.validate(response, self.defaultResponseScheme), "error, create response is invalid")

        response = self.productController.getAll()
        createdProduct = GetItemById(response, self.createdProducts[0]['id'])

        newProduct = createdProduct
        newProduct.update(self.data['null_product'])

        response = self.productController.edit(newProduct)
        updatedProduct = GetItemById(self.productController.getAll(), self.createdProducts[0]['id'])

        self.assertTrue(response['status'] == 1, "error, response status for edit is fail")
        self.assertTrue(AreProductsEqual(updatedProduct, createdProduct), "error, created product data is not equal to updated product data")

    def test_GenerateAlias_NewProduct_Success(self):
        self.createdProducts.append(self.productController.create(self.data['valid_product']))
        self.createdProducts.append(self.productController.create(self.data['valid_product']))

        response = self.productController.getAll()

        firstProduct = GetItemById(response, self.createdProducts[0]['id'])
        secondProduct = GetItemById(response, self.createdProducts[1]['id'])

        self.assertTrue(firstProduct['alias'] == slugify(self.data['valid_product']['title']), 'error, alias was equal to slugify title')
        self.assertTrue(secondProduct['alias'] == slugify(self.data['valid_product']['title']) + '-0', 'error, alias was equal to slugify title and -0')

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

        self.assertTrue(firstProduct['alias'] == slugify(self.data['another_one_valid_product']['title']), 'error, alias was equal to slugify title')
        self.assertTrue(secondProduct['alias'] == slugify(self.data['another_one_valid_product']['title']) + '-' + secondProduct['id'], 'error, alias was equal to slugify title and -id')

    def test_EditAliasBySameTitle_SameProduct_Success(self):
        self.createdProducts.append(self.productController.create(self.data['valid_product']))

        response = self.productController.getAll()

        firstProduct = GetItemById(response, self.createdProducts[0]['id'])

        firstProduct.update(self.data['valid_product'])

        self.productController.edit(firstProduct)

        response = self.productController.getAll()

        firstProduct = GetItemById(response, self.createdProducts[0]['id'])

        self.assertTrue(firstProduct['alias'] == slugify(self.data['valid_product']['title']) + '-' + str(self.createdProducts[0]['id']), 'error, alias was invalid created after editing')
