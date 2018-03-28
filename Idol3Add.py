#coding=utf-8
from appium import webdriver
import time
import unittest

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.2'
desired_caps['deviceName'] = 'Onetouch Idol 3(4.7)'
desired_caps['appPackage'] = 'com.tct.calculator'
desired_caps['appActivity'] = '.Calculator'

class AddTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testStart(self):
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("5").click()
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("delete").click()
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("5").click()
        self.driver.find_element_by_name("+").click()
        self.driver.find_element_by_name("6").click()
        self.driver.find_element_by_name("=").click()
        time.sleep(3)

        self.assertEqual(self.driver.find_element_by_id('formula').text, '1601')
        time.sleep(3)

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(AddTest)

    unittest.TextTestRunner(verbosity=2).run(suite)


    


