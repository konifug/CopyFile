#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rowsplitcsv
import shutil

def Main():
    targetCsv = os.path.join(os.path.dirname(__file__),'copy.csv')

    # CSVを配列へ取り込み(引数: 0=from,1=to)
    fromPath = []
    fromPath = rowsplitcsv.ImpCsv(targetCsv,0)
        
    toPath = []
    toPath = rowsplitcsv.ImpCsv(targetCsv,1)

    # フォルダがなければ作成する
    print('Now Making ...')
    for tmp in toPath:
        if not os.path.exists(os.path.dirname(tmp)):
            os.makedirs(os.path.dirname(tmp))

    # ファイルをコピー
    cnt = 0
    for buf in toPath:
        try:
            shutil.copy(fromPath[cnt],toPath[cnt])
        except:
            print('ERROR ' + fromPath[cnt])
        cnt = cnt + 1

    print('Complete !!')
    
if __name__ == '__main__': Main()
