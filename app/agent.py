from browser.browser import Browser
from browser.navigator import Navigator


class GovAgent:

    def __init__(self):
        self.browser = Browser()
        self.navigator = None

    def start(self):
        self.browser.start()
        self.navigator = Navigator(self.browser.page)

    def open_procedure(self, procedure_name):
        self.browser.open(
            "https://villanuevadelavera.sedelectronica.es/info.0"
        )

        self.navigator.click_text("Trámites")

        return self.navigator.click_first_matching_link(
            procedure_name
        )

    def download_form(self, button_text, save_path):
        return self.navigator.download_by_text(
            button_text,
            save_path
        )

    def wait(self):
        self.browser.wait()