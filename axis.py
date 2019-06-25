"""
The axis module provides

:class:`OneAxis`
    One subplot, one axis

:class:`TwoAxis`
    One subplot, two axes

:class:`FourAxis`
    Two subplots, four axes

"""

import matplotlib.pyplot as plt


class OneAxis():
    def __init__(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111)

        self.fig_width = 8
        self.fig_height = 6

        self.line_width = 2
        self.spine_width = 3

        self.label_font_size = 32
        self.legend_font_size = 22
        self.title_font_size = 28
        self.tick_font_size = 24

        self.legend_name = ''
        self.x_label_name = 'x'
        self.y_label_name = 'y'
        self.fig_name = 'general_plot'
        self.fig_title = ''

        self.dpi = 150
        self.gridon = True

        self.x_color = 'k'
        self.y_color = 'k'

    def config_fig(self, **kwargs):
        self.fig_width = kwargs.get('fig_width', self.fig_width)
        self.fig_height = kwargs.get('fig_height', self.fig_height)
        self.line_width = kwargs.get('line_width', self.line_width)
        self.spine_width = kwargs.get('spine_width', self.spine_width)
        self.label_font_size = kwargs.get('label_font_size', self.label_font_size)
        self.legend_font_size = kwargs.get('legend_font_size', self.legend_font_size)
        self.title_font_size = kwargs.get('title_font_size', self.title_font_size)
        self.tick_font_size = kwargs.get('tick_font_size', self.tick_font_size)
        self.legend_name = kwargs.get('legend_name', self.legend_name)
        self.x_label_name = kwargs.get('x_label_name', self.x_label_name)
        self.y_label_name = kwargs.get('y_label_name', self.y_label_name)
        self.fig_name = kwargs.get('fig_name', self.fig_name)
        self.fig_title = kwargs.get('fig_title', self.fig_title)
        self.dpi = kwargs.get('dpi', self.dpi)
        self.gridon = kwargs.get('gridon', self.gridon)
        self.x_color = kwargs.get('x_color', self.x_color)
        self.y_color = kwargs.get('y_color', self.y_color)

    def set_fig(self):
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig.set_figwidth(self.fig_width)
        self.fig.set_figheight(self.fig_height)

        self.ax1.spines['bottom'].set_linewidth(self.spine_width)
        self.ax1.spines['left'].set_linewidth(self.spine_width)
        self.ax1.spines['right'].set_linewidth(self.spine_width)
        self.ax1.spines['top'].set_linewidth(self.spine_width)

        self.ax1.set_title(self.fig_title, fontdict={'fontsize': self.title_font_size})
        self.ax1.set_xlabel(self.x_label_name)
        self.ax1.set_ylabel(self.y_label_name)

        self.ax1.grid(b=self.gridon)

        self.ax1.xaxis.label.set_color(self.x_color)
        self.ax1.xaxis.label.set_fontsize(self.label_font_size)
        self.ax1.tick_params(axis='x', colors=self.x_color)
        for label in self.ax1.get_xticklabels():
            label.set_color(self.x_color)
            label.set_fontsize(self.tick_font_size)

        self.ax1.yaxis.label.set_color(self.y_color)
        self.ax1.yaxis.label.set_fontsize(self.label_font_size)
        self.ax1.tick_params(axis='y', colors=self.y_color)
        for label in self.ax1.get_yticklabels():
            label.set_color(self.y_color)
            label.set_fontsize(self.tick_font_size)


