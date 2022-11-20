from lab9.common.Client import Client
from lab9.common.URL import *


class ProductController:
    def deleteById(self, id):
        response = Client.custom_request('GET', BASE_URL + API_PREFIX + DELETE_PRODUCT_REQUEST, id)
        return response

    def create(self, params):
        response = Client.custom_request('POST', BASE_URL + API_PREFIX + CREATE_PRODUCT_REQUEST, params)
        return response

    def edit(self, params):
        response = Client.custom_request('POST', BASE_URL + API_PREFIX + EDIT_PRODUCT_REQUEST, params)
        return response

    def getAll(self):
        response = Client.custom_request('GET', BASE_URL + API_PREFIX + GET_ALL_PRODUCTS_REQUEST)
        return response
