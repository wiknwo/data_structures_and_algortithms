"""
In graph theory and computer science, an adjacency list is 
a collection of unordered lists used to represent a finite 
graph. Each unordered list within an adjacency list 
describes the set of neighbors of a particular vertex in 
the graph. An adjacency list representation for a graph 
associates each vertex in the graph with the collection of 
its neighbouring vertices or edges. Let's say both edge lists 
and adjacency matrices seem to fail our requirements, what 
do we do? Well, we combine them together and create a 
hybrid implementation! This is what an adjacency list is - 
a hybrid between an adjacency matrix and an edge list. 
Representing a graph with adjacency lists combines adjacency 
matrices with edge lists. For each vertex i, store an array 
of the vertices adjacent to it. We typically have an array 
of |V| adjacency lists, one adjacency list per vertex.
Due to this, an adjacency list is the most common 
representation of a graph. Another reason is that graph 
traversal problems often require us to be able to easily 
figure out which nodes are the neighbors of another node. 
In most graph traversal interview problems, we don't 
really need to build the entire graph. Rather, it's 
important to know where we can travel (or in other words, 
who the neighbors of a node are). 

Vertex numbers in an adjacency list are not required to 
appear in any particular order, though it is often 
convenient to list them in increasing order.

We can get to each vertex's adjacency list in constant time, 
because we just have to index into an array. To find out 
whether an edge (i,j) is present in the graph, we go to i's 
adjacency list in constant time and then look for j in i's 
adjacency list. How long does that take in the worst case? 
The answer is O(d) where d is the degree of vertex i, because 
that's how long i's adjacency list is, 0 <= d <= |V| - 1.

In an undirected graph, vertex j is in vertex i's adjacency 
list if and only if i is in j's adjacency list. If the 
graph is weighted, then each item in each adjacency list 
is either a two-item array or an object, giving the vertex 
number and the edge weight.

How much space do adjacency lists take? We have |V| lists and
although each list could have as many as |V| - 1 vertices, in
total the adjacency lists for an undirected graph contain 2|E|
elements. Why 2|E|? Each edge (i,j) appears exactly twice in the 
adjacency lists, once in i's list and once in j's list, and there 
are |E| edges. For a directed graph, the adjacency lists contain 
a total of |E| elements, one element per directed edge.

************ ADVANTAGES ************
- Space-efficient for sparse graphs compared to adjacency matrix
- Simple representation
- Most common representation of graphs
- Efficient listing of neighbours of a vertex

************ DISADVANTAGES ************
- Less space-efficient for dense graphs
- Checking if there is an edge between two vertices is slower than an adjacency matrix
"""
# https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c
# https://en.wikipedia.org/wiki/Adjacency_list
# http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/weighted.html
class AdjacencyListGraph:
    """Class representing simple undirected unweighted/weighted graphs using adjacency list"""
    def __init__(self):
        """Initializes adjacency list"""
        self.__adjacencylist = {}
    
    def vertices(self):
        """Method to return all the vertices in the graph as an iterable"""
        return iter(self.__adjacencylist.keys())

    def edges(self):
        """Method to return all the edges in the graph as an iterable"""
        return iter(self.__adjacencylist.values())

    def has_vertex(self, v):
        """Method to return boolean indicating if a vertex is in the graph"""
        return v in self.__adjacencylist

    def has_edge(self, s, d, w = 0):
        """Method to return boolean indicating if an edge is in the graph"""
        if not self.has_vertex(s):
            raise ValueError('Source vertex not in graph!')
        if not self.has_vertex(d):
            raise ValueError('Destination vertex not in graph!')
        else:
            return (d, w) in self.__adjacencylist[s]

    def add_vertex(self, v):
        """Method to add vertex to graph"""
        if self.has_vertex(v):
            raise ValueError('Vertex already in graph!')
        else:
            self.__adjacencylist[v] = set()

    def add_edge(self, s, d, w = 0):
        """Method to add edge between two vertices in graph"""
        if not self.has_vertex(s):
            raise ValueError('Source vertex not in the graph!')
        if not self.has_vertex(d):
            raise ValueError('Destination vertex not in the graph!')
        if self.has_edge(s, d, w) or self.has_edge(d, s, w):
            raise ValueError('No parallel edges in graph!')
        if s == d:
            raise ValueError('No self loops in graph!')
        else:
            # Adding edge from source to destination with weight w
            self.__adjacencylist[s].add((d, w))
            # Adding edge from destination to source with weight w
            self.__adjacencylist[d].add((s, w))

    def remove_edge(self, s, d, w = 0):
        """Method to remove edge between two vertices in graph"""
        if not self.has_vertex(s):
            raise ValueError('Source vertex not in the graph!')
        if not self.has_vertex(d):
            raise ValueError('Destination vertex not in the graph!')
        elif self.has_edge(s, d, w) or self.has_edge(d, s, w):
            # Remove edge from source to destination with weight w
            self.__adjacencylist[s].remove((d, w))
            # Remove edge from destination to source with weight w
            self.__adjacencylist[d].remove((s, w))
    
    def remove_vertex(self, v):
        """Method to remove vertex and its associated edges from graph"""
        if not self.has_vertex(v):
            raise ValueError('Vertex not in graph!')
        else:
            # Getting edges to delete
            edges_to_remove = [(u, w) for u, w in self.__adjacencylist[v]]
            # Removing all edges associated with v
            for u, w in edges_to_remove:
                self.remove_edge(v, u, w)
            edges_to_remove.clear()
            # Deleting v from adjacency list
            del self.__adjacencylist[v]