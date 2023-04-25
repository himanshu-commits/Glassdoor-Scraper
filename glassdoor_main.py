from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

import pandas as pd

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
data_science_url = "https://www.glassdoor.co.in/Job/india-data-scientist-jobs-SRCH_IL.0,5_IN115_KO6,20.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=india&context=Jobs&dropdown=0"
#web_dev_url = "https://www.glassdoor.co.in/Job/india-web-developer-jobs-SRCH_IL.0,5_IN115_KO6,19.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=India&context=Jobs&dropdown=0"
driver.get(data_science_url)


def jobs(num_jobs):
    #print('inside 1')
    
    max = 0
    job = []
    

    while(len(job) < num_jobs):
        try:
            # wait for the "Next" button to be clickable
            grid = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="MainCol"]/div[1]/ul'))
            )
        except NoSuchElementException:
            print('not found')
    
        options = grid.find_elements(By.TAG_NAME, "li")
        #print("the length of the list is", len(options))
        for op in options:     # 0<30   30<30 next page
            if(len(job) < num_jobs):
                max = max+1
                #print('maximum value reached',max)
                #time.sleep(4)
                #print("the length of the jobs are",len(job))
                try:
                    clicking = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "jobLink"))
                    
        )
                    clicking.click()
                    #print('yes')
                except ElementClickInterceptedException:
                    pass
                #time.sleep(5)
                try:
                    driver.find_element(By.CSS_SELECTOR,"span[class='SVGInline modal_closeIcon']").click()  #clicking to the X.
                    #print('success')
                except NoSuchElementException:
                    pass
                
                
                #print('inside 6')
                print("Progress: {}".format("" + str(len(job)) + "/" + str(num_jobs)))
                op.click
                #time.sleep(5)
                collection_successfully = False
        #      print('inside 7')
                while not collection_successfully:
                    #time.sleep(2)
        #         print('inside 8')
        
                    
                    
                    try:
                        company_name = op.find_element(By.CSS_SELECTOR,"a[class=' css-l2wjgv e1n63ojh0 jobLink']").text
                    except  NoSuchElementException:
                        company_name = "Not available"
                        pass
                    try:
                        title = op.find_element(By.CSS_SELECTOR,"a[data-test='job-link']").text
                    except  NoSuchElementException:
                        title = "Not available"
                        pass
                    
                    
                    #size  = option2.find_element(By.XPATH,"//*[@id='EmpBasicInfo']/div[1]/div/div[1]/span[2]").text
                    try:
                        location = op.find_element(By.CSS_SELECTOR,"span[data-test='emp-location']").text
                    except  NoSuchElementException:
                        location = "Not available"
                        pass
                    
                    try:
                        estimated_sal = op.find_element(By.CSS_SELECTOR,"span[data-test='detailSalary']").text
                    except  NoSuchElementException:
                        estimated_sal = "Unrevealed"
                        pass
                    try:
                        posted = op.find_element(By.CSS_SELECTOR,"div[class='d-flex align-items-end pl-std css-1vfumx3']").text
                    except  NoSuchElementException:
                        estimated_sal = "Not available"
                        pass
                    try:
                        rating = op.find_element(By.CSS_SELECTOR,"span[class=' css-2lqh28 e1cjmv6j1']").text
                    except  NoSuchElementException:
                        rating = "Not available"
                        pass
                    try:
                        link = op.find_element(By.CSS_SELECTOR,"a[data-test='job-link']").get_attribute('href')
                    except  NoSuchElementException:
                        title = "Not available"
                        pass
                    

                        
                    
                    #founded = option2.find_element(By.CSS_SELECTOR,"span[class='css-i9gxme e1pvx6aw2']")
            #        print('inside 9')
                    collection_successfully = True
                    #print(title)
                    #print(size)
                    
            #       print('inside 10')
                    
                job.append({"company name":company_name,
                            "job_title":title,
                            "Location":location,
                            "Estimated salary":estimated_sal,
                            "posted":posted,
                            "rating":rating,
                            "link":link
                            })
                #30 times
            if(len(options)==max):
                try:
            # wait for the "Next" button to be clickable
                    next_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='MainCol']/div[2]/div/div[1]/button[7]"))
            )
            
            # click on the "Next" button
                    next_button.click()
                    max = 0
                    print('next in action')
                    time.sleep(8)
                    break
                except NoSuchElementException:
                    return pd.DataFrame(job)
                    #print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                    #break
            
    return pd.DataFrame(job)
        
df = jobs(897)
data = df.to_csv('glassdoor_script2.csv')