from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ThemesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    EXTEND = (By.XPATH, "//span[text()='Extend']")
    SEARCH_BOX = (By.ID, "wp-block-search__input-8")
    SEARCH_BTN = (By.XPATH, "(//button[@aria-label='Search'])[2]")
    THEME_CARD = (By.XPATH, "//h2[contains(text(),'Astra')]")
    THEME_H1 = (By.XPATH, "//*[@id='wp--skip-link--target']//h1")

    # Actions
    def open_site(self):
        self.driver.get("https://wordpress.org/")

    def get_title(self):
        return self.driver.title

    def hover_extend(self):
        menu = self.wait.until(EC.visibility_of_element_located(self.EXTEND))
        ActionChains(self.driver).move_to_element(menu).perform()

    def open_themes_page(self):
        self.driver.get("https://wordpress.org/themes/")
        # # Step 2: Hover Extend
    extend_menu = wait.until(EC.visibility_of_element_located(EXTEND))
    ActionChains(driver).move_to_element(extend_menu).perform()

    # Step 3: Open Themes
    THEMES_LINK = (By.LINK_TEXT, "Themes")
    wait.until(EC.element_to_be_clickable(THEMES_LINK)).click()

    def search_theme(self, theme_name):
        search = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
        search.clear()
        search.send_keys(theme_name)
        return search.get_attribute("value").strip()

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

    def open_theme_card(self):
        theme = self.wait.until(EC.visibility_of_element_located(self.THEME_CARD))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", theme
        )
        theme.click()

    def get_theme_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.THEME_H1)
        ).text.strip()
