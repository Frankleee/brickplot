import os
import matplotlib as mpl
import pandas as pd
import numpy as np
from brickplot import *
from xlrd import open_workbook
from pandas import ExcelWriter


def extract():  # 提取和筛选数据
    drain = []  # 定义两个列表，分别存放传导电流和发射电流数据
    gate = []
    home_path = './100times/'  # xls文件所在文件夹
    path_dir = os.listdir(home_path)  # 文件夹中所有文件名的列表
    for file_name in path_dir:  # 遍历文件夹提取数据
        print(file_name)
        file_path = os.path.join('%s%s' % (home_path, file_name))  # 用文件夹路径和文件名生成文件路径
        sheet_names = open_workbook(file_path).sheet_names()  # 打开该文件，列出sheet名
        for sheet_name in sheet_names:  # 遍历sheet名
            if 'Data' in sheet_name or 'Append' in sheet_name:  # 名字中含有'Data'或'Append‘是目标sheet
                print(sheet_name)
                df1 = pd.read_excel(file_path, sheet_name=sheet_name)  # 读取该sheet中所有数据
                DrainI = list(abs(df1.iloc[:, 1]))  # 提取DrainI和GateI所在列
                GateI = list(abs(df1.iloc[:, 4]))
                drain.append(DrainI)  # 存放
                gate.append(GateI)

    writer = ExcelWriter('100times-all-data.xlsx')  # 把提取得到的数据保存到Excel表格
    df = pd.DataFrame(drain)
    df.to_excel(writer, 'DrainI', index=False)  # 100次测试的DrainI数据放在'DrainI'sheet里
    df = pd.DataFrame(gate)
    df.to_excel(writer, 'GateI', index=False)  # 100次测试的GateI数据放在'GateI'sheet里
    writer.save()


def clean(str):  # 去除列表中的缺失值，否则无法计算均值和标准差
    temp = []
    for i in range(len(str)):
        if str[i] != '':
            temp.append(str[i])
    return temp


def compute():  # 计算均值、标准差、变异系数
    file_path = '100times-all-data.xlsx'  # 打开刚刚得到的Excel

    step = 0.005  # 取点间隔0.005V
    num = open_workbook(file_path).sheet_by_name('DrainI').ncols  # 读取DrainV的取点数
    vmax = step * (num - 1)
    # print(num, vmax)
    DrainV = np.linspace(0, vmax, num)  # 生成DrainV的列表

    mean_drain = []  # 定义空列表用来存放数据
    std_drain = []
    fluc_drain = []
    num_drain = []

    mean_gate = []
    std_gate = []
    fluc_gate = []
    num_gate = []
    df1 = pd.read_excel(file_path, sheet_name='DrainI', keep_default_na=False)  # 分别读取DrainI和GateI数据
    df2 = pd.read_excel(file_path, sheet_name='GateI', keep_default_na=False)
    for index in range(len(DrainV)):  # 每一列数据代表某各电压下多次测试的数据
        drainI = list(df1.iloc[:, index])
        drainI = clean(drainI)  # 去除缺失值，缺失值是不同次测试下扫描范围不同导致的
        mean_drain.append(np.mean(drainI))  # 计算均值标准差
        std_drain.append(np.std(drainI))
        fluc_drain.append(np.std(drainI) / np.mean(drainI) * 100)
        num_drain.append(len(drainI))  # 同样因为不同次测试下扫描范围不同，某电压的测试次数也不同

        gateI = list(df2.iloc[:, index])
        gateI = clean(gateI)
        mean_gate.append(np.mean(gateI))
        std_gate.append(np.std(gateI))
        fluc_gate.append(np.std(gateI) / np.mean(gateI) * 100)
        num_gate.append(len(gateI))

    writer = ExcelWriter('fluctuation.xlsx')  # 将数据保存到Excel的一个Sheet里
    df = pd.DataFrame({'DrainV': DrainV, 'mean1': mean_drain, 'std1': std_drain, 'fluc1': fluc_drain, 'num1':
        num_drain, 'mean2': mean_gate, 'std2': std_gate, 'fluc2': fluc_gate, 'num2': num_gate})
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()


