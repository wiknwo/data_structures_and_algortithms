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
        pass

    def test_addVertex(self):
        # Case: Vertex already exists in graph
        self.assertRaises(ValueError, self.g1.addVertex, 1)
        # Case: Vertex does not exist in graph
        self.g1.addVertex(4)
        self.assertEqual(self.g1.order(), 4)

    def test_addEdge(self):
        # Case: Source vertex does not exist in graph
        self.assertRaises(ValueError, self.g1.addEdge, 0, 1)
        # Case: Destination vertex does not exist in graph
        self.assertRaises(ValueError, self.g1.addEdge, 1, 0)
        # Case: No parrallel edges
        self.assertRaises(ValueError, self.g1.addEdge, 1, 2)
        # Case: No self loops
        self.assertRaises(ValueError, self.g1.addEdge, 1, 1)
        # Case: Adding a valid edge
        self.g1.addEdge(3, 1)
        self.assertEqual(self.g1.hasEdge(3, 1), True)

    def test_removeEdge(self):
        # Case: Source vertex not in graph
        self.assertRaises(ValueError, self.g1.removeEdge, 0, 1)
        # Case: Destination vertex not in graph
        self.assertRaises(ValueError, self.g1.removeEdge, 1, 0)
        # Case: Remove valid edge in order (source, destination)
        self.g1.removeEdge(1, 2)
        self.assertEqual(self.g1.size(), 1)
        # Case: Remove valid edge in order (destination, source)
        self.g1.removeEdge(3, 2)
        self.assertEqual(self.g1.size(), 0)

    def test_removeVertex(self):
        # Case: Vertex does not exist in graph
        self.assertRaises(ValueError, self.g1.removeVertex, 0)
        # Case: Vertex exists in graph
        self.g1.removeVertex(1)
        self.assertEqual(self.g1.hasVertex(1), False)
        self.assertEqual(self.g1.order(), 2)
        self.assertEqual(self.g1.size(), 1)

    def test_degree(self):
        # Case: Vertex does not exist in graph
        self.assertRaises(ValueError, self.g1.degree, 0)
        # Case: Vertex exists in graph
        self.assertEqual(self.g1.degree(2), 2)
        self.assertEqual(self.g1.degree(1), 1)
        self.assertEqual(self.g1.degree(3), 1)

    def test_weightOfGraph(self):
        self.assertEqual(self.g1.weightOfGraph(), 0)

    def test_areAdjacentVertices(self):
        # Case: Vertices not in graph
        self.assertRaises(ValueError, self.g1.areAdjacentVertices, 0, 5)
        # Case: One vertex in graph and one not in graph
        self.assertRaises(ValueError, self.g1.areAdjacentVertices, 0, 1)
        # Case: Vertices in graph
        self.assertEqual(self.g1.areAdjacentVertices(1, 2), True)
        self.assertEqual(self.g1.areAdjacentVertices(1, 3), False)

    def test_isConnected(self):
        # Case: Connected graph
        self.assertEqual(self.g2.isConnected(), True)
        # Case: Disconnected graph
        self.g2.removeEdge('e', 'c')
        self.assertEqual(self.g2.isConnected(), False)


    def test_countConnectedComponents(self):
        self.assertEqual(self.g2.countConnectedComponents(), 1)

    def test_hasPathDFS(self):
        # Case: There exists a path between two vertices
        self.assertEqual(self.g2.hasPathDFS('a', 'f'), True)
        # Case: There does not exist a path between two vertices
        self.assertEqual(self.g2.hasPathDFS('a', 'c'), False)

    def test_isCyclic(self):
        # Case: Acyclic graph
        self.assertEqual(self.g2.isCyclic(), False)
        # Case: Cyclic graph
        self.g2.addEdge('b', 'c')
        self.assertEqual(self.g2.isCyclic(), True)

    def test_isTree(self):
        # Case: Graph is not a tree
        self.assertEqual(self.g3.isTree(), False)

    def test_isCutEdge(self):
        # Case: Edge is a cut-edge
        self.assertEqual(self.g3.isCutEdge((3, 4, 0)), True)
        # Case: Edge is not a cut-edge
        self.assertEqual(self.g3.isCutEdge((0, 1, 0)), False)

    def test_isCutVertex(self):
        # Case: Vertex is a cut-vertex
        self.assertEqual(self.g3.isCutVertex(3), True)
        # Case: Vertex is not a cut-vertex
        self.assertEqual(self.g3.isCutVertex(1), False)

    def test_shortestPathUnweighted(self):
        # Case: There exists a path between two vertices
        self.assertEqual(self.g3.shortestPathUnweighted(0, 4), 2)
        # Case: There does not exist a path between two vertices
        self.g3.removeEdge(3, 4)
        self.assertEqual(self.g3.shortestPathUnweighted(1, 4), -1)

if __name__ == '__main__':
    unittest.main()