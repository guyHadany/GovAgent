from browser.navigator import Navigator
from browser.browser import Browser
from browser.explorer import Explorer


def main():
    print()
    print("🟢 GovAgent")
    print("-------------------------")

    browser = Browser()
    browser.start()
    browser.open("https://example.com")
    navigator = Navigator(browser.page)
    navigator.click_text("Learn more")
    print(f"עבר אל: {browser.page.url}")


    navigator.go_back()
    print(f"חזר אל: {browser.page.url}")
    
    explorer = Explorer()
    page_info = explorer.inspect(browser.page)
    print()
    print("──────── PageInfo ────────")
    print(page_info.title)
    print(page_info.url)
    browser.wait()


if __name__ == "__main__":
    main()