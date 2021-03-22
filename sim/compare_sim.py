import matplotlib.pyplot as plt

#Reference
#https://benalexkeen.com/bar-charts-in-matplotlib/
def compare(algos,inters):
    x_cor = [i for i, _ in enumerate(algos)]
    plt.bar(x_cor, inters, color='green')
    plt.xlabel("Algorithm")
    plt.ylabel("Number of Interrupts")
    plt.title("Algorithm vs Number of interrupts (Lower is better)")
    plt.xticks(x_cor, algos)
    plt.show()