class TwoAxis():
    def __init__(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax2 = self.ax1.twinx()

        self.fig_width = 8
        self.fig_height = 6

        self.line_width = 2
        self.spine_width = 3

        self.label_font_size = 32
        self.legend_font_size = 22
        self.title_font_size = 28
        self.tick_font_size = 24

        self.legend_name = ''
        self.x_label_name = 'x'
        self.y1_label_name = 'y1'
        self.y2_label_name = 'y2'
        self.fig_name = 'general_plot'
        self.fig_title = ''

        self.dpi = 150
        self.gridon = True

        self.x_color = 'k'
        self.y1_color = 'k'
        self.y2_color = 'k'

    def config_fig(self, **kwargs):
        self.fig_width = kwargs.get('fig_width', self.fig_width)
        self.fig_height = kwargs.get('fig_height', self.fig_height)
        self.line_width = kwargs.get('line_width', self.line_width)
        self.spine_width = kwargs.get('spine_width', self.spine_width)
        self.label_font_size = kwargs.get('label_font_size', self.label_font_size)
        self.legend_font_size = kwargs.get('legend_font_size', self.legend_font_size)
        self.title_font_size = kwargs.get('title_font_size', self.title_font_size)
        self.tick_font_size = kwargs.get('tick_font_size', self.tick_font_size)
        self.legend_name = kwargs.get('legend_name', self.legend_name)
        self.x_label_name = kwargs.get('x_label_name', self.x_label_name)
        self.y1_label_name = kwargs.get('y1_label_name', self.y1_label_name)
        self.y2_label_name = kwargs.get('y2_label_name', self.y2_label_name)
        self.fig_name = kwargs.get('fig_name', self.fig_name)
        self.fig_title = kwargs.get('fig_title', self.fig_title)
        self.dpi = kwargs.get('dpi', self.dpi)
        self.gridon = kwargs.get('gridon', self.gridon)
        self.x_color = kwargs.get('x_color', self.x_color)
        self.y1_color = kwargs.get('y1_color', self.y1_color)
        self.y2_color = kwargs.get('y2_color', self.y2_color)

    def set_fig(self):
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig.set_figwidth(self.fig_width)
        self.fig.set_figheight(self.fig_height)

        self.ax1.spines['bottom'].set_linewidth(self.spine_width)
        self.ax1.spines['left'].set_linewidth(self.spine_width)
        self.ax1.spines['right'].set_linewidth(self.spine_width)
        self.ax1.spines['top'].set_linewidth(self.spine_width)

        self.ax1.set_title(self.fig_title, fontdict={'fontsize': self.title_font_size})
        self.ax1.set_xlabel(self.x_label_name)
        self.ax1.set_ylabel(self.y1_label_name)
        self.ax2.set_ylabel(self.y2_label_name)

        self.ax1.grid(b=self.gridon)

        self.ax1.xaxis.label.set_color(self.x_color)
        self.ax1.xaxis.label.set_fontsize(self.label_font_size)
        self.ax1.tick_params(axis='x', colors=self.x_color)
        for label in self.ax1.get_xticklabels():
            label.set_color(self.x_color)
            label.set_fontsize(self.tick_font_size)

        self.ax1.yaxis.label.set_color(self.y1_color)
        self.ax1.yaxis.label.set_fontsize(self.label_font_size)
        self.ax1.tick_params(axis='y', colors=self.y1_color)
        for label in self.ax1.get_yticklabels():
            label.set_color(self.y1_color)
            label.set_fontsize(self.tick_font_size)

        self.ax2.yaxis.label.set_color(self.y2_color)
        self.ax2.yaxis.label.set_fontsize(self.label_font_size)
        self.ax2.tick_params(axis='y', colors=self.y2_color)
        for label in self.ax2.get_yticklabels():
            label.set_color(self.y2_color)
            label.set_fontsize(self.tick_font_size)


class FourAxis():
    def __init__(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.ax1.twinx()
        self.ax3 = self.fig.add_subplot(212)
        self.ax4 = self.ax3.twinx()

        self.fig_width = 17
        self.fig_height = 6

        self.line_width = 2
        self.spine_width = 3

        self.label_font_size = 32
        self.legend_font_size = 22
        self.title_font_size = 28
        self.tick_font_size = 24

        self.legend_name = ''
        self.x1_label_name = 'x'
        self.x2_label_name = 'x'
        self.y1_label_name = 'y1'
        self.y2_label_name = 'y2'
        self.y3_label_name = 'y3'
        self.y4_label_name = 'y4'
        self.fig_name = 'general_plot'
        self.fig_title = ''

        self.dpi = 150
        self.gridon = True

        self.x1_color = 'k'
        self.x2_color = 'k'
        self.y1_color = 'k'
        self.y2_color = 'k'
        self.y3_color = 'k'
        self.y4_color = 'k'

    def config_fig(self, **kwargs):
        self.fig_width = kwargs.get('fig_width', self.fig_width)
        self.fig_height = kwargs.get('fig_height', self.fig_height)
        self.line_width = kwargs.get('line_width', self.line_width)
        self.spine_width = kwargs.get('spine_width', self.spine_width)
        self.label_font_size = kwargs.get('label_font_size', self.label_font_size)
        self.legend_font_size = kwargs.get('legend_font_size', self.legend_font_size)
        self.title_font_size = kwargs.get('title_font_size', self.title_font_size)
        self.tick_font_size = kwargs.get('tick_font_size', self.tick_font_size)
        self.legend_name = kwargs.get('legend_name', self.legend_name)
        self.x1_label_name = kwargs.get('x1_label_name', self.x1_label_name)
        self.y1_label_name = kwargs.get('y1_label_name', self.y1_label_name)
        self.y2_label_name = kwargs.get('y2_label_name', self.y2_label_name)
        self.x2_label_name = kwargs.get('x2_label_name', self.x2_label_name)
        self.y3_label_name = kwargs.get('y3_label_name', self.y3_label_name)
        self.y4_label_name = kwargs.get('y4_label_name', self.y4_label_name)
        self.fig_name = kwargs.get('fig_name', self.fig_name)
        self.fig_title = kwargs.get('fig_title', self.fig_title)
        self.dpi = kwargs.get('dpi', self.dpi)
        self.gridon = kwargs.get('gridon', self.gridon)
        self.x1_color = kwargs.get('x1_color', self.x1_color)
        self.x2_color = kwargs.get('x2_color', self.x2_color)
        self.y1_color = kwargs.get('y1_color', self.y1_color)
        self.y2_color = kwargs.get('y2_color', self.y2_color)
        self.y3_color = kwargs.get('y3_color', self.y3_color)
        self.y4_color = kwargs.get('y4_color', self.y4_color)

    def set_fig(self):
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig.set_figwidth(self.fig_width)
        self.fig.set_figheight(self.fig_height)

        self.ax1.spines['bottom'].set_linewidth(self.spine_width)
        self.ax1.spines['left'].set_linewidth(self.spine_width)
        self.ax1.spines['right'].set_linewidth(self.spine_width)
        self.ax1.spines['top'].set_linewidth(self.spine_width)

        self.ax1.set_title(self.fig_title, fontdict={'fontsize': self.title_font_size})
        self.ax1.set_xlabel(self.x1_label_name)
        self.ax1.set_ylabel(self.y1_label_name)
        self.ax2.set_ylabel(self.y2_label_name)

        self.ax1.grid(b=self.gridon)

        self.ax1.xaxis.label.set_color(self.x1_color)
        self.ax1.xaxis.label.set_fontsize(self.label_font_size)
        self.ax1.tick_params(axis='x', colors=self.x1_color)
        for label in self.ax1.get_xticklabels():
            label.set_color(self.x1_color)
            label.set_fontsize(self.tick_font_size)

        self.ax1.yaxis.label.set_color(self.y1_color)
        self.ax1.yaxis.label.set_fontsize(self.label_font_size)
        self.ax1.tick_params(axis='y', colors=self.y1_color)
        for label in self.ax1.get_yticklabels():
            label.set_color(self.y1_color)
            label.set_fontsize(self.tick_font_size)

        self.ax2.yaxis.label.set_color(self.y2_color)
        self.ax2.yaxis.label.set_fontsize(self.label_font_size)
        self.ax2.tick_params(axis='y', colors=self.y2_color)
        for label in self.ax2.get_yticklabels():
            label.set_color(self.y2_color)
            label.set_fontsize(self.tick_font_size)

        self.ax3.spines['bottom'].set_linewidth(self.spine_width)
        self.ax3.spines['left'].set_linewidth(self.spine_width)
        self.ax3.spines['right'].set_linewidth(self.spine_width)
        self.ax3.spines['top'].set_linewidth(self.spine_width)

        self.ax3.set_xlabel(self.x2_label_name)
        self.ax3.set_ylabel(self.y3_label_name)
        self.ax4.set_ylabel(self.y4_label_name)

        self.ax3.xaxis.label.set_color(self.x2_color)
        self.ax3.xaxis.label.set_fontsize(self.label_font_size)
        self.ax3.tick_params(axis='x', colors=self.x2_color)
        for label in self.ax3.get_xticklabels():
            label.set_color(self.x2_color)
            label.set_fontsize(self.tick_font_size)

        self.ax3.yaxis.label.set_color(self.y3_color)
        self.ax3.yaxis.label.set_fontsize(self.label_font_size)
        self.ax3.tick_params(axis='y', colors=self.y3_color)
        for label in self.ax3.get_yticklabels():
            label.set_color(self.y3_color)
            label.set_fontsize(self.tick_font_size)

        self.ax4.yaxis.label.set_color(self.y4_color)
        self.ax4.yaxis.label.set_fontsize(self.label_font_size)
        self.ax4.tick_params(axis='y', colors=self.y4_color)
        for label in self.ax2.get_yticklabels():
            label.set_color(self.y4_color)
            label.set_fontsize(self.tick_font_size)