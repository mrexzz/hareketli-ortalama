import ccxt
import pandas as pd
import matplotlib.pyplot as plt
from tradingview_ta import TA_Handler, Interval, Exchange
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.switch_backend('QtAgg')

symbol1 = input("Hisse: ")

def fetch_historical_data(symbol, timeframe, limit):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

def calculate_moving_average(df, window):
    df['ma'] = df['close'].rolling(window=window).mean()
    return df

def plot_chart(df, symbol, window):
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label=f'{symbol} fiyat')
    plt.plot(df['ma'], label=f'{symbol} {window}-hareketli ortalama', color='red')
    plt.title(f'{symbol} 50 GÜNLÜK HAREKETLİ ORTALAMA')
    plt.xlabel('ZAMAN')
    plt.ylabel('FİYAT')
    plt.legend()
    plt.show()

def main():
    symbol = symbol1 +"/USDT"
    timeframe = '1h'
    limit = 200
    window = 50

    df = fetch_historical_data(symbol, timeframe, limit)
    df = calculate_moving_average(df, window)

    print(df.tail())  # Hareketli ortalama ve fiyat verilerini yazdır
    plot_chart(df, symbol, window)  # Grafik çizdir

'''url = "https://fintables.com/son-bilancolar"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
fiyat = soup.find_all("span",attrs={"class":"font-semibold text-shared-danger-solid-01"})
print(fiyat)'''

'''country = input("Hissenin işlem gördüğü ülke:")
hisse_pys = input("Hissenin işlem gördüğü piyasa:")
hisse_adı = input("Hissenin adı:")
hisse = TA_Handler(
    symbol= hisse_adı,
    screener= country,
    exchange=hisse_pys,
    interval=Interval.INTERVAL_1_DAY,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
print(hisse.get_analysis().summary)'''


""""
ad = input("hisse adı giriniz:")
ortalama = input("hareketli ortalamanın altında mı?:(y/n)")
rsi = input("Rsi sinyal verdi mi?:(y/n)")
puan = 0

if(ortalama == "y"):
    puan = puan+1
    print(puan)
if(ortalama != "y" or ortalama != "n"):
    print("yanlış bir değer girdiniz...")
elif(ortalama =="n"):
    puan = puan-1

if(rsi == "y"):
    puan = puan+1
    print(puan)
if(rsi != "y" or rsi != "n"):
    print("yanlış bir değer girdiniz...")
elif(rsi =="n"):
    puan = puan-1

print(ad +" : "+ str(puan)) 

else: 
    print("yeni bir değer giriniz")

"""

if __name__ == "__main__":
    main()
