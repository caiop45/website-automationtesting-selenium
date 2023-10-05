from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os

# WebDriver configs
os.environ['PATH'] += r"C:/Users/Caio Pereira/Desktop/QA PROJECTS/"

# Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Open URL
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)  # Define uma espera padrão de 10 segundos

try:
    # ... [restante do código anterior até o checkout]
     # phones button
    phones = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
    phones.click()

    # iphone
    iphone = driver.find_element(By.XPATH, '//a[text()="Palm Treo Pro"]')
    iphone.click()
    time.sleep(1)

    # first picture
    first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    first_pic.click()
    time.sleep(2)

    # next picture
    next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')

    for i in range(0,2):
        driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')
        next_click.click()
        time.sleep(2)

    driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

    # close
    x_button = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
    x_button.click()
    time.sleep(1)

    # quantity
    quantity = driver.find_element(By.ID, 'input-quantity')
    quantity.click()
    time.sleep(1)

    quantity.clear()
    time.sleep(1)
    quantity.send_keys('2')
    time.sleep(1)

    # add to cart
    add_to_button = driver.find_element(By.ID, 'button-cart')
    add_to_button.click()
    time.sleep(2)

    laptops = driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
    action = ActionChains(driver)
    action.move_to_element(laptops).perform()
    time.sleep(2)
    laptops_2 = driver.find_element(By.XPATH, '//a[text()="Show AllLaptops & Notebooks"]')
    laptops_2.click()
    time.sleep(1)

    # click on HP laptop
    HP = driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
    HP.click()

    # scroll
    add_to_button_2 = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
    add_to_button_2.location_once_scrolled_into_view
    time.sleep(1)

    # calendar
    calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
    calendar.click()
    time.sleep(1)

    next_click_calendar = driver.find_element(By.XPATH, '//th[@class="next"]')
    month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')

    # year:2023 month:december
    while month_year.text != 'December 2023':
        next_click_calendar.click()
    time.sleep(2)

    # day 31
    calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
    calendar_date.click()
    time.sleep(2)

    # add to button
    add_to_button_2.click()
    time.sleep(3)
    # Checkout
    go_to_cart = wait.until(EC.element_to_be_clickable((By.ID, 'cart-total')))
    go_to_cart.click()

    checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@class="text-right"]/a[2]')))
    checkout.click()
   
    try:
        popup_close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.popup-close-button')))
        popup_close_button.click()
        time.sleep(4)
    except:
        print("No popup has been found")

    # click on guest account
    guest = driver.find_element(By.XPATH, '//input[@value="guest"]')
    guest.click()

    # click continue 1
    continue_1 = driver.find_element(By.ID, 'button-account')
    continue_1.click()
    time.sleep(1)

    # scrolling
    step_2 = driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
    step_2.location_once_scrolled_into_view
    time.sleep(2)

    # first name
    first_name = driver.find_element(By.ID, 'input-payment-firstname')
    first_name.click()
    time.sleep(1)
    first_name.send_keys('test_first_name')
    time.sleep(1)

    # last_name
    last_name = driver.find_element(By.ID, 'input-payment-lastname')
    last_name.click()
    time.sleep(1)
    last_name.send_keys('test_last_name')
    time.sleep(1)

    # email
    email = driver.find_element(By.ID, 'input-payment-email')
    email.click()
    time.sleep(1)
    email.send_keys('test@test.com')
    time.sleep(1)

    # telephone
    telephone = driver.find_element(By.ID, 'input-payment-telephone')
    telephone.click()
    time.sleep(1)
    telephone.send_keys('012345678')
    time.sleep(1)

    # address
    address = driver.find_element(By.ID, 'input-payment-address-1')
    address.click()
    time.sleep(1)
    address.send_keys('teststreet 18733')
    time.sleep(1)

    # city
    city = driver.find_element(By.ID, 'input-payment-city')
    city.click()
    time.sleep(1)
    city.send_keys('São Paulo')
    time.sleep(1)

    # postcode
    postcode = driver.find_element(By.ID, 'input-payment-postcode')
    postcode.click()
    time.sleep(1)
    postcode.send_keys('112233')
    time.sleep(1)

    # country
    country = driver.find_element(By.ID, 'input-payment-country')
    dropdown_1 = Select(country)
    time.sleep(1)
    dropdown_1.select_by_index(33)
    time.sleep(4)

    region = driver.find_element(By.ID, 'input-payment-zone')
    dropdown_2 = Select(region)
    time.sleep(1)
    dropdown_2.select_by_visible_text('São Paulo')
    time.sleep(1)

    # click continue 2
    continue_2 = driver.find_element(By.XPATH, '//input[@id="button-guest"]')
    continue_2.click()
    time.sleep(1)

    # click continue 3
    continue_3 = driver.find_element(By.XPATH, '//input[@id="button-shipping-method"]')
    continue_3.click()
    time.sleep(1)

    # accept terms & conditions
    t_e = driver.find_element(By.XPATH, '//input[@name="agree"]')
    t_e.click()
    time.sleep(1)

    # click continue 4
    continue_4 = driver.find_element(By.XPATH, '//input[@id="button-payment-method"]')
    continue_4.click()
    time.sleep(3)

    # final price
    final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

    print("The final price of both products is " + final_price.text)
    time.sleep(2)

    # click on the confirmation button
    confirmation_button = driver.find_element(By.ID, 'button-confirm')
    confirmation_button.click()
    time.sleep(2)

    # success text
    success_text = driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
    print(success_text.text)
    time.sleep(1)
except Exception as e:
    print(traceback.format_exc())
finally:
    driver.close()
