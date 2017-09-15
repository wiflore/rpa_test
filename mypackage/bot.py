import pyautogui
from pywinauto.application import Application
import time
import os

#"Imaging tolerance"
#excel


def open_app(text):
    app = Application().start(text)
    time.sleep(3)
#create folder, optional parameter

def click_screen(path, button):
    img = path + button
    screenshot = path + "screen/" + button

    if not os.path.exists(screenshot):
        os.makedirs(screenshot)

    pyautogui.screenshot(screenshot)
    address = pyautogui.locateOnScreen(img)
    coordinate_x, coordinate_y = pyautogui.center(address)
    pyautogui.click(coordinate_x, coordinate_y)
    time.sleep(0.8)


def double_click_screen(path, button):
    img = path + button
    screenshot = path + "screen/"

    if not os.path.exists(screenshot):
        os.makedirs(screenshot)
    screenshot = screenshot + button
    pyautogui.screenshot(screenshot)
    address = pyautogui.locateOnScreen(img)
    coordinate_x, coordinate_y = pyautogui.center(address)
    pyautogui.click(coordinate_x, coordinate_y, clicks = 2,  interval= 0.5)
    time.sleep(0.8)

def write_text(text):
    pyautogui.typewrite(text, interval=0.05)


def locate(path, text):
    name = 'locate_rstudio.PNG'
    click_screen(name)


def save(text, path_save):
    name = text
    click_screen(name)
    time.sleep(1)
    write_text(r+path_save)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(0.5)

def presskey(key):
    pyautogui.press(key)

def send_email(subject, body, to):
    import win32com.client
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)

    newMail.Subject = subject
    newMail.Body = body
    newMail.To = to

    # newMail.CC = "moreaddresses here"
    # newMail.BCC = "address"
    # attachment1 = "Path to attachment no. 1"
    # attachment2 = "Path to attachment no. 2"
    # newMail.Attachments.Add(attachment1)
    # newMail.Attachments.Add(attachment2)
    # newMail.display()
    newMail.Send()

def pause(sec):
    time.sleep(sec)


def mouse_moveTo(x, y):
    pyautogui.moveTo(x, y)
