
# Imports
from selenium import webdriver
from time import sleep

# CONFIG Options

url = input("Enter the url to test\n\n") # Url To Test
browsers = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox] # List of Browser Drivers to Test
screens = [[1024, 0], [768, 0], [402, 0]] # List of Screen Sizes to Test

# Gets relevant options object based on browser
def getOptions(browser):
    if browser == webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new") # Hides the browser
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # Disables Logging
        return options

    if browser == webdriver.Edge:
        options = webdriver.EdgeOptions()
        options.add_argument("--headless=new") # Hides the browser
        return options

    if browser == webdriver.Firefox:
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless=new") # Hides the browser
        return options

    if browser == webdriver.Ie:
        options = webdriver.IeOptions()
        options.add_argument("--headless=new") # Hides the browser
        return options

    if browser == webdriver.Safari:
        options = webdriver.SafariOptions()
        options.add_argument("--headless=new") # Hides the browser
        return options

# Testing Loop
for browser in browsers:
    options = getOptions(browser)
    driver = browser(options=options)

    driver.maximize_window()
    driver.get(url)

    print(f"\n{driver.name}\n")

    for screen in screens:

        if screen[0] == 0:
            screen[0] = driver.get_window_size()['width']

        if screen[1] == 0:
            screen[1] = driver.get_window_size()['height']

        driver.set_window_size(screen[0], screen[1])
        sleep(0.5)
        ok = driver.save_screenshot(f"screenshots/{driver.name} {screen[0]}x{screen[1]}.png")
        if ok:
            print(f"{screen[0]}x{screen[1]} saved")
        else:
            print(f"{screen[0]}x{screen[1]} error")

    driver.quit()