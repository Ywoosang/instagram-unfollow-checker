from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Crawl:
    def __init__(self, Id, Passwd):
        self.Id = Id
        self.passwd = Passwd
        self.followingList = []
        self.followerList = []
        self.unfollowerList = []
        self.follow_number = 0
        self.following_number = 0

    def getProfile(self):
        Id = self.Id
        passwd = self.passwd
        chromedriver = "C:/Users/python/Webdriver/chromedriver.exe"
        driver = webdriver.Chrome(chromedriver)
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(time_to_wait=3)
        driver.get('https://www.instagram.com/')
        assert "Instagram" in driver.title
        time.sleep(2)
        id_section = driver.find_element_by_name('username')
        id_section.clear()
        id_section.send_keys(Id)
        pw_section = driver.find_element_by_name('password')
        pw_section.clear()
        pw_section.send_keys(passwd)
        try:
            pw_section.send_keys(Keys.RETURN)
            time.sleep(3)
        except Exception as e:
            print(e)
            driver.close()
            return 'Error'
        try:
            driver.get('https://www.instagram.com/%s/' % Id)
        except Exception as e:
            print("error :", e)
            driver.close()
            return 'Error'
        time.sleep(3)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        contents = soup.find('header', class_='vtbgv')
        try:
            img_link = contents.find('img', class_='be6sR')['src'] 
        except:
            try :
                img_link = contents.find('img',class_='_6q-tv')['src']
            except :
                img_link = 'notSet'
        name = contents.find('h1', class_='rhpdm').get_text()
        post_number = contents.find_all('span', class_='g47SY')[0].get_text()
        follow_number = contents.find_all('span', class_='g47SY')[1].get_text()  # string 타입
        following_number = contents.find_all(
            'span', class_='g47SY')[2].get_text()
        if follow_number == '' or following_number == '':
            driver.close()
            return 'Error'
        self.follow_number = follow_number
        self.following_number = following_number
        response = {}
        response['img'] = img_link
        response['name'] = name if name != '' else 'Unnamed'
        response['posts'] = post_number
        response['follower'] = follow_number
        response['following'] = following_number
        returnResponse = {'res': response, 'driver': driver}
        return returnResponse

    def startCrawl(self, driver):
        try:
            driver.find_element_by_css_selector(
                'ul > li:nth-child(2) > a').click()
        except Exception as e:
            print("error :", e)
            driver.close()
            return 'Error'
        result = self.getUserObject(driver, self.follow_number)
        if result != 'Error':
            self.followerList = result
        else:
            driver.close()
            return 'Error'
        try:
            xbutton = driver.find_element_by_css_selector(
                "div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg")
            xbutton.click()

        except TimeoutException as e:
            print(e, "Page load Timeout Occured")
            driver.close()
            pass
        try:
            driver.find_element_by_css_selector(
                'ul > li:nth-child(3) > a').click()
        except Exception as e:
            print("error :", e)
            driver.close()
            return 'Error'
        time.sleep(2)
        result = self.getUserObject(driver, self.following_number)
        print(self.following_number)
        if result != 'Error':
            self.followingList = result
        else:
            return 'Error'
        response = self.makeRetrunList()
        driver.close()
        return response

    def makeRetrunList(self):
        follower = [x['id'] for x in self.followerList]
        following = [x['id'] for x in self.followingList]
        unfollower = [x for x in following if x not in follower]
        unfollowerInfo = [
            x for x in self.followingList if x['id'] in unfollower]
        return unfollowerInfo

    def getUserObject(self, driver, follow_number):
        time.sleep(3)
        scrollbar = driver.find_element_by_css_selector('div.isgrP')
        scrollbar.click()
        time.sleep(2)
        currentFollowNumber = len(
            driver.find_elements_by_css_selector("li.wo9IH"))
        actionChain = webdriver.ActionChains(driver)
        while ((int(currentFollowNumber)+2) < int(follow_number)):
            time.sleep(1)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            if currentFollowNumber == len(driver.find_elements_by_css_selector("li.wo9IH")):

                scrollbar = driver.find_element_by_css_selector('div.isgrP')
                scrollbar.click()
            else:
                currentFollowNumber = len(
                    driver.find_elements_by_css_selector("li.wo9IH"))
        user_list = []
        time.sleep(1)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        items = soup.find_all('li', class_='wo9IH')
        for item in items:
            userObj = {}
            userObj['id'] = item.find('a', class_='_0imsa').get_text()
            if item.find('div', class_='wFPL8').get_text() != '':
                userObj['name'] = item.find('div', class_='wFPL8').get_text()
            else:
                userObj['name'] = 'Unnamed'
            userObj['img'] = item.find('img')['src']
            userObj['link'] = 'https://www.instagram.com' + \
                item.find('a', class_='_0imsa')['href']
            user_list.append(userObj)
        driver.set_page_load_timeout(2)
        return user_list
