from selenium import webdriver


def main():
   driver = webdriver.Chrome()
   driver.get("https://skillhub.ru/")
   #result = driver.find_elements_by_class_name("main-button")
   #result.click()

if __name__ == "__main__":
   main()