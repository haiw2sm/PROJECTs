# import requests
import pandas as pd
import time
from module.geocode_geocoder import get_coordinate_geocoder


# 写入经纬度到文件
def write_coordinate_tofile():
    filename = '../data/groupbySort.csv'
    df = pd.read_csv(filename, encoding='gb18030', usecols=['regAddr'])
    for i,regAddr in enumerate(df.regAddr):
        if i>17559:
            maxretry = 3
            with open('../result/groupbySort.txt','a+',encoding='utf-8') as f:
                coordinate = get_coordinate_geocoder(regAddr)
                time.sleep(0.2)
                while coordinate=='0,0' and maxretry!=0:
                    maxretry -= 1
                    time.sleep(1)
                    coordinate = get_coordinate_geocoder(regAddr)
                print(i,'\t写入',regAddr,'经纬度:',coordinate)
                line = str(i) + '\t' + coordinate + '\n'
                f.write(line)
    print('完成')

# 主函数
def main():
    write_coordinate_tofile()

if __name__ == '__main__':
    main()
