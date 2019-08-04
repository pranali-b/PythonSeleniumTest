'''
Created on Aug 2, 2019

@author: pranalibankar
'''
import unittest
from selenium import webdriver
from Modules.LoginModule import testMymodule
from Modules.AccountModule import testMyAccountmodule


class Test(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        
        self.driver =webdriver.Chrome(executable_path="/Users/pranalibankar/eclipse-workspace/chromedriver")
        self.driver.get("https://login.salesforce.com/")

    @classmethod
    def tearDown(self):
        self.driver.quit()

#testcase1
    def testloginerror(self):
          
        driver=self.driver
        driver.find_element_by_id("username").send_keys("User@gmail.com")          
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("Login").click()
        actual=driver.find_element_by_id("error").text
        driver.implicitly_wait(5)
          
        expected = "Please enter your password."
        self.assertEquals(expected,actual)
        driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/login.png")
           
  #testcase2        
    def testCheckrememberme(self):
        driver=self.driver
        loginobj=testMymodule(driver)
        loginobj.testMyLogin()
        driver.find_element_by_id("userNav-arrow").click()
        driver.find_element_by_partial_link_text("Logout").click()
        driver.implicitly_wait(20)
        actualid=driver.find_element_by_id("idcard-identity").text
        expected = "pranali.lonkar030@gmail.com"
        self.assertEquals(expected,actualid)
        driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/checkrememberme.png")
        
#testcase3
    def testForgotPassword(self):
              
         driver=self.driver
         driver.find_element_by_id("forgot_password_link").click()
         driver.implicitly_wait(20)
         driver.find_element_by_name("un").send_keys("pranali.lonkar030@gmail.com")
         driver.implicitly_wait(20)
         driver.find_element_by_id("continue").click() 
         actualresetpage=driver.find_element_by_id("header").text
         expected = "Check Your Email"
         self.assertEquals(expected,actualresetpage)
         driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/forgotpswd.png")
               
#testcase4
    def testValidatelogin(self):
         driver=self.driver
         driver.find_element_by_id("username").send_keys("123")
         driver.find_element_by_id("password").clear()
         driver.find_element_by_id("password").send_keys("22131")
         driver.find_element_by_id("Login").click()
         driver.implicitly_wait(20)
         actualerrmsg=driver.find_element_by_id("error").text
         driver.implicitly_wait(5)
              
         expected = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."
         self.assertEquals(expected,actualerrmsg)
         driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/loginerrormsg.png")
              
#testcase5
    def testCreateaccnt(self):
        driver=self.driver
        loginobj=testMymodule(driver)
        loginobj.testMyLogin()
        acntobj=testMyAccountmodule(driver)
        acntobj.testAccnt()
        driver.find_element_by_name("new").click()
        driver.find_element_by_id("acc2").send_keys("ppppr")
        driver.implicitly_wait(20)
        driver.find_element_by_name("save").click()
        driver.implicitly_wait(20)
        self.assertIn("Salesforce - Developer Edition",driver.title)
        driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/createacnt.png")
            
#testcase6
    def testCreatenewlink(self):
        driver=self.driver
        loginobj=testMymodule(driver)
        loginobj.testMyLogin()
        acntobj=testMyAccountmodule(driver)
        acntobj.testAccnt()
        driver.find_element_by_partial_link_text("Create New View").click()
        driver.implicitly_wait(20)
        driver.find_element_by_id("fname").send_keys("prana")
        driver.implicitly_wait(20)
        driver.find_element_by_id("devname").send_keys("praaaaa") 
        driver.find_element_by_name("save").click()
        driver.implicitly_wait(20)
       # self.assertIn("Accounts ~ Salesforce - Developer Edition",driver.title)
        driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/createnewlink.png") 
            
    #testcase7    
    def testOpportunitylink(self):   
         driver=self.driver
         loginobj=testMymodule(driver)
         loginobj.testMyLogin()
         driver.find_element_by_id("Opportunity_Tab").click()
         driver.implicitly_wait(20)
         driver.find_element_by_id("fcf").click()
         driver.implicitly_wait(20)
         self.assertIn("Opportunities: Home ~ Salesforce - Developer Edition",driver.title)
         driver.implicitly_wait(50)
         driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/opprtlink.png") 
          
 #testcase8     
    def testContactTab(self):
         driver=self.driver
         loginobj=testMymodule(driver)
         loginobj.testMyLogin()
         driver.find_element_by_id("Contact_Tab").click()
         driver.implicitly_wait(20)
         driver.find_element_by_name("new").click()
         driver.implicitly_wait(20)
         driver.find_element_by_id("name_lastcon2").send_keys("praha")
         driver.implicitly_wait(20)
         driver.find_element_by_id("con4").send_keys("ppp")
         driver.implicitly_wait(20)
         driver.find_element_by_name("save").click()
         driver.implicitly_wait(20)
         self.assertIn("",driver.title)
         driver.save_screenshot("/Users/pranalibankar/eclipse-workspace/PythonSeleniumTest/reports/contactlnk.png")          
          
         
    if __name__ == "__main__":
        
    #import sys;sys.argv = ['', 'Test.testName']
         unittest.main()
    