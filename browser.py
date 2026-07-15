from playwright.sync_api import sync_playwright


class Browser:

    def __init__(self):
        self.playwright = None
        self.browser = None

    def start(self):
        print("Starting browser...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )
        page = self.browser.new_page()
        page.goto("https://example.com")

        print("Browser started.")
        input("Press Enter to close the browser...")