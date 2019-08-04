'''
Created on Aug 2, 2019

@author: pranalibankar
'''

class testMyAccountmodule(object):
    def __init__(self, driver):
         self.driver = driver
         
    def testAccnt(self):
        driver=self.driver
        driver.find_element_by_id("Account_Tab").click()
        driver.implicitly_wait(20)