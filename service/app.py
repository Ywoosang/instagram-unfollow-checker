from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import urllib.request
import time
from selenium.common.exceptions import TimeoutException 
# chromedriver 설치된 경로를 정확히 기재해야 함

app = Flask(__name__, static_url_path="/static")

@app.route('/') 
def mainpage():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def resultpage():
    Id = request.form['Id']  
    passwd = request.form['passwd']  


# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
    chromedriver ="C:\Users\python\Webdriver/chromedriver.exe" 
    # headless_options = webdriver.ChromeOptions() 

    #옵션을 넣어서 좀더 사용자가 웹브라우저를 들어가는 것 처럼 
    # headless_options.add_argument('headless')
    # headless_options.add_argument('window-size=1920x1080')
    # headless_options.add_argument("disable_gpu")
    # headless_options.add_argument("lang=ko_KR")

    # driver = webdriver.Chrome(chromedriver, options= headless_options)
    driver = webdriver.Chrome(chromedriver)
    driver.set_window_size(1920, 1080) 
    driver.get('https://www.instagram.com/')
    #웹페이지 이름에 Instagram 이 없으면 에러 발생 (중단)
    assert "Instagram"  in driver.title 

    #웹 페이지 로드를 보장하기 위해 3초 쉰다.
    time.sleep(3)

    id_section = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input") 
    #검색 창에 미리 써있는 내용들 지워줌 
    id_section.clear()
    #검색할 내용 전송 (키 이벤트)
    id_section.send_keys("yd_w_sang") 

    pw_section = driver.find_element_by_name('password')
    pw_section.clear() 

    pw_section.send_keys("Hje5227070!") 
    pw_section.send_keys(Keys.RETURN)
    # 엔터 입력  
    time.sleep(3)


    #계정 이메일로 수정 요망
    driver.get('https://www.instagram.com/yd_w_sang/followers/')  
    time.sleep(3)

    #계정의 팔로우, 팔로잉 수 가져오기  
    follow = driver.find_elements_by_css_selector('ul>li> a > span')
    follow_number_list = []

    for i in follow :
        follow_number_list.append(i.text) 
        
    follow_number = follow_number_list[0] 
    following_number = follow_number_list[1] 
    print(follow_number)
    print(following_number)


    #css_selector 로 코드 구성이 ul> li > a 인 태그들을 가져온다 (팔로워,팔로잉 버튼) 
    followersLink = driver.find_elements_by_css_selector('ul> li > a') 
    followersLink[0].click() 
    time.sleep(3) 

    #div 태그 안에있는  role 속성 값이 'dialog' 인 ul 태그를 선택. 파이썬이 문자열이 여기서 끝난다고 인식하지 않도록 / 붙여줌
    followersList = driver.find_element_by_css_selector('div div div.isgrP') 


    print(followersList) 
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('div li.wo9IH')) 
    

    #아래로 스크롤을 내릴 수 있도록 스페이스키 동작시킴
    followersList.click()
    time.sleep(2)
    actionChain = webdriver.ActionChains(driver)  
    followersName = []
    followersId = [] 
    
    while ((int(numberOfFollowersInList)+2)< int(follow_number)):
        actionChain.key_down(Keys.SPACE).perform()
        actionChain.key_up(Keys.SPACE).perform()
        numberOfFollowersInList = len(driver.find_elements_by_css_selector("li.wo9IH" )) 
        if numberOfFollowersInList == 24 :
            followersList.click() 
            
        #print(numberOfFollowersInList)    
    for person in followersList.find_elements_by_css_selector('li'):
        username = person.find_elements_by_css_selector('li > div >div>div>div')
        userId = person.find_elements_by_css_selector('li > div > div > div > div > span > a')
        followersName.append(username[2].text) 
        followersId.append(userId[0].text)
        
        #userLink = user.find_element_by_css_selector('a').get_attribute('href')
        
        # if (len(followers) == max):
        #     break 
    # print(followersName) 


    print(followersId)


    driver.set_page_load_timeout(2)
    try :
        xbutton=driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg")
        xbutton.click() 
        driver.get("https://www.instagram.com/yd_w_sang/")
        print("URL successfully Accessed")
        time.sleep(2)
    except TimeoutException as e:
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()
    
        
    print("넘어감") 
    followingLink = driver.find_elements_by_css_selector('header section ul li a') 
    followingLink[1].click() 
    time.sleep(3) 

    #div 태그 안에있는  role 속성 값이 'dialog' 인 ul 태그를 선택. 파이썬이 문자열이 여기서 끝난다고 인식하지 않도록 / 붙여줌
    followingList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul') 
    numberOfFollowingsInList = len(followingList.find_elements_by_css_selector('li')) 
    print("넘어감2") 

    #아래로 스크롤을 내릴 수 있도록 스페이스키 동작시킴
    followingList.click() 
    time.sleep(2)
    
    actionChain = webdriver.ActionChains(driver)  
    while (numberOfFollowingsInList+2 < int(following_number)):
        actionChain.key_down(Keys.SPACE).perform()
        actionChain.key_up(Keys.SPACE).perform()
        print('여기까지 ok')
        numberOfFollowersInList = len(driver.find_elements_by_css_selector("li.wo9IH" )) 
        if numberOfFollowersInList == 24 :
            followingList.click() 
            
            
        
        #숫자 갱신  
    #  followersList.click()
        numberOfFollowingsInList = len(followingList.find_elements_by_css_selector('li')) 
        if numberOfFollowingsInList == 24 :
            followingList.click()
        #print(numberOfFollowersInList) 
    time.sleep(2)    
    followingsName = []
    followingsId = [] 
    print('여기까지 ok')
    for person in followingList.find_elements_by_css_selector('li'):
        username = person.find_elements_by_css_selector('li > div >div>div>div')
        userId = person.find_elements_by_css_selector('li > div > div > div > div > span > a') 
        print('여기까지 ok')
        followingsName.append(username[2].text) 
        followingsId.append(userId[0].text) 

    same_membersId = set(followersId) & set(followingsId)
    only_membersId = set(followingsId) - set(same_membersId)

    same_membersName = set(followersName) & set(followingsName)
    only_membersName = set(followingsName) - set(same_membersName)
    print(list(only_membersId))  
    print(list(only_membersName))

    ziplist = zip(list(only_membersId),list(only_membersName)) 
    print(ziplist)

    return render_template("result.html" , ziplist=ziplist)
         

if __name__ == '__main__':
    app.run()  







        