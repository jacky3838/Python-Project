#import LineNotify

#msg = "123456"
#LineNotify.lineNotifyMessage(msg)
# Import yfinance
import yfinance as yf
# Plot the close prices
import matplotlib.pyplot as plt
import tkinter as tk
import math
import GetUrlData
import GetPrice
window = tk.Tk()
window.title('張震琳機器人')
window.geometry('400x300')
window.configure(background='pink1')

def start():

    GetPrice.plot(stock_entry.get(), stock_bak_entry.get())
    #GetPrice.plot("2330","2454")

def stop():
    result = '測試抓取資料'
    result_label.configure(text=result)
    price = GetUrlData.getPrice(stock_entry.get())
    result_label.configure(text=price)

header_label = tk.Label(window, text='股票代碼')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
stock_entry = tk.Entry(height_frame)
stock_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
stock_bak_entry = tk.Entry(weight_frame)
stock_bak_entry.pack(side=tk.LEFT)




btn_start = tk.Button(window, text='比較圖', command=start)
btn_start.pack()

btn_stop= tk.Button(window, text='取得個股報價', command=stop)
btn_stop.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()


