from app import app

import json
import unittest


class TestViews(unittest.TestCase):

    def setUp(self):
        # self.app_context = app.app_context()
        # self.app_context.push()
        pass

    def tearDown(self):
        # self.app_context.pop()
        pass

    def test_get_permissions_pass(self):
        test_client = app.test_client(self)
        response = test_client.get(
            '/user/user1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {
            'permissions': [
                'Can deposit', 'Can Transfer', 'Can withdraw'
            ]})

    def test_get_permissions_fail(self):
        test_client = app.test_client(self)
        response = test_client.get(
            '/user/user2', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_check_permission_pass1(self):
        test_client = app.test_client(self)
        response = test_client.get(
            '/check_permission/user1/perm1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'response': True})

    def test_check_permission_pass2(self):
        test_client = app.test_client(self)
        response = test_client.get(
            '/check_permission/user1/perm2', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'response': False})

    def test_check_permission_fail(self):
        test_client = app.test_client(self)
        response = test_client.get(
            '/check_permission/user2/perm2', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_update_role_pass(self):
        test_client = app.test_client(self)
        response = test_client.post(
            '/update_roles/roles/role1', content_type='application/json',
            data=json.dumps({"permissions": ["perm5"]}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'role': [u'perm5']})

    def test_update_role_fail1(self):
        test_client = app.test_client(self)
        response = test_client.get(
            '/update_roles/roles/role1', content_type='application/json',
            data=json.dumps({"permissions": ["perm5"]}))
        self.assertEqual(response.status_code, 405)

    def test_update_role_fail2(self):
        test_client = app.test_client(self)
        response = test_client.post(
            '/update_roles/roles/role5', content_type='application/json',
            data=json.dumps({"permissions": ["perm5"]}))
        self.assertEqual(response.status_code, 404)

    def test_delete_permission_pass(self):
        test_client = app.test_client(self)
        response = test_client.delete(
            'delete_permission/permissions/perm1',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_delete_permission_fail(self):
        test_client = app.test_client(self)
        response = test_client.delete(
            'delete_permission/permissions/perm3',
            content_type='application/json')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
