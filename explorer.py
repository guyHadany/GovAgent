def get_links(page):
    links = page.eval_on_selector_all(
        "a[href]",
        "elements => elements.map(e => e.href)"
    )

    unique_links = sorted(set(link for link in links if link))

    return unique_links