"""
Title: Cookie Clicker AI
Author: Jackson Reid
Date Created: 2022-01-23
"""

import mouse


def autoclick(pos, click):
    """
    Auto-clicks the cookie
    :param pos: tuple - position on screen
    :param click: boolean - whether to click or not
    :return: None
    """
    while click:
        # mouse.click()
        if mouse.is_pressed("right"):
            click = False
            print("Right click")


autoclick((1, 1), True)
