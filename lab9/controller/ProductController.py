from lab9.common.Client import Client
from lab9.common.URL import *


class ProductController:
    def deleteById(self, id):
        response = Client.custom_request('GET', BASE_URL + API_PREFIX + DELETE_PRODUCT_REQUEST, id)
        return response
