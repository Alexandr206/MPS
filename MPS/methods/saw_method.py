def __count__(row, weights):
    return sum([row[i] * weights[i] for i in range(len(row))])


def saw_method(dataset: list[list], name, weights: list):
    max_score = 0
    max_score_ind = 0
    res = []
    print('\n---------МЕТОД SAW---------\n')
    for ind, elem in enumerate(dataset):
        c = round(__count__(elem, weights), 3)
        if c > max_score:
            max_score = c
            max_score_ind = ind
        res.append(c)
        print(f'Счет {name[ind]}: {c}')
    print(f'\n{name[max_score_ind]} лучше всего. Его счет: {max_score}\n')
    print('\n---------------------------\n')
    return res
