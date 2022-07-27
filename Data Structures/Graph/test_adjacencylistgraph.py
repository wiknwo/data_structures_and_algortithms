import unittest
from adjacencylistgraph import AdjacencyListGraph

class TestAdjacencyListGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up TestAdjacencyListGraph test suite')

    @classmethod
    def tearDownClass(cls):
        print('')
        print('Tearing down TestAdjacencyListGraph test suite')

    def setUp(self):
        # Creating simple graph self.g1
        self.g1 = AdjacencyListGraph()
        self.g1.add_vertex(1)
        self.g1.add_vertex(2)
        self.g1.add_vertex(3)
        self.g1.add_edge(1, 2)
        self.g1.add_edge(2, 3)

        # Creating a simple graph self.g2
        self.g2 = AdjacencyListGraph()
        self.g2.add_vertex('a')
        self.g2.add_vertex('b')
        self.g2.add_vertex('c')
        self.g2.add_vertex('d')
        self.g2.add_vertex('e')
        self.g2.add_vertex('f')
        self.g2.add_edge('a', 'b')
        self.g2.add_edge('a', 'c')
        self.g2.add_edge('b', 'd')
        self.g2.add_edge('c', 'e')
        self.g2.add_edge('d', 'f')

        # Creating a simple graph self.g3
        self.g3 = AdjacencyListGraph()
        self.g3.add_vertex(0)
        self.g3.add_vertex(1)
        self.g3.add_vertex(2)
        self.g3.add_vertex(3)
        self.g3.add_vertex(4)
        self.g3.add_edge(0, 1)
        self.g3.add_edge(0, 2)
        self.g3.add_edge(0, 3)
        self.g3.add_edge(1, 2)
        self.g3.add_edge(3, 4)

        # Creating a simple graph self.g4
        self.g4 = AdjacencyListGraph()
        self.g4.add_vertex(0)
        self.g4.add_vertex(1)
        self.g4.add_vertex(2)
        self.g4.add_vertex(3)
        self.g4.add_edge(0, 1, 10)
        self.g4.add_edge(0, 2, 6)
        self.g4.add_edge(0, 3, 5)
        self.g4.add_edge(1, 3, 15)
        self.g4.add_edge(2, 3, 4)

    def tearDown(self):
        pass

    def test_order(self):
        self.assertEqual(self.g1.order(), 3)
        self.assertEqual(self.g2.order(), 6)
        self.assertEqual(self.g3.order(), 5)
        self.assertEqual(self.g4.order(), 4)

    def test_size(self):
        self.assertEqual(self.g1.size(), 2)
        self.assertEqual(self.g2.size(), 5)
        self.assertEqual(self.g3.size(), 5)
        self.assertEqual(self.g4.size(), 5)

if __name__ == '__main__':
    unittest.main()