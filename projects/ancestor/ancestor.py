# Will need -> Queue, Graph, earliest ancestor


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    # build out the graph
    # add vertex pairs
    # build edges from back to front
    # BFS and store path
    graph = Graph()
    for pear in ancestors:
        graph.add_vertex(pear[0])
        graph.add_vertex(pear[1])
        graph.add_edge(pear[1], pear[0])
    cue = Queue()
    cue.enqueue([starting_node])
    max_path = 1
    earliest_ancestor = -1
    while cue.size() > 0:
        path = cue.dequeue()
        last = path[-1]
        if (len(path) >= max_path & last < earliest_ancestor) | (len(path) > max_path):
            earliest_ancestor = last
            max_path = len(path)
        for neighbors in graph.vertices[last]:
            copy = list(path)
            copy.append(neighbors)
            cue.enqueue(copy)
    return earliest_ancestor
