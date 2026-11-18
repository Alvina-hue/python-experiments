
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()

# Step 2: Open DemoQA Text Box page
driver.get("https://demoqa.com/text-box")

# Step 3: Maximize browser window
driver.maximize_window()

# Step 4: Enter Full Name
driver.find_element(By.ID, "userName").send_keys("Alvina K V")

# Step 5: Enter Email
driver.find_element(By.ID, "userEmail").send_keys("alvina@gmail.com")

# Step 6: Enter Current Address
driver.find_element(By.ID, "currentAddress").send_keys("Thrissur, Kerala")

# Step 7: Enter Permanent Address
driver.find_element(By.ID, "permanentAddress").send_keys("Kodaly, Kerala")

# Step 8: Scroll to and click Submit button
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    submit_button
)

try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    ).click()
except TimeoutException:
    driver.execute_script("arguments[0].click();", submit_button)

# Step 9: Wait for submitted details and display them
try:
    output_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "output"))
    )
    output = output_element.text
except (TimeoutException, NoSuchElementException):
    output = ""

if ("Alvina K V" in output and
    "alvina@gmail.com" in output and
    "Thrissur, Kerala" in output and
    "Kodaly, Kerala" in output):

    print("Form submitted successfully!")
    print("All details are verified.")
    print("\nSubmitted Details:")
    print(output)
else:
    print("Data verification failed.")

# Step 11: Close browser
driver.quit()
