from page_info import PageInfo

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

        print(f"URL: {page.url}")
        print(f"Title: {page.title()}")

        print(f"Links: {page.locator('a').count()}")
        print(f"Buttons: {page.locator('button').count()}")
        print(f"Forms: {page.locator('form').count()}")
        print(f"Images: {page.locator('img').count()}")
        print(f"Inputs: {page.locator('input').count()}")

        print(
            f"Headings: {page.locator('h1, h2, h3, h4, h5, h6').count()}"
        )

        return info