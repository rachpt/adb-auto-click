#!/usr/bin/env python
import time
from adb import Adb

adb = Adb()


def taobao_18dianpu(num=18, th=0):
    '''
    淘宝浏览18个店铺15秒
    '''
    for i in range(num):
        print("第{}次".format(i + 1))
        adb.adb_click(873, 1930 - 180 * th)
        time.sleep(3)
        for _ in range(3):
            adb.adb_swipe_down()
            time.sleep(1)
        time.sleep(15)
        adb.adb_put_back()
        time.sleep(1)


def unicom_qiandao():
    '''
    联通签到，包括3次转盘游戏
    '''
    adb.adb_back_to_desktop()
    time.sleep(1)
    adb.adb_back_to_desktop()
    time.sleep(2)
    adb.adb_swipe_right()
    time.sleep(1)
    adb.click_by_content_after_refresh('手机营业厅')
    time.sleep(5)
    adb.click_by_text_after_refresh('签到')
    time.sleep(5)
    adb.adb_put_back()
    time.sleep(1)
    adb.adb_put_back()

    adb.click_by_some_text_after_refresh('万人获奖')
    time.sleep(5)
    for _ in range(3):
        adb.click_by_rid_after_refresh('zhuanpan_1')
        time.sleep(5)

    adb.adb_put_back()
    time.sleep(2)
    adb.adb_put_back()


def yundong_2_liuliang():
    '''
    我特权换流量
    '''
    adb.adb_back_to_desktop()
    time.sleep(1)
    adb.adb_back_to_desktop()
    time.sleep(2)
    adb.adb_swipe_right(100)
    time.sleep(2)
    adb.adb_swipe_right(100)
    time.sleep(1)
    adb.click_by_content_after_refresh('运动助手')
    time.sleep(3)
    adb.click_by_text_after_refresh('切换微信运动')
    time.sleep(1)
    adb.adb_input('rachpt')
    time.sleep(1)
    adb.click_by_text_after_refresh('输入要刷的步数')
    time.sleep(1)
    adb.adb_input(56743)
    time.sleep(1)
    adb.click_by_text('提交')
    time.sleep(3)
    adb.adb_put_back()
    time.sleep(0.5)
    adb.adb_put_back()
    time.sleep(0.5)
    adb.adb_put_back()
    time.sleep(2)

    adb.click_by_content_after_refresh('沃特权')
    time.sleep(6)
    adb.adb_swipe_up()
    time.sleep(2)
    adb.adb_click(540, 733)
    time.sleep(3)
    adb.adb_refresh()
    time.sleep(1)
    adb.click_by_some_text_after_refresh("立即兑换")
    time.sleep(4)
    adb.adb_keyboard(187)
    time.sleep(0.8)
    adb.adb_swipe_left(100)
    time.sleep(0.8)

    adb.adb_put_back()
    time.sleep(0.5)
    adb.adb_put_back()
    time.sleep(0.5)


def jd_qiandao():
    adb.click_by_content_after_refresh('京东')
    time.sleep(5)
    adb.adb_swipe(adb.s_w * 7 / 8, 930, adb.s_w * 1 / 8, 930, 200)
    time.sleep(0.8)
    adb.adb_click(740, 1024)  # 领流量
    time.sleep(2)
    adb.adb_click(adb.s_w / 2, 450)  # 签到
    time.sleep(1)
    adb.adb_put_back()
    time.sleep(0.5)
    adb.adb_put_back()
    time.sleep(0.5)
    adb.adb_put_back()
    time.sleep(0.5)


def taobao():
    '''
    淘宝 领猫币
    '''
    taobao_18dianpu()
    for i in range(4):
        taobao_18dianpu(5,i+1)
    adb.adb_click(873, 1930 - 180 * 6)

## 淘宝 领猫币
# taobao()

## 联通签到
# unicom_qiandao()

## 联通运动领流量
# yundong_2_liuliang()

## 京东签到
jd_qiandao()
