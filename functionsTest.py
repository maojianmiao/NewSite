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
        navigation = ['首页','科技','社会','娱乐','体育','军事','about']
        for na in navigation:
            assert na in driver.page_source
        driver.close()
        
    def test_login(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/user/login/')
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        assert '请输入正确的账号密码' in driver.page_source
        
        driver.find_element_by_name('username').send_keys('jm')
        driver.find_element_by_name('passwd').clear()
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        assert '请输入正确的账号密码' in driver.page_source
         
        driver.find_element_by_name('username').send_keys('jm')
        driver.find_element_by_name('passwd').send_keys('123123')
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        assert driver.current_url == 'http://127.0.0.1:8000/home/'
        driver.close()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_serverStatus']
    unittest.main()