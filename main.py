# encoding : utf-8

from tkinter.ttk import *
from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint
import sys
from 货币缩写库 import 缩写库 as sxk
from 汇率查询 import GetRoot
import threading

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
win_width, win_height = work_area[2], work_area[3]

class windows():
	def __init__(self):
		# 主窗体
		self.root = Tk()
		self.root.title('汇率计算器         **本程序需联网')
		self.root.geometry('%dx%d+%d+%d'%(win_width // 1.3, win_height // 1.3, (win_width - win_width // 1.3) // 2, (win_height - win_height // 1.3) // 2))
		# 标签框1
		self.label1 = Label(self.root, text='目标金额：', font=("黑体",18))
		self.label1.place(relx=0, rely=0.1, relwidth=0.1, relheight=0.1)
		# 输入框1
		self.text1 = Entry(self.root, font=("黑体",18))
		self.text1.place(relx=0.1, rely=0.1, relwidth=0.25, relheight=0.1)
		# 选择框1
		self.var1 = StringVar()
		self.var1.set("目标币种")
		self.comb1 = Combobox(self.root, textvariable=self.var1, font=("黑体",18), values=sxk)
		self.comb1.place(relx=0, rely=0.25, relwidth=0.35, relheight=0.1)
		# 选择框2
		self.var2 = StringVar()
		self.var2.set("持有币种")
		self.comb2 = Combobox(self.root, textvariable=self.var2, font=("黑体",18), values=sxk)
		self.comb2.place(relx=0, rely=0.4, relwidth=0.35, relheight=0.1)
		# 按钮1
		self.btn1 = Button(self.root, text='获取汇率情况', command=self.command_get, font=("黑体",18))
		self.btn1.place(relx=0.1, rely=0.55, relwidth=0.15, relheight=0.15)
		# 按钮2
		self.btn1 = Button(self.root, text='开始计算价格', command=self.command_run, font=("黑体",18))
		self.btn1.place(relx=0.1, rely=0.7, relwidth=0.15, relheight=0.15)
		# 标签框2
		self.label2 = Label(self.root, text='今日汇率情况：', font=("黑体",18))
		self.label2.place(relx=0.5, rely=0, relwidth=0.48, relheight=0.48)
		# 标签框3
		self.label3 = Label(self.root, text='计算结果：', font=("黑体",18))
		self.label3.place(relx=0.5, rely=0.5, relwidth=0.48, relheight=0.48)
		# 状态栏
		self.statusbar = Label(self.root, text="当前无任务。", bd=1, relief=SUNKEN, anchor=W)
		self.statusbar.pack(side=BOTTOM, fill=X)

	def command_get(self):
		try:
			self.statusbar.configure(text="正在获取今日汇率。。。")
			if self.comb1.current() >= 0:
				flag1 = self.comb1.current()
			else:
				flag1 = 2 # 阿根廷比索
			if self.comb2.current() >= 0 and self.comb1.current() != self.comb2.current():
				flag2 = self.comb2.current()
			else:
				flag2 = 82 # 人民币
			Get_Float = GetRoot(sxk[flag2][1], sxk[flag1][1])
			ReturnString = "1 %s = %s %s"%(sxk[flag1][1], str(Get_Float), sxk[flag2][1])
			self.label2.configure(text="今日汇率情况：" + ReturnString)
			self.statusbar.configure(text="今日汇率获取获取完成。")
			return Get_Float, sxk[flag2][1]
		except:
			self.statusbar.configure(text="过程错误，请重新获取。")

	def command_run(self):
		try:
			self.statusbar.configure(text="正在获取今日汇率。。。")
			try:
				innumber = float(self.text1.get())
			except:
				innumber = 0.0
			Get_Float = self.command_get()
			self.statusbar.configure(text="正在计算结果。。。")
			self.label3.configure(text="计算结果：" + str(Get_Float[0]*innumber) + " " + Get_Float[1])
			self.statusbar.configure(text="计算结束。")
		except:
			self.statusbar.configure(text="过程错误，请重新获取。")

	def run(self):
		self.root.mainloop()

	def destroy(self):
		sys.exit()

def main():
	root = windows()
	root.run()
	root.destroy()

if __name__ == '__main__':
	main()