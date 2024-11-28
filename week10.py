import matplotlib.pyplot as plt
import numpy as np

def exercise():
    graph_type=["plot","scatter","bar"]
    size=input("size of array: ")

    while not size.isdigit():
        print("Not a digit")
        size=input("size of array: ")
    type=input("type of graph (plot,scatter,bar): ")
    while type.lower() not in graph_type:
        print("not a valid type")
        type=input("type of graph (plot,scatter,bar): ")
    x=np.array([i for i in range(int(size)+1)])
    y=np.array([i**2 for i in range(int(size)+1)])

    if type == "plot":
        plt.plot(x,y,"o-")
    if type == "scatter":
        plt.scatter(x,y)
    if type== "bar":
        plt.bar(x,y)


    plt.show()

exercise()
