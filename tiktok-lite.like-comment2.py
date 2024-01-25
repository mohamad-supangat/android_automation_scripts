import random
from autoclick import helpers, db
from autoclick.helpers import (
    device,
    tap,
    random_sleep,
    locateCenterOnImage,
    screenshot,
)


total_like = 0
total_comment = 0

imgs = {
    'like_button': './imgs/tiktok_lite/like_button2.png',
    'comment_button': './imgs/tiktok_lite/comment_button2.png',
    'submit_comment_button': './imgs/tiktok_lite/submit_comment_button.png',
    'close_comment_button': './imgs/tiktok_lite/close_comment_button.png',
}


def search_like_button():
    return locateCenterOnImage(
        imgs.get('like_button'), screenshot(), confidence=0.8
    )


def scroll_page():
    return helpers.device.swipe(292, 1050, 292, 163, 0.1)


def close_comment():
    close_comment = locateCenterOnImage(
        imgs.get('close_comment_button'), screenshot(), confidence=0.9
    )
    if close_comment:
        tap(*close_comment)


def auto_comment():
    global total_comment
    # random_sleep()

    has_comment_button = locateCenterOnImage(
        imgs.get('comment_button'), screenshot(), confidence=0.8
    )
    # klik tombol komentar
    if has_comment_button:
        tap(*has_comment_button)
        # random_sleep()
        has_comment_input = device(
            className='android.widget.EditText', textContains='Add comment'
        )
        if has_comment_input:
            position = has_comment_input.center()
            tap(position[0], position[1])
            tap(position[0], position[1])

            random_sleep()
            comment_text = random.choice(db.comments)
            print(f'comment: {comment_text}')
            device.send_keys(comment_text)
            # has_comment_input.set_text(comment_text)
            random_sleep()

            submit_button = locateCenterOnImage(
                imgs.get('submit_comment_button'), screenshot(), confidence=0.9
            )
            tap(*submit_button)
            total_comment += 1
            random_sleep()


while True:
    if random.randint(1, 999) % 2 == 1:
        continue

    random_sleep()
    has_like_button = search_like_button()
    if has_like_button:
        tap(*has_like_button)
        print('Like')
        total_like += 1

    if random.randint(1, 999) % 2 == 0:
        auto_comment()

    close_comment()
    random_sleep()
    print(f'like: {total_like}')
    print(f'comment: {total_comment}')

    scroll_page()
