import pyautogui, time
time.sleep(3)
f = open("Bee Movie Script - Dialogue Transcript", 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	time.sleep(1.2)
