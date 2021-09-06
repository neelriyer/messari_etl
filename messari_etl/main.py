import pandas as pd
import requests
from datetime import datetime
# from private import api_key

__all__ = ['MessariEtl']

class MessariEtl():
    def __init__(self, api_key = ''):
        self.api_key = api_key

    def get_data(self, assets = ['yfi'],
        metric = 'price',
        col = None, # desired column
        start_date = '2021-01-01', # yyyy-mm-dd
        end_date = '2021-02-01'):

        df = pd.DataFrame()
        for asset in assets:
            df2 = self.get_asset(asset, metric, col, start_date, end_date)
            df = pd.concat([df, df2], axis=1)

        # formatting
        df.index = df.index.map(lambda ts: format_timestamp(ts))
        df.columns = df.columns.map(lambda col: col.upper())
        return df

    def make_request(self, url):
        try:
            r = requests.get(url, headers = { "x-messari-api-key": self.api_key})
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

        data = r.json()
        # data = {"status":{"elapsed":144,"timestamp":"2021-09-05T22:09:07.188894633Z"},"data":{"id":"75af0d92-7ec7-4279-bd5b-05eafa1090bf","symbol":"YFI","name":"yearn.finance","slug":"yearn-finance","contract_addresses":[{"platform":"avalanche","contract_address":"0x9eaac1b23d935365bd7b542fe22ceee2922f52dc"},{"platform":"ethereum","contract_address":"0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e"},{"platform":"harmony-shard-0","contract_address":"0xa0dc05f84a27fccbd341305839019ab86576bc07"},{"platform":"huobi-token","contract_address":"0xb4f019beac758abbee2f906033aaa2f0f6dacb35"},{"platform":"polygon-pos","contract_address":"0xda537104d6a5edd53c6fbba9a898708e465260b6"},{"platform":"xdai","contract_address":"0xbf65bfcb5da067446cee6a706ba3fe2fb1a9fdfd"}],"_internal_temp_agora_id":"dec55ce3-f153-424b-843a-1969eeb6d6d4","parameters":{"asset_key":"yfi","asset_id":"75af0d92-7ec7-4279-bd5b-05eafa1090bf","start":"2021-01-01T00:00:00Z","end":"2021-02-01T00:00:00Z","interval":"1d","order":"ascending","format":"json","timestamp_format":"unix-milliseconds","columns":["timestamp","open","high","low","close","volume"]},"schema":{"metric_id":"price","name":"Price","description":"Volume weighted average price computed using Messari Methodology","values_schema":{"timestamp":"Timestamp in milliseconds since the epoch (1 January 1970 00:00:00 UTC)","open":"The price of the asset at the beginning of the specified interval in US dollars.","high":"The highest price of the asset during the specified interval in US dollars.","low":"The lowest price of the asset during the specified interval in US dollars","close":"The price of the asset at the end of the specified interval in US dollars.","volume":"The total volume traded during the specified interval across all Messari method markets in US dollars"},"minimum_interval":"1m","source_attribution":[{"name":"Kaiko","url":"https://www.kaiko.com/"}]},"values":[[1609459200000,22746.764122012675,23524.908696707724,21600.876704653012,21898.581377230672,96343748.36482261],[1609545600000,21892.873883354347,22528.487192764485,21331.687019863803,21467.05619065761,137286346.74884903],[1609632000000,21493.73852499608,25048.69417601038,20395.47599317904,23903.58593535771,262642604.4480318],[1609718400000,24100.048234553593,26909.154270033665,21440.871124410412,23391.12702824766,319010301.5575631],[1609804800000,23417.300390678676,25163.283812053487,21942.83266371615,23810.774761321238,177199398.63818988],[1609891200000,23831.94917929366,25636.953670968236,22697.115447850872,24813.37879848419,169275910.99404445],[1609977600000,24871.999935443975,37660.165033217825,24176.66652744357,33040.112402255414,1121397824.8220227],[1610064000000,33098.48890513814,38661.870526636194,25551.633320623103,34958.72005834251,994002056.7262814],[1610150400000,34997.09029613498,40024.342283861806,33564.176104939506,35864.87063002945,746443272.3675171],[1610236800000,35951.08554152634,38363.93079958213,30841.478859373987,33963.191431982326,518299881.6016861],[1610323200000,34056.522023381614,43890.440976554695,25244.744972761528,30118.928875144386,567116920.1678898],[1610409600000,30111.701066956466,33353.6,27991.894769408034,29714.699709251225,302873225.50499815],[1610496000000,29646.88962787239,33898.84605237247,28214.239462447895,33600.879573541264,424663763.504829],[1610582400000,33623.44751700702,34224.20726860095,31171.97631153601,32864.73052729972,291640973.1934936],[1610668800000,32860.93239810062,33750,28369.92896483068,30221.105691558296,344932144.04501694],[1610755200000,30316.53200929344,35231.27805695166,30241.920418328005,33797.82904560528,420881055.5029677],[1610841600000,33820.64549517554,36874.65838203851,32315.28780509324,34566.96362762743,483701536.9830972],[1610928000000,34580.17941652284,40255.32176389166,34470.18531325036,37986.40175461426,529140673.93739855],[1611014400000,37948.81819314624,38541.75997685914,33811.18477975659,34403.59251562048,285341441.17491335],[1611100800000,34488.544584212905,35473.68033438371,31245.093439183718,34075.71570793629,250551730.80930582],[1611187200000,34065.46379336628,34249.11543727733,26501.947962150978,27907.758305774376,277949361.3500012],[1611273600000,27946.192134926525,32167.350582600255,26059.37369221779,30809.704416509743,172258906.9702703],[1611360000000,30861.124636355813,31629.64830568232,29695.1255878465,30588.343301568675,132078692.52535416],[1611446400000,30549.361040862703,33074.25346836997,30274.660576154558,32235.388855437588,172546074.04404324],[1611532800000,32218.97266806434,33336.43374249604,29265.033011442203,29304.062090290914,164011377.8829159],[1611619200000,29312.05218907036,30722.77820756718,28400.21213086618,30322.551898300106,140024059.0470512],[1611705600000,30321.64308531588,30353.871694492685,26994.103656276046,27675.340767009864,127182089.22719346],[1611792000000,27686.020691312067,30754.96359698605,27336.286088548346,29768.03917600178,97280599.1347744],[1611878400000,30317.479734124277,32083.305400496647,28523.311110278213,29963.712759292892,206451810.05184028],[1611964800000,29982.060059375763,32353.09232515804,28507.536910669547,31188.81273402653,189010287.05574676],[1612051200000,31129.38701452104,33573.4132594276,28555.35569199317,30169.13608490405,183177362.12069055],[1612137600000,30162.602576222096,32763.4,29264.646402414866,31144.90912856814,87798456.36901638]]}}

        if 'error_code' in data['status'].keys():
            raise SystemExit(data['status']['error_message'])

        return data

    def get_asset(self, 
        asset = 'yfi',
        metric = 'price',
        col = None, # desired column
        start_date = '2021-01-01', # yyyy-mm-dd
        end_date = '2021-02-01'):

        url = f'https://data.messari.io/api/v1/assets/{asset}/metrics/{metric}/time-series?start={start_date}&end={end_date}&interval=1d'
        data = self.make_request(url)

        data = data['data']
        columns = data['parameters']['columns']
        values = data['values']

        df = pd.DataFrame(values, columns = columns)
        if col is None: col = df.columns[1] # take the first column if none selected
        df = df.rename(columns = {col: asset})
        df.index = df['timestamp']
        df = df[[asset]]
        return df

def format_timestamp(ts):
    return datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d')

if __name__ == '__main__':
    # client = MessariEtl()
    # df = client.get_data(assets = ['uni', 'mkr', 'aave', 'cake'], metric = 'price', col = 'close', start_date = '2021-01-01', end_date = '2021-03-01')
    # print(df.head())
    pass
