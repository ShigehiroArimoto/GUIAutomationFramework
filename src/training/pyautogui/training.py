import logging,os
import subprocess
import pyautogui
import csv,pprint
import pyperclip

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width,height = pyautogui.size()
print(pyautogui.size())

pyautogui.moveTo(100,100,duration=0.25) # 指定した絶対座標にマウスカーソルを移動する。duration:移動に要する時間

for i in range(5):
    pyautogui.moveRel(10,10,duration=0.25) #現地点を基準とした相対的な座標にマウスカーソルを移動する。

print(pyautogui.position())

pyautogui.click(0,1070,button='left')
pyautogui.click(button='right')
pyautogui.doubleClick()

pyautogui.moveTo(width/3,height/3,duration=0.25)
pyautogui.doubleClick()

pyautogui.dragRel(0,100,duration=1)


x,y = pyautogui.locateCenterOnScreen(os.path.join(os.path.dirname(__file__),"command.png"),confidence=0.8,region=(0,500,1927,1079))
pyautogui.click(x,y)

pyautogui.write("ShigehiroArimoto")

pyperclip.copy(u"リラックマ")
pyautogui.hotkey('ctrl','v')

pyautogui.press("enter")

screenshot = pyautogui.screenshot()
screenshot.save(os.path.join(os.path.dirname(__file__),"test.png"))



