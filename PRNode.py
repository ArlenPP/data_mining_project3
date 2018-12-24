import math
import random
class node():
    def __init__(self, value):
        self.parents = []
        self.children = []
        self.node_value = value
        self.pr = random.randint(1,100) / 100
        self.prev_pr = 0
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
        self.iter_pr = []
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
    def cal_PR(self):
        diff = 0
        num = len(self.graph)
        for node in self.graph:
            diff += math.pow((node.pr - node.prev_pr), 2)
        ans = diff / num
        self.iter_pr.append(ans)
        return ans
    def PR_iter(self):
        d = 0.15
        for node in self.graph:
            node.prev_pr = node.pr
        num_node = len(self.graph)
        for node in self.graph:
            sum_pr_parent = 0.0
            for p in node.parents:
                sum_pr_parent += (p.prev_pr / len(p.children))
            node.pr = (d / num_node) + (1 - d)*sum_pr_parent
        num_all_pr = 0.0
        for node in self.graph:
            num_all_pr += node.pr
        for node in self.graph:
            node.pr = node.pr / num_all_pr

    