import os
import matplotlib as mpl
import pandas as pd
import numpy as np
from brickplot import *
from xlrd import open_workbook
from pandas import ExcelWriter


def extract():
    drain = []
    gate = []
    home_path = './100times/'
    path_dir = os.listdir(home_path)
    for file_name in path_dir:
        print(file_name)
        file_path = os.path.join('%s%s' % (home_path, file_name))
        sheet_names = open_workbook(file_path).sheet_names()
        for sheet_name in sheet_names:
            if 'Data' in sheet_name or 'Append' in sheet_name:
                print(sheet_name)
                df1 = pd.read_excel(file_path, sheet_name=sheet_name)
                DrainI = list(abs(df1.iloc[:, 1]))
                GateI = list(abs(df1.iloc[:, 4]))
                drain.append(DrainI)
                gate.append(GateI)

    writer = ExcelWriter('100times-all-data.xlsx')
    df = pd.DataFrame(drain)
    df.to_excel(writer, 'DrainI', index=False)
    df = pd.DataFrame(gate)
    df.to_excel(writer, 'GateI', index=False)
    writer.save()


def clean(str):
    temp = []
    for i in range(len(str)):
        if str[i] != '':
            temp.append(str[i])
    return temp


def compute():
    file_path = '100times-all-data.xlsx'

    step = 0.005
    num = open_workbook(file_path).sheet_by_name('DrainI').ncols
    vmax = step * (num - 1)
    print(num, vmax)
    sourceV = np.linspace(0, vmax, num)

    mean_drain = []
    std_drain = []
    fluc_drain = []
    num_drain = []

    mean_gate = []
    std_gate = []
    fluc_gate = []
    num_gate = []
    df1 = pd.read_excel(file_path, sheet_name='DrainI', keep_default_na=False)
    df2 = pd.read_excel(file_path, sheet_name='GateI', keep_default_na=False)
    for index in range(len(sourceV)):
        drainI = list(df1.iloc[:, index])
        drainI = clean(drainI)
        mean_drain.append(np.mean(drainI))
        std_drain.append(np.std(drainI))
        fluc_drain.append(np.std(drainI) / np.mean(drainI) * 100)
        num_drain.append(len(drainI))

        gateI = list(df2.iloc[:, index])
        gateI = clean(gateI)
        mean_gate.append(np.mean(gateI))
        std_gate.append(np.std(gateI))
        fluc_gate.append(np.std(gateI) / np.mean(gateI) * 100)
        num_gate.append(len(gateI))

    writer = ExcelWriter('fluctuation.xlsx')
    df = pd.DataFrame({'sourceV': sourceV, 'mean1': mean_drain, 'std1': std_drain, 'fluc1': fluc_drain, 'num1':
        num_drain, 'mean2': mean_gate, 'std2': std_gate, 'fluc2': fluc_gate, 'num2': num_gate})
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()


def plot_fluc():
    pt = TwoAxis()
    pt.config_fig(
        x_label_name='Bias voltage (V)',
        y1_label_name='Current (A)',
        y2_label_name='Fluctuation (%)',
    )
    pt.set_fig()

    file_path = 'fluctuation.xlsx'
    df1 = pd.read_excel(file_path, sheet_name='Sheet1')
    sourceV = list(df1.iloc[:, 0])
    gateI = list(df1.iloc[:, 5])
    fluc_gate = list(df1.iloc[:, 7])

    step = 0.005
    index0 = int(2.5 / step)
    sourceV = sourceV[index0:]
    gateI = gateI[index0:]
    fluc_gate = fluc_gate[index0:]

    size = 0
    linewidth = 3
    l1 = pt.ax1.semilogy(sourceV, gateI, '-o', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{I}_{emission}$')
    l2 = pt.ax2.plot(sourceV, fluc_gate, '--', color='red', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{CV}_{emission}$')

    ls = l1 + l2
    labs = [l.get_label() for l in ls]
    pt.ax1.legend(ls, labs, loc=6, fontsize=pt.legend_font_size + 3)
    plt.tight_layout()
    plt.show()
    # plt.savefig('repeat1.png')


if __name__ == '__main__':
    # extract()
    # compute()
    plot_fluc()