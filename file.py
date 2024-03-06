

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
driver.get("https://search4faces.com/search_vkwall.html")


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


try:
    # Wait for the element to be located on the page
    click(driver, By.ID, "upload-button")
    upload(driver, "C:/Users/bgpra/OneDrive/Desktop/jaw.jpg")
    # click(driver, By.CLASS_NAME, "uppload-button--cta")
    click(driver, By.CLASS_NAME, "effects-continue--upload")
    # wait_until_not_hidden(driver, By.ID, "search-button")
    click(driver, By.ID, "search-button")

    # Find the div with class 'search-results2'
    search_results_div = driver.find_element_by_css_selector("div.search-results2")

    # Find all descendant div elements within the search_results_div
    card_divs = search_results_div.find_elements_by_css_selector("div")

    # List to store information for each card
    cards_info = []

    # Process each card
    for card in card_divs:
        card_info = []

        # Find the div with class 'card-vk01-fixed' within the card
        card_vko1_fixed_div = card.find_element_by_css_selector("div.card-vk01-fixed")

        # Find the img tag within the a tag within the card_vko1_fixed_div and extract the src attribute
        img_src = card_vko1_fixed_div.find_element_by_css_selector("a > img").get_attribute("src")
        card_info.append(img_src)

        # Find the div with class 'col' within the card
        col_div = card.find_element_by_css_selector("div.col")

        # Find the div with class 'div-body' within the col_div
        div_body_div = col_div.find_element_by_css_selector("div.div-body")

        # Find the div with class 'card-vk01-header' within the div_body_div and extract its text
        header_text = div_body_div.find_element_by_css_selector("div.card-vk01-header").text
        card_info.append(header_text)

        # Find the div with class 'card-vk01-score' within the div_body_div and extract the text of the span within it
        score_text = div_body_div.find_element_by_css_selector("div.card-vk01-score span").text
        card_info.append(score_text)

        # Append the card_info to the cards_info list
        cards_info.append(card_info)

    print(cards_info)








  
    
    
except Exception as e:
    # In case of any exceptions, you can handle them here
    print("Exception occurred:", e)

finally:
    # Remember to close the WebDriver
    time.sleep(20)
    driver.quit()
