#!/usr/bin/env python
#! -*- coding: utf-8 -*-
from keras.preprocessing import image
import keras
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import pygame.mixer
import numpy as np
from PIL import Image
import sys, os
# from timeit import default_timer as timer
import time
import datetime

sys.path.append(os.path.abspath(".."))
import yolo_tiny
from yolo_tiny import YOLO


if __name__ == '__main__':
    # 音声ファイル初期化
    # pygame.mixer.init()
    # pygame.mixer.music.load("Cash_Register-Beep01-1.mp3")

    # 商品価格
    money = {'ayataka':110, 'choya_umeshu':120, 'claft_boss':130, 'coca_cola':140, 'dole_orange':150, 'sonota':0}
    money_sum = 0 
    product = []
    while True:
        key = input('商品をスキャンする場合は「Enter」, 会計に進む場合は「y」を押して下さい：　')
        if key == 'y':
          print('支払い金額：{}'.format(money_sum))
          print('商品リスト：{}'.format(product))
          break
        else:
            print('Camera is stanby. Please wait.')
        while True:
            pred = yolo_tiny.detect_img(YOLO())
            if pred == 0:
                print('Finish register item')
                break
            
            elif len(pred) == 1:
                money_sum += money[pred[0]]
                print('商品名: {}'.format(pred[0]))
                print('小計：{}'.format(money[pred[0]]))
                
            elif len(pred) == 0:
                print('登録されていない商品です。やり直してください。')
                print('Camera is standby. Please wait.')
                continue
            
            elif len(pred) > 1:
                for i in range(len(pred)):
                    money_sum += money[pred[i]]
                    print('商品名: {}'.format(pred[i]))
                    print('小計：{}'.format(money[pred[i]]))
                    if 'sonota' in pred:
                      print('scan result have [sonota]. Please scan again it.')
                      continue

            # # 音声再生
            # pygame.mixer.music.play(1)
            # sleep(1)
            # # 再生の終了
            # pygame.mixer.music.stop()
            
            print("合計金額：",money_sum)
            product.append(pred)
            key = input('続けて商品をスキャンする場合は「y」,会計する場合は「Enter」を押して下さい')
            if key != 'y':
                print("合計:{}円".format(money_sum))
                break
            else:
              print('Camera is standby. Please wait.')
              continue