def plot_all1():  # 作图，所有次数的drainI画在一张图上
    pt = OneAxis()  # 基于Matplotlib包装的brickplot包，单个纵轴的图
    pt.config_fig(
        x_label_name='Bias voltage (V)',
        y_label_name='Conduction current (A)',
    )
    pt.set_fig()

    file_path = '100times-all-data.xlsx'  # 打开文件
    df1 = pd.read_excel(file_path, sheet_name='DrainI', keep_default_na=False)  # 分别读取DrainI和GateI数据
    num = open_workbook(file_path).sheet_by_name('DrainI').nrows - 1

    size = 0
    linewidth = 1.5
    for i in range(num):
        step = 0.005
        gateI = list(df1.iloc[i, :])
        gateI = clean(gateI)  # 去除缺失值，不然容易出错
        drainV = [step * i for i in range(len(gateI))]
        pt.ax1.plot(drainV, gateI, '-o', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2)

    plt.tight_layout()
    # plt.show()
    plt.savefig('all-drain.png')


def plot_all2():  # 作图，所有次数的gateI画在一张图上
    pt = OneAxis()  # 单个纵轴的图
    pt.config_fig(
        x_label_name='Bias voltage (V)',
        y_label_name='Emission current (A)',
    )
    pt.set_fig()

    file_path = '100times-all-data.xlsx'  # 打开刚刚得到的Excel
    df2 = pd.read_excel(file_path, sheet_name='GateI', keep_default_na=False)
    num = open_workbook(file_path).sheet_by_name('DrainI').nrows - 1

    size = 0
    linewidth = 1.5
    for i in range(num):
        step = 0.005
        gateI = list(df2.iloc[i, :])
        gateI = clean(gateI)  # 去除缺失值，不然容易出错
        drainV = [step * i for i in range(len(gateI))]
        pt.ax1.semilogy(drainV, gateI, '-o', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2)

    plt.tight_layout()
    # plt.show()
    plt.savefig('all-gate.png')


