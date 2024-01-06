from os import posix_fallocate
import time
import random
from autoclick import helpers, db
import autoclick
from autoclick.helpers import device, tap


total = 0
imgs = {
    'follow_button': './imgs/tiktok/follow_button.png',
    'like_buttton': './imgs/tiktok/like_button.png',
    'comment_button': './imgs/tiktok/comment_button.png'
}


def search_like_button():
    return device(descriptionContains="Like video", className="android.widget.Button")


def scroll_page():
    return helpers.device.swipe(292, 1050, 292, 163, 0.1)


def close_comment():
    position = device(descriptionContains="Close comments").center()
    tap(position[0], position[1])


def auto_comment():
    time.sleep(random.randint(5, 8))

    has_comment_button = device(
        className="android.widget.Button", descriptionContains="Read or add comments")
    # klik tombol komentar
    if has_comment_button:
        position = has_comment_button.center()
        tap(position[0], position[1])
        time.sleep(1)

        # check jika komentar di aktifkan
        # position = auto.locateCenterOnScreen(
        #     "./tiktok/img/emoticon_komentar.png", confidence=0.4)

        has_comment_input = device(
            className="android.widget.EditText", textContains="Add comment")
        if has_comment_input:
            # position = has_comment_input.center()
            # tap(position[0], position[1])
            # klik kolom komentar
            # helpers.click(168, 718)
            # helpers.click(168, 718)

            time.sleep(0.5)

            comment_text = random.choice(db.comments)
            print(f'comment: {comment_text}')
            has_comment_input.set_text(comment_text)
            # helpers.write(comment_text, interval=0.01)
            time.sleep(2)

            submit_button = device(className="android.widget.ImageView",
                                   descriptionContains="Post comment").center()
            tap(submit_button[0], submit_button[1])
            time.sleep(1)

        close_comment()
        time.sleep(random.randint(5, 8))
    else:
        close_comment()


while True:
    time.sleep(10)
    has_like_button = search_like_button()
    if has_like_button:
        position = has_like_button.center()
        tap(x=position[0], y=position[1])
        print('Like')
        auto_comment()

    # time.sleep(10)
    scroll_page()
