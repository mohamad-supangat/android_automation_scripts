import time
from autoclick.helpers import device, tap


total = 0
imgs = {'follow_button': './imgs/tiktok/follow_button.png'}


def search_follow_button():
    return device(text='Follow', className='android.widget.Button')


def scroll_page():
    return device.swipe(292, 1250, 292, 163, 0.5)


while True:

    follow_button = search_follow_button()
    if follow_button:
        position = follow_button.center()
        tap(position[0], position[1])
        total += 1
    else:
        print(f'total: {total}')
        scroll_page()

    # break
    time.sleep(2)
