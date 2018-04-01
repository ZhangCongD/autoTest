# -*- coding: utf-8 -*-
# from appium import webdriver
import time
# import unittest
# import os
import subprocess
import threading

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

# 调用子进程devices = []
devices = subprocess.Popen(  
    'adb devices'.split(),  
    stdout=subprocess.PIPE,  
    stderr=subprocess.PIPE  
).communicate()[0]  

#获取设备号
serial_nos = []  
for item in devices.split():  
    itemStr = item.decode(encoding="utf-8")
    filters = ['list','of','device','devices','attached']  
    if itemStr.lower() not in filters: 
        serial_nos.append(itemStr)  

reboot_cmds = []
for serial_no in serial_nos: 
    reboot_cmds.append('adb -s %s reboot' % serial_no) 

#执行多次adb reboot命令，实现多次重启测试
def rebootLoop():
    for i in range(1,5):
        p = subprocess.Popen(  
        	reboot_cmd.split(),	
            stdout=subprocess.PIPE,  
            stderr=subprocess.PIPE, shell=True
        )

        #如果在执行重启命令时报错，则终止重启循环，比打印报错信息（手机断开与电脑的连接）
        stdout,stderr = p.communicate()
        stderrStr = stderr.decode(encoding="utf-8")
        print('the %d times reboot by thread %s' % (i, threading.current_thread().name)) 
        if stderrStr is not None and len(stderrStr) != 0 :
            print('stop reboot becasuse there is an error : ',stderrStr)
            return       
        time.sleep(60) 

#创建多个线程，实现多台手机同时测试
# i = 0
for reboot_cmd in reboot_cmds:
    print(reboot_cmd)
    # str1 = str(i) 
    # t = threading.Thread(target=rebootLoop, name='rebootLoopThread'+str1)
    t = threading.Thread(target=rebootLoop, name='rebootLoopThread')
    # i = i+1
    t.start()
  
# print('thread %s ended.' % threading.current_thread().name)