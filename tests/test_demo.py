import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://minimals.cc/")
    page.get_by_role("link", name="Login").click()
    page.get_by_label("Email address").click()
    page.get_by_label("Email address").fill("demo@minimals.cc")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("demo1234")
    page.get_by_label("Password").press("Enter")
