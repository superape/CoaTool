import time
import win32api
import win32con
from ctypes import *
from pynput.keyboard import Key, Controller

is_quite = 0

# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def on_press(key):
#     try:
#         print('字母键： {} 被按下'.format(key.char))
#     except AttributeError:
#         print('特殊键： {} 被按下'.format(key))
#
#
# def on_release(key):
#     print('{} 释放了'.format(key))
#     if key == keyboard.Key.esc:
#         # 释放了esc 键，停止监听
#         return False
#
#
# def on_keyboard_event():
#     with keyboard.Events() as events:
#         for event in events:
#
#             # 监听esc键，释放esc键，停止监听。
#             if event.key == keyboard.Key.esc:
#                 print('接收到事件 {}, 停止监听'.format(event))
#                 break
#             else:
#                 if isinstance(event, keyboard.Events.Press):
#                     print('按下按键 {} '.format(event))
#                 elif isinstance(event, keyboard.Events.Release):
#                     print('松开按键 {}'.format(event))


def on_press_a():
    is_quite = 1


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
    keyboard_controller.type(item_name)
    time.sleep(0.1)
    keyboard_controller.press('1')
    keyboard_controller.release('1')

    time.sleep(0.3) #这里必须0.3s
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
    keyboard_controller.press(Key.esc)
    keyboard_controller.release(Key.esc)

# Press the green button in the gutter to run the script.1
if __name__ == '__main__':
    # seria = win32gui.FindWindow(None, "Seria")kelao1kelao1kelao1kelao1

    # 定义一个键盘对象
    keyboard_controller = Controller()

    # listener111 = keyboard.Listener(
    #     on_press=on_press,
    #     on_release=on_release)
    # listener111.join()

    # keyboard.listen('a', on_press=on_press_a)

    # test
    # trade_tool(keyboard_controller, 'kelao')

    index = 1
    while index <= 100: #test
    #while 1:
        trade_tool(keyboard_controller, 'monv')
        time.sleep(0.1)
        # trade_tool(keyboard_controller, 'gangtie')
        # time.sleep(0.1)
        print(index)
        index = index + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
