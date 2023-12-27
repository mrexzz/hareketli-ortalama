import ccxt
import pandas as pd
import matplotlib.pyplot as plt

plt.switch_backend('QtAgg')

symbol1 = input("Coin: ")

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
    symbol = symbol1.upper() +"/USDT"
    timeframe = '1h'
    limit = 200
    window = 50

    df = fetch_historical_data(symbol, timeframe, limit)
    df = calculate_moving_average(df, window)

    print(df.tail())  # Hareketli ortalama ve fiyat verilerini yazdır
    plot_chart(df, symbol, window)  # Grafik çizdir


if __name__ == "__main__":
    main()
