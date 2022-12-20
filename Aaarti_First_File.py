from selenium import webdriver

def launch_browser(name):
    if name.lower() == 'chrome':
        driver = webdriver.Chrome("driver path")
    elif name.lower() == 'firefox':
        driver = webdriver.firefox("driver path")

    return driver

def launch_website(url,  driver):
    driver.get(url)


driver = launch_browser('chrome')
launch_website('https://www.google.co.in', driver)

