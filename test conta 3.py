from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/dedec/Downloads/chromedriver.exe")
driver.get('https://twitter.com/explore')

lblUser = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input')
lblUser.send_keys('rolanice')
time.sleep(5.0)
lblSenha = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input')
lblSenha.send_keys('flamengo12')
time.sleep(5.0)
btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div')
btn.click()
time.sleep(10.0)

#postando
driver.get('https://twitter.com/_BrunoMestre_')
driver.get('https://twitter.com/_BrunoMestre_/status/1209258353978937344')
time.sleep(5.0)
btnComent = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[5]/div[1]/div')
btnComent.click()
time.sleep(5.0)
lblPost = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
for x in frases:
    lblPost.send_keys(x)
    btnResponder = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]')
    btnResponder.click()


#saindo
driver.get('https://twitter.com/logout')
time.sleep(10.0)
btnSair = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]')
btnSair.click()
time.sleep(5.0)
time.sleep(5.0)

#saindo
driver.get('https://twitter.com/logout')
time.sleep(10.0)
btnSair = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]')
btnSair.click()
time.sleep(5.0)