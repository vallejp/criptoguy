import matplotlib.pylab as plt
import numpy as np


def rules(left, mid, right, rule):
    """
    Here, we set some binary operations the define the Wolfram CA rule
    For example, the rule 250 we have (where 11111010 is 250 in binary:
    111 --> 1
    110 --> 1
    101 --> 1
    100 --> 1
    011 --> 1
    010 --> 0
    001 --> 1
    000 --> 0
    :param left: the left cell
    :param mid: the middle cell
    :param right: the right cell
    :param rule: the decimal number
    that your binary form defines the output
    :return: Return the next generation cell
    """
    idx = (left << 2 | mid << 1 | right)
    return rule >> idx & 1


def generations(cells, rule, counter):
    """
    :param cells: The initial matrix, where the middle element
    of the first row is one and the others elements are zeros
    :param rule: The Wolfram CA rule
    :return: The final matrix applied the Wolfram CA
    """

    for i in range(len(cells) - 1):
        for j in range(1, len(cells[i]) - 1):
            left = cells[i][j - 1]
            mid = cells[i][j]
            right = cells[i][j + 1]
            cells[i + 1][j] = rules(left, mid, right, rule)

        plt.imshow(cells, cmap='Greys', interpolation='nearest')
        plt.title("Rule {}".format(rule), loc='right')
        plt.axis('off')
        plt.savefig("figures/fig{}.png".format(counter))
        counter += 1

    return cells, counter


def CAconstuction(steps, width):
    cells = np.zeros((steps, width), dtype=int)
    cells[0][len(cells[0]) // 2] = 1
    return cells


"""
Creating cellular automata figures for some rules
"""
setRules = (30, 54, 60, 62, 90, 94, 102, 110, 122, 126, 150, 158)
steps = 50
width = 101
counter = 0

for i in setRules:
    cells = CAconstuction(steps, width)  # Initial matrix
    cells, counter = generations(cells, i, counter)


print(counter)
