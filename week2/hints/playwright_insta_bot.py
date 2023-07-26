"""
인스타 그램에서 자동으로 글을 쓰는 봇
"""

from datetime import datetime
import os
import time
from playwright.sync_api import Locator, Page, sync_playwright, Playwright
import pathlib
from dotenv import load_dotenv
load_dotenv()

# 현재 파일의 폴더 경로
PATH = pathlib.Path(__file__).resolve().parent
CONTENT = "안녕하세요. 첫 포스팅입니다."


def open_insta_login(page: Page):
    """인스타그램에 접속하여 로그인 하는 함수"""
    # https://playwright.dev/python/docs/pages
    page.goto("https://www.instagram.com/")
    # https://playwright.dev/python/docs/selectors
    id_input: Locator = page.locator("[name=username]")
    # https://playwright.dev/python/docs/locators#locate-by-placeholder
    pw_input: Locator = page.locator("[type=password]")
    login_button: Locator = page.locator("[type=submit]")
    id_input.fill(os.environ['INSTA_ID'])
    pw_input.fill(os.environ['INSTA_PASSWORD'])
    time.sleep(1)
    login_button.click()


def post(page: Page):
    """인스타그램에서 사진과 글을 업로드하는 함수
    headless 모드에서는 영문으로 열리기에 이렇게함
    만약 headless가 아니라면 바꿔줘야한다.
    """
    # https://playwright.dev/docs/selectors#pick-n-th-match-from-the-query-result
    # https://playwright.dev/python/docs/locators#filtering-locators
    # https://github.com/microsoft/playwright/issues/15059#issuecomment-1163989286

    # 새 포스트 작성 버튼을 찾는다.
    post_button: Locator = page.locator("[aria-label='New post']")
    post_button.click()
    # 이미지를 업로드한다. test.png 사진이 존재해야함.
    page.set_input_files('input[type="file"]', str(PATH / "test.png"))
    # 다음으로 넘어간다.
    next_button: Locator = page.locator("button:text('Next')")
    next_button.click()
    next_button: Locator = page.locator("button:text('Next')")
    next_button.click()
    # 글 내용을 작성한다.
    text_area: Locator = page.locator("[aria-label='Write a caption...']")
    text_area.fill(CONTENT)
    # 업로드한다.
    share_button: Locator = page.locator("button:text('Share')")
    share_button.click()
    time.sleep(10)



with sync_playwright() as playwright:
    args = [
        "--disable-gpu",
    ]
    browser = playwright.chromium.launch(headless=False, args=args)
    page = browser.new_page()  # 
    open_insta_login(page)
    post(page)
    print(datetime.datetime.today(), 'success')
    browser.close()


