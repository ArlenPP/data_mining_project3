import matplotlib.pyplot as plt
import numpy as np
import csv
import PRNode as node
def PageRank(filename, early_stopping, plot_time):
    G = node.Graph()
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
    for i in range(10000):
        G.PR_iter()
        if((G.cal_PR()) < early_stopping):
            break;
    # print picture
    diff_auth_hub = G.iter_pr[:plot_time] 
    plt.plot(range(1, plot_time + 1), diff_auth_hub)
    plt.yscale('log')
    plt.title("graph 1")
    plt.xlabel('iteration times')
    plt.ylabel('mean variance')
    plt.show()
                                                                                                                                        
if __name__ == "__main__":
    early_stopping = 10 ** -15
    plot_time = 20
    PageRank('./hw3dataset/graph_1.txt', early_stopping, plot_time)