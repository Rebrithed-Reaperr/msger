import pythonautogui, time
time.sleep(5)
f = open("hi", 'r')
for word in f:
    pythonautogui.typewrite(word)
    pythonautogui.press("enter")