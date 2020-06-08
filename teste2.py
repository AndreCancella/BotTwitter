from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/dedec/Downloads/chromedriver.exe")
driver.get('https://twitter.com/login')
driver.maximize_window()

lblUser = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
lblUser.send_keys('AndreCancella')

lblSenha = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
lblSenha.send_keys('cancella12')
time.sleep(5.0)
btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
btn.click()
time.sleep(5.0)

driver.get('https://twitter.com/SeliniumTeste')
time.sleep(5.0)
btnRt = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/div/div/div/article')
btnRt.click()
time.sleep(5.0)
btnRT2 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[3]/div[2]/div')
btnRT2.click()
time.sleep(5.0)
btnRT3 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div')
btnRT3.click()
