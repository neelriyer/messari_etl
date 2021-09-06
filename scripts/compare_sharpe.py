from messari_etl import get_assets
df = get_assets(assets = ['yfi', 'uni'], metric = 'daily.shp', col = 'sharpe_30d', start_date = '2021-01-01', end_date = '2021-03-01')
print(df.head())
