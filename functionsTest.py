#coding:utf-8
'''
Created on 2016-6-12

@author: jm
'''
import unittest
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Test(unittest.TestCase):
    
    def test_serverStatus(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/')
        assert 'Page not found' in driver.page_source
        driver.close()
    
    def test_homePage(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/home')
        assert 'Home' in driver.title
        navigation = ['首页','科技','社会','娱乐','体育','军事']
        for na in navigation:
            assert na in driver.page_source
        driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_serverStatus']
    unittest.main()