from browser.browser import Browser
from browser.explorer import Explorer
from browser.navigator import Navigator


def main():
    print()
    print("🟢 GovAgent")
    print("-------------------------")

    browser = Browser()
    browser.start()

    browser.open(
        "https://villanuevadelavera.sedelectronica.es/info.0"
    )

    navigator = Navigator(browser.page)
    print(f"קיים טקסט Trámites: {navigator.text_exists('Trámites')}")
    navigator.click_text("Trámites")
    print(f"עבר אל: {browser.page.url}")

    print()
    print("──────── Links ────────")
    navigator.list_matching_links("Licencia")
    opened = navigator.click_first_matching_link(
    "Solicitud de Licencia o Autorización Urbanística"
    )
    print(f"הליך נפתח: {opened}")
    print(f"כתובת נוכחית: {browser.page.url}")
    print()
    print("──────── Buttons ────────")
    navigator.list_buttons()
    downloaded_file = navigator.download_by_text(
    "Descargar instancia",
    "output/solicitud_licencia_urbanistica.pdf"
    )
    print(f"קובץ הורד אל: {downloaded_file}")
    #print()
    #print("──────── Text ────────")
    #print(browser.page.locator("body").inner_text())
    print()
    print("Buscando trámites con 'Licencia'...")
    explorer = Explorer()
    page_info = explorer.inspect(browser.page)

    print()
    print("──────── PageInfo ────────")
    print(page_info.title)
    print(page_info.url)

    browser.wait()


if __name__ == "__main__":
    main()