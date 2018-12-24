import math
import random
class node():
    def __init__(self, value):
        self.parents = []
        self.children = []
        self.node_value = value
        self.prev_hub = 0
        self.prev_authority = 0
        self.hub = random.randint(1,100) / 10
        self.authority = random.randint(1,100) / 10
        self.name = value
    def addParent(self, p):
        self.parents.append(p)
    def addChild(self, c):
        self.children.append(c)
    def prientParent(self):
        for p in self.parents:
            print(p.name)
    def prientChildren(self):
        for c in self.children:
            print(c.name)

class Graph():
    def __init__(self):
        self.graph = []
        self.iter_hub = []
        self.iter_auth = []
    def find_node(self, value):
        for node in self.graph:
            if(value == node.name):
                return node
        return None
    def addNode(self, n):
        self.graph.append(n)
    def printNode(self):
        if(len(self.graph) <= 0):
            print("No thing in graph")
            return
        for node in self.graph:
            print(node.name)
    # for hits
    def cal_hub(self):
        diff = 0
        num = len(self.graph)
        for node in self.graph:
            diff += math.pow((node.hub - node.prev_hub), 2)
        ans = diff / num
        self.iter_hub.append(ans)
        return ans
    def cal_authority(self):
        diff = 0
        num = len(self.graph)
        for node in self.graph:
            diff += math.pow((node.authority - node.prev_authority), 2)
        ans = diff / num
        self.iter_auth.append(ans)
        return ans
    def hits_iter(self):
        for node in self.graph:
            node.prev_authority = node.authority
            node.prev_hub = node.hub
        # cal hub and authority
        for node in self.graph:
            hub_new = 0.0;
            for child in node.children:
                hub_new += child.prev_authority
                child.authority = node.prev_hub
            node.hub = hub_new
        # normalization
        all_hub = 0.0
        all_auth = 0.0
        for node in self.graph:
            all_hub += node.hub
            all_auth += node.authority
        for node in self.graph:
            node.hub = node.hub / all_hub
            node.authority = node.authority / all_auth

        