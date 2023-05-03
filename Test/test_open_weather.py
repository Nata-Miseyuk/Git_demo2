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


def test_check_page_title(driver, wait, open_page):
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


def test_home_page_header(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    assert header.text == "OpenWeather", "Wrong h1 Header"


def test_should_refresh_link(driver, open_page):
    current_title = driver.title
    driver.refresh()
    title_after_refresh = driver.title
    assert current_title == title_after_refresh


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_logo_is_visible_on_dashboard_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    logo_on_dashboard_page = driver.find_element(By.CSS_SELECTOR, "#first-level-nav > li.logo")
    assert logo_on_dashboard_page.is_displayed()


def test_logo_redirecting_from_dashboard_to_main_page(driver):
    driver.get('https://openweathermap.org/weather-dashboard/')
    logo_on_dashboard_page = driver.find_element(By.CSS_SELECTOR, "#first-level-nav > li.logo")
    logo_on_dashboard_page.click()
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_logo_is_presented_on_main_page(driver):
    driver.get('https://openweathermap.org/')
    logo = driver.find_element(By.XPATH, "//li[contains(@class, 'logo')]")
    assert logo.is_displayed(), "Logo not found on the Home page"
