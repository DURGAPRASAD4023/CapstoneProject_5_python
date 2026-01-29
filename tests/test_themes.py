import pytest
from pages.themes_page import ThemesPage


@pytest.mark.smoke
def test_wordpress_theme_search(setup):
    driver = setup
    page = ThemesPage(driver)

    # Step 1: Launch site & verify title
    page.open_site()
    assert "WordPress.org" in page.get_title()

    # Step 2: Hover Extend
    page.hover_extend()

    # Step 3: Open Themes page
    page.open_themes_page()

    # Step 4: Search theme
    searched_text = page.search_theme("Astra")
    page.click_search()

    # Step 5: Open theme card
    page.open_theme_card()

    # Step 6: Verify theme page title
    theme_title = page.get_theme_page_title()
    assert searched_text.lower() in theme_title.lower(), \
        f"Mismatch! Searched: {searched_text}, Found: {theme_title}"

    print("=======================Search text matches theme page===================================")
