# products/tests/test_routes.py
import json
import unittest
from products.routes import app  # Importando a aplicação Flask

class ProductsTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_create_product(self):
        data = {"name": "Product A", "price": 19.99}
        response = self.app.post('/products', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        product = json.loads(response.data)
        self.assertEqual(product['name'], "Product A")

    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        products = json.loads(response.data)
        self.assertIsInstance(products, list)
