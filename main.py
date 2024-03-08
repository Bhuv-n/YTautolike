import pyautogui,time
import openpyxl
import pyperclip
from openpyxl import Workbook, load_workbook

#variable = 'Some really "complex" string with\na bunch of stuff in it.'
#pyperclip.copy(variable)

time.sleep(10)

book = load_workbook('links.xlsx')
sheet = book.active
link = sheet['A']
for i in link:
    pyperclip.copy(i.value)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.click(819,930)
    #pyautogui.click("like2.png")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')