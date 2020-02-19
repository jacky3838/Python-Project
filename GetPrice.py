import pandas as pd
import pandas_datareader.data as web
import datetime
import time
import threading  # 引入threading
import matplotlib.pyplot as plt
import LineNotify

def sleep():
    while (True):
        print(time.ctime().__str__())
        msg = time.ctime().__str__()
        LineNotify.lineNotifyMessage(msg)
        time.sleep(30)

# 用 yahoo finance
def plot(stock_id, stock_bak_id):
    start = datetime.datetime(2016, 9, 1)
    end = datetime.date.today()
    # 台灣股市的話要用 股票代號 加上 .TW
    df_1 = web.DataReader(stock_id+'.TW', 'yahoo', start, end)
    df_1.tail(10)
    df_2= web.DataReader(stock_bak_id+'.TW', 'yahoo', start, end)
    df_2.tail(10)

    ma50 = df_1['Close'].rolling(50).mean()
    df_1['Close'].plot()

    ma50.plot()

    ma50 = df_2['Close'].rolling(50).mean()
    df_2['Close'].plot()
    ma50.plot()
    filename = "result.png"
    plt.savefig(filename,dpi=500,bbox_inches = 'tight')
    LineNotify.lineNotifyImage("Hello ~下圖視查詢結果" ,filename)
#thread_1 = threading.Thread(target=sleep_3)  # 例項化一個執行緒物件，使執行緒執行這個函式
#thread_1.start()  # 啟動這個執行緒
