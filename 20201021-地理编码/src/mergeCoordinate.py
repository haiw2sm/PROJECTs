import pandas as pd
from module.geocode_geocoder import get_coordinate_geocoder

# 提取经纬度坐标文件内容,并合并经纬度坐标到原始csv文件中
def deal_coordinate():
    file_path = '../result/regAddrCoordinate.txt'
    orgin_data_path = '../data/regAddr.csv'
    df = pd.read_csv(orgin_data_path, encoding='gb18030')
    f = open(file_path, 'r')
    coordinates = []
    for line in f:
        i, coordinate = line.strip().split('\t')
        regAddr = df.loc[int(i), 'regAddr']
        if coordinate=='0,0':
            coordinate = get_coordinate_geocoder(regAddr)
            if coordinate == '0,0':
                coordinate = get_coordinate_geocoder(regAddr)
            print(coordinate)
        coordinates.append(coordinate)
    df['coordinate'] = coordinates
    df.to_csv("../result/regAddrCoordinate.csv", encoding="gb18030")


def main():
    deal_coordinate()

if __name__ == "__main__":
    main( )
    
