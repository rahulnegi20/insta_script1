#madeby - rahulnegi , ig : _sarcaxtic_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

chromedriver_path = 'C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path="C:\\Users\\rahul negi\\Downloads\\whatsappBomber-master\\chromedriver.exe")
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(10)

print('Enter your username :')
key1 = input()
print('Enter your password: ')
key2 = input()


username = webdriver.find_element_by_name('username')
username.send_keys(key1)
password = webdriver.find_element_by_name('password')
password.send_keys(key2)

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(10)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm') #body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
sleep(4)
i = 1

name = "https://www.instagram.com/"
name += key1
name +="/"

webdriver.get(name)
sleep(3)
hash = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span').text
y= hash.replace(',', '')
flag = int(y)   # no. you are following


def unfollower_func() :
    try:
        # CLICKING THE CROSS BUTTON
        webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg').click()

        unfollow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span')
        # /html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span
        unfollow.click()
        sleep(2)
        # CONFIRMING UNFOLLOW
        webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_').click()


    except NoSuchElementException:
        # CLICKING THE CROSS BUTTON
        webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg').click()

        unfollow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
        unfollow.click()
        sleep(2)

        # CONFIRMING UNFOLLOW
        webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_').click()


while(flag >=0 ) :
        webdriver.get('https://www.instagram.com/ignoredbycrush/')
        sleep(5)
        # OUR FOLLOWING LIST :-
        following = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a')
        following.click()
        sleep(5)
        # FIRST SUBJECT PROFILE :-
        xpath1 = "/html/body/div[4]/div/div[2]/ul/div/li["
        xpath1 += str(i)
        xpath1 += "]/div/div[2]/div[1]/div/div/a"

        its_pro = webdriver.find_element_by_xpath(xpath1)
        its_pro.click()
        sleep(5)
        # SUBJECT'S FOLLOWING LIST :-
        its_list = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a')
        its_list.click()
        sleep(2)

        n = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span').text  # following of subject in int
        m = n.replace(',', '')
        print(m)
        l = int(m)
#calculations for no. of times of scroll down
        o = l // 2
        sleep(3)
        if l <= 10:
            unfollower_func()
            flag -=1

        else:
            try:

                while (o >= 1):
                    label = webdriver.find_element_by_xpath('//div[@class="PZuss"]//a')
                    label.send_keys(Keys.END)
                    sleep(5)
                    o -= 1
            except NoSuchElementException:
                pass

            for x in range(1, int(m)):

                xpath2 = "/html/body/div[4]/div/div[2]/ul/div/li["  # /html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a
                xpath2 += str(x)
                xpath2 += "]/div/div[1]/div[2]/div[1]/a"  # /html/body/div[4]/div/div[2]/ul/div/li/div/div[2]/div[1]/div/div/a if subject has only one follower unfollow

                ck = webdriver.find_element_by_xpath(xpath2).text

                if ck == key1 :
                    i += 1
                    flag -= 1
                    break

                if x == l - 1:
                    unfollower_func()
                    flag -=1

