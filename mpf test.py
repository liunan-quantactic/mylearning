import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import sys
sys.path.append('F:\\quantactic')
from quantactic import sql_connector
#   录入数据
user2 = 'root'
pw2 = '7026155@Liu'
h2 = '127.0.0.1'
sch2 = 'astocks'
p = 3306
engine = sql_connector(user2,pw2,h2,p,sch2)

start=20160101
end=20210831
code='000002.SZ'
df_query = "select td,codenum,open,high,low,chg,close,vol from astocks.market where codenum=\'"+code+"\' " \
             "and td>="+str(start)+" and td<="+str(end)+" order by td;"
df = pd.read_sql(df_query,engine,index_col='td')
df.index=pd.to_datetime(df.index,format='%Y%m%d')
df.columns=['codenum','open','high','low','change','close','volume']
#------取其中100个数据作为测试
plot_data = df.iloc[100: 200]
# 读取显示区间最后一个交易日的数据
last_data = plot_data.iloc[-1]
#------------一些参数设置-----------------
my_color = mpf.make_marketcolors(up='r',
                                 down='g',
                                 edge='inherit',
                                 wick='inherit',
                                 volume='inherit')
my_style = mpf.make_mpf_style(marketcolors=my_color,
                                  figcolor='(0.82, 0.83, 0.85)',
                                  gridcolor='(0.82, 0.83, 0.85)')


title_font = {'fontname': 'Arial',
              'size':     '16',
              'color':    'black',
              'weight':   'bold',
              'va':       'bottom',
              'ha':       'center'}
large_red_font = {'fontname': 'Arial',
                  'size':     '24',
                  'color':    'red',
                  'weight':   'bold',
                  'va':       'bottom'}
large_green_font = {'fontname': 'Arial',
                    'size':     '24',
                    'color':    'green',
                    'weight':   'bold',
                    'va':       'bottom'}
small_red_font = {'fontname': 'Arial',
                  'size':     '12',
                  'color':    'red',
                  'weight':   'bold',
                  'va':       'bottom'}
small_green_font = {'fontname': 'Arial',
                    'size':     '12',
                    'color':    'green',
                    'weight':   'bold',
                    'va':       'bottom'}
normal_label_font = {'fontname': 'Arial',
                     'size':     '12',
                     'color':    'black',
                     'weight':   'normal',
                     'va':       'bottom',
                     'ha':       'right'}
normal_font = {'fontname': 'Arial',
               'size':     '12',
               'color':    'black',
               'weight':   'normal',
               'va':       'bottom',
               'ha':       'left'}


