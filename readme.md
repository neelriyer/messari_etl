# Messari Etl

Unofficial Python Wrapper for Messari data.

# Quickstart

```shell
pip install 'git+https://github.com/spiyer99/messari_etl.git#egg=messari_etl'
```

```python
from messari_etl import MessariEtl

client = MessariEtl()
df = client.get_data(assets = ['uni', 'mkr', 'aave', 'cake'], metric = 'price', col = 'close', start_date = '2021-01-01', end_date = '2021-03-01')

print(df.head())
```

```s
                 UNI         MKR        AAVE      CAKE
timestamp                                             
2021-01-01  4.746491  582.250897   90.909013  0.662272
2021-01-02  4.859523  610.555553   85.785492  0.616879
2021-01-03  5.520508  676.267938   93.877038  0.631175
2021-01-04  5.425185  687.521230  114.181577  0.648479
2021-01-05  6.271046  766.814017  119.851195  0.679934
```

Please note all prices in USD. All dates are in yyyy-mm-dd.

## Transaction Gas Average (requires a pro or enterprise subscription)
```python
from messari_etl import MessariEtl

client = MessariEtl('YOUR_API_KEY') # input your api key here
df = client.get_data(assets = ['uni', 'mkr', 'aave', 'cake'], metric = "txn.gas.avg", col = 'transaction_gas_avg', start_date = '2021-01-01', end_date = '2021-03-01')

print(df.head())
```

## Circulating MarketCap
```python
from messari_etl import MessariEtl

client = MessariEtl()
df = client.get_data(assets = ['uni', 'mkr', 'aave', 'cake'], metric = 'mcap.circ', col = 'circulating_marketcap', start_date = '2021-01-01', end_date = '2021-03-01')

print(df.head())
```

## Sharpe Ratio
```python
from messari_etl import MessariEtl

client = MessariEtl()
df = client.get_data(assets = ['uni', 'mkr', 'aave', 'cake'], metric = 'daily.shp', col = 'sharpe_30d', start_date = '2021-01-01', end_date = '2021-03-01')

print(df.head())
```

## Others

Can be used for all metrics listed [here](https://data.messari.io/api/v1/assets/metrics). 