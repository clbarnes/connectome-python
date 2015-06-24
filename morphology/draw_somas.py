import json
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


morphology_path = '/home/cbarnes/data/connectome/morphologies.json'
morph = json.load(open(morphology_path, 'r'))


def draw(threeD=True):

    coords = [cell['soma'] for cell in morph.values()]
    xyz = list(zip(*coords))

    fig = plt.figure()

    if threeD:
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(*xyz)
        # ax.autoscale()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.axis('equal')
    else:
        ax1 = fig.add_subplot(1, 3, 1)
        plt.axis('equal')
        plt.xlabel('xyz[0]')
        plt.ylabel('xyz[1]')
        ax2 = fig.add_subplot(1, 3, 2)
        plt.xlabel('xyz[1]')
        plt.ylabel('xyz[2]')
        plt.axis('equal')
        ax3 = fig.add_subplot(1, 3, 3)
        plt.xlabel('xyz[0]')
        plt.ylabel('xyz[2]')
        plt.axis('equal')
        ax1.scatter(xyz[0], xyz[1])
        ax2.scatter(xyz[1], xyz[2])
        ax3.scatter(xyz[0], xyz[2])

    plt.show()

draw(False)