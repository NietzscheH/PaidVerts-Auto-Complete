import requests, math, operator, time, os, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from bs4 import BeautifulSoup
from functools import reduce
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 修改header，设置代理
chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument('headless') # 静默模式
chromeOptions.add_argument("--disable-infobars")
chromeOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    #chromeOptions.add_argument("--proxy-server=http://162.243.99.57:3128")

# 打开网页
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.get('https://www.paidverts.com/login.html')

time.sleep(7) # 获取验证码目标信息前先等网页加载完毕，否则无法获取

def login():
    # 验证码目标
    target = browser.find_element_by_xpath('//*[@id="captcha"]/p/strong').text

    # 判断是否已收录目标
    while not os.path.exists('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % target):
        browser.refresh()
        time.sleep(7)
        target = browser.find_element_by_xpath('//*[@id="captcha"]/p/strong').text
        if os.path.exists('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % target):
            break

    # 输入登陆信息
    browser.find_element_by_xpath('//*[@id="email"]').send_keys('hyq0401@outlook.com')
    browser.find_element_by_xpath('//*[@id="password"]').send_keys('HYQ~874121')
    time.sleep(4)

    # 保存选项
    pic1 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-0"]')
    pic1.screenshot('Desktop\\py_project\\PaidVerts\\test_pics\\pic1.png')
    pic2 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-1"]')
    pic2.screenshot('Desktop\\py_project\\PaidVerts\\test_pics\\pic2.png')
    pic3 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-2"]')
    pic3.screenshot('Desktop\\py_project\\PaidVerts\\test_pics\\pic3.png')
    pic4 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-3"]')
    pic4.screenshot('Desktop\\py_project\\PaidVerts\\test_pics\\pic4.png')
    pic5 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-4"]')
    pic5.screenshot('Desktop\\py_project\\PaidVerts\\test_pics\\pic5.png')

    def compare(pic1,pic2):
        '''
        :param pic1: 图片1路径
        :param pic2: 图片2路径
        :return: 返回对比的结果
        '''
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)

        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, histogram1, histogram2)))/len(histogram1))

        return differ

    difference = []
    answer = 0
    for i in [1, 2, 3, 4, 5]:
        difference.append(compare('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % target, 'Desktop\\py_project\\PaidVerts\\test_pics\\pic%s.png' % i))
    for i in [0, 1, 2, 3, 4]:
        if difference[i] == min(difference):
            answer = i
    browser.find_element_by_xpath('//*[@id="visualCaptcha-img-%s"]' % answer).click()

    # 登陆
    browser.find_element_by_xpath('//*[@id="loginFrm"]/div/fieldset/div[2]/div[9]/input').click()
    time.sleep(7)

def task():
    # skip tutoriul
    for i in range(20):
        try:
            browser.find_element_by_xpath('/html/body/div[%s]/div/div[5]/a[1]' % i).click()
            break
        except NoSuchElementException:
            continue
    time.sleep(2.3)
    # 进入任务界面
    browser.find_element_by_id('paidAdsLink').click()
    time.sleep(2)

    for i in range(20):
        try:
            browser.find_element_by_xpath('//*[@id="view-1"]').click() # 点击任务
            time.sleep(7)

            def Try():
                task_target = browser.find_element_by_xpath('//*[@id="captcha"]/p/strong').text # 获取验证目标

                while not os.path.exists('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % task_target): # 检查是否已收录
                    browser.find_element_by_xpath('//*[@id="captcha"]/div[2]/div').click()
                    time.sleep(4)
                    task_target = browser.find_element_by_xpath('//*[@id="captcha"]/p/strong').text
                    continue
                    if os.path.exists('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % task_target):
                        break

                task_pic1 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-0"]') # 搜集选项
                task_pic1.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic1.png')
                task_pic2 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-1"]')
                task_pic2.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic2.png')
                task_pic3 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-2"]')
                task_pic3.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic3.png')
                task_pic4 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-3"]')
                task_pic4.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic4.png')
                task_pic5 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-4"]')
                task_pic5.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic5.png')

                def compare(pic1,pic2):
                    '''
                    :param pic1: 图片1路径
                    :param pic2: 图片2路径
                    :return: 返回对比的结果
                    '''
                    image1 = Image.open(pic1)
                    image2 = Image.open(pic2)

                    for i in range(32): # 替换颜色 将绿色改为白
                        for j in range(32):
                            try:
                                r,g,b,alpha = image2.getpixel((i,j))
                                if r==50 and g==199 and b==95:
                                    r, g, b = 255, 255, 255
                                    image2.putpixel((i,j), (r,g,b,alpha))
                            except Exception as e:
                                continue

                    image2.save(pic2)

                    histogram1 = image1.histogram()
                    histogram2 = image2.histogram()

                    differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, histogram1, histogram2)))/len(histogram1))

                    return differ

                task_difference = []
                task_answer = 0
                for i in [1, 2, 3, 4, 5]:
                    task_difference.append(compare('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % task_target, 'Desktop\\py_project\\PaidVerts\\task_pics\\pic%s.png' % i))
                for i in [0, 1, 2, 3, 4]:
                    if task_difference[i] == min(task_difference):
                        task_answer = i
                print(task_difference)
                browser.find_element_by_xpath('//*[@id="visualCaptcha-img-%s"]' % task_answer).click() # 选择
                time.sleep(3)
                browser.find_element_by_xpath('//*[@id="captcha_button"]').click() # confirm
                time.sleep(10)

            Try()
            
            try:
                wait = WebDriverWait(browser, 30, 0.5)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="closeBtn"]'))).click()
                time.sleep(3)
            except TimeoutException:
                Try()

        except NoSuchElementException:
            print('tasks are all done.')
            time.sleep(2.4)
            break

def grid():
    # 进入任务界面
    browser.maximize_window()
    browser.find_element_by_xpath('//*[@id="adGridLink"]').click()
    time.sleep(2)

    count = 0
    goal = browser.find_element_by_xpath('//*[@id="adGridLink"]/span').text
    while True:
        try:
            randA = random.randrange(1, 11)
            randB = random.randrange(1, 11)
            browser.find_element_by_xpath('//*[@id="gridtable"]/tbody/tr[%s]/td[%s]' % (str(randA), str(randB))).click() # 点击grid link
            time.sleep(7)

            def Try():
                task_target = browser.find_element_by_xpath('//*[@id="captcha"]/p/strong').text # 获取验证目标

                while not os.path.exists('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % task_target): # 检查是否已收录
                    browser.find_element_by_xpath('//*[@id="captcha"]/div[2]/div').click()
                    time.sleep(4)
                    task_target = browser.find_element_by_xpath('//*[@id="captcha"]/p/strong').text
                    continue
                    if os.path.exists('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % task_target):
                        break

                task_pic1 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-0"]') # 搜集选项
                task_pic1.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic1.png')
                task_pic2 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-1"]')
                task_pic2.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic2.png')
                task_pic3 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-2"]')
                task_pic3.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic3.png')
                task_pic4 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-3"]')
                task_pic4.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic4.png')
                task_pic5 = browser.find_element_by_xpath('//*[@id="visualCaptcha-img-4"]')
                task_pic5.screenshot('Desktop\\py_project\\PaidVerts\\task_pics\\pic5.png')

                def compare(pic1,pic2):
                    '''
                    :param pic1: 图片1路径
                    :param pic2: 图片2路径
                    :return: 返回对比的结果
                    '''
                    image1 = Image.open(pic1)
                    image2 = Image.open(pic2)

                    for i in range(32): # 替换颜色 将绿色改为白
                        for j in range(32):
                            try:
                                r,g,b,alpha = image2.getpixel((i,j))
                                if r==50 and g==199 and b==95:
                                    r, g, b = 255, 255, 255
                                    image2.putpixel((i,j), (r,g,b,alpha))
                            except Exception as e:
                                continue

                    image2.save(pic2)

                    histogram1 = image1.histogram()
                    histogram2 = image2.histogram()

                    differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, histogram1, histogram2)))/len(histogram1))

                    return differ

                task_difference = []
                task_answer = 0
                for i in [1, 2, 3, 4, 5]:
                    task_difference.append(compare('Desktop\\py_project\\PaidVerts\\pics\\%s.png' % task_target, 'Desktop\\py_project\\PaidVerts\\task_pics\\pic%s.png' % i))
                for i in [0, 1, 2, 3, 4]:
                    if task_difference[i] == min(task_difference):
                        task_answer = i
                print(task_difference)
                browser.find_element_by_xpath('//*[@id="visualCaptcha-img-%s"]' % task_answer).click() # 选择
                time.sleep(3)
                browser.find_element_by_xpath('//*[@id="captcha_button"]').click() # confirm
                time.sleep(10)

            Try()
            
            try:
                wait = WebDriverWait(browser, 30, 0.5)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="playGridAgn"]'))).click()
                time.sleep(3)
            except TimeoutException:
                Try()
            
            count += 1
            print(str(count), 'are done so far')

        except NoSuchElementException:
            if count == goal:
                break
            else:
                print('oops!', str(count), 'are done so far')
                browser.refresh()
                time.sleep(2.4)
                continue
    print('grids are all done')

def showBalence():
    balence = browser.find_element_by_xpath('//*[@id="navbar-mobile"]/div/a[1]/span[1]').text
    BAPS = browser.find_element_by_xpath('//*[@id="navbar-mobile"]/div/a[2]/span').text
    print('Your current balence is', balence, '\nYour current BAPS is', BAPS)
    time.sleep(5)

if __name__ == "__main__":
    login()
    task()
    grid()
    showBalence()
    browser.quit()
