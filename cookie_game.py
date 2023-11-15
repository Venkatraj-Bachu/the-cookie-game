from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Keep Chrome open after program finishes
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)


class ClassicCookie:
    """
        A class to interact with a classic cookie-clicker game using Selenium.

        Attributes:
            url (str): The URL of the cookie-clicker game.
        Methods:
            get_item_ids():
                Retrieves IDs of store items available for purchase.
            click_cookie():
                Simulates clicking on the cookie to earn points.
            get_available_upgrades():
                Retrieves available upgrades based on current score.
            make_upgrade(item_id):
                Purchases an upgrade using its ID.
    """

    def __init__(self, url):
        """
            Initializes the ClassicCookie object with the URL of the cookie-clicker game.

            Args:
                url (str): The URL of the cookie-clicker game.
        """

        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)
        self.driver.get(url)

        # Find the cookie element on the page
        self.cookie = self.driver.find_element(By.ID, value="cookie")
        self.item_ids = self.get_item_ids()

    def get_item_ids(self):
        """
            Retrieves IDs of store items available for purchase.

            Returns:
                list: IDs of store items.
        """

        # Find all the store items' IDs
        items = self.driver.find_elements(By.CSS_SELECTOR, value='#store div')
        return [item.get_attribute("id") for item in items]

    def click_cookie(self):
        """
            Simulates clicking on the cookie to earn points.
        """

        timeout = time.time() + 5
        while True:
            if time.time() > timeout:
                break
            self.cookie.click()

    def get_available_upgrades(self):
        """
            Retrieves available upgrades based on the current score.

            Returns:
                list: Available upgrades.
        """

        current_score = int(self.driver.find_element(By.ID, value="money").text)
        print(current_score)
        store = self.driver.find_element(By.ID, value='store')
        upgrades = store.find_elements(By.CSS_SELECTOR, value='#store b')
        upgrades = [upgrade.text.split('-')[1].replace(',', '').strip() for upgrade in upgrades if
                    upgrade.text != '' and
                    int(upgrade.text.split('-')[1].replace(',', '').strip()) <= current_score]
        return upgrades

    def make_upgrade(self, item_id):
        """
            Purchases an upgrade using its ID.

            Args:
                item_id (str): ID of the upgrade item.
        """

        upgrade_item = self.driver.find_element(By.ID, value=item_id)
        upgrade_item.click()
