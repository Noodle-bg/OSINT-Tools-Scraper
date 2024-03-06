from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# Initialize the WebDriver
driver = webdriver.Chrome()

# Set the maximum wait time in seconds
wait_time = 20
# Navigate to your desired URL
driver.get("https://whatsmyname.app/#")


def upload(driver: webdriver.Chrome, file_path):
    file_input = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=file]"))
    )
    file_input.send_keys(file_path)


def wait_until_not_hidden(driver, by, selector):
    revealed = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((by, selector))
    )
    wait = WebDriverWait(driver, timeout=10)
    wait.until(lambda d : revealed.is_displayed())



def click(driver, by, selector):
    element = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((by, selector))
    )
    
    # Create an instance of ActionChains
    actions = ActionChains(driver)
    
    # Scroll to the element
    actions.move_to_element(element).perform()
    
    # Once the element is scrolled into view, click on it
    element.click()


def type_text(driver, by, selector, text):


    element = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((by, selector))
    )
    
    # Create an instance of ActionChains
    actions = ActionChains(driver)
    
    # Scroll to the element
    actions.move_to_element(element).perform()
    
    # Once the element is scrolled into view, click on it
    element.click()
    
    # Type the text into the input field
    element.send_keys(text)



def wait_until_21_results(driver):
    return EC.presence_of_all_elements_located((By.TAG_NAME, "td"))





try:
    query="noodle"
    type_text(driver,By.CSS_SELECTOR,"textarea[type='text']",query)
    click(driver,By.CLASS_NAME,"btn-success")

    profiles = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.TAG_NAME,  "td"))
    )  # Use find_elements instead of find_element
    print(profiles)
    i=1
    results=[]
    result=[]
    for profile in profiles:
        if(i%4==0):
            results.append(result)
            result=[]
            i=i+1
        else:
            info = profile.text
            print(info)
            result.append(info)
            i=i+1
    print(results)


    # # cards_info = []
    # results=[]
    # for profile in profiles:
    #     result =[]
    #     img_url=profile.find_element(By.TAG_NAME,"img").get_attribute('src')
    #     user=profile.find_element(By.CLASS_NAME,"result-username").text
    #     result.append(img_url)
    #     result.append(user)
    #     results.append(result)
    

    # print(results[0])#Result stored in results in list in list form.

    
    
except Exception as e:
    # In case of any exceptions, you can handle them here
    print("Exception occurred:", e)

finally:
    # Remember to close the WebDriver
    time.sleep(20)
    driver.quit()
