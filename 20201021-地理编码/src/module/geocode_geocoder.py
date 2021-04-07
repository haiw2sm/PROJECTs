import geocoder

# 全球地图（多提供者）
def get_coordinate_geocoder(addr):
    '''
    @ 地图封装库-多提供商可选
    优点： 不需要vpn
    reason：1、全球经纬查询 2、没有使用限制
    tutorial：https://geocoder.readthedocs.io/providers/ArcGIS.html
    params：
        addr: 输入地址
    return:
        latlng: 经纬坐标
    '''
    try:
        g = geocoder.arcgis(addr)
    except Exception as e:
        pass
    else:
        if g:
            return '{},{}'.format(*g.latlng[::-1])
    return '0,0'