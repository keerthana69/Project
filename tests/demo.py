import re

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_update_billing_information(browser):
    page = browser.new_page()
    page.goto("https://minimals.cc/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("demo@minimals.cc")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demo1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="user").click()
    page.get_by_role("button", name="account").click()
    page.get_by_role("tab", name="Billing").click()
    page.get_by_role("button", name="Jayvion Simon").click()
    page.get_by_role("button", name="Deja Brady 18605 Thompson").click()
    page.get_by_role("button", name="**** **** ****").click()
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^\*\*\*\* \*\*\*\* \*\*\*\* 1234$")).click()


def test_search_order(browser):
    page = browser.new_page()
    page.goto("https://minimals.cc/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("demo@minimals.cc")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demo1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="order").click()
    page.get_by_role("button", name="list").click()
    page.get_by_placeholder("Search customer or order").click()
    page.get_by_placeholder("Search customer or order").fill("cor")
    page.get_by_role("row", name="#60111 Cortez Herring Cortez").get_by_role("checkbox").check()


def test_filter_jobs(browser):
    page = browser.new_page()
    page.goto("https://minimals.cc/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("demo@minimals.cc")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demo1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="job").click()
    page.get_by_role("button", name="list").click()
    page.get_by_role("button", name="Filters").click()
    page.get_by_label("On Demand").check()
    page.get_by_role("button").nth(1).click()


def test_send_chat_message(browser):
    page = browser.new_page()
    page.goto("https://minimals.cc/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("demo@minimals.cc")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demo1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="chat").click()
    page.get_by_role("button", name="Deja Brady Deja Brady You:").click()
    page.get_by_placeholder("Type a message").click()
    page.get_by_placeholder("Type a message").fill("hey, how are you")
    page.get_by_placeholder("Type a message").press("Enter")


def test_all_file_deleted(browser):
    page = browser.new_page()
    page.goto("https://minimals.cc/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("demo@minimals.cc")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demo1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="File Manager").click()
    page.get_by_role("row", name="Name sorted ascending Size").get_by_role("checkbox").check()
    page.get_by_label("Delete").click()
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("alert").get_by_role("button").click()
