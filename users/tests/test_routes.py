# users/tests/test_routes.py
import json
import unittest
from users.routes import app  # Importando a aplicação Flask

class UsersTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_create_user(self):
        data = {"username": "john_doe", "email": "john.doe@example.com"}
        response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        user = json.loads(response.data)
        self.assertEqual(user['username'], "john_doe")

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.data)
        self.assertIsInstance(users, list)
