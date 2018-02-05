import matplotlib.pyplot as plt


def create_plots():
    fig = plt.figure(figsize=(14, 7))
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4])

    fig.savefig("test.pdf")
    fig.savefig("test.png")


if __name__ == "__main__":
    create_plots()
