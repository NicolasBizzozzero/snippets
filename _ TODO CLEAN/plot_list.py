import matplotlib.pyplot as plt


def plot_function(xvalues, yvalues, title="", xlabel="", ylabel="", show=True):
    plt.plot(xvalues, yvalues, label="")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # plt.xlim(xmax=0.8, xmin=0.1)
    # plt.ylim(ymax=1.0, ymin=0.5)
    # plt.legend(loc=4)

    if show:
        plt.show()


if __name__ == '__main__':
    plot_function([1, 1.5, 4, 4.7, 9], [2, 4, 6, 8, 10])
