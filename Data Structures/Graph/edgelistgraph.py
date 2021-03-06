import heapq
import sys
sys.path.insert(1, '../')
from Set.disjointset import DisjointSet
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

|V| = n = order, |E| = m = size

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
            raise ValueError('No parallel edges in graph!')
        if s == d:
            raise ValueError('No self loops in graph!')
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
            return sum(1 for e in self.__edges if v == e[0] or v == e[1])

    def order(self):
        """Method to return number of vertices (order) in graph"""
        return len(self.__vertices)

    def size(self):
        """Method to return number of edges (size) in graph"""
        return len(self.__edges)

    def weightOfGraph(self):
        """Method to return the weight of the graph defined as the sum of the weights of all its edges"""
        return sum(w for s, d, w in self.__edges)

    def areAdjacentVertices(self, u, v):
        """Method that returns boolean indictaing whether vertices u and v are adjacent in the graph"""
        if not self.hasVertex(u) or not self.hasVertex(v):
            raise ValueError('Vertex not in the graph!')
        else:    
            return u in self.adjacentVertices(v) and v in self.adjacentVertices(u)
    
    def incidentEdges(self, v):
        """Method to return list of edges incident to v in graph"""
        if not self.hasVertex(v):
            raise ValueError('Vertex not in graph!')
        else:
            return [e for e in self.__edges if v == e[0] or v == e[1]]

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
        French mathematician Charles Pierre Tr??maux as a strategy for 
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
        Plankalk??l programming language, but this was not published 
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

    def findPathDFS(self, source, destination):
        """
        Method to find path from source to desination if it 
        exists in graph using DFS. 
        
        Walk: A walk in a graph is an alternating sequence of 
        vertices and edges. The length of a walk is the number
        of edges. 

        Trail: A trail is a walk with no repeated edges but a
        vertex can be repeated.

        Path: A path is a walk with no repeated vertices. A path
        is always a trail since to repeat an edge you must repeat
        at least one vertex.
        """
        vertexLabels, edgeLabels = {}, {}
        for v in self.__vertices:
            vertexLabels[v] = 'UNEXPLORED'
        for e in self.__edges:
            edgeLabels[e] = 'UNEXPLORED'
        return self.__findPathDFS(source, destination, vertexLabels, edgeLabels)

    def __findPathDFS(self, source, destination, vertexLabels, edgeLabels, stack = []):
        """Helper method to find path from source to destination if it exists in graph using DFS"""
        vertexLabels[source] = 'VISITED' # Mark vertex as visited
        stack.append(source) # Push vertex onto stack as it is on path
    
        if source == destination:
            return stack

        for e in self.incidentEdges(source):
            if edgeLabels[e] == 'UNEXPLORED':
                u = self.oppositeVertexOnEdge(source, e)
                if vertexLabels[u] == 'UNEXPLORED':
                    edgeLabels[e] = 'DISCOVERY'
                    stack.append(e)
                    partialpath = self.__findPathDFS(u, destination, vertexLabels, edgeLabels, stack)
                    if partialpath:
                        return partialpath
                    stack.pop()
                else:
                    edgeLabels[e] = 'BACK'
        stack.pop()

    def hasPathDFS(self, source, destination, visited = set()):
        """Method to return boolean indicating if there is a path from source to destination in graph using DFS"""
        # Base cases / stopping conditions
        if source == destination:
            return True
        if source in visited:
            return False
        # Mark vertex as visited
        visited.add(source)
        # Iterate through neighours of source vertex
        for neighbour in self.adjacentVertices(source):
            # Inductive step: Do some work to shrink the problem space
            if self.hasPathDFS(neighbour, destination, visited):
                return True
        return False
           
    def isCyclic(self):
        """
        Method to detect simple cycle in graph using DFS.
        Simple cycle: A simple cycle is a non-empty trail 
        in a graph with no repeated vertices (except for 
        the beginning and ending vertex). A cycle is a path
        that is also a circuit and a closed walk.
        """
        visited = set()
        for vertex in self.__vertices:
            if vertex not in visited:
                # Call recursive helper function to detect cycle in different DFS trees
                if self.__isCyclic(vertex, visited):
                    return True
        return False

    def __isCyclic(self, vertex, visited, parent = None):
        """Helper Method to detect cycle in graph using DFS"""
        visited.add(vertex) # Mark vertex as visited
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.adjacentVertices(vertex):
            if neighbour not in visited:
                if self.__isCyclic(neighbour, visited, vertex):
                    return True
            # If an adjacent vertex is visited and is not the
            # parent of the current vertex then there is a cycle
            elif parent != neighbour:
                return True
        return False

    def isCutEdge(self, e):
        """Method to check whether an edge is a cut-edge/bridge"""
        if self.hasEdge(e[0], e[1], e[2]):
            wG = self.countConnectedComponents()
            self.removeEdge(e[0], e[1], e[2])
            wGWithoutE = self.countConnectedComponents()
            self.addEdge(e[0], e[1], e[2])
            return wGWithoutE > wG

    def findAllCutEdges(self):
        """Method to find all cut edges in graph"""
        return set(e for e in self.__edges if self.isCutEdge(e))

    def isCutVertex(self, v):
        """Method to check if a vertex is a cut-vertex"""
        if self.hasVertex(v):
            wG = self.countConnectedComponents()
            tmp = self.incidentEdges(v)
            self.removeVertex(v)
            wGWithoutV = self.countConnectedComponents()
            self.addVertex(v)
            for e in tmp:
                self.addEdge(e[0], e[1], e[2])
            return wGWithoutV > wG

    def findAllCutVertices(self):
        """Method to find all cut-vertices in graph"""
        return set(v for v in self.__vertices if self.isCutVertex(v))

    def isTree(self):
        """Method to check if a graph is a tree"""
        return self.isConnected() and not self.isCyclic()

    def shortestPathUnweighted(self, source, destination):
        """
        Method to find shortest path between two vertices
        in graph with distance between two vertices being 
        the number of edges between them as we are assuming
        that edges are unwieghted.

        Params:
            source(): The start vertex
            destination(): The end vertex

        Returns:
            distance: The shortest path length between source and destination measured in number of edges
            -1: If there is no such path between source and destination
        """
        visited, q = set(), [(source, 0)] # Distance from start is 0 initially
        while q:
            current, distance = q.pop(0)
            if current == destination:
                return distance
            for neighbour in self.adjacentVertices(current):
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, distance + 1))
        return -1

    def kruskalsAlgorithm(self):
        """
        Kruskal's algorithm finds a minimum spanning forest of 
        an undirected edge-weighted graph. If the graph is 
        connected, it finds a minimum spanning tree. (A minimum 
        spanning tree of a connected graph is a subset of the 
        edges that forms a tree that includes every vertex, where 
        the sum of the weights of all the edges in the tree is 
        minimized. For a disconnected graph, a minimum 
        spanning forest is composed of a minimum spanning tree 
        for each connected component.) It is a greedy 
        algorithm in graph theory as in each step it adds the 
        next lowest-weight edge that will not form a cycle to 
        the minimum spanning forest.

        1. Sort all the edges in non-decreasing order of their weight. 
        2. Pick the smallest edge. Check if it forms a cycle 
        with the spanning tree formed so far. If cycle is not 
        formed, include this edge. Else, discard it. 
        3. Repeat step 2 until there are (V-1) edges in the 
        spanning tree.
        """
        # Minimum Spanning Tree represented as a set of edges
        mst, min_cost = set(), 0
        # Disjoint set to determine if  two vertices are aprt of same tree
        ds = DisjointSet()
        # 1. Sort edges in ascending order
        copy_of_edges = sorted(self.__edges, key=lambda e:e[2])
        copy_of_vertices = self.__vertices.copy()
        # 2. and 3.  
        for v in copy_of_vertices:
            ds.make_set(v)
        for e in copy_of_edges:
            if ds.find(e[0]) != ds.find(e[1]):
                mst.add(e)
                min_cost += e[2]
                ds.union(e[0], e[1])
        return min_cost

    def primsAlgorithm(self):
        """
        Prim's algorithm (also known as Jarn??k's algorithm) 
        is a greedy algorithm that finds a minimum spanning 
        tree for a weighted undirected graph. . The algorithm 
        operates by building this tree one vertex at a time, 
        from an arbitrary starting vertex, at each step adding 
        the cheapest possible connection from the tree to 
        another vertex.

        1. Initialize a tree with a single vertex, chosen 
        arbitrarily from the graph.
        2. Grow the tree by one edge: of the edges that 
        connect the tree to vertices not yet in the tree, 
        find the minimum-weight edge, and transfer it to 
        the tree.
        3. Repeat step 2 (until all vertices are in the tree).

        IMPORTANT POINT ON HEAPQ: According to the example 
        from the documentation, you can use tuples, and it 
        will sort by the first element of the tuple
        https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
        """
        # Weight of minimum spanning tree
        min_weight = 0
        # Visited set to keep track of vertices already seen
        visited = set()
        # Arbitrary vertex to begin growing mst cloud
        random_vertex = next(iter(self.__vertices))
        # Heap-based priority queue to grow mst cloud
        q = [(0, random_vertex)]
        # Growing minimum spanning tree cloud
        while q:
            weight, u = heapq.heappop(q)
            if u in visited:
                continue
            else:
                min_weight += weight
                visited.add(u)
                for e in self.incidentEdges(u):
                    neighbour = self.oppositeVertexOnEdge(u, e)
                    neighbour_weight = e[2]
                    if neighbour not in visited:
                        heapq.heappush(q, (neighbour_weight, neighbour))
        return min_weight

    def dijkstrasAlgorithm(self, source):
        """
        Dijkstra's algorithm is an algorithm for finding 
        the shortest paths between nodes in a weighted
        undirected graph. Dijkstra's original algorithm 
        found the shortest path between two given nodes, 
        but a more common variant fixes a single node as 
        the "source" node and finds shortest paths from 
        the source to all other nodes in the graph, 
        producing a shortest-path tree. Dijkstra's 
        algorithm uses a data structure for storing and 
        querying partial solutions sorted by distance from 
        the start. While the original algorithm uses a 
        min-priority queue. In some fields, artificial 
        intelligence in particular, Dijkstra's algorithm or 
        a variant of it is known as uniform cost search and 
        formulated as an instance of the more general idea 
        of best-first search.
        """    
        # Visited set to keep track of vertices already seen
        visited = set()
        # Heap-based priority queue to store and query partial solutions
        q = []
        # Create distances dictionary
        distances = {}
        # Set tentative distances for all vertices
        for u in self.__vertices:
            if u == source:
                distances[u] = 0
                q.append([0, source])
            else:
                distances[u] = float('inf')
        # Form shortest paths tree
        while q:
            distance, u = heapq.heappop(q)
            if u in visited:
                continue
            else:
                visited.add(u)
                for e in self.incidentEdges(u):
                    neighbour = self.oppositeVertexOnEdge(u, e)
                    neighbour_weight = e[2]
                    if neighbour not in visited:
                        new_distance = distance + neighbour_weight
                        distances[neighbour] = new_distance if new_distance < distances[neighbour] else distances[neighbour]
                        heapq.heappush(q, [distances[neighbour], neighbour])
        return distances

    def aStarAlgorithm(self, source, destination):
        """
        A* is a graph traversal and path search algorithm, 
        which is often used in many fields of computer 
        science due to its completeness, optimality, and 
        optimal efficiency. One major practical drawback 
        is its O(b^d) space complexity, as it stores all 
        generated nodes in memory. Compared to Dijkstra's 
        algorithm, the A* algorithm only finds the 
        shortest path from a specified source to a 
        specified goal, and not the shortest-path tree 
        from a specified source to all possible goals. 
        This is a necessary trade-off for using a 
        specific-goal-directed heuristic.

        A* was created as part of the Shakey project, which 
        had the aim of building a mobile robot that could 
        plan its own actions. A* is an informed search 
        algorithm, or a best-first search, meaning that it 
        is formulated in terms of weighted graphs: starting 
        from a specific starting node of a graph, it aims to 
        find a path to the given goal node having the 
        smallest cost (least distance travelled, shortest 
        time, etc.). It does this by maintaining a tree of 
        paths originating at the start node and extending 
        those paths one edge at a time until its termination 
        criterion is satisfied.

        At each iteration of its main loop, A* needs to 
        determine which of its paths to extend. It does 
        so based on the cost of the path and an estimate 
        of the cost required to extend the path all the 
        way to the goal. Specifically, A* selects the path 
        that minimizes f(n) = g(n) + h(n) where n is the 
        next node on the path, g(n) is the cost of the path 
        from the start node to n, and h(n) is a heuristic 
        function that estimates the cost of the cheapest 
        path from n to the goal.

        Typical implementations of A* use a priority queue 
        to perform the repeated selection of minimum 
        (estimated) cost nodes to expand. This priority 
        queue is known as the open set or fringe. At each 
        step of the algorithm, the node with the lowest f(x) 
        value is removed from the queue, the f and g values 
        of its neighbors are updated accordingly, and these 
        neighbors are added to the queue. The algorithm 
        continues until a removed node (thus the node with 
        the lowest f value out of all fringe nodes) is a goal 
        node.[b] The f value of that goal is then also the 
        cost of the shortest path, since h at the goal is zero 
        in an admissible heuristic.
        """
        # Heap-based priority queue representing the open set
        # or fringe or frontier which are the discovered vertices
        # that may need to be (re-)expanded
        fringe = [] 
        # Variable to keep track of order in which vertices
        # enter the fringe. We use this to break ties when
        # two vertices have the same fScore
        count = 0
        # Dictionary with key: vertex, value: vertex. For 
        # vertex v, came_from[v] is the vertex immediately 
        # preceding it on the cheapest path from start
        # to v currently known.
        came_from = {}
        # Dictionary with key: vertex, value: number. For 
        # vertex v, g_score[v] is the cost of the cheapest 
        # path from start to v currently known. 
        g_score = {vertex: float('inf') for vertex in self.__vertices}
        # Set the g_score of the source vertex to 0.
        g_score[source] = 0
        # Dictionary with key: vertex, value: number. For 
        # vertex v, f_score[v] := g_score[v] + h(v). f_score[v] 
        # represents our current best guess as to how cheap 
        # a path could be from start to finish if it goes 
        # through v.
        f_score = {vertex: float('inf') for vertex in self.__vertices}
        # Set the f_score of the source vertex to h(source).
        f_score[source] = self.__h(source, destination)
        # Add source to fringe
        heapq.heappush(fringe, (f_score[source], count, source))
        # Process vertices in A* fashion
        while fringe:
            current = heapq.heappop(fringe)
            if current[2] == destination:
                return self.__reconstruct_path(came_from, current[2])
            for e in self.incidentEdges(current[2]):
                neighbour = self.oppositeVertexOnEdge(current[2], e)
                tentative_g_score = g_score[current[2]] + e[2]
                if tentative_g_score < g_score[neighbour]:
                    # This path to neighbour is better than any previous one, record it!
                    came_from[neighbour] = current[2]
                    g_score[neighbour] = tentative_g_score
                    f_score[neighbour] = g_score[neighbour] + self.__h(neighbour, destination)
                    if neighbour not in fringe:
                        count += 1
                        heapq.heappush(fringe, (f_score[neighbour], count, neighbour))
        return False

    def __h(self, source, destination):
        """
        Heuristic function to estimate distance from source
        to destination. This is an A* helper function.
        """
        estimate = 0
        path = self.findPathDFS(source, destination)
        for step in path:
            if isinstance(step, tuple):
                estimate += step[2]
        return estimate

    def __reconstruct_path(self, came_from, current):
        """
        A* algorithm helper method to reconstruct path
        from current to the source
        """
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current)
        return ' -> '.join(map(str, total_path))

g = EdgeListGraph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(7, 8, 7)
g.addEdge(7, 6, 1)
g.addEdge(6, 8, 6)
g.addEdge(6, 5, 2)
g.addEdge(2, 8, 2)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(5, 4, 10)
g.addEdge(4, 3, 9)
print(g.dijkstrasAlgorithm(0))
print(g.findPathDFS(0, 6))
print(g.aStarAlgorithm(0, 6))