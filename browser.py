from urllib.parse import urlparse
from playwright.sync_api import sync_playwright


class Browser:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        print("Starting browser...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

        print("Browser started.")

    def open(self, url):
        self.page.goto(url)

        print(f"Title: {self.page.title()}")

        domain = urlparse(url).netloc

        self.page.screenshot(
            path=f"output/{domain}.png"
        )

    def wait(self):
        input("Press Enter to close the browser...")