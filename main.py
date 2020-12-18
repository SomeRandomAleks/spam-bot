import pyautogui, time
time.sleep(3)
f = open("text", 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	time.sleep(1.2)
