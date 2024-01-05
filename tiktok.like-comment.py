from os import posix_fallocate
import time
import random
from autoclick import helpers, db


total = 0
imgs = {
    'follow_button': './imgs/tiktok/follow_button.png',
    'like_buttton': './imgs/tiktok/like_button.png',
    'comment_button': './imgs/tiktok/comment_button.png'
}


def search_like_button(ss):
    return helpers.locateCenterOnImage(imgs['like_buttton'], ss, confidence=0.78, region=(600, 560, 600 + 100, 560 + 100))


def scroll_page():
    return helpers.d.swipe(292, 1050, 292, 163, 0.1)


def close_comment():
    # position = auto.locateCenterOnScreen(
    #     './tiktok/img/close_comment_button.png', confidence=confidence)
    print("close comment")
    # print(position)
    # if position:
    #     auto.click(position.x, position.y)
    # else:
    #     close_comment(confidence=0.7)

    helpers.rightClick()


def auto_comment(ss):
    time.sleep(random.randint(5, 8))
    position = helpers.locateCenterOnImage(
        imgs['comment_button'], ss, confidence=0.8, region=(354, 93, 67, 595)
    )
    # klik tombol komentar
    if position:
        helpers.click(position.x, position.y)
        time.sleep(1)

        # check jika komentar di aktifkan
        # position = auto.locateCenterOnScreen(
        #     "./tiktok/img/emoticon_komentar.png", confidence=0.4)

        position = True
        if position:
            # klik kolom komentar
            helpers.click(168, 718)
            helpers.click(168, 718)

            time.sleep(0.5)

            comment_text = random.choice(db.comments)
            print(f'comment: {comment_text}')
            helpers.write(comment_text, interval=0.01)
            time.sleep(0.5)

            position = helpers.locateCenterOnScreen(
                "./tiktok/img/send_message_button.png",
                confidence=0.8,
                region=(363, 689, 100, 100),
            )
            if position:
                helpers.click(*position)

            time.sleep(1)

        count_comment += 1
        time.sleep(1)
        close_comment()
        time.sleep(random.randint(5, 8))
    else:
        close_comment()


while True:
    time.sleep(10)
    ss = helpers.screenshot()
    position = search_like_button(ss)
    print(position)
    # print(position)
    if position:
        print(position)
        # like postingan
        helpers.tap(*position)
        total += 1
    # break

    scroll_page()
