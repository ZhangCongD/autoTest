#coding=utf-8
# from appium import webdriver
# import time
# import unittest
# import os
import subprocess

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.0.2'
# desired_caps['deviceName'] = 'Onetouch Idol 3(4.7)'
# desired_caps['appPackage'] = 'android'
# # desired_caps['appActivity'] = '.Calculator'

# # class RestartTest(unittest.TestCase):
# #     def setUp(self):
# #         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# #     def tearDown(self):
# #         self.driver.quit()

# #     def testStart(self):
# #         self.driver.find_element_by_id("reboot_layout").click()
# #         time.sleep(1)
# #         self.driver.find_element_by_id("button1").click()
# #         time.sleep(1)

# #         # self.assertEqual(self.driver.find_element_by_id('formula').text, '1601')
# #         time.sleep(3)

# if __name__ == '__main__':

#     suite = unittest.TestLoader().loadTestsFromTestCase(AddTest)

#     unittest.TextTestRunner(verbosity=2).run(suite)

# n = 1
# for n in range(1,100):
#     os.system("adb shell reboot")
#     print("第%d次重启"%n) 
#     n = n + 1
#     time.sleep(60)
#     if os.system("adb devices"):
#     	print("手机断开连接")
#     	break


devices = subprocess.Popen(  
    'adb devices'.split(),  
    stdout=subprocess.PIPE,  
    stderr=subprocess.PIPE  
).communicate()[0]  

serial_nos = []  
for item in devices.split():  
    itemStr = item.decode(encoding="utf-8")
    filters = ['list','of','device','devices','attached']  
    if itemStr.lower() not in filters: 
        print(itemStr) 
        serial_nos.append(itemStr)  
reboot_cmds = []
for serial_no in serial_nos: 
    reboot_cmds.append('adb -s %s reboot' % serial_no)  
for reboot_cmd in reboot_cmds:  
    subprocess.Popen(  
        reboot_cmd.split(),  
        stdout=subprocess.PIPE,  
        stderr=subprocess.PIPE  
    ).communicate()[0]  



