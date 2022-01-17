from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.hltv.org/stats/teams/matches/10709/sws")

#astralis
#evilgeniuses
#navi
#redragon
#sws

ar1 = [el.text for el in driver.find_elements_by_xpath("//tr/td[6]/span")]

x=0
t=30
tkd = []

for i in range(20):
    x += 1
    t += 30
    driver.find_element_by_xpath(f'//tr[{x}]/td[4]/a').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/form/select/option[3]').click()
    tkd.append(driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[8]/div[3]/div[1]").text)
    print(tkd[i])
    time.sleep(0.5)
    driver.back()
    driver.back()
    driver.execute_script(f"window.scrollTo(0, {t})")
    time.sleep(0.5)

f = open("csgo.txt", "a")
f.write("W, L, MP")

for i in range(20):
    x = ar1[i].split();
    kd = tkd[i]
    y = ""
    if int(x[0]) > int(x[2]):
        y = "1"
    else:
        y = "0"
    f.write("\n"+ x[0] + ", " + x[2] + ", " + y +", " + "1.0" + ", " + kd)

print("done.")
driver.quit()