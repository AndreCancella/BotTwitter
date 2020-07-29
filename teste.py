from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/dedec/Downloads/chromedriver.exe")
driver.get('https://twitter.com/login')
driver.maximize_window()

#entrando na primeira conta
lblUser = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
lblUser.send_keys('selinium12@gmail.com')
time.sleep(5.0)
lblSenha = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
lblSenha.send_keys('flamengo12')
time.sleep(5.0)
btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
btn.click()
time.sleep(10.0)

#postando
lblPost = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
lblPost.send_keys('Boa noite meus consagrados')
btnPost = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div')
btnPost.click()
time.sleep(10.0)

#saindo
driver.get('https://twitter.com/logout')
time.sleep(10.0)
btnSair = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]')
btnSair.click()
time.sleep(5.0)


driver.quit()
