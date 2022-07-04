import unittest
import edgelistgraph

class TestEdgeListGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up TestEdgeListGraph test suite')

    @classmethod
    def tearDownClass(cls):
        print('')
        print('Tearing down TestEdgeListGraph test suite')

    def setUp(self):
        """Method that runs before every test"""
        print('setUp')

    def tearDown(self):
        """Method that runs after every test"""
        print('tearDown')

    def test_addVertex(self):
        print('test_addVertex')

if __name__ == '__main__':
    unittest.main()