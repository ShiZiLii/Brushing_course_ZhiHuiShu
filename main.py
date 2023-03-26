import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import datetime

url = "https://onlineweb.zhihuishu.com"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(1)


# log in
button_path = "/html/body/div[4]/div/form/div[1]/span"

PhoneNumber = ""  # 输入你自己的手机号
PassWord = ""  # 输入自己的密码

user = driver.find_element(
    By.XPATH, '/html/body/div[4]/div/form/div[1]/ul[1]/li[1]/input[4]')
password = driver.find_element(
    By.XPATH, '/html/body/div[4]/div/form/div[1]/ul[1]/li[2]/input')
user.send_keys(PhoneNumber)
password.send_keys(PassWord)
button = driver.find_element(By.XPATH, button_path)
button.click()
# 等待输入验证码
time.sleep(10)   # 十秒钟等候你输入验证码

# 选择课程：
select_class_way = '/html/body/div[1]/section/div[2]/section[2]/section/div/div/div/div[2]/div[2]/div[2]/ul/div/dl'
select_class = driver.find_element(By.XPATH, select_class_way)
select_class.click()

# 继续学习按钮
continue_button_way = '/html/body/div[1]/div/div/div/div[4]/div[1]/div[1]/span[3]'
continue_button = driver.find_element(By.XPATH, continue_button_way)
print(driver.window_handles)
continue_button.click()
print("继续学习")
time.sleep(2)
# 此时会跳转到一个新界面
# 下面两行代码进入新界面

handles = driver.window_handles  # 获取当前浏览器所有窗口句柄
driver.switch_to.window(handles[-1])  # 切换最新窗口句柄


# 暂停按钮: 每进去一次视频，就会产生一个暂停按钮，需要控制鼠标点击视频后才会继续播放
def stop_to_continue():
    pyautogui.click(628, 962)

# 获取视频的currentTime, 以及duration：分别作为两个返回值返回


def getTime():
    currentTime = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[10]/div[4]/span[1]').text
    duration = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[10]/div[4]/span[2]').text
    return str(currentTime), str(duration)


time.sleep(4)
stop_to_continue()
time.sleep(1)

for i in range(3704 - 3673 + 1):
    """
    查看后发现列表中视频的播放是file_15473673 到 file_15473704的，以下遍历视频列表
    本人最初打算通过getTime()获取每次的视频的当前播放时间currentTime以及当前视频的总持续时间duration，但是发现这两个量一直持续相等
    最终采取了每次等候560秒的方式
    """
    i += 3673
    id = 'file_1547' + str(i)
    driver.find_element(By.ID, id).click()
    time.sleep(3)
    stop_to_continue()
    time.sleep(1)
    name = driver.find_element(By.ID, id).text
    print(
        f'视频{i}: {name}, 开始时间:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    time.sleep(560)  # 等候560s
    # 循环移动鼠标，同时检查时间，判断当时间匹配时候，切换到下个视频
    # click = 0
    # while True:
    #     time.sleep(1)
    #     if click / 2 == 0:
    #         pyautogui.moveTo(700,962)
    #     else:
    #         pyautogui.moveTo(628,900)
    #     time.sleep(0.5)
    #     currentTime = driver.find_element(By.XPATH,
    #                                       '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[10]/div[4]/span[1]').text
    #     duration = driver.find_element(By.XPATH,
    #                                    '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[10]/div[4]/span[2]').text
    #     print(currentTime, duration)
    #     print(type(currentTime), type(currentTime))
    #     if str(currentTime) == str(duration):
    #         print(f'视频{i}: {name}, 完成时间：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    #         break
    #     else:
    #         click += 1
