from behave import *
from selenium import webdriver
import time


@given('launch application')
def launch_application(context):
    # object of ChromeOptions class
    c = webdriver.ChromeOptions()

    # incognito parameter passed
    c.add_argument("--incognito")
    c.add_argument("--start-maximized")
    c.add_experimental_option("useAutomationExtension", False)
    c.add_experimental_option("excludeSwitches", ["enable-automation"])

    # set chromedriver.exe path
    context.driver = webdriver.Chrome(options=c)
    time.sleep(1)
    context.driver.get("https://default.fashlab-staging.fashcon.com/")


@then('verify home page')
def verify_home_page(context):
    assert 'Research Vintage Fashion | Fashion Constellate' in context.driver.title


@when('click on sign in button')
def click_on_sign_in_button(context):
    context.driver.find_element_by_xpath("//*[text()='Sign In']").is_displayed()
    context.driver.find_element_by_xpath("//*[text()='Sign In']").click()


@then('user redirected to sign in page')
def user_redirected_to_sign_in_page(context):
    assert 'Sign In | Fashion Constellate' in context.driver.title


@then('user enters "{email}" and "{password}"')
def user_enters_email_and_password(context, email, password):
    context.driver.find_element_by_id("edit-mail").send_keys(email)
    time.sleep(1)
    context.driver.find_element_by_id("edit-pass").send_keys(password)


@then('click on log in button')
def click_on_log_in_button(context):
    context.driver.find_element_by_id("edit-submit").is_displayed()
    context.driver.find_element_by_id("edit-submit").click()


@then('verify label page')
def verify_label_page(context):
    assert 'Label Archive | Fashion Constellate' in context.driver.title


@then('logged out from the application')
def logged_out(context):
    context.driver.find_element_by_xpath("//*[@title='/user/logout']").is_displayed()
    time.sleep(4)
    context.driver.find_element_by_xpath("//*[@title='/user/logout']").click()


