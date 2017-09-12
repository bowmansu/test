#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://service.zol.com.cn/user/login.php')
#driver.find_element_by_xpath('//*[@id="unauth_main"]/div[1]/div[1]/h3[1]').click()
#driver.quit()
bbs_login_user_loc = {By.PARTIAL_LINK_TEXT, '账号登录'}
aboutlink= driver.find_element(By.XPATH,'//*[@id="unauth_main"]/div[1]/div[1]/h3[1]')
aboutlink.click()
#<h3>帐号登录</h3>
#//*[@id="unauth_main"]/div[1]/div[1]/h3[1]
#unauth_main > div.loginb > div.sitenav-login-top.clearfix > h3:nth-child(1)
#<h3>帐号登录</h3>
driver.close()