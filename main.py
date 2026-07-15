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
    explorer.inspect(browser.page)
    browser.wait()


if __name__ == "__main__":
    main()