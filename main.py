from browser import open_browser
from config import BASE_URL
from explorer import get_links

print("GovAgent מתחיל...")

playwright, browser, page = open_browser()

page.goto(BASE_URL, wait_until="networkidle")

print("כותרת:")
print(page.title())

links = get_links(page)

print()
print(f"נמצאו {len(links)} קישורים:")

for link in links:
    print(link)

browser.close()
playwright.stop()

print()
print("GovAgent הסתיים.")