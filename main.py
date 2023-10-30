import time
import win32api
import win32con
import pyperclip
from ctypes import *
from pynput import keyboard
from threading import Thread

is_quite = False


# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def listen():  # 键盘监听函数
    print("listening")

    def on_press(key):
        global is_quite_global
        if key == keyboard.Key.f1:
            is_quite_global = True

    def on_release(key):
        global is_quite_global

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


class ListenThread(Thread):  # 截屏监听线程
    def __init__(self):
        super().__init__()

    def run(self):
        listen()


def mouse_click(x, y, interval):
    # 把鼠标放置到登陆框的输入处
    # 用坐标工具获取
    windll.user32.SetCursorPos(x, y)
    time.sleep(interval)
    # 按下鼠标再释放
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # press mouse

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # release mouse


def trade_tool(keyboard_controller, item_name):
    # 输入商品名
    mouse_click(2150, 274, 0)
    time.sleep(0.01)
    pyperclip.copy(item_name)
    keyboard_controller.press(keyboard.Key.ctrl_l)
    keyboard_controller.press('v')
    keyboard_controller.release('v')
    keyboard_controller.release(keyboard.Key.ctrl_l)

    time.sleep(0.2)
    # 点击商品名
    mouse_click(2026, 360, 0)

    time.sleep(0.2)
    # 点击商品
    mouse_click(1124, 495, 0)

    time.sleep(0.1)
    # 点击购买
    mouse_click(1278, 900, 0)

    time.sleep(0.1)

    # test
    # keyboard_controller.press(keyboard.Key.esc)
    # keyboard_controller.release(keyboard.Key.esc)


def trade_tool_full_screen(keyboard_controller, item_name):
    # 输入商品名
    mouse_click(2300, 150, 0)
    time.sleep(0.01)
    pyperclip.copy(item_name)
    keyboard_controller.press(keyboard.Key.ctrl_l)
    keyboard_controller.press('v')
    keyboard_controller.release('v')
    keyboard_controller.release(keyboard.Key.ctrl_l)

    time.sleep(0.2)
    # 点击商品名
    mouse_click(2296, 240, 0)

    time.sleep(0.2)
    # 点击商品
    mouse_click(1046, 422, 0)

    time.sleep(0.1)
    # 点击购买
    mouse_click(1300, 992, 0)

    time.sleep(0.1)

    # test
    keyboard_controller.press(keyboard.Key.esc)
    keyboard_controller.release(keyboard.Key.esc)


# Press the green button in the gutter to run the script.1
if __name__ == '__main__':
    global is_quite_global
    is_quite_global = False

    # seria = win32gui.FindWindow(None, "Seria")kelao1kelao1kelao1kelao1

    # 定义一个键盘对象
    keyboard_controller = keyboard.Controller()

    # 创建退出键监听线程
    listenThread = ListenThread()
    listenThread.start()

    # test
    # trade_tool(keyboard_controller, '克劳')

    index = 1
    # while index <= 10: #test
    while not is_quite_global:
        trade_tool_full_screen(keyboard_controller, '魔女')
        time.sleep(0.1)

        # test
        # trade_tool(keyboard_controller, '钢铁')
        # time.sleep(0.1)

        print(index)
        index = index + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
