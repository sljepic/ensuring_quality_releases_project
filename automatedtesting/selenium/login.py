# #!/usr/bin/env python
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


shopping_cart = {
    "backpack": "sauce-labs-backpack",
    "bike light": "sauce-labs-bike-light",
    "gray T-shirt": "sauce-labs-bolt-t-shirt",
    "jacket": "sauce-labs-fleece-jacket",
    "onesie": "sauce-labs-onesie",
    "red T-shirt": "test.allthethings()-t-shirt-(red)"
}


def initialize_browser():
    logging.info('Starting the browser...')
    #--uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    logging.info('Browser started successfully. Navigating to the demo page to login.')
    return driver

# Start the browser and login with standard_user
def login (user, password, driver):
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    logging.info("Succesfully navigated to " + url)
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_css_selector("input[id='login-button']").click()

    login_page_element = driver.find_element_by_css_selector("div[id='header_container'] > div[class='header_secondary_container'] > span.title").text
    assert "PRODUCTS" == login_page_element
    logging.info("Succesfully loggeed to " + url + " with user " + user)


def add_items_to_shopping_cart(driver):
    for item, item_id in shopping_cart.items():
        css_selector = "button[id='add-to-cart-" + item_id + "']"
        driver.find_element_by_css_selector(css_selector).click()
        logging.info(item + " has been added to a shopping cart.")

def remove_items_from_shopping_cart(driver):
    for item, item_id in shopping_cart.items():
        css_selector = "button[id='remove-" + item_id + "']"
        driver.find_element_by_css_selector(css_selector).click()
        logging.info(item + " has been removed to a shopping cart.")

def test_if_items_are_in_shopping_cart(driver):
    shopping_cart_items = driver.find_element_by_css_selector("div[id='shopping_cart_container'] > a > span.shopping_cart_badge").text
    assert '6' in shopping_cart_items
    logging.info("All products are successfully added to a cart. Totally found " + shopping_cart_items + " items.")

def test_if_shoping_cart_is_empty(driver):
    try:
        driver.find_element_by_css_selector("div[id='shopping_cart_container'] > a > span.shopping_cart_badge").text
        cart_badge_not_found = False
    except:
        cart_badge_not_found = True

    assert cart_badge_not_found
    logging.info("Shopping cart is empty.")

def main():
    logging.basicConfig(filename="selenium-test.log", level=logging.INFO)
    logging.info("-------------------------------")
    logging.info("Starting execution")
    logging.info("-------------------------------")
    driver = initialize_browser()
    ###login to page
    login('standard_user', 'secret_sauce', driver)
    logging.info("Check if shopping cart is empty...")
    test_if_shoping_cart_is_empty(driver)
    logging.info("Adding items to shopping cart...")
    add_items_to_shopping_cart(driver)
    logging.info("Check if items are succesfully added to a shopping cart")
    test_if_items_are_in_shopping_cart(driver)
    logging.info("Removing objects from shopping cart...")
    remove_items_from_shopping_cart(driver)
    logging.info("Check if shopping cart is empty...")
    test_if_shoping_cart_is_empty(driver)
    logging.info("End of execution.")


if __name__ == '__main__':
    main()
