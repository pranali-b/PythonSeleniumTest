'''
Created on Aug 3, 2019

@author: pranalibankar
'''
import unittest
import os
import HtmlTestRunner
direct = os.getcwd()
from SalesforceTestCases.automation import Test

class MyTestSuite(unittest.TestCase):


    def testSalesforce(self):
        Functional_Test = unittest.TestSuite()
        Functional_Test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test)
        ])
 
        outfile = open(direct + "\reportTest.html", "w")
 
        runner =HtmlTestRunner.HTMLTestRunner(
            stream=outfile,
            descriptions='Test Report',

            
        )
 
        runner.run(Functional_Test)
 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
     unittest.main()