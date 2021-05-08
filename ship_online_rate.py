import requests

"""
()代表元组,是一种不可变序列: 创建tup = (1,2,3)
[]代表list数据类型,列表是一种可变序列 list = ['P', 'y', 't', 'h', 'o', 'n']
{}代表字典类型,创建scores = {'语文': 89, '数学': 92, '英语': 93}
"""


# 船舶离线率
class ShipOnline:
    """
    根据船舶名称查询船舶mmsi
    """

    def get_ship_mmsi(self, ship_name):
        url = 'http://172.21.80.171:30111/basics-program/queryShip/shipSearch?page=1&size=20&query=' + ship_name
        r = requests.get(url)
        json = r.json()
        data = json['datas']['datas'][0]
        print(data)
        mmsi = data['mmsi']
        ship_name_cn = data['shipNameCn']
        if ship_name == ship_name_cn:
            return mmsi
        return None

    '''
    根据船舶mmsi查询船舶在线率
    '''

    def ship_online_rate(self, mmsi, start_time, end_time):
        url = 'http://172.21.80.171:30111/sx-ship-manage/sxth/selectOnlineRateList'
        param = {"startTime": "2021-05-03 16:36:16", "endTime": "2021-05-07 16:36:16", "mmsi": "413855686",
                 "pageSize": 6, "pageNum": 1, "sourceType": "03001,03002", "OLT": 1}

        param.update({"mmsi": mmsi})
        param.update({"startTime": start_time})
        param.update({"endTime": end_time})

        r = requests.post(url, json=param)
        data = r.json()['datas']
        return data
