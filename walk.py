import time
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

N_STEPS = int(1e2)
N_RUNS = int(1e5)
BIAS = 0.5

def walk(n_steps):
    displacements = np.zeros(n_steps)
    displacement = 0
    for i in range(n_steps):
        if np.random.random() > BIAS:
            displacement += 1
        else:
            displacement -= 1
        displacements[i] = displacement
    return displacements


if __name__ == '__main__':
    paths = np.zeros((N_RUNS, N_STEPS))
    for i in tqdm(range(N_RUNS)):
        paths[i, :] = walk(N_STEPS)

    plt.figure()
    plt.plot(range(N_STEPS), paths[0])
    plt.show()

    for step in range(0, N_STEPS, 10):
        plt.figure()
        plt.hist(paths[:, step], bins=100)
        plt.title('Step ' + str(step+1))
        plt.xlabel('Distance')
        plt.ylabel('Number of samples')
        plt.show()
