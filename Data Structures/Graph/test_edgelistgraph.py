import unittest
from edgelistgraph import EdgeListGraph

class TestEdgeListGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up TestEdgeListGraph test suite')

    @classmethod
    def tearDownClass(cls):
        print('')
        print('Tearing down TestEdgeListGraph test suite')

    def setUp(self):
        print('setUp')

        # Creating simple graph self.g1
        self.g1 = EdgeListGraph()
        self.g1.addVertex(1)
        self.g1.addVertex(2)
        self.g1.addVertex(3)
        self.g1.addEdge(1, 2)
        self.g1.addEdge(2, 3)

        # Creating a simple graph self.g2
        self.g2 = EdgeListGraph()
        self.g2.addVertex('a')
        self.g2.addVertex('b')
        self.g2.addVertex('c')
        self.g2.addVertex('d')
        self.g2.addVertex('e')
        self.g2.addVertex('f')
        self.g2.addEdge('a', 'b')
        self.g2.addEdge('a', 'c')
        self.g2.addEdge('b', 'd')
        self.g2.addEdge('c', 'e')
        self.g2.addEdge('d', 'f')

        # Creating a simple graph self.g3
        self.g3 = EdgeListGraph()
        self.g3.addVertex(0)
        self.g3.addVertex(1)
        self.g3.addVertex(2)
        self.g3.addVertex(3)
        self.g3.addVertex(4)
        self.g3.addEdge(0, 1)
        self.g3.addEdge(0, 2)
        self.g3.addEdge(0, 3)
        self.g3.addEdge(1, 2)
        self.g3.addEdge(3, 4)

    def tearDown(self):
        print('tearDown')

    def test_addVertex(self):
        print('test_addVertex')
        self.assertRaises(ValueError, self.g1.addVertex, 1)
        self.g1.addVertex(4)
        self.assertEqual(self.g1.order(), 4)

    def test_addEdge(self):
        pass

if __name__ == '__main__':
    unittest.main()