class InterTrade:
    def __init__(self,df,my_style):
        self.pressed = False
        self.xpress = None

        # 初始化交互式K线图对象，历史数据作为唯一的参数用于初始化对象
        self.data = df
        self.style = my_style
        # 设置初始化的K线图显示区间起点为0，即显示第0到第99个交易日的数据（前100个数据）
        self.idx_start = 0
        self.idx_range = 100
        # 设置ax1图表中显示的均线类型
        self.avg_type = 'ma'
        self.indicator = 'macd'

        #----------------画图测试----------------------------
        # 初始化figure对象，在figure上建立三个Axes对象并分别设置好它们的位置和基本属性
        # 使用mpf.figure()函数可以返回一个figure对象，从而进入External Axes Mode，从而实现对Axes对象和figure对象的自由控制
        self.fig = mpf.figure(style=my_style, figsize=(12, 8), facecolor=(0.82, 0.83, 0.85))
        fig = self.fig
        # 添加三个图表，四个数字分别代表图表左下角在figure中的坐标，以及图表的宽（0.88）、高（0.60）
        self.ax1 = fig.add_axes([0.08, 0.25, 0.88, 0.60])
        # 添加第二张图表时，使用sharex关键字指明与ax1在x轴上对齐，且共用x轴
        self.ax2 = fig.add_axes([0.08, 0.15, 0.88, 0.10], sharex=self.ax1)
        self.ax2.set_ylabel('volume')
        # 初始化figure对象，在figure上预先放置文本并设置格式，文本内容根据需要显示的数据实时更新
        self.t1 = fig.text(0.50, 0.94, '000002.SZ', **title_font)
        self.t2 = fig.text(0.12, 0.90, 'open/close: ', **normal_label_font)
        self.t3 = fig.text(0.14, 0.89, f'{np.round(last_data["open"], 3)} / {np.round(last_data["close"], 3)}', **large_red_font)
        #self.t4 = fig.text(0.14, 0.86, f'{last_data["change"]}', **small_red_font)
        #self.t5 = fig.text(0.22, 0.86, f'[{np.round(last_data["pct_change"], 2)}%]', **small_red_font)
        self.t6 = fig.text(0.12, 0.86, f'{last_data.name.date()}', **normal_label_font)
        self.t7 = fig.text(0.40, 0.90, 'high: ', **normal_label_font)
        self.t8 = fig.text(0.40, 0.90, f'{last_data["high"]}', **small_red_font)
        self.t9 = fig.text(0.40, 0.86, 'low: ', **normal_label_font)
        self.t10 = fig.text(0.40, 0.86, f'{last_data["low"]}', **small_green_font)
        self.t11 = fig.text(0.55, 0.90, 'vol(1million): ', **normal_label_font)
        self.t12 = fig.text(0.55, 0.90, f'{np.round(last_data["volume"] / 10000, 3)}', **normal_font)
        self.t13 = fig.text(0.55, 0.86, 'amt(100million): ', **normal_label_font)
        #self.t14 = fig.text(0.55, 0.86, f'{last_data["value"]}', **normal_font)
        #self.t15 = fig.text(0.70, 0.90, 'limit up: ', **normal_label_font)
        #self.t16 = fig.text(0.70, 0.90, f'{last_data["upper_lim"]}', **small_red_font)
        #self.t17 = fig.text(0.70, 0.86, 'limit down: ', **normal_label_font)
        #self.t18 = fig.text(0.70, 0.86, f'{last_data["lower_lim"]}', **small_green_font)
        #self.t19 = fig.text(0.85, 0.90, 'average: ', **normal_label_font)
        #self.t20 = fig.text(0.85, 0.90, f'{np.round(last_data["average"], 3)}', **normal_font)
        #self.t21 = fig.text(0.85, 0.86, 'preclose: ', **normal_label_font)
        #self.22 = fig.text(0.85, 0.86, f'{last_data["last_close"]}', **normal_font)

        #------------初始化数据结束
        # 下面的代码在__init__()中，告诉matplotlib哪些回调函数用于响应哪些事件
        # 鼠标按下事件与self.on_press回调函数绑定
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        # 鼠标按键释放事件与self.on_release回调函数绑定
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        # 鼠标移动事件与self.on_motion回调函数绑定
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        # 将新增的回调函数on_scroll与鼠标滚轮事件绑定起来
        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)

    def refresh_plot(self, idx_start, idx_range):
        """ 根据最新的参数，重新绘制整个图表
        """
        all_data = self.data
        plot_data = all_data.iloc[idx_start: idx_start + idx_range]
        ap = []
        '''
        # 添加K线图重叠均线，根据均线类型添加移动均线或布林带线
        if self.avg_type == 'ma':
            ap.append(mpf.make_addplot(plot_data[['MA5', 'MA10', 'MA20', 'MA60']], ax=self.ax1))
        elif self.avg_type == 'bb':
            ap.append(mpf.make_addplot(plot_data[['bb-u', 'bb-m', 'bb-l']], ax=self.ax1))
        # 添加指标，根据指标类型添加MACD或RSI或DEMA
        if self.indicator == 'macd':
            ap.append(mpf.make_addplot(plot_data[['macd-m', 'macd-s']], ylabel='macd', ax=self.ax3))
            bar_r = np.where(plot_data['macd-h'] > 0, plot_data['macd-h'], 0)
            bar_g = np.where(plot_data['macd-h'] <= 0, plot_data['macd-h'], 0)
            ap.append(mpf.make_addplot(bar_r, type='bar', color='red', ax=self.ax3))
            ap.append(mpf.make_addplot(bar_g, type='bar', color='green', ax=self.ax3))
        elif self.indicator == 'rsi':
            ap.append(mpf.make_addplot([75] * len(plot_data), color=(0.75, 0.6, 0.6), ax=self.ax3))
            ap.append(mpf.make_addplot([30] * len(plot_data), color=(0.6, 0.75, 0.6), ax=self.ax3))
            ap.append(mpf.make_addplot(plot_data['rsi'], ylabel='rsi', ax=self.ax3))
        else:  # indicator == 'dema'
            ap.append(mpf.make_addplot(plot_data['dema'], ylabel='dema', ax=self.ax3))'''
        # 绘制图表
        mpf.plot(plot_data,
                 ax=self.ax1,
                 volume=self.ax2,
                 addplot=ap,
                 type='candle',
                 style=self.style,
                 datetime_format='%Y-%m',
                 xrotation=0)
        self.fig.show()

    def refresh_texts(self, display_data):
        """ 更新K线图上的价格文本
        """
        # display_data是一个交易日内的所有数据，将这些数据分别填入figure对象上的文本中
        self.t3.set_text(f'{np.round(display_data["open"], 3)} / {np.round(display_data["close"], 3)}')
        #self.t4.set_text(f'{np.round(display_data["change"], 3)}')
        #self.t5.set_text(f'[{np.round(display_data["pct_change"], 3)}%]')
        self.t6.set_text(f'{display_data.name.date()}')
        self.t8.set_text(f'{np.round(display_data["high"], 3)}')
        self.t10.set_text(f'{np.round(display_data["low"], 3)}')
        self.t12.set_text(f'{np.round(display_data["volume"] / 10000, 3)}')
        #self.t14.set_text(f'{display_data["value"]}')
        #self.t16.set_text(f'{np.round(display_data["upper_lim"], 3)}')
        #self.t18.set_text(f'{np.round(display_data["lower_lim"], 3)}')
        #self.t20.set_text(f'{np.round(display_data["average"], 3)}')
        #self.t22.set_text(f'{np.round(display_data["last_close"], 3)}')
        # 根据本交易日的价格变动值确定开盘价、收盘价的显示颜色
        if display_data['change'] > 0:  # 如果今日变动额大于0，即今天价格高于昨天，今天价格显示为红色
            close_number_color = 'red'
        elif display_data['change'] < 0:  # 如果今日变动额小于0，即今天价格低于昨天，今天价格显示为绿色
            close_number_color = 'green'
        else:
            close_number_color = 'black'
        self.t3.set_color(close_number_color)
        #self.t4.set_color(close_number_color)
        #self.t5.set_color(close_number_color)

    def on_press(self, event):
        # 当鼠标按键按下时，调用该函数，event为事件信息，是一个dict对象，包含事件相关的信息
        # 如坐标、按键类型、是否在某个Axes对象内等等
        # event.inaxes可用于判断事件发生时，鼠标是否在某个Axes内，在这里我们指定，只有鼠
        # 标在ax1内时，才能平移K线图，否则就退出事件处理函数
        if not event.inaxes == self.ax1:
            return
        # 检查是否按下了鼠标左键，如果不是左键，同样退出事件处理函数
        if event.button != 1:
            return
        # 如果鼠标在ax1范围内，且按下了左键，条件满足，设置鼠标状态为pressed
        self.pressed = True
        # 同时记录鼠标按下时的x坐标，退出函数，等待鼠标移动事件发生
        self.xpress = event.xdata

    # 鼠标移动事件处理
    def on_motion(self, event):
        # 如果鼠标按键没有按下pressed == False，则什么都不做，退出处理函数
        if not self.pressed:
            return
        # 如果移动出了ax1的范围，也退出处理函数
        if not event.inaxes == self.ax1:
            return
        # 如果鼠标在ax1范围内，且左键按下，则开始计算dx，并根据dx计算新的K线图起点
        dx = int(event.xdata - self.xpress)
        # 前面介绍过了，新的起点N(new) = N - dx
        new_start = self.idx_start - dx
        # 设定平移的左右界限，如果平移后超出界限，则不再平移
        if new_start <= 0:
            new_start = 0
        if new_start >= len(self.data) - 100:
            new_start = len(self.data) - 100
            # 清除各个图表Axes中的内容，准备以新的起点重新绘制
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        # 更新图表上的文字、以新的起点开始绘制K线图
        self.refresh_texts(self.data.iloc[new_start])
        self.refresh_plot(new_start,self.idx_range)

    # 鼠标按键释放
    def on_release(self, event):
        # 按键释放后，设置鼠标的pressed为False
        self.pressed = False
        # 此时别忘了最后一次更新K线图的起点，否则下次拖拽的时候就不会从这次的起点开始移动了
        dx = int(event.xdata - self.xpress)
        self.idx_start -= dx
        if self.idx_start <= 0:
            self.idx_start = 0
        if self.idx_start >= len(self.data) - 100:
            self.idx_start = len(self.data) - 100

    def on_scroll(self, event):
        # 仅当鼠标滚轮在axes1范围内滚动时起作用
        if event.inaxes != self.ax1:
            return
        if event.button == 'down':
            # 缩小20%显示范围
            scale_factor = 0.8
        if event.button == 'up':
            # 放大20%显示范围
            scale_factor = 1.2
        # 设置K线的显示范围大小
        self.idx_range = int(self.idx_range * scale_factor)
        # 限定可以显示的K线图的范围，最少不能少于30个交易日，最大不能超过当前位置与
        # K线数据总长度的差
        data_length = len(self.data)
        if self.idx_range >= data_length - self.idx_start:
            self.idx_range = data_length - self.idx_start
        if self.idx_range <= 30:
            self.idx_range = 30
            # 更新图表（注意因为多了一个参数idx_range，refresh_plot函数也有所改动）
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.refresh_texts(self.data.iloc[self.idx_start])
        self.refresh_plot(self.idx_start, self.idx_range)

c=InterTrade(df,my_style)
c.idx_start = 150
c.idx_range = 100
c.refresh_texts(df.iloc[249])
c.refresh_plot(150, 100)