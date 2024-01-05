import time
from autoclick import helpers


device = helpers.d
total = 0
imgs = {
    'follow_button': './imgs/tiktok/follow_button.png'
}


def search_follow_button():
    return device(text='Follow', className='android.widget.Button')


def scroll_page():
    return helpers.d.swipe(292, 1250, 292, 163, 0.5)


while True:

    follow_button = search_follow_button()
    if follow_button:
        follow_button.click()
        total += 1
    else:
        print(f"total: {total}")
        scroll_page()

    # break
    time.sleep(2)
