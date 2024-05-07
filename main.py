import MetaTrader5 as mt5
import pandas as pd
import talib as ta
import candlestick_patterns as cp

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

def get_data(symbol, timeframe, n_periods):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_periods)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df

def trend_following(data):
    macd, macdsignal, macdhist = ta.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    adx = ta.ADX(data['high'], data['low'], data['close'], timeperiod=14)
    ma = ta.MA(data['close'], timeperiod=30)
    buy_signal = (data['close'] > ma) & (macd > macdsignal) & (adx > 25)
    sell_signal = (data['close'] < ma) & (macd < macdsignal) & (adx > 25)
    return buy_signal.astype(int) - sell_signal.astype(int)

def range_trading(data):
    rsi = ta.RSI(data['close'], timeperiod=14)
    stoch_k, stoch_d = ta.STOCH(data['high'], data['low'], data['close'], fastk_period=5, slowk_period=3, slowd_period=3)
    lowerband, middleband, upperband = ta.BBANDS(data['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    buy_signal = ((rsi < 30) & (data['close'] < lowerband))
    sell_signal = ((rsi > 70) & (data['close'] > upperband))
    return buy_signal.astype(int) - sell_signal.astype(int)

def breakout_trading(data):
    atr = ta.ATR(data['high'], data['low'], data['close'], timeperiod=14)
    upperband, middleband, lowerband = ta.BBANDS(data['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    buy_signal = (data['close'] > upperband) & (atr > atr.mean())
    sell_signal = (data['close'] < lowerband) & (atr > atr.mean())
    return buy_signal.astype(int) - sell_signal.astype(int)

def scalping(data):
    fast_ema = ta.EMA(data['close'], timeperiod=5)
    slow_ema = ta.EMA(data['close'], timeperiod=10)
    psar = ta.SAR(data['high'], data['low'], acceleration=0.02, maximum=0.2)
    buy_signal = (fast_ema > slow_ema) & (data['close'] > psar)
    sell_signal = (fast_ema < slow_ema) & (data['close'] < psar)
    return buy_signal.astype(int) - sell_signal.astype(int)

def carry_trade(data):
    return 0  # Placeholder: Implement logic based on interest rates differences

def position_trading(data):
    long_term_ma = ta.EMA(data['close'], timeperiod=200)
    macd, macdsignal, macdhist = ta.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    buy_signal = (data['close'] > long_term_ma) & (macd > macdsignal)
    sell_signal = (data['close'] < long_term_ma) & (macd < macdsignal)
    return buy_signal.astype(int) - sell_signal.astype(int)

def dmac(data):
    fast_ema = ta.EMA(data['close'], timeperiod=10)
    slow_ema = ta.EMA(data['close'], timeperiod=50)
    buy_signal = (fast_ema > slow_ema) & (fast_ema.shift() <= slow_ema.shift())
    sell_signal = (fast_ema < slow_ema) & (fast_ema.shift() >= slow_ema.shift())
    return buy_signal.astype(int) - sell_signal.astype(int)

def heikin_ashi_smoothed(data):
    ha_close = (data['open'] + data['high'] + data['low'] + data['close']) / 4
    ha_open = (data['open'].shift() + data['close'].shift()) / 2
    ha_high = data[['high', 'open', 'close']].max(axis=1)
    ha_low = data[['low', 'open', 'close']].min(axis=1)
    rsi = ta.RSI(ha_close, timeperiod=14)
    buy_signal = (ha_close > ha_open) & (rsi > 70)
    sell_signal = (ha_close < ha_open) & (rsi < 30)
    return buy_signal.astype(int) - sell_signal.astype(int)

def fibonacci_stochastic(data):
    minima = data['low'].min()
    maxima = data['high'].max()
    diff = maxima - minima
    fib_levels = [minima + 0.236 * diff, minima + 0.382 * diff, minima + 0.618 * diff]
    stoch_k, stoch_d = ta.STOCH(data['high'], data['low'], data['close'], fastk_period=5, slowk_period=3, slowd_period=3)
    buy_signal = ((data['close'] > fib_levels[0]) & (stoch_k > 80)) | ((data['close'] > fib_levels[1]) & (stoch_k > 80))
    sell_signal = ((data['close'] < fib_levels[0]) & (stoch_k < 20)) | ((data['close'] < fib_levels[1]) & (stoch_k < 20))
    return buy_signal.astype(int) - sell_signal.astype(int)

def confluence_zone_trading(data):
    macd, macdsignal, macdhist = ta.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    adx = ta.ADX(data['high'], data['low'], data['close'], timeperiod=14)
    buy_signal = (macd > macdsignal) & (adx > 25)
    sell_signal = (macd < macdsignal) & (adx > 25)
    return buy_signal.astype(int) - sell_signal.astype(int)

def pivot_point_breakout(data):
    high = data['high'].max()
    low = data['low'].min()
    close = data['close'].iloc[-1]
    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    s1 = 2 * pivot - high
    buy_signal = (close > r1)
    sell_signal = (close < s1)
    return buy_signal.astype(int) - sell_signal.astype(int)

def bollinger_band_squeeze(data):
    upperband, middleband, lowerband = ta.BBANDS(data['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    bandwidth = (upperband - lowerband) / middleband
    buy_signal = (bandwidth < 0.05) & (data['close'] > upperband.shift())
    sell_signal = (bandwidth < 0.05) & (data['close'] < lowerband.shift())
    return buy_signal.astype(int) - sell_signal.astype(int)

def execute_strategy(strategy_func, symbol, timeframe, n_periods):
    data = get_data(symbol, timeframe, n_periods)
    signals = strategy_func(data)
    return signals

def majority_rule_decision(symbol, timeframe, n_periods):
    data = get_data(symbol, timeframe, n_periods)
    strategies = [trend_following, range_trading, breakout_trading, scalping, carry_trade, position_trading, dmac, heikin_ashi_smoothed, fibonacci_stochastic, confluence_zone_trading, pivot_point_breakout, bollinger_band_squeeze]
    strategy_signals = pd.DataFrame({strategy.__name__: execute_strategy(strategy, symbol, timeframe, n_periods) for strategy in strategies})
    candle_signals = cp.detect_patterns(data)  # Get candlestick patterns signals
    candle_signals['bullish_sum'] = (candle_signals.iloc[:, :-2] > 0).sum(axis=1)  # Sum of bullish patterns
    candle_signals['bearish_sum'] = (candle_signals.iloc[:, :-2] < 0).sum(axis=1)  # Sum of bearish patterns

    # Summing up all strategy signals and candlestick pattern signals
    decision = strategy_signals.sum(axis=1) + candle_signals['bullish_sum'] - candle_signals['bearish_sum']
    buy = decision > 0
    sell = decision < 0
    return buy, sell

def place_order(symbol, lot, order_type):
    price = mt5.symbol_info_tick(symbol).ask if order_type == 'buy' else mt5.symbol_info_tick(symbol).bid
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY if order_type == 'buy' else mt5.ORDER_TYPE_SELL,
        "price": price,
        "deviation": 10,
        "magic": 234000,
        "comment": "python script trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    result = mt5.order_send(request)
    return result

symbol = 'EURUSD'
timeframe = mt5.TIMEFRAME_M1
n_periods = 100
buy, sell = majority_rule_decision(symbol, timeframe, n_periods)
if buy.iloc[-1]:
    place_order(symbol, 0.1, 'buy')
elif sell.iloc[-1]:
    place_order(symbol, 0.1, 'sell')

mt5.shutdown()
