from browser import Browser
from explorer import Explorer


def main():
    print()
    print("🟢 GovAgent")
    print("-------------------------")

    browser = Browser()
    browser.start()
    browser.open("https://example.com")
    explorer = Explorer()
    page_info = explorer.inspect(browser.page)
    print()
    print("──────── PageInfo ────────")
    print(page_info.title)
    print(page_info.url)
    browser.wait()


if __name__ == "__main__":
    main()