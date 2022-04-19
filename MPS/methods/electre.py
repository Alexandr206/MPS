import numpy as np


def __normalize__(dataset):
    n = dataset.shape[0]
    m = dataset.shape[1]
    n_dataset = np.zeros((n, m))
    for j in range(m):
        _max = max(dataset[:, j])
        n_dataset[:, j] = [dataset[i, j] / _max for i in range(n)]
    return n_dataset


def __concordance_matrix__(dataset, weigths):
    concordance = np.zeros((dataset.shape[0], dataset.shape[0]))
    for i in range(0, concordance.shape[0]):
        for j in range(0, concordance.shape[1]):
            concordance[i, j] = sum(weigths[k] for k in range(0, dataset.shape[1]) if (dataset[i, k] >= dataset[j, k]))
    return concordance


def __discordance_matrix__(dataset):
    n = dataset.shape[0]
    discordance = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            discordance[i, j] = round(max(dataset[j, :] - dataset[i, :]), 2)
    return discordance


# Function: Dominance Matrix
def __dominance_matrix__(concordance, discordance, c_lim, d_lim):
    dominance = np.zeros((concordance.shape[0], concordance.shape[0]))
    for i in range(0, dominance.shape[0]):
        for j in range(0, dominance.shape[1]):
            if concordance[i, j] >= c_lim and discordance[i, j] <= d_lim and i != j:
                dominance[i, j] = 1
    return dominance


def __lim_concordance_list__(concordance):
    return [round(min(x), 4) for x in concordance]


def __lim_discordance_list__(discordance):
    return [round(max(x), 4) for x in discordance]


def __prepare_text_info__(dominance,name):
    dominated = [(f'{name[i]}', elem) for i, elem in enumerate(dominance)]
    dominated = sorted(dominated, key=lambda k: sum(k[1]), reverse=True)
    info = '\n---------МЕТОД ELECTRE---------\n'
    for ind, el in enumerate(dominated):
        info += f'Место №{ind + 1}: {el[0]}\n'
    return info


def electre(dataset,name, weigths, c_lim=0.45, d_lim=0.5):
    dataset = np.array(dataset)
    dataset = __normalize__(dataset)
    concordance = __concordance_matrix__(dataset, weigths)
    discordance = __discordance_matrix__(dataset)
    dominance = __dominance_matrix__(concordance, discordance, c_lim, d_lim)
    print(__prepare_text_info__(dominance,name))
    print('\n-------------------------------\n')
    return concordance, discordance, dominance

