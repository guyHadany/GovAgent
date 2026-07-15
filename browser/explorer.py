from models.page_info import PageInfo

class Explorer:

    def inspect(self, page):
        info = PageInfo()

        info.url = page.url
        info.title = page.title()

        info.links = page.locator("a").count()
        info.buttons = page.locator("button").count()
        info.forms = page.locator("form").count()
        info.images = page.locator("img").count()
        info.inputs = page.locator("input").count()
        info.headings = page.locator("h1, h2, h3, h4, h5, h6").count()

        print()
        print("──────── GovAgent Explorer ────────")
        print()

        print(f"URL: {info.url}")
        print(f"Title: {info.title}")

        print(f"Links: {info.links}")       
        print(f"Buttons: {info.buttons}")
        print(f"Forms: {info.forms}")
        print(f"Images: {info.images}")
        print(f"Inputs: {info.inputs}")
        print(f"Headings: {info.headings}")

        return info