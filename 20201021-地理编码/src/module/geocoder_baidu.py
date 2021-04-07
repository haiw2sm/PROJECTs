def get_coordinate_baiduapi(addr,ak):
    '''
    @ 百度地图api
    缺点： 每日请求有上限
    params:
        addr: 地址
        ak: 应用秘钥
    return:
        coordinate: 经纬度字符串 如'112,34.1'
    '''
    url = 'http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'.format(addr,ak)
    headers = {
            'User-Agent':uae.random
    }
    try:
        response = requests.get(url,headers)
        loc = response.json()['result']['location']
    except Exception as e:
        return '0'
    else:
        values = loc.values()
        return '{},{}'.format(*values)