import pyautogui
import subprocess
import time

# Open the VPN software
subprocess.call("C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\\vpnui.exe")

# Click buttons based on reference images
time.sleep(1)
pyautogui.click('images/button2.png') # Find where image appears on the screen and click it.
time.sleep(8)
pyautogui.click('images/connect_anyway.png') # Find where image appears on the screen and click it.
time.sleep(5) # Delay to allow screen to come up before typing
pyautogui.write('hvac', interval=0.25)
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click()

