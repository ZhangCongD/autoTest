# -*- coding: utf-8 -*-

from appium import webdriver
import time
import unittest
time.sleep(3)

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.0.2"
desired_caps["deviceName"] = "Onetouch Idol 3(4.7)"
desired_caps["appPackage"] = "com.android.contacts"
desired_caps["appActivity"] = ".contacts"

class AddContactTest(unittest.TestCase):
	"""docstring for AddContactTest"""
	def setUp(self):
		self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
	def tearDown(self):
		self.driver.quit()

	def test_start(self):

		el1 = self.driver.find_element_by_id("com.android.contacts:id/floating_action_button")
		el1.click()

		el2 =self.driver.find_element_by_name("OK")
		el2.click()

		driver.quit()

if __name__ == '_main_':
	suite = unittest.TestLoader().loadTestsFromTestCase(AddContactTest)
	unittest.TextTestRunner(verbosity=2).run(suite)