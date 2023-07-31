import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




def scrapeData(budget_request) :
        url = "https://www.billhighway.com/aph/forChapters/v2/login.aspx?logoff=timeout"
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1480")
        options.add_argument("disable-dev-shm-usage")
        
        service = Service(executable_path=ChromeDriverManager().install())
        chromedriver_autoinstaller.install()  
        driver  = webdriver.Chrome(options=options, service=service)
        driver.get(url)

        login(driver)
        print("logged in")
        driver.get("https://www.billhighway.com/APH/forChapters/home.aspx")
        time.sleep(5)
        # close_buttons = driver.find_elements(By.CLASS_NAME, "bc-closeButton")
        # if (len(close_buttons) > 0) :
        #       close_buttons[0].click()
        #       time.sleep(3)
                    

        driver.get("https://www.billhighway.com/aph/forChapters/budgetVariance.aspx")
        time.sleep(5)
        submit = driver.find_elements(By.CLASS_NAME, "RadButton")
        submit[0].click()
        time.sleep(3)


       
        budget_information = driver.find_elements(By.CLASS_NAME, "alignRight")

        temp_index = 0
        for b in budget_information: 
                print("budget: ", b.text, "index: ", temp_index)
                temp_index = temp_index + 1
        
        
        index = 32
        for row in range(12,15) :
             path = '//*[@id="ctl00_cphBody_aphBudgetVarianceGrid_tblBudgetVariance"]/tbody/tr[' + str(row) + ']/td[1]'
             label = driver.find_element(By.XPATH, path)
             temp = label.text.split(" ")
             temp.remove(temp[0])
             listToStr = ' '.join([str(elem) for elem in temp])
             if (listToStr == budget_request) :
                spent = budget_information[index].text
                budget = budget_information[index + 1].text
                return [listToStr, budget, spent]
             index = index + 4 

        index = index + 4
        for row in range(18,23) :
             path = '//*[@id="ctl00_cphBody_aphBudgetVarianceGrid_tblBudgetVariance"]/tbody/tr[' + str(row) + ']/td[1]'
             label = driver.find_element(By.XPATH, path)
             temp = label.text.split(" ")
             temp.remove(temp[0])
             listToStr = ' '.join([str(elem) for elem in temp])
             if (listToStr == budget_request) :
                spent = budget_information[index].text
                budget = budget_information[index + 1].text
                return [listToStr, budget, spent]
             index = index + 4 

        index = index + 4
        for row in range(26,34) :
             path = '//*[@id="ctl00_cphBody_aphBudgetVarianceGrid_tblBudgetVariance"]/tbody/tr[' + str(row) + ']/td[1]'
             label = driver.find_element(By.XPATH, path)
             temp = label.text.split(" ")
             temp.remove(temp[0])
             listToStr = ' '.join([str(elem) for elem in temp])
             if (listToStr == budget_request) :
                spent = budget_information[index].text
                budget = budget_information[index + 1].text
                return [listToStr, budget, spent]
             index = index + 4 
                

def login(driver) :
     
     driver.find_element("id", "ctl00_cphBody_Login_memID").send_keys("nmeini01")
     driver.find_element("id", "ctl00_cphBody_Login_pswrd").send_keys("Flower12!")
     buttons = driver.find_elements(By.CLASS_NAME, "RadButton")
     buttons[0].click()

if __name__ == '__main__' :
    
    budget_request = "Fall Formal"
    
    response = scrapeData(budget_request)
    print(response)
