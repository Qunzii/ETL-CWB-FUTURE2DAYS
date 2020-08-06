def fetchDataId(seq, datasetType):
    # Administrative District
    districtDataId_list = ['F-D0047-001', # 宜蘭縣
                             'F-D0047-005', # 桃園市
                             'F-D0047-009', # 新竹縣
                             'F-D0047-013', # 苗栗縣
                             'F-D0047-017', # 彰化縣
                             'F-D0047-021', # 南投縣
                             'F-D0047-025', # 雲林縣
                             'F-D0047-029', # 嘉義縣
                             'F-D0047-033', # 屏東縣
                             'F-D0047-037', # 台東縣
                             'F-D0047-041', # 花蓮縣
                             'F-D0047-045', # 澎湖縣
                             'F-D0047-049', # 基隆市
                             'F-D0047-053', # 新竹市
                             'F-D0047-057', # 嘉義市
                             'F-D0047-061', # 臺北市
                             'F-D0047-065', # 高雄市 
                             'F-D0047-069', # 新北市
                             'F-D0047-073', # 臺中市
                             'F-D0047-077', # 臺南市
                             'F-D0047-081', # 連江縣
                             'F-D0047-085', # 金門縣
                             'F-D0047-089'] # 台灣
    
    # Attractions
    attractionsDataId_list = ['F-B0053-005', # 海水浴場
                                'F-B0053-011', # 單車
                                'F-B0053-017', # 農場旅遊
                                'F-B0053-023', # 海釣
                                'F-B0053-029', # 娛樂漁業
                                'F-B0053-035', # 登山
                                'F-B0053-041', # 國家公園
                                'F-B0053-047', # 國家風景區
                                'F-B0053-053', # 港口
                                'F-B0053-059', # 國家森林遊樂區
                                'F-B0053-065', # 水庫
                                'F-B0053-071'] # 觀星
    
    if datasetType == 1:
        if seq < len(districtDataId_list):
            return districtDataId_list[seq]
        else:
            return ''
    elif datasetType == 2:
        if seq < len(attractionsDataId_list):
            return attractionsDataId_list[seq]
        else:
            return ''
