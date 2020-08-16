from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import urllib.request
import time
# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver ="c:/Users/82105/Desktop/Python/chromedriver.exe" 
headless_options = webdriver.ChromeOptions()

#옵션을 넣어서 좀더 사용자가 웹브라우저를 들어가는 것 처럼 
headless_options.add_argument('headless')
headless_options.add_argument('window-size=1920x1080')
headless_options.add_argument("disable_gpu")
headless_options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(chromedriver, options= headless_options)


driver.get('https://www.instagram.com/')
#웹페이지 이름에 Instagram 이 없으면 에러 발생 (중단)
assert "Instagram"  in driver.title 

#웹 페이지 로드를 보장하기 위해 3초 쉰다.
time.sleep(3)

id_section = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input") 
#검색 창에 미리 써있는 내용들 지워줌 
id_section.clear()
#검색할 내용 전송 (키 이벤트)
id_section.send_keys("계정의 아이디") 

pw_section = driver.find_element_by_name('password')
pw_section.clear() 

pw_section.send_keys("계정의 비밀번호") 
pw_section.send_keys(Keys.RETURN)
# 엔터 입력  
time.sleep(2)


#계정 이메일로 수정 요망
driver.get('https://www.instagram.com/yd_w_sang/followers/')  


#계정의 팔로우, 팔로잉 수 가져오기  
follow = driver.find_elements_by_css_selector('ul>li> a > span')
follow_number_list = []

for i in follow :
    follow_number_list.append(i.text) 
follow_number = follow_number_list[0] 
following_number = follow_number_list[1] 


#css_selector 로 코드 구성이 ul> li > a 인 태그들을 가져온다 (팔로워,팔로잉 버튼) 
followersLink = driver.find_elements_by_css_selector('ul> li > a') 
followersLink[0].click() 
time.sleep(2) 

#div 태그 안에있는  role 속성 값이 'dialog' 인 ul 태그를 선택. 파이썬이 문자열이 여기서 끝난다고 인식하지 않도록 / 붙여줌
followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul') 
numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li')) 


#아래로 스크롤을 내릴 수 있도록 스페이스키 동작시킴
followersList.click()
 
actionChain = webdriver.ActionChains(driver)  
while (numberOfFollowersInList < int(follow_number)):
    actionChain.key_down(Keys.SPACE).perform()
    actionChain.key_up(Keys.SPACE).perform()
     
    #숫자 갱신  
  #  followersList.click()
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li')) 
    if numberOfFollowersInList == 24 :
        followersList.click()
    #print(numberOfFollowersInList)    

followers = []
for person in followersList.find_elements_by_css_selector('li'):
    username = person.find_elements_by_css_selector('li > div >div>div>div')
    followers.append(username[2].text) 
    
    #userLink = user.find_element_by_css_selector('a').get_attribute('href')
    
    # if (len(followers) == max):
    #     break 
print(followers)



time.sleep(2) 
driver.get('https://www.instagram.com/yd_w_sang/followers/') 

followingLink = driver.find_elements_by_css_selector('ul> li > a') 
followingLink[1].click() 
time.sleep(2) 

#div 태그 안에있는  role 속성 값이 'dialog' 인 ul 태그를 선택. 파이썬이 문자열이 여기서 끝난다고 인식하지 않도록 / 붙여줌
followingList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul') 
numberOfFollowingsInList = len(followingList.find_elements_by_css_selector('li')) 


#아래로 스크롤을 내릴 수 있도록 스페이스키 동작시킴
followingList.click()
 
actionChain = webdriver.ActionChains(driver)  
while (numberOfFollowingsInList < int(following_number)):
    actionChain.key_down(Keys.SPACE).perform()
    actionChain.key_up(Keys.SPACE).perform()
     
    #숫자 갱신  
  #  followersList.click()
    numberOfFollowingsInList = len(followingList.find_elements_by_css_selector('li')) 
    if numberOfFollowingsInList == 24 :
        followingList.click()
    #print(numberOfFollowersInList)    
followings = []
for person in followingList.find_elements_by_css_selector('li'):
    username = person.find_elements_by_css_selector('li > div >div>div>div')
    followings.append(username[2].text) 
print(followings) 

same_members = set(followers) & set(followings)
only_members = set(followings) - set(same_members)
print(list(only_members))  