def plot_fluc1():  # 均值和稳定性作图
    pt = TwoAxis()  # 两个纵轴的图
    pt.config_fig(  # 设置各轴名称
        x_label_name='Bias voltage (V)',
        y1_label_name='Current (A)',
        y2_label_name='Fluctuation (%)',
    )
    pt.set_fig()

    file_path = 'fluctuation.xlsx'  # 读取处理过的drainI的均值和标准差
    df1 = pd.read_excel(file_path, sheet_name='Sheet1')
    drainV = list(df1.iloc[:, 0])
    drainI = list(df1.iloc[:, 1])
    fluc_drain = list(df1.iloc[:, 3])

    step = 0.005  # 2.5V之前的信息信息少，只画2.5V之后的数据
    index0 = int(2.5 / step)
    drainV = drainV[index0:]
    drainI = drainI[index0:]
    fluc_drain = fluc_drain[index0:]

    size = 0
    linewidth = 3
    l1 = pt.ax1.semilogy(drainV, drainI, '-o', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{I}_{conduction}$')
    l2 = pt.ax2.plot(drainV, fluc_drain, '--', color='red', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{CV}_{conduction}$')

    ls = l1 + l2  # 图例设置
    labs = [l.get_label() for l in ls]
    pt.ax1.legend(ls, labs, loc=8, fontsize=pt.legend_font_size + 3)
    plt.tight_layout()  # 优化显示效果
    # plt.show()
    plt.savefig('fluc-drain.png')


def plot_fluc2():  # 均值和稳定性作图
    pt = TwoAxis()  # 基于Matplotlib包装的brickplot包，两个纵轴的图
    pt.config_fig(  # 设置各轴名称
        x_label_name='Bias voltage (V)',
        y1_label_name='Current (A)',
        y2_label_name='Fluctuation (%)',
    )
    pt.set_fig()

    file_path = 'fluctuation.xlsx'  # 读取处理过的gateI的均值和标准差
    df1 = pd.read_excel(file_path, sheet_name='Sheet1')
    drainV = list(df1.iloc[:, 0])
    gateI = list(df1.iloc[:, 5])
    fluc_gate = list(df1.iloc[:, 7])

    step = 0.005  # 2.5V之前的信息信息少，只画2.5V之后的数据
    index0 = int(2.5 / step)
    drainV = drainV[index0:]
    gateI = gateI[index0:]
    fluc_gate = fluc_gate[index0:]

    size = 0
    linewidth = 3
    l1 = pt.ax1.semilogy(drainV, gateI, '-o', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{I}_{emission}$')
    l2 = pt.ax2.plot(drainV, fluc_gate, '--', color='red', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{CV}_{emission}$')

    ls = l1 + l2  # 图例设置
    labs = [l.get_label() for l in ls]
    pt.ax1.legend(ls, labs, loc=6, fontsize=pt.legend_font_size + 3)
    plt.tight_layout()  # 优化显示效果
    # plt.show()
    plt.savefig('fluc-gate.png')


def plot_error_bar():  # 以errorbar的形式作图，包括conduction current和emisison current
    pt = TwoAxis()
    pt.config_fig(
        x_label_name='Bias voltage (V)',
        y1_label_name='Conduction current (A)',
        y2_label_name='Emission current (A)',
    )
    pt.set_fig()

    file_path = 'fluctuation.xlsx'  # 读取数据
    df1 = pd.read_excel(file_path, sheet_name='Sheet1')
    drainV = list(df1.iloc[:, 0])
    mean_drain = list(df1.iloc[:, 1])
    std_drain = list(df1.iloc[:, 2])
    mean_gate = list(df1.iloc[:, 5])
    std_gate = list(df1.iloc[:, 6])

    step = 0.005  # 截取2.5V之后的数据，也可以用改坐标轴显示范围的方式实现
    index0 = int(2.8 / step)
    drainV = drainV[index0:]
    mean_drain = mean_drain[index0:]
    std_drain = std_drain[index0:]
    mean_gate = mean_gate[index0:]
    std_gate = std_gate[index0:]

    pt.ax1.errorbar(drainV, mean_drain, std_drain, ecolor='red')  # errorbar作图，坐标轴改成对数坐标
    pt.ax1.set_yscale('log')
    pt.ax2.errorbar(drainV, mean_gate, std_gate, ecolor='red')
    pt.ax2.set_yscale('log')

    plt.tight_layout()
    # plt.show()
    plt.savefig('errorbar.png')


def plot_stages():  # 不同偏压下稳定性
    pt = OneAxis()  # 单个纵轴的图
    pt.config_fig(  #
        x_label_name='number',
        y_label_name='Emission current (A)',
    )
    pt.set_fig()

    file_path = '100times-all-data.xlsx'  # 读取处理过的gateI的均值和标准差
    df1 = pd.read_excel(file_path, sheet_name='GateI')

    voltages = np.linspace(3.1, 3.7, 7)  # 取几个偏压值
    step = 0.005
    index = [int(voltage / step) for voltage in voltages]

    size = 5
    linewidth = 0
    for i in index:
        gateI = list(df1.iloc[:, i])
        num = range(len(gateI))
        pt.ax1.semilogy(num, gateI, '-o', linewidth = linewidth, ms = size, markerfacecolor = 'None', markeredgewidth = 2, label='$\it{I}_{emission}$')

    plt.tight_layout()
    # plt.show()
    plt.savefig('stages.png')


if __name__ == '__main__':
    # extract()
    # compute()
    # plot_all1()
    # plot_all2()
    # plot_fluc1()
    # plot_fluc2()
    # plot_error_bar()
    plot_stages()