import matplotlib.pyplot as plt
import simNode as node
import numpy as np
import csv
from CommonUtil import read_csv_file
import time
def SimRank(filename, early_stopping, plot_time):
    G = node.Graph()
    # c = 0.5直接設定在G裡面了
    # read csv and create graph
    with open(filename, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            n = G.find_node(row[0])
            if(n == None):
                n = node.node(row[0])
                G.graph.append(n)
                n2 = G.find_node(row[1])
                if(n2 == None):
                    n2 = node.node(row[1])
                    G.graph.append(n2)
                    n2.addParent(n)
                    n.addChild(n2)
                else:
                    n.addChild(n2)
                    n2.addParent(n)
            else:
                n2 = G.find_node(row[1])
                if(n2 == None):
                    n2 = node.node(row[1])
                    G.graph.append(n2)
                    n2.addParent(n)
                    n.addChild(n2)
                else:
                    n.addChild(n2)
                    n2.addParent(n)
    # iteration
    for i in range(1000):
        G.sim_iter()
        if((G.cal_sim()) < early_stopping):
            break;
    # print picture
    diff_sim = G.iter_pr[:plot_time] 
    plt.plot(range(1, plot_time + 1), diff_sim)
    plt.yscale('log')
    plt.title("graph 1")
    plt.xlabel('iteration times')
    plt.ylabel('mean variance')
    plt.show()
                                                                                                                                        
if __name__ == "__main__":
    early_stopping = 10 ** -15
    plot_time = 20
    it_total = 10000
    C = 0.5
    filename = './hw3dataset/graph_5.txt'
    # SimRank(filename, early_stopping, plot_time)

    sim_rank_graph = node.SimRankGraph(read_csv_file(filename), C)
    diff_sim = [0] * plot_time
    first = True
    start=time.time()
    for j in range(0, it_total):
        d = sim_rank_graph.iterate()
        if j < plot_time:
            diff_sim[j] = d
        if d < early_stopping and first:
            end = time.time()
            print(end - start)
            first=False
        if d < early_stopping and j >= plot_time:
            break
    # plot
    # plt.plot(range(1, plot_time + 1), diff_sim)
    # plt.yscale('log')
    # plt.title("graph 5")
    # plt.xlabel('iteration times')
    # plt.ylabel('mean variance')
    # plt.show()