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
