from cookie_game import ClassicCookie

url = "http://orteil.dashnet.org/experiments/cookie/"


# Main loop for the automation process
cookie_game = ClassicCookie(url)
item_ids = cookie_game.item_ids
while True:
    # Click the cookie for a set time
    cookie_game.click_cookie()

    # Get available upgrades
    available_upgrades = cookie_game.get_available_upgrades()

    # Select the item ID to upgrade (choosing the last available upgrade)
    itemid = item_ids[len(available_upgrades) - 1]

    # Make the upgrade
    cookie_game.make_upgrade(itemid)
