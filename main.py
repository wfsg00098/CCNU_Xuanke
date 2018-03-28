from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

print("温馨提示：请将浏览器最小化以加快速度，但是不可关闭！\n")


username = ""

password = ""

class_name = "法律与生活"

class_number = "1"

firefoxdir = "C:\\Program Files\\Mozilla Firefox\\"
chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
# browser = webdriver.Firefox(firefoxdir)
browser.implicitly_wait(30)
try:
    url = "http://xk.ccnu.edu.cn/ssoserver/login?ywxt=jw&url=xtgl/index_initMenu.html"
    browser.get(url)
except:
    pass

delay = 1
count = 0
flag = 0
while 1:
    print("尝试登录")
    while 1:
        try:
            browser.find_element_by_name("username").send_keys(username)
            browser.find_element_by_name("password").send_keys(password)
            break
        except:
            count = count + 1
            print("页面加载失败，刷新重试..." + str(count))
            if browser.current_url == url:
                try:
                    browser.refresh()
                except:
                    pass
            else:
                try:
                    browser.get(url)
                except:
                    pass
            continue

    try:
        browser.find_element_by_xpath("//*[@id=\"fm1\"]/section[3]/table/tbody/tr/td[2]/img")
        print("发现验证码，请打开网页识别后在本程序中输入！")
        code = input()
        browser.find_element_by_xpath("//*[@id=\"captcha\"]").send_keys(code)
    except:
        print("未发现验证码")

    try:
        browser.find_element_by_name("submit").send_keys(Keys.ENTER)
        print("登陆成功！")
        flag = 1
    except:
        print("登录失败")

    if flag == 1:
        break


try:
    browser.switch_to.alert.accept()
except:
    pass

browser.implicitly_wait(120)
try:
    url2 = "http://xk.ccnu.edu.cn//xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=" + username
    browser.get(url2)
except:
    pass

try:
    browser.switch_to.alert.accept()
except:
    pass

print("登录成功")

while 1:
    try:
        print("尝试搜索课程，步骤1")
        browser.find_element_by_xpath("//*[@id=\"searchBox\"]/div/div[2]/div/div/div/div/a/span").click()
        browser.find_element_by_name("searchInput").send_keys(class_name)
        browser.find_element_by_name("query").send_keys(Keys.ENTER)
        break
    except:
        print("页面加载失败，刷新重试")
        if browser.current_url == url2:
            try:
                browser.refresh()
            except:
                pass
        else:
            try:
                browser.get(url2)
            except:
                pass
        continue

class_id = None
class_n = None

while 1:
    print("尝试搜索课程，步骤2-1")
    lists = browser.find_elements_by_class_name("body_tr")
    print("尝试搜索课程，步骤2-2")
    if (len(lists) > 0): break

print("课程搜索完成\n尝试查找教学班")
i = 0
for i in range(0, len(lists) + 1):
    class_id = lists[i].get_attribute("id")[3:]
    class_n = browser.find_element_by_xpath("//*[@id=\"tr_" + class_id + "\"]/td[13]/a").text
    if class_n == class_number:
        break

if (class_n == class_number):
    print("教学班查找成功")
else:
    print("教学班查找失败，请检查教学班是否存在")
    browser.quit()
    exit(0)

print("尝试选课")
count = 0
while 1:
    choose = browser.find_element_by_xpath("//*[@id=\"tr_" + class_id + "\"]/td[20   ]/button")
    sleep(delay)
    if choose.text == "选课":
        choose.send_keys(Keys.ENTER)
        count = count + 1
        print("第" + str(count) + "次尝试选课~")
        try:
            alert = browser.find_element_by_xpath("//*[@id=\"alertModal\"]/div/div/div[2]/div/div/p").text
            print("    " + alert)
            browser.find_element_by_xpath("//*[@id=\"btn_ok\"]").send_keys(Keys.ENTER)
            if alert == "服务器作为网关或代理，从上游服务器收到无效响应!":
                print("出现问题，刷新重试")
                browser.refresh()
                while 1:
                    try:
                        print("尝试搜索课程，步骤1")
                        browser.find_element_by_xpath("//*[@id=\"searchBox\"]/div/div[2]/div/div/div/div/a/span").click()
                        browser.find_element_by_name("searchInput").send_keys(class_name)
                        browser.find_element_by_name("query").send_keys(Keys.ENTER)
                        break
                    except:
                        print("页面加载失败，刷新重试")
                        if browser.current_url == url2:
                            browser.refresh()
                        else:
                            browser.get(url2)
                        continue
                class_id = None
                class_n = None

                while 1:
                    print("尝试搜索课程，步骤2-1")
                    lists = browser.find_elements_by_class_name("body_tr")
                    print("尝试搜索课程，步骤2-2")
                    if (len(lists) > 0): break

                print("课程搜索完成\n尝试查找教学班")
                i = 0
                for i in range(0, len(lists) + 1):
                    class_id = lists[i].get_attribute("id")[3:]
                    class_n = browser.find_element_by_xpath("//*[@id=\"tr_" + class_id + "\"]/td[13]/a").text
                    if class_n == class_number:
                        break

                if (class_n == class_number):
                    print("教学班查找成功")
                else:
                    print("教学班查找失败，请检查教学班是否存在")
                    browser.quit()
                    exit(0)

                print("尝试选课")
        except:
            continue
    else:
        print("\n******选课成功！******\n")
        break

browser.quit()
print("按任意键退出！")
input()
