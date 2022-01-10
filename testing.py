import unittest
from func import DB

class test_db(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.database = DB("1.db")

    def test_or(self):
        res = self.database.order_info(1)
        self.assertEqual(res, [(30.0, 'Name1')])
        
    def test_list(self):
        res = self.database.order_list(1)
        self.assertEqual(res, [('id', 'Login1', '2005-11-12', '2021-11-23', 'Moscow', 'Chertanovo', '1')])  
        
    def test_address(self):
        res = self.database.address_list(1)
        self.assertEqual(res, [(1, 'Login1', '2005-11-12', '2021-11-23', 'Moscow', 'Chertanovo', '1')])      

if __name__ == '__main__':
    unittest.main() 