import numpy as np
from tabulate import tabulate
from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    name = ['Paint 3D','Photoshop','Gravit Designer','Vectr','SVG‑Edit']
    har =['Цена.','Функциональная пригодность','Временные характеристики','Удобство использования','Уровень производительности','Сопровождаемость','Эффективность']
    m = np.array([[0, 33.4, 66.9, 97, 60.3, 100, 60.3],
                  [3, 94.7, 33.2, 98, 90.7, 100, 95.8],
                  [1, 39.8, 73.7, 88, 83.5, 25, 61.4],
                  [1, 47.3, 39.5, 83, 71.4, 30, 66.7],
                  [2, 58.7, 55.6, 76, 54.9, 40, 73.9]])
    wei = [0.01, 0.2, 0.05, 0.25, 0.09, 0.15,0.25]

    dh = DecisionHelper(m, wei,name)
    print("------Исходная таблица------")
    print(tabulate(m, headers=har, tablefmt="grid", showindex=name, numalign="center"))
    print("----------------------------")
    dh.saw()
    dh.topsis()
    dh.electre()
