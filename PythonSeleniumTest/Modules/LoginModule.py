'''
Created on Aug 2, 2019

@author: pranalibankar
'''

#from selenium import webdriver

class testMymodule(object):
    def __init__(self, driver):
         self.driver = driver
         
    def testMyLogin(self):
        driver=self.driver
        driver.find_element_by_id("username").send_keys("pranali.lonkar030@gmail.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("pranali321")
        driver.implicitly_wait(20)
        driver.find_element_by_name("rememberUn").click()
        driver.find_element_by_id("Login").click()
        driver.get("https://na49.salesforce.com/home/home.jsp?source=lex")
        driver.implicitly_wait(20)