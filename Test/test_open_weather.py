import time
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
selector_dashboard = (By.XPATH, "//h1[contains(text(),'Weather dashboard')]")
selector_api = (By.XPATH, "//h1[contains(text(),'Weather API')]")
tab_desk_api = (By.CSS_SELECTOR, '#desktop-menu a[href="/api"]')
btn_desc_dashboard = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
title_weatherDashboard = (By.CLASS_NAME, 'breadcrumb-title')
selector_marketplace_tab = (By.XPATH, '//div[@id="desktop-menu"]//li[4]/a')
footer_panel = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
btn_allow_all = (By.CLASS_NAME, "stick-footer-panel__link")
btn_go_home = (By.XPATH, "//a[contains(text(),'Home')]")
# TODO (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
footer_copyright = (By.XPATH, "//div[@class='horizontal-section my-5']/div[1]")
logo = (By.CSS_SELECTOR, ".logo > a > img")
API_LINK = (By.XPATH, "//*[@id='desktop-menu']/ul/li[2]/a")

# About As
btn_about_us = (By.CSS_SELECTOR, 'a[href*="/about-us"]')
btn_product_doc = (By.CSS_SELECTOR, 'div.grid-container [href="/api"]')
weather_title_api = (By.CLASS_NAME, 'breadcrumb-title')
btn_buy_subst = (By.CSS_SELECTOR, 'a[href="https://home.openweathermap.org/subscriptions"]')
alert_txt = (By.CLASS_NAME, "panel-body")
assert_mmg = '\n====You need to sign in or sign up before continuing.===\n'
btn_newAndUpd = (By.CSS_SELECTOR, 'a.round[href*="blog"]')
text_openweather = (By.XPATH, '//div/h1/span["orange -text"]')
search_city_field_selector = (By.XPATH, '//div[@id="weather-widget"]//div/input')
search_submit_button = (By.XPATH, '//div[@id="weather-widget"]//div/button')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
btn_contact_as = (By.CSS_SELECTOR, '.about-us :nth-child(9) [href="https://home.openweathermap.org/questions"]')
question_page = (By.CLASS_NAME, 'headline')
btn_marketplace = (By.CSS_SELECTOR, 'div.grid-container a[href$="/marketplace"]')
txt_mp_page = (By.XPATH, '//*[@id="custom_weather_products"]/h1')
# Support tab
support_tab = (By.CSS_SELECTOR, '#support-dropdown')
faq_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="FAQ"]')
how_to_start_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="How to start"]')
ask_question_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="Ask a question"]')
BTN_DASHBOARD = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
BTN_TRY_THE_DASHBOARD_2 = (By.XPATH, "//div[6]//a[text()='Try the Dashboard']")
BTN_COOKIES = (By.CLASS_NAME, "stick-footer-panel__link")
ALERT_PANEL_SINGIN = (By.CSS_SELECTOR, '.col-md-6 .panel-heading')


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    yield wait


@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


@pytest.fixture()
def cookies_panel_w(driver, open_page):
    btn_click_all = driver.find_element(*btn_allow_all)
    cookies_panel = driver.find_element(*footer_panel)
    if cookies_panel:
        btn_click_all.click()


# def test_open_page(driver):
#     driver.get('https://openweathermap.org/')
#     driver.maximize_window()
#     assert 'openweathermap' in driver.current_url
#     print(driver.current_url)


def test_check_page_title(driver, open_and_load_main_page):
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


# def test_fill_search_city_field(driver, open_page):
#     WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
#         (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
#     search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
#     search_city_field.send_keys('New York')
#     search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
#     search_button.click()
#     search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
#         (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
#     search_option.click()
#     expected_city = 'New York City, US'
#     WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
#         (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
#     displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
#     assert displayed_city == expected_city


def test_fill_search_city_field(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_field = driver.find_element(*search_city_field_selector)
    search_city_field.send_keys('New York')
    search_button = driver.find_element(*search_submit_button)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(search_dropdown_option))
    search_option.click()
    expected_city = 'New York City, US'
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


'''Footer / Copyright/  Visability, content '''


def test_visability_copyright(driver, open_page, wait):
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*footer_copyright).is_displayed()


def test_home_page_header(driver, open_and_load_main_page):
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    assert header.text == "OpenWeather", "Wrong h1 Header"


def test_should_refresh_link(driver, open_and_load_main_page):
    current_title = driver.title
    driver.refresh()
    title_after_refresh = driver.title
    assert current_title == title_after_refresh


def test_should_open_given_link(driver, open_and_load_main_page):
    assert 'openweathermap' in driver.current_url


def test_logo_is_visible_on_dashboard_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    driver.find_element(*logo).is_displayed()


def test_TC_002_01_04_Header_Logo_Verify_logo_redirects_from_dashboard_page_to_main_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    driver.find_element(*logo).click()
    assert driver.current_url == 'https://openweathermap.org/'
    # assert 'openweathermap' in driver.current_url


def test_logo_is_presented_on_main_page(driver, open_and_load_main_page):
    driver.find_element(*logo).is_displayed()


def test_TC_006_02_03_weather_dashboard_verify_the_transition_to_another_page(driver, open_and_load_main_page, wait):
    driver.find_element(*BTN_DASHBOARD).click()
    cookie_close = driver.find_element(*BTN_COOKIES)
    driver.execute_script("arguments[0].click();", cookie_close)
    driver.find_element(*BTN_TRY_THE_DASHBOARD_2).click()
    driver.switch_to.window(driver.window_handles[1])
    alert_mms = driver.find_element(*ALERT_PANEL_SINGIN)
    assert alert_mms.is_displayed(), 'WELCOME EVENTS PAGE'


def test_api_label_is_visible_on_main_page(driver, open_and_load_main_page, wait):
    api_label = driver.find_element(*API_LINK)
    assert api_label.is_displayed() and api_label.is_enabled()


def test_api_label_is_clickable_on_main_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(API_LINK))
    api_label = driver.find_element(*API_LINK)
    expected_api_label = 'API'
    assert expected_api_label in api_label.text


def test_api_link_redirects_to_api_page(driver, open_and_load_main_page, wait):
    driver.find_element(*API_LINK).click()
    assert driver.current_url == 'https://openweathermap.org/api'
