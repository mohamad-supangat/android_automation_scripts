#!/bin/env python

import time
from autoclick.helpers import device, tap, locateCenterOnImage, screenshot


total = 0

imgs = {'follow_button': './imgs/tiktok_lite/follow_button.png'}


def search_follow_button():
    return locateCenterOnImage(
        imgs.get('follow_button'), screenshot(), confidence=0.9
    )


def scroll_page():
    return device.swipe(292, 1250, 292, 163, 0.5)


device.app_stop_all()
device.app_start(
    'com.zhiliaoapp.musically.go',
    'com.bytedance.hybrid.spark.page.SparkActivity',
)
device.wait_activity(
    'com.bytedance.hybrid.spark.page.SparkActivity', timeout=10
)

while True:

    follow_button = search_follow_button()
    if follow_button:
        print(follow_button)
        tap(*follow_button)
        total += 1
    else:
        print(f'total: {total}')
        scroll_page()

    # break
    time.sleep(2)
