class Navigator:

    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()

    def click_text(self, text):
        self.page.get_by_text(text, exact=True).click()