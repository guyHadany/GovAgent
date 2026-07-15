class Navigator:

    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_text(self, text):
        self.page.get_by_text(text, exact=True).click()
        self.page.wait_for_load_state("domcontentloaded")

    def download_by_text(self, text, save_path):
        with self.page.expect_download() as download_info:
            self.page.get_by_text(text, exact=True).click()

        download = download_info.value
        download.save_as(save_path)

        return save_path
    
    def text_exists(self, text):
        return self.page.get_by_text(text, exact=True).count() > 0

    def go_back(self):
        self.page.go_back()
        self.page.wait_for_load_state("domcontentloaded")
    def list_links(self):
        links = self.page.locator("a")

        for i in range(links.count()):
            link = links.nth(i)

            text = link.inner_text().strip()
            href = link.get_attribute("href")

            print(f"{i + 1}. {text}")
            print(f"   {href}")
    def find_links(self, text):
        return self.page.locator("a").filter(has_text=text)

    def list_matching_links(self, text):
        links = self.find_links(text)

        for i in range(links.count()):
            link = links.nth(i)

            print(f"{i + 1}. {link.inner_text()}")

    def list_buttons(self):
        buttons = self.page.locator("button")

        for i in range(buttons.count()):
            button = buttons.nth(i)
            text = button.inner_text().strip()

            print(f"{i + 1}. {text}")
    
    def click_first_matching_link(self, text):
        links = self.find_links(text)

        if links.count() == 0:
            print(f"לא נמצא קישור שמכיל: {text}")
            return False

        links.first.click()
        self.page.wait_for_load_state("domcontentloaded")
        return True