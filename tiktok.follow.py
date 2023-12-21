import time
from autoclick import helpers


total = 0
imgs = {
    'follow_button': './imgs/tiktok/follow_button.png'
}


def search_follow_button(ss):
    return helpers.locateCenterOnImage(imgs['follow_button'], ss)

def scroll_page():
    return helpers.d.swipe(292, 1250, 292, 163, 0.5)

while True:
    ss = helpers.screenshot()

    position = search_follow_button(ss)
    if position:
        helpers.tap(*position)
        total += 1
    else:
        print(f"total: {total}")
        scroll_page()

    # break
    time.sleep(2)


