from uiautomator2 import connect
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.completion import WordCompleter

import requests
import pyscreeze
from PIL import Image
import io
import os
import cv2
from subprocess import Popen, PIPE, call
from dotenv import load_dotenv

load_dotenv()

keycodes = {
    "space": 62,
    "up": 19,
    "down": 20,
    "left": 21,
    "right": 22,
}

d = connect()


def tap(x, y):
    """simulasikan menekan layar

    Args:
        x ():
        y ():

    Returns:

    """
    return d.click(x, y)
    # return adb_shell(f"input tap {x} {y}")


def tapHold(x, y, time=1):
    """simulasi tekan layar / hold

    Args:
        x ():
        y ():
        time ():

    Returns:

    """
    print('hold', x, y)
    return d.long_click(x, y, time)


def getKeyCode(key):
    """mendapatkan key code

    Args:
        key ():

    Returns:

    """
    return keycodes.get(key)


def press(keycodes):
    """simulasi tekan tombol tertentu (contoh: a, b, c harus dengan ke code)

    Args:
        keycodes ():

    Returns:

    """
    return d.press(keycodes)


def send_keys(key):
    """mengirikan send key

    Args:
        key ():

    Returns:

    """
    return d.send_keys(key)


def screenshot():
    """mengambil screenshot

    Returns:

    """
    pilimg = d.screenshot('/tmp/screenshot_tmp.png')
    return "/tmp/screenshot_tmp.png"


def ocr(file_path, encoding="utf-8"):
    """mengekstrak text dari file gambar

    Args:
        file_path ():  lokasi file gambar
        encoding ():

    Returns:

    """
    p = Popen(["gocr", file_path], stdin=PIPE, stdout=PIPE)
    text = p.stdout.read()
    p.stdout.close()
    return text.decode(encoding).strip("\n")


def gpt(ask, encoding="utf-8"):
    """Ask GPT a question.

    Args:
        ask (str): The question.
        encoding (str): Encoding type. Defaults to "utf-8".

    Returns:
        str: Response from GPT.
    """
    try:
        p = Popen(["bard-cli", ask], stdin=PIPE, stdout=PIPE)
        text = p.stdout.read()
        p.stdout.close()
        return text.decode(encoding).strip("\n")
    except Exception as e:
        print(f"An error occurred: {e}. Retrying...")
        return gpt(ask, encoding)  # Recalling the function if an error occurs


def extract_text_from_image(image_path, location=None):
    """

    Args:
        image_path ():
        location (): List left, upper, right, and lower pixel coordinate.

    Returns:

    """
    if location:
        image = Image.open(image_path)
        cropped_image = image.crop(location)
        # cropped_image.show()
        cropped_image.save('/tmp/cropped_imag.png')
        image_text = ocr('/tmp/cropped_imag.png')
    else:
        image_text = ocr(image_path)

    return image_text


def image_has_text(image_path, text, location=None, debug=False):
    """

    Args:
        image_path ():
        text ():
        location (): List left, upper, right, and lower pixel coordinate.

    Returns:

    """

    image_text = extract_text_from_image(image_path, location=location)
    if debug:
        print(image_text)

    return text.lower() in image_text.lower()


def locateImage(*args, **kwargs):
    """mengambil lokasi gambar di dalam sebuah gambar
        *args:
        **kwargs:

    Returns:

    """
    return pyscreeze.locate(*args, **kwargs)


def locateCenterOnImage(*args, **kwargs):
    """mencari gambar di tengah, gambar yang dicari + gambar bg
        *args:
        **kwargs:

    Returns:

    """

    try:
        coords = locateImage(*args, **kwargs)
        if coords is None:
            return None
        else:
            location = pyscreeze.center(coords)
            return (location.x.item(), location.y.item())
    except Exception as e:
        return None


def send_notify(message):
    """mengirim notifikasi melalui telegram api

    Args:
        message ():
    """
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")


def create_select_interface(options_list, return_index=True):
    """
    Creates a select interface with the provided options, showing the list beforehand.

    Args:
      options_list: A list of strings representing the options.

    Returns:
      The selected option or None if the user cancels.
    """
    completer = WordCompleter(options_list)

    # Show list of options
    print_formatted_text("Available options:")
    for index, option in enumerate(options_list):
        print_formatted_text(f"{index + 1}. {option}")

    while True:
        # Prompt the user for selection
        option = prompt(
            "Please select an option (type number or option name): \n",
            completer=completer,
        )

        # Validate the selection
        try:
            # Check if user entered option number
            option_index = int(option) - 1
            if option_index >= 0 and option_index < len(options_list):
                selected_option = options_list[option_index]
                break
        except ValueError:
            # User might have entered option name
            if option not in options_list:
                print("Invalid option. Please try again.")
            else:
                selected_option = option
                break

    # Return the selected option
    if return_index:
        return option_index
    else:
        return selected_option
