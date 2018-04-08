#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

# 2列のCSVファイルをそれぞれ配列へ読み込む
def ImpCsv(targetCsv,flg):    
    with open(targetCsv, 'r') as f:
        reader = csv.reader(f)
        next(reader)  #ヘッダ行をスキップ

        fromPath = []
        toPath = []

        num = 0 # 取り込み配列切り替え用

        for row in reader:
            for col in row:
                if num == 0:
                    fromPath.append(col)            
                    num = 1
                else:
                    toPath.append(col)
                    num = 0

    # 引数flgにより返すListを指定
    if flg == 0:
        return fromPath
    else:
        return toPath
