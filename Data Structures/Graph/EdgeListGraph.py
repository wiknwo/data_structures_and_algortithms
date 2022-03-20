"""
In an edge list, we maintain an unordered list of all 
edges. This minimally suffices, but there is no efficient 
way to locate a particular edge (u,v), or the set of all 
edges incident to a vertex v.

To represent an edge, we just have an array of two vertex 
numbers, or an array of objects containing the vertex numbers 
of the vertices that the edges are incident on. If edges 
have weights, add either a third element to the array or 
more information to the object, giving the edge's weight. 
Since each edge contains just two or three numbers, the 
total space for an edge list is O(E) where E is the number
of edges.

Edge lists are simple, but if we want to find whether the 
graph contains a particular edge, we have to search through 
the edge list. If the edges appear in the edge list in no 
particular order, that's a linear search through |E| edges.

|V| = n, |E| = m

************ ADVANTAGES ************
- Space-efficient for sparse graphs
- Iterating over edges is efficient
- Extremely simple representation

************ DISADVANTAGES ************
- Less space-efficient for dense graphs
- Edge weight lookup is O(E)
- This representation lacks structure

Question to think about: How can you organize an edge list 
to make searching for a particular edge take O(log(E)) time? 
The answer is a little tricky.

Answer: Sort the list by the 1st vertex in each edge, and 
then by 2nd vertex in each edge. The list is sorted, so we 
can now use a binary search on it. Our comparison is a little 
bit more complicated now. 

[v1,v2] < [v3,v4] if (v1 < v3) OR ( (v1 === v3) AND v2 < v4 )

If we have an edge [v1,v2] we do a binary search for [v1,v2] 
on the list. Time O(log E)

If your edges are not directed i.e. [v1,v2] is equivalent to 
[v2,v1] then perform a second search on the equivalent edge 
[v2,v1] if your first search wasn't successful. 
Double O(log E) is still O(log E).

Hope this makes sense -Cameron

https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
"""
class EdgeListGraph:
    """Class representing simple undirected weighted/unweighted graphs using edge list"""
    def __init__(self, v = (), e = ()):
        """Initialize vertices and edges objects"""
        self.__vertices = set()
        self.__edges = set()

        for vertex in v:
            self.addVertex(vertex)
        for s, d, w in e:
            self.addEdge(s, d, w)

    def vertices(self):
        """Method to return all the vertices in the graph as an iterable"""
        return iter(self.__vertices)

    def edges(self):
        """Method to return all the edges in the graph as an iterable"""
        return iter(self.__edges)
    
    def addVertex(self, v):
        """Method to add vertex to graph"""
        # Check if this vertex is aleady in our list of vertices
        if v in self.__vertices:
            raise ValueError('Vertex already in graph!')
        else:
            self.__vertices.add(v)
    
    def addEdge(self, s, d, w = 0):
        """Method to add edge between two vertices in graph"""
        # Check if both vertices are in the graph, we should
        # be smart about how we handle this error. What is the
        # expected behaviour of this piece of software on the
        # user's end? Should we automatically add an edge between
        # s and d if either of these vertices is non-existant?
        # These are good questions to ask and lead to smarter
        # and more resilient software.
        if s not in self.__vertices or d not in self.__vertices:
            raise ValueError('One or both vertices are not in the graph!')
        else:
            self.__edges.add((s, d, w))

    def removeEdge(self, s, d, w = 0):
        """Method to remove edge between two vertices in graph"""
        # Check if both vertices are in graph, we should be
        # smart about how we handle this error. What is the
        # expected behaviour of this piece of software on the
        # user's end? 
        if (s, d, w) not in self.__edges:
            raise ValueError('One or both of the vertices are not in the graph and the weight maybe incorrect!')
        else:
            self.__edges.remove((s, d, w))

    def removeVertex(self, v):
        """Method to remove vertex and its associated edges from graph"""
        # Check if vertex is in the graph
        if v not in self.__vertices:
            raise ValueError('Vertex not in graph!')
        else:
            # Remove all edges associated with v
            edges_to_remove = []

            for s, d, w in self.__edges:
                if s == v or d == v:
                    edges_to_remove.append((s, d, w))

            for s, d, w in edges_to_remove:
                self.removeEdge(s, d, w)

            edges_to_remove.clear()
            # Remove v from graph 
            self.__vertices.remove(v)

    def hasVertex(self, v):
        """Method to return boolean indicating if a vertex is in the graph"""
        return v in self.__vertices

    def hasEdge(self, s, d, w = 0):
        """Method to return boolean indicating if an edge is in the graph"""
        return (s, d, w) in self.__edges

    def adjacentVertices(self, v):
        """Method to return a list of all adjacent vertices to v in graph"""
        # Check if vertex is in graph
        if v not in self.__vertices:
            raise ValueError('Vertex not in graph!')
        else:
            neighbours = []
            for s, d, w in self.__edges:
                if s == v:
                    neighbours.append(d)
                elif d == v:
                    neighbours.append(s)
            return neighbours

    def degree(self, v):
        """Method to return degree of vertex"""
        # Check if vertex is in graph
        if v not in self.__vertices:
            raise ValueError('Vertex not in graph!')
        else: 
            return sum(1 for e in self.__edges if v in e)

    def n(self):
        """Method to return number of vertices in graph"""
        return len(self.__vertices)

    def m(self):
        """Method to return number of edges in graph"""
        return len(self.__edges)

if __name__ == '__main__':
    simplegraph = EdgeListGraph([1, 2, 3], {(1, 2, 0), (2, 3, 0)})
    
    # Print definition of our simple graph
    print("Vertices of G: {}".format(list(simplegraph.vertices())))
    print("Edges of G: {}".format(list(simplegraph.edges())))

    # Print the degrees of our vertices
    for i in range(3):
        print("Degree of vertex {} = {}".format(i + 1, simplegraph.degree(i + 1)))

    # Print neighbours or adjacent vertices of vertex 2
    print("Neighoburs of {}: {}".format(2, simplegraph.adjacentVertices(2)))

    # Print number of vertices and edges
    print("Number of vertices in graph: {}".format(simplegraph.n()))
    print("Number of edges in graph: {}".format(simplegraph.m()))

    # Remove an edge from the graph
    print("Remove edge: ({}, {}, {}) to graph".format(1, 2, 0))
    simplegraph.removeEdge(1, 2)
    print("Number of vertices in graph: {}".format(simplegraph.n()))
    print("Number of edges in graph: {}".format(simplegraph.m()))

    # Remove an edge from the graph that doesn't exist
    try:
        print("Remove edge: ({}, {}, {}) to graph".format(1, 3, 0))
        simplegraph.removeEdge(1, 3)
        print("Number of vertices in graph: {}".format(simplegraph.n()))
        print("Number of edges in graph: {}".format(simplegraph.m()))
    except:
        print("Edge does not exist in graph")
    
    # Add an edge to the graph
    print("Add edge: ({}, {}, {}) to graph".format(1, 2, 0))
    simplegraph.addEdge(1, 2)
    print("Number of vertices in graph: {}".format(simplegraph.n()))
    print("Number of edges in graph: {}".format(simplegraph.m()))

    # Remove a vertex from the graph
    print("Remove vertex: {} from graph".format(2))
    simplegraph.removeVertex(2)
    print("Number of vertices in graph: {}".format(simplegraph.n()))
    print("Number of edges in graph: {}".format(simplegraph.m()))

    