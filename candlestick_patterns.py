import talib as ta
import pandas as pd

def detect_patterns(data):
    patterns = {
        'CDL2CROWS': ta.CDL2CROWS(data['open'], data['high'], data['low'], data['close']),
        'CDL3BLACKCROWS': ta.CDL3BLACKCROWS(data['open'], data['high'], data['low'], data['close']),
        'CDL3INSIDE': ta.CDL3INSIDE(data['open'], data['high'], data['low'], data['close']),
        'CDL3LINESTRIKE': ta.CDL3LINESTRIKE(data['open'], data['high'], data['low'], data['close']),
        'CDL3OUTSIDE': ta.CDL3OUTSIDE(data['open'], data['high'], data['low'], data['close']),
        'CDL3STARSINSOUTH': ta.CDL3STARSINSOUTH(data['open'], data['high'], data['low'], data['close']),
        'CDL3WHITESOLDIERS': ta.CDL3WHITESOLDIERS(data['open'], data['high'], data['low'], data['close']),
        'CDLABANDONEDBABY': ta.CDLABANDONEDBABY(data['open'], data['high'], data['low'], data['close']),
        'CDLADVANCEBLOCK': ta.CDLADVANCEBLOCK(data['open'], data['high'], data['low'], data['close']),
        'CDLBELTHOLD': ta.CDLBELTHOLD(data['open'], data['high'], data['low'], data['close']),
        'CDLBREAKAWAY': ta.CDLBREAKAWAY(data['open'], data['high'], data['low'], data['close']),
        'CDLCLOSINGMARUBOZU': ta.CDLCLOSINGMARUBOZU(data['open'], data['high'], data['low'], data['close']),
        'CDLCONCEALBABYSWALL': ta.CDLCONCEALBABYSWALL(data['open'], data['high'], data['low'], data['close']),
        'CDLCOUNTERATTACK': ta.CDLCOUNTERATTACK(data['open'], data['high'], data['low'], data['close']),
        'CDLDARKCLOUDCOVER': ta.CDLDARKCLOUDCOVER(data['open'], data['high'], data['low'], data['close']),
        'CDLDOJI': ta.CDLDOJI(data['open'], data['high'], data['low'], data['close']),
        'CDLDOJISTAR': ta.CDLDOJISTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLDRAGONFLYDOJI': ta.CDLDRAGONFLYDOJI(data['open'], data['high'], data['low'], data['close']),
        'CDLENGULFING': ta.CDLENGULFING(data['open'], data['high'], data['low'], data['close']),
        'CDLEVENINGDOJISTAR': ta.CDLEVENINGDOJISTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLEVENINGSTAR': ta.CDLEVENINGSTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLGAPSIDESIDEWHITE': ta.CDLGAPSIDESIDEWHITE(data['open'], data['high'], data['low'], data['close']),
        'CDLGRAVESTONEDOJI': ta.CDLGRAVESTONEDOJI(data['open'], data['high'], data['low'], data['close']),
        'CDLHAMMER': ta.CDLHAMMER(data['open'], data['high'], data['low'], data['close']),
        'CDLHANGINGMAN': ta.CDLHANGINGMAN(data['open'], data['high'], data['low'], data['close']),
        'CDLHARAMI': ta.CDLHARAMI(data['open'], data['high'], data['low'], data['close']),
        'CDLHARAMICROSS': ta.CDLHARAMICROSS(data['open'], data['high'], data['low'], data['close']),
        'CDLHIGHWAVE': ta.CDLHIGHWAVE(data['open'], data['high'], data['low'], data['close']),
        'CDLHIKKAKE': ta.CDLHIKKAKE(data['open'], data['high'], data['low'], data['close']),
        'CDLHIKKAKEMOD': ta.CDLHIKKAKEMOD(data['open'], data['high'], data['low'], data['close']),
        'CDLHOMINGPIGEON': ta.CDLHOMINGPIGEON(data['open'], data['high'], data['low'], data['close']),
        'CDLIDENTICAL3CROWS': ta.CDLIDENTICAL3CROWS(data['open'], data['high'], data['low'], data['close']),
        'CDLINNECK': ta.CDLINNECK(data['open'], data['high'], data['low'], data['close']),
        'CDLINVERTEDHAMMER': ta.CDLINVERTEDHAMMER(data['open'], data['high'], data['low'], data['close']),
        'CDLKICKING': ta.CDLKICKING(data['open'], data['high'], data['low'], data['close']),
        'CDLKICKINGBYLENGTH': ta.CDLKICKINGBYLENGTH(data['open'], data['high'], data['low'], data['close']),
        'CDLLADDERBOTTOM': ta.CDLLADDERBOTTOM(data['open'], data['high'], data['low'], data['close']),
        'CDLLONGLEGGEDDOJI': ta.CDLLONGLEGGEDDOJI(data['open'], data['high'], data['low'], data['close']),
        'CDLLONGLINE': ta.CDLLONGLINE(data['open'], data['high'], data['low'], data['close']),
        'CDLMARUBOZU': ta.CDLMARUBOZU(data['open'], data['high'], data['low'], data['close']),
        'CDLMATCHINGLOW': ta.CDLMATCHINGLOW(data['open'], data['high'], data['low'], data['close']),
        'CDLMATHOLD': ta.CDLMATHOLD(data['open'], data['high'], data['low'], data['close']),
        'CDLMORNINGDOJISTAR': ta.CDLMORNINGDOJISTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLMORNINGSTAR': ta.CDLMORNINGSTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLONNECK': ta.CDLONNECK(data['open'], data['high'], data['low'], data['close']),
        'CDLPIERCING': ta.CDLPIERCING(data['open'], data['high'], data['low'], data['close']),
        'CDLRICKSHAWMAN': ta.CDLRICKSHAWMAN(data['open'], data['high'], data['low'], data['close']),
        'CDLRISEFALL3METHODS': ta.CDLRISEFALL3METHODS(data['open'], data['high'], data['low'], data['close']),
        'CDLSEPARATINGLINES': ta.CDLSEPARATINGLINES(data['open'], data['high'], data['low'], data['close']),
        'CDLSHOOTINGSTAR': ta.CDLSHOOTINGSTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLSHORTLINE': ta.CDLSHORTLINE(data['open'], data['high'], data['low'], data['close']),
        'CDLSPINNINGTOP': ta.CDLSPINNINGTOP(data['open'], data['high'], data['low'], data['close']),
        'CDLSTALLEDPATTERN': ta.CDLSTALLEDPATTERN(data['open'], data['high'], data['low'], data['close']),
        'CDLSTICKSANDWICH': ta.CDLSTICKSANDWICH(data['open'], data['high'], data['low'], data['close']),
        'CDLTAKURI': ta.CDLTAKURI(data['open'], data['high'], data['low'], data['close']),
        'CDLTASUKIGAP': ta.CDLTASUKIGAP(data['open'], data['high'], data['low'], data['close']),
        'CDLTHRUSTING': ta.CDLTHRUSTING(data['open'], data['high'], data['low'], data['close']),
        'CDLTRISTAR': ta.CDLTRISTAR(data['open'], data['high'], data['low'], data['close']),
        'CDLUNIQUE3RIVER': ta.CDLUNIQUE3RIVER(data['open'], data['high'], data['low'], data['close']),
        'CDLUPSIDEGAP2CROWS': ta.CDLUPSIDEGAP2CROWS(data['open'], data['high'], data['low'], data['close']),
        'CDLXSIDEGAP3METHODS': ta.CDLXSIDEGAP3METHODS(data['open'], data['high'], data['low'], data['close'])
    }

    # Convert to DataFrame
    pattern_data = pd.DataFrame(patterns, index=data.index)

    # Optional: Add a summary column that counts how many bullish or bearish patterns are detected
    pattern_data['bullish'] = (pattern_data > 0).sum(axis=1)
    pattern_data['bearish'] = (pattern_data < 0).sum(axis=1)

    return pattern_data
