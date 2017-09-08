from pyautogui import keyDown, press, keyUp
from ctypes import windll, Structure, c_long, byref
from time import sleep
from json import dump, load
from os.path import exists, abspath, join, pardir
from os import environ, makedirs
from sys import argv, exit

FILE_CONFIG = environ['APPDATA'] + '\\wingnome\\areas.json'  # file with configured areas
CHECKING_DELAY = 0.2  # how often to check if mouse entered checked range


def get_parent_dir(file_path): return abspath(join(file_path, pardir))


def toggle_activities() -> None:
    """
    Shows or hides all active windows by simulating keypresses
    :return: None
    """
    keyDown('win')
    press('tab')
    keyUp('win')


class Point(Structure):
    """
    Point with x and y coordinates
    """
    def __init__(self, x, y):
        Structure.__init__(self)
        self.x = x
        self.y = y

    _fields_ = [("x", c_long), ("y", c_long)]

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)


def get_mouse_pos() -> Point:
    """
    Gets current position of the mouse
    :return: Point object with x and y set to the current mouse position
    """
    pt = Point(0, 0)
    windll.user32.GetCursorPos(byref(pt))
    return pt


def edit_settings() -> None:
    """
    Interactively edit configured areas
    Break with ^C
    :return: None
    """
    areas = list()
    try:
        print('Changing settings for checked areas')
        print('Press ^C at any time to finish creating new rectagles')
        while True:
            rect_data = []
            input('Move mouse to the upper left corner of area and press enter ')
            rect_data.append(get_mouse_pos())
            input('Now the lower right corner ')
            rect_data.append(get_mouse_pos())
            areas.append(rect_data)
            print('Rectangle coordinates: ', rect_data, '\n')
    except KeyboardInterrupt:
        if input('\nDo you want to save settings? Y/n ').lower() == 'n':
            return
        # Save settings
        for area in areas:
            for i, subarea in enumerate(area):
                area[i] = [subarea.x, subarea.y]
        if not exists(get_parent_dir(FILE_CONFIG)):
            makedirs(get_parent_dir(FILE_CONFIG))
        with open(FILE_CONFIG, 'wt') as f:
            dump(areas, f)
        print('Saved')


def main_loop() -> None:
    """
    Checks if mouse enters one of the areas and if so toggles activities shown status
    :return: None
    """
    if not exists(FILE_CONFIG):
        print('Error: config file on "%s" does not exist' % FILE_CONFIG)
        print('Create it by running this script with -c parameter')
        return
    mouseover = False
    # Load config
    with open(FILE_CONFIG, 'rt') as f:
        areas = load(f)
    for area in areas:
        for i, subarea in enumerate(area):
            area[i] = Point(subarea[0], subarea[1])
    while True:
        mouseover_now = False
        mouse = get_mouse_pos()
        for area in areas:
            pos1 = area[0]
            pos2 = area[1]
            mouseover_now = pos1.x <= mouse.x <= pos2.x and pos1.y <= mouse.y <= pos2.y
            if mouseover_now:
                break
        if mouseover_now and not mouseover:
            toggle_activities()
        mouseover = mouseover_now
        sleep(CHECKING_DELAY)

if __name__ == '__main__':
    if '-c' in argv:
        edit_settings()
        exit(0)
    print('Entering main loop')
    try:
        main_loop()
    except KeyboardInterrupt:
        pass
    exit(0)
