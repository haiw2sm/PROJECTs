# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:20:10 2021

@author: w2hi
"""
import os
try:
    from settings import *
except Exception as e:
    raise e

class ParseEncodedStr(object):
    """docstring for parseEncodedStr"""
    def __init__(self, DATA_DIR):
        super(ParseEncodedStr, self).__init__()
        self.review_woff_path = os.path.join(DATA_DIR, 'woff/1aa71721.woff')
        self.shopnum_woff_path = os.path.join(DATA_DIR, 'woff/409fe85f.woff')
        self.woff_ocr_font_path = os.path.join(DATA_DIR, 'font.txt')

    def get_ocr_woff_text_lst(self, woff_ocr_font_path):
        '''获取解密后的文本，通过ocr识别图片上的文本'''
        f = open(woff_ocr_font_path, 'r', encoding='utf-8')
        content = f.read()
        woff_text_lst = [_ for _ in content]
        f.close()
        del content
        return woff_text_lst

    def make_data_map(self, font, woff_ocr_font_path):
        '''生成混淆字体与解密字体映射表'''
        data_map = create_font_inflect_table(self.get_ocr_woff_text_lst, font, woff_ocr_font_path)
        return data_map

    def parse(self, rawStr, className='review'):
        '''解析混淆字体文本'''
        rawStr = rawStr.replace('<br />', '')  # 取出换行符
        rawStr = rawStr.replace('\n', '')
        if className == 'review':
            font = TTFont(self.review_woff_path)
            # 正则表达式前面必须加 r 否则提取不到数据
            patt = re.compile(r'<svgmtsi class=\\"review\\">&#x([^>]*);</"?svgmtsi>')
            hStrs = re.findall(patt, rawStr)
            template = '<svgmtsi class=\\"review\\">&#x%s;</svgmtsi>'
        else:
            rawStr, font, hStrs, template = deal_shopNum_confusion(rawStr, shopnum_woff_path=self.shopnum_woff_path)

        data_map = self.make_data_map(font, self.woff_ocr_font_path)
        result = []
        # 转换成同woff转成的xml中的文本一样的name
        unis = ['uni' + hstr for hstr in hStrs]
        for uni in unis:
            gid = font.getGlyphID(uni)
            result.append(data_map[uni])

        for i, hStr in enumerate(hStrs):
            # 替换混淆标签
            if className == 'review':
                rawStr = rawStr.replace(template % hStr, result[i])
            else:
                rawStr = rawStr.replace(template % hStr, result[i])
        try:
            nrawStr = json.loads(rawStr)
        except:
            return rawStr
        else:
            return nrawStr




if __name__ == '__main__':
    try:
        from settings import *
    except ImportError as ie:
        raise ie

    # 实例化对象
    pes = ParseEncodedStr(DATA_DIR=DATA_DIR)

    # 解析
    # rawStr = '\ueadd'
    # rawStr = '\uf46c\ue2df\ue076\ue2df'
    # rawStr = '\ued04\n.\n\ued04\n1'
    # rawStr = '11\n\ueadd'
    rawStr =  '\uf46c\n\ue2df\n\ue076\n\ued04'
    newStr = pes.parse(rawStr=rawStr, className='shopNum')
    print(newStr)

    # 保存
    with open(os.path.join(DATA_DIR, 'decode.txt'), 'w', encoding='utf-8') as f:
        f.write(newStr)
