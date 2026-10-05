import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        hello_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        screenshot_path = os.path.join (
            screenshots_dir, "screenshot_lesson06_task1.png"
        )
        driver.save_screenshot(screenshot_path)

        assert hello_element.text == "Hello World!", (
            f"Текст не совпадает. Получено: {hello_element.text}"
        )
    finally:
        driver.quit()
