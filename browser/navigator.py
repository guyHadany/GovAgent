class Navigator:

    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_text(self, text):
        self.page.get_by_text(text, exact=True).click()
        self.page.wait_for_load_state("domcontentloaded")

    def text_exists(self, text):
        return self.page.get_by_text(text, exact=True).count() > 0

    def go_back(self):
        self.page.go_back()
        self.page.wait_for_load_state("domcontentloaded")