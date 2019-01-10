import math
import csv
import random
from itertools import combinations
from CommonUtil import read_csv_file, diff, Node
class node():
    def __init__(self, value):
        self.parents = []
        self.children = []
        self.node_value = value
        self.sim = random.randint(1,100) / 100
        self.prev_sim = 0.0
        self.name = value
        self.edge = {}
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
    def cal_sim(self):
        diff = 0
        num = len(self.graph)
        for node in self.graph:
            diff += math.pow((node.sim - node.prev_sim), 2)
        ans = diff / num
        self.iter_pr.append(ans)
        return ans
    def sim(self, node1, node2):
        C = 0.8
        sum_parent_sim = 0
        if(node1.name == node2.name):
            return 1
        node1_p_number = len(node1.parents)
        node2_p_number = len(node2.parents)
        if(node1_p_number == 0 or node2_p_number == 0):
            return 0
        for n1 in node1.parents:
            for n2 in node2.parents:
                sum_parent_sim += self.sim(n1, n2)
        ans = (C/(node1_p_number)*(node2_p_number))*sum_parent_sim
        return ans

    def sim_iter(self):
        for node in self.graph:
            node.prev_sim = node.sim
        node1_p_count = 0
        node2_p_count = 0
        for node1 in self.graph:
            for node2 in self.graph:
                node1.sim = node2.sim = self.sim(node1, node2)

class SimRankGraph():
    def __init__(self, rows, c):
        data = dict()
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                if not rows[i][j] in data:
                    data[rows[i][j]] = Node()
            data[rows[i][0]].add_children(rows[i][1])
            data[rows[i][1]].add_parent(rows[i][0])
        keys = data.keys()
        pairs = list(combinations(keys, 2))
        sim = dict()
        for pair in pairs:
            sim[tuple(sorted(pair))] = random.random()
        self.data = data
        self.sim = sim
        self.c = c
    def iterate(self):
        new_sim = dict()
        for pair in self.sim:
            a_parents = self.data[pair[0]].parents
            b_parents = self.data[pair[1]].parents
            if len(a_parents) * len(b_parents) == 0:
                new_sim[pair] = 0
                continue
            sum = 0
            for a_parent in a_parents:
                for b_parent in b_parents:
                    if a_parent == b_parent:
                        sum += 1
                    else:
                        sum += self.sim[tuple(sorted([a_parent, b_parent]))]
            new_sim[pair] = self.c / (len(a_parents) * len(b_parents)) * sum
        diff_sim = diff(new_sim, self.sim)
        self.sim = new_sim
        return diff_sim
        
        

    