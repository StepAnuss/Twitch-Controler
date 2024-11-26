import pyautogui
from twitch_chat_irc import twitch_chat_irc
import time

InputDelay = 1
PowerOfDrag = 100
def do_something(message):
    mes = message['message']
    print(mes)
    if len(mes) == 1:
        pyautogui.keyDown(mes)
        time.sleep(InputDelay)
        pyautogui.keyUp(mes)
    elif mes == 'Right':
        pyautogui.drag(PowerOfDrag, 0,0.5)
    elif mes == 'Left':
        pyautogui.drag(-PowerOfDrag,0,0.5)
    elif mes == 'Up':
        pyautogui.drag(0,-PowerOfDrag,0.5)
    elif mes == 'Down':
        pyautogui.drag(0,PowerOfDrag,0.5)
    elif mes == 'Jump':
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
    elif mes == 'Punch':
        pyautogui.click()
    elif mes == 'Place':
        pyautogui.rightClick()


connection = twitch_chat_irc.TwitchChatIRC('USERNAME', 'oauth:')
connection.listen('USERNAME', on_message=do_something)
