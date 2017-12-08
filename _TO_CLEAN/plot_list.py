import matplotlib.pyplot as plt


def plot_function(xvalues, yvalues, title="", xlabel="", ylabel="", show=True):
    plt.plot(xvalues, yvalues)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if show:
        plt.show()


if __name__ == '__main__':
    plot_function([1, 1.5, 4, 4.7, 9], [2, 4, 6, 8, 10])
