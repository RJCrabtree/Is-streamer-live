from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
twitch_streams = ["BigBorisBongBen", "ogfruittyyy", "ogsirtacticsfb"]

def check_if_adam_live():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/div[2]/div[1]/div[1]/button")
    except:
        print("Adam isn't live")
    else:
        print("Adam is live")

def check_if_ash_live():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[9]/div/div[2]/div[1]/div[1]/button")
    except:
        print("Ash isn't live")
    else:
        print("Ash is live")

def check_if_robbie_live():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[7]/div/div[2]/div[1]/div[1]/button")
    except:
        print("Robbie isn't live")
    else:
        print("Robbie is live")
        

def check_if_start_exists_adam():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/div[3]/button")                                    
    except:
        print("doesnt exist")
    else:
        print("exists")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/div[3]/button").click()

def check_if_start_exists_ash():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/div[3]/button")
    except:
        print("doesnt exist")
    else:
        print("exists")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[8]/div/div[3]/button").click()        

def check_if_start_exists_robbie():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[7]/div/div[3]/button")
    except:
        print("doesnt exist")
    else:
        print("exists")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[7]/div/div[3]/button").click()        

twitch_streams = ["BigBorisBongBen", "ogfruittyyy", "ogsirtacticsfb"]

print("Whose stream would you like to open?")
stream_open = int(input("Robbie: 0, Adam: 1, Ash: 2, All:3\n"))

if stream_open == 0:
    twitch_streams[0]
    driver.get("https://www.twitch.tv/" + twitch_streams[0])
    time.sleep(2)
    check_if_start_exists_robbie()
    time.sleep(2)
    check_if_robbie_live()
    driver.close()

elif stream_open == 1:
    driver.get("https://www.twitch.tv/" + twitch_streams[1])
    time.sleep(2)
    check_if_start_exists_adam()
    time.sleep(2)
    check_if_adam_live()
    driver.close()
    
elif stream_open == 2:
    driver.get("https://www.twitch.tv/" + twitch_streams[2])
    time.sleep(2)
    check_if_start_exists_ash()
    time.sleep(2)
    check_if_ash_live()
    driver.close()
    
elif stream_open == 3:
    driver.get("https://www.twitch.tv/" + twitch_streams[0])
    time.sleep(2)
    check_if_start_exists_robbie()
    time.sleep(2)
    check_if_robbie_live()
    
    driver.get("https://www.twitch.tv/" + twitch_streams[1])
    time.sleep(2)
    check_if_start_exists_adam()
    time.sleep(2)
    check_if_adam_live()
    
    driver.get("https://www.twitch.tv/" + twitch_streams[2])
    time.sleep(2)
    check_if_start_exists_ash()
    time.sleep(2)
    check_if_ash_live()
    driver.close()
    
else:
    print("please enter a correct stream number.")



























