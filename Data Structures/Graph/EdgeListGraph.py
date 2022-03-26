"""
Simple Graph: A graph with no self loops or parallel edges.

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
    def __init__(self):
        """Initialize vertices and edges objects"""
        self.__vertices = set()
        self.__edges = set()

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
        if not self.hasVertex(s):
            raise ValueError('Source vertex not in the graph!')
        if not self.hasVertex(d):
            raise ValueError('Destination vertex not in the graph!')
        if self.hasEdge(s, d, w) or self.hasEdge(d, s, w):
            raise ValueError('No parallel edges or self loops in graph!')
        else:
            self.__edges.add((s, d, w))

    def removeEdge(self, s, d, w = 0):
        """Method to remove edge between two vertices in graph"""
        # Check if both vertices are in graph and if the edge exists 
        # in the graph, we should be smart about how we handle these errors. 
        # What is the expected behaviour of this piece of software on the
        # user's end? 
        if not self.hasVertex(s):
            raise ValueError('Source vertex not in the graph!')
        if not self.hasVertex(d):
            raise ValueError('Destination vertex not in the graph!')
        elif self.hasEdge(s, d, w):
            self.__edges.remove((s, d, w))
        elif self.hasEdge(d, s, w):
            self.__edges.remove((d, s, w))
            
    def removeVertex(self, v):
        """Method to remove vertex and its associated edges from graph"""
        # Check if vertex is in the graph
        if not self.hasVertex(v):
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
        if not self.hasVertex(v):
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
        if not self.hasVertex(v):
            raise ValueError('Vertex not in graph!')
        else: 
            return sum(1 for e in self.__edges if v in e)

    def n(self):
        """Method to return number of vertices (order) in graph"""
        return len(self.__vertices)

    def m(self):
        """Method to return number of edges (size) in graph"""
        return len(self.__edges)

    def weightOfGraph(self):
        """Method to return the weight of the graph defined as the sum of the weights of all its edges"""
        return sum(w for s, d, w in self.__edges)

    def areAdjacentVertices(self, u, v):
        """Method that returns boolean indictaing whether vertices u and v are adjacent in the graph"""
        return u in self.adjacentVertices(v) and v in self.adjacentVertices(v)
    
    def incidentEdges(self, v):
        """Method to return list of edges incident to v in graph"""
        if not self.hasVertex(v):
            raise ValueError('Vertex not in graph!')
        else:
            return [e for e in self.__edges if v in e]

    def oppositeVertexOnEdge(self, v, e):
        """Method to return the opposite vertex on the given edge in the graph"""
        return e[1] if v == e[0] else e[0]

    def getDegreeSequence(self):
        """Method to return the degree sequence of the graph in non-decreasing order"""
        return sorted([self.degree(v) for v in self.__vertices])

    def dfs(self):
        """
        Method to perform Depth-First Traversal of entire graph.
        Depth-first search (DFS) is an algorithm for traversing 
        or searching tree or graph data structures. The algorithm 
        starts at the root node (selecting some arbitrary node as 
        the root node in the case of a graph) and explores as far 
        as possible along each branch before backtracking. A version 
        of depth-first search was investigated in the 19th century by 
        French mathematician Charles Pierre Trémaux as a strategy for 
        solving mazes. It is called DFS because it starts from the 
        root and follows each path to its greatest depth node (leaf/dead end)
        before backtracking and moving to the next node. A stack is used
        to store the nodes on the path from root node to the current
        node. In recusive version, the stack is implicit (call stack) 
        DFS works by searching deeper before it searches wider.

        Steps to perform DFS:
        1. Choose the initial vertex to visit and start exploring it
        2. Find the adjacent vertices to the initial vertex
        3. Visit any one of the adjacent vertices, suspend the exploration
        of the initial vertex by placing it on the stack and start exploring 
        its neighbor
        4. Repeat this process until the entire graph is traversed.

        The properties of a depth-first traversal of a graph are 
        as follows:
        - Visits all the vertices and edges of the graph
        - Determines whether the graph is connected
        - Computes the connected components of the graph
        - Computes a spanning forest of the graph

        Applications of dfs:
        - Find and report a path between two given vertices
        - Detect and find a cycle in the graph
        - Compute a graph's Minimum Spanning Tree (MST)
        - Find strongly connected components 
        - Topologically sort the vertices of a digraph/DAG
        - Find bridges/cut-edges/isthmus/cut-arc/articulation points of a graph
        - Find augmenting paths in a flow network
        - Generate mazes
        - Solving puzzles with only one solution, such as mazes
        - Planarity testing

        This method ouputs a labelling of the edges of the 
        graph as discovery and back edges. 
        """
        vertexLabels, edgeLabels = {}, {}

        for u in self.__vertices:
            vertexLabels[u] = 'UNEXPLORED'
        for e in self.__edges:
            edgeLabels[e] = 'UNEXPLORED'
        for v in self.__vertices:
            if vertexLabels[v] == 'UNEXPLORED':
                self.__dfs(v, vertexLabels, edgeLabels)

    def __dfs(self, vertex, vLabels, eLabels):
        """Method to perform depth-first search starting from a given node in graph"""
        vLabels[vertex] = 'VISITED'
        print(vertex)
        for e in self.incidentEdges(vertex):
            if eLabels[e] == 'UNEXPLORED':
                u = self.oppositeVertexOnEdge(vertex, e)
                if vLabels[u] == 'UNEXPLORED':
                    eLabels[e] = 'DISCOVERY'
                    self.__dfs(u, vLabels, eLabels)
                else:
                    eLabels[e] = 'BACK'

    def depthFirstPrint(self):
        """Method to print vertices of graph in dfs manner"""
        visited = {}

        for v in self.__vertices:
            visited[v] = False
        for v in self.__vertices:
            if not visited[v]:
                self.__depthFirstPrint(v, visited)
    
    def __depthFirstPrint(self, source, visited):
        """Helper method to print vertices of graph in dfs manner"""
        stack = [source]

        while stack:
            current_vertex = stack.pop()
            visited[current_vertex] = True
            print(current_vertex)
            for neighbour in self.adjacentVertices(current_vertex):
                if not visited[neighbour]:
                    stack.append(neighbour)

    def depthFirstPrintRecursive(self):
        """Method to print vertices in dfs manner recursively"""
        visited = {}

        for v in self.__vertices:
            visited[v] = False
        for v in self.__vertices:
            if not visited[v]:
                self.__depthFirstPrintRecursive(v, visited)
    
    def __depthFirstPrintRecursive(self, source, visited):
        """Helper method to print vertices in graph in dfs manner recursively"""
        print(source)
        visited[source] = True
        for neighbour in self.adjacentVertices(source):
            if not visited[neighbour]:
                self.__depthFirstPrintRecursive(neighbour, visited)

    def bfs(self):
        """
        Method to perform Breadth-First Search traversal of 
        entire graph. BFS and its application in finding 
        connected components of graphs were invented in 1945 
        by Konrad Zuse, in his (rejected) Ph.D. thesis on the 
        Plankalkül programming language, but this was not published 
        until 1972. It was reinvented in 1959 by Edward F. Moore, 
        who used it to find the shortest path out of a maze, and 
        later developed by C. Y. Lee into a wire routing algorithm 
        (published 1961).

        Steps to perform BFS:
        1. Choose an initial vertex to start the search and
        enqueue it.
        2. Dequeue a vertex and start exploring it
            a. Look at the neighbours of the vertex, mark 
            them as visited and enqueue them for 
            exploration
        3. Repeat step 2 until entire graph is traversed.

        The properties of a breadth-first traversal of a graph are 
        as follows:
        - Visits all the vertices and edges of the graph
        - Determines whether the graph is connected
        - Computes the connected components of the graph
        - Computes a spanning forest of the graph

        Applications of bfs:
        - Find and report a path with the minimum number of edges between two given vertices i.e.
        find the shortest path in an unweigthed graph
        - Find a simple cycle, if there is one
        - Copying garbage collection, Cheney's algorithm
        - Construction of the failure function of the Aho-Corasick pattern matcher.
        - Testing bipartiteness of a graph.
        """
        vertexLabels, edgeLabels = {}, {}

        for u in self.__vertices:
            vertexLabels[u] = 'UNEXPLORED'
        for e in self.__edges:
            edgeLabels[e] = 'UNEXPLORED'
        for v in self.__vertices:
            if vertexLabels[v] == 'UNEXPLORED':
                self.__bfs(v, vertexLabels, edgeLabels)
    
    def __bfs(self, vertex, vLabels, eLabels):
        """Method to perform breadth-first search starting from a given node in graph"""
        vLabels[vertex] = 'VISITED'
        q = [vertex]
        while q:
            current = q.pop(0)
            print(current)
            for e in self.incidentEdges(current):
                if eLabels[e] == 'UNEXPLORED':
                    u = self.oppositeVertexOnEdge(current, e)
                    if vLabels[u] == 'UNEXPLORED':
                        eLabels[e] = 'DISCOVERY'
                        vLabels[u] = 'VISITED'
                        q.append(u)
                    else:
                        eLabels[e] = 'CROSS'

    def breadthFirstPrint(self):
        """Method to print vertices of graph in bfs manner"""
        visited = {}

        for v in self.__vertices:
            visited[v] = False
        for v in self.__vertices:
            if not visited[v]:
                self.__breadthFirstPrint(v, visited)

    def __breadthFirstPrint(self, source, visited):
        """Helper method to print vertices of graph in bfs manner"""
        q = [source]
        while q:
            current_vertex = q.pop(0)
            visited[current_vertex] = True
            print(current_vertex)
            for neighbour in self.adjacentVertices(current_vertex):
                if not visited[neighbour]:
                    q.append(neighbour)

    def isConnected(self):
        """
        Method to determine if graph is connected using DFS.
        In an undirected graph G, a connected graph is graph 
        that is connected in the sense of a topological space, 
        i.e., there is a path from any point to any other point 
        in the graph. A graph that is not connected is said to 
        be disconnected. A graph is said to be connected if 
        every pair of vertices in the graph is connected. 
        This means that there is a path between every pair 
        of vertices. An undirected graph that is not 
        connected is called disconnected. 
        """
        visited = {}

        for v in self.__vertices:
            visited[v] = False

        stack = [next(iter(self.__vertices))] # Some logic to retrieve an element from a set without removing it

        while stack:
            current_vertex = stack.pop()
            visited[current_vertex] = True
            for neighbour in self.adjacentVertices(current_vertex):
                if not visited[neighbour]:
                    stack.append(neighbour)

        return all(visited.values())

    def countConnectedComponents(self):
        """
        Method to count the number of connected components in the graph
        using DFS. In graph theory, a component of an undirected graph is 
        a connected subgraph that is not part of any larger connected subgraph. 
        The components of any graph partition its vertices into disjoint sets, 
        and are the induced subgraphs of those sets. A graph that is itself 
        connected has exactly one component, consisting of the whole graph. 
        Components are sometimes called connected components. Additional
        examples include the following special cases:

        - Empty graph: In an empty graph, each vertex forms a component 
        with one vertex and zero edges. More generally, a component of 
        this type is formed for every isolated vertex in any graph.

        - Connected graph: In a connected graph, there is exactly one component, 
        the whole graph.

        - Forest: In a forest, every component is a tree.

        - Cluster graph: In a cluster graph, every component is a maximal clique. 
        These graphs may be produced as the transitive closures of arbitrary undirected graphs, 
        for which finding the transitive closure is an equivalent formulation of identifying 
        the connected components.
        """
        vertexLabels, edgeLabels, count = {}, {}, 0

        for v in self.__vertices:
            vertexLabels[v] = 'UNEXPLORED'
        for e in self.__edges:
            edgeLabels[e] = 'UNEXPLORED'
        for v in self.__vertices:
            if vertexLabels[v] == 'UNEXPLORED':
                self.__dfs(v, vertexLabels, edgeLabels)
                count += 1
        return count


if __name__ == '__main__':
    simplegraph = EdgeListGraph()
    simplegraph.addVertex(1)
    simplegraph.addVertex(2)
    simplegraph.addVertex(3)
    simplegraph.addEdge(1, 2)
    simplegraph.addEdge(2, 3)

    # Depth-First Print
    print("Depth-First Print")
    simplegraph.depthFirstPrint()
    
    # Print definition of our simple graph
    print("Vertices of G: {}".format(list(simplegraph.vertices())))
    print("Edges of G: {}".format(list(simplegraph.edges())))

    # Print the degree sequence of the graph
    print("Degree sequence of graph: {}".format(simplegraph.getDegreeSequence()))

    # Print the edges incident to specified vertex
    print("Edges incident to vertex {}: {}".format(1, simplegraph.incidentEdges(1)))

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

    # Display the weight of the graph
    print("Weight of graph: {}".format(simplegraph.weightOfGraph()))

    # Print whether the specificied vertices are adjacent
    print("Vertices {} and {} are adjacent in graph: {}".format(1, 3, simplegraph.areAdjacentVertices(1, 3)))

    # Print the edges incident to specified vertex
    print("Edges incident to vertex {}: {}".format(1, simplegraph.incidentEdges(1)))

    # Print definition of our simple graph
    print("Vertices of G: {}".format(list(simplegraph.vertices())))
    print("Edges of G: {}".format(list(simplegraph.edges())))

    # Print the degree sequence of the graph
    print("Degree sequence of graph: {}".format(simplegraph.getDegreeSequence()))

    # Linebreak in CMD
    print("********NEW GRAPH********")

    # Create a second graph
    simplegraph2 = EdgeListGraph()
    simplegraph2.addVertex('a')
    simplegraph2.addVertex('b')
    simplegraph2.addVertex('c')
    simplegraph2.addVertex('d')
    simplegraph2.addVertex('e')
    simplegraph2.addVertex('f')
    simplegraph2.addEdge('a', 'b')
    simplegraph2.addEdge('a', 'c')
    simplegraph2.addEdge('b', 'd')
    simplegraph2.addEdge('c', 'e')
    simplegraph2.addEdge('d', 'f')
    
    # Print the definition of the second graph
    print("Vertices of G: {}".format(list(simplegraph2.vertices())))
    print("Edges of G: {}".format(list(simplegraph2.edges())))

    # Print the degree sequence of the graph
    print("Degree sequence of graph: {}".format(simplegraph2.getDegreeSequence()))

    # Depth-First Print
    print("Depth-First Print")
    simplegraph2.depthFirstPrint()

    # Depth-First Print Recursive
    print("Depth-First Print Recursive")
    simplegraph2.depthFirstPrintRecursive()

    # Depth-First Print from Vertex
    print("Breadth-First Print")
    simplegraph2.breadthFirstPrint()

    # Depth-First Search
    print("Depth-First Search (DFS)")
    simplegraph2.dfs()

    # Breadth-First Search
    print("Breadth-First Search (BFS)")
    simplegraph2.bfs()

    # Check if graph is connected
    print("Graph is connected: {}".format(simplegraph2.isConnected()))

    # Count connected components
    print("Connected components count of graph: {}".format(simplegraph2.countConnectedComponents()))

    # Remove edge
    simplegraph2.removeEdge('e', 'c')

    # Check if graph is connected
    print("Graph is connected: {}".format(simplegraph2.isConnected()))

    # Count connected components
    print("Connected components count of graph: {}".format(simplegraph2.countConnectedComponents()))