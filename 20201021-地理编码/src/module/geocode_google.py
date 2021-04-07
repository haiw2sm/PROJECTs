from geopy.geocoders import Nominatim

def get_coordinate_geopy(addr):
    '''
    @ 谷歌地理编码三方库
    缺点：需要vpn连接 [经本人测试准雀度不是很高，只能获取部分比较显著的地址]
    params:
        addr: 地址
    return:
        latitude: 经度
        longitude: 纬度
    '''
    geolocator=Nominatim(user_agent='myuseragent')   # 应用名称-指定参数[myuseragent]
    data = geolocator.geocode(addr)
    return data.latitude, data.longitude