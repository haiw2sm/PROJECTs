# 爬虫要求
- 爬取对象
  
    `大众点评->苏州->美食->店铺信息`

- 爬取字段

    1. 店铺名称  dptitle  `纯文字`
    2. 店铺星级  dpstar  `纯文字`
    3. 评论人数  plnum  `字体混淆-shopNum`
    4. 人均消费  rjcost  `字体混淆(shopNum)+纯文字`
    5. 口味评分  kwscore  `字体混淆-shopNum`
    6. 环境评分  hjscore  `字体混淆-shopNum`
    7. 服务评分  fwscore  `字体混淆-shopNum`