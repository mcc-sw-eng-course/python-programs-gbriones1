import unittest
import json

import ex_15

class TestDirectory(unittest.TestCase):

    def setUp(self):
        self.d = ex_15.Directory()
        self.d.add_user("Gabriel", "Tlajomulco", "3366998855", "gabriel@email.com")
        self.d.add_user("Edgar", "Ciudad del Sol", "3322114455", "edgar@email.com")
        self.d.add_user("Samuel", "Zapopan", "3355887744", "samuel@email.com")

    def test_add_user(self):
        self.assertEqual({
            "name": "Gabriel",
            "address": "Tlajomulco",
            "phone": "3366998855",
            "email": "gabriel@email.com"
        }, self.d.users[0])

    def test_get_data(self):
        self.assertEqual({
            "name": "Gabriel",
            "address": "Tlajomulco",
            "phone": "3366998855",
            "email": "gabriel@email.com"
        }, self.d.get_data("Gabriel"))

    def test_save_directory(self):
        self.d.save_directory("directory.json")
        with open("directory.json", "r") as f:
            saved = json.loads(f.read())
        self.assertEqual(saved, self.d.users)

    def test_load_directory(self):
        self.d.users = [{
            "name": "Gabriel",
            "address": "Tlajomulco",
            "phone": "3366998855",
            "email": "gabriel@email.com"
        }]
        self.d.save_directory("directory.json")
        self.d.users = []
        self.d.load_directory("directory.json")
        self.assertEqual([{
            "name": "Gabriel",
            "address": "Tlajomulco",
            "phone": "3366998855",
            "email": "gabriel@email.com"
        }], self.d.users)

if __name__ == '__main__':
    unittest.main()
