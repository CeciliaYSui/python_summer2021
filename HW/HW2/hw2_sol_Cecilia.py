# ----------------------------------------------------------------------------------------------------
# Project Name -------- HW#2 for Python Camp
# Developer ----------- Cecilia Y. Sui
# Date last updated --- Aug 19, 2021
# Date last run ------- Aug 19, 2021 (output are based on the website content on Aug 19, 2021)
# 
# Project Desription -- Create a csv file with the following information for each spoken address
# --------------------- given by President Biden since he became president on 2021-01-20
# Output -------------- csv file with 4 cols (date, title, full text, citation/footnote if exists)
# sources -------------
# https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks
# https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-tag-name
# ----------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import csv, os, time, random
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime


# ---------------------------------------------------------------------------
# Set up chrome driver using selenium
# ---------------------------------------------------------------------------
chrome_driver_path = '/Users/ysui/Desktop/chromedriver' # abs path 
chrome_options = Options()  # Option class 
chrome_options.add_argument('--headless') # avoid popping up a window
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options) # create chrome driver
url = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks" # given url for presidency project
driver.get(url) # navigate to the given url
# assert that it actually went to the correct website
assert "The American Presidency Project" in driver.title


# ---------------------------------------------------------------------------
# Create a pandas dataframe 
# ---------------------------------------------------------------------------
df = pd.DataFrame(columns=["Date", "Title", "Link", "Remarks", "Footnote", "Citation"])

# ---------------------------------------------------------------------------
# Set the cutpoint for date and president for filtering
# Easy to modify for later use and future applications
# ---------------------------------------------------------------------------
begin_date = datetime(2021,1,20)
president = "Joseph R. Biden"

# ---------------------------------------------------------------------------
# Create a while loop to continously scrape the pages
# ---------------------------------------------------------------------------
flag = True # use the flag to handle when to stop
# since the website is dynamically updating, we should not use a specific counter for pages to handle the loop
page_cnt = 1 # use the page count to inform users of the ongoing process

while True:
    print("Page No. " + str(page_cnt))
    page_cnt += 1  # increment page counter
    print(driver.current_url) # grab current url to make sure it is working on the correct page
    
    row_cnt = driver.find_elements_by_class_name("row")
    # start at 1 to handle first duplicate 
    for i in range(1, len(row_cnt)):
        # find the row element using this line to resolve the StaleElementReferenceException (try and except not necessary)
        rows = driver.find_elements_by_class_name("row")[i] 

        # ---------------------------------------------------
        # 1. Extract the name of the speech giver
        # 2. Make sure the remarks are given by Biden
        # ---------------------------------------------------
        name = rows.find_element_by_class_name("col-sm-4.margin-top").find_element_by_tag_name("a").text
        # If the speech if by Biden, we do the following. 
        # If not, we stop here and continue to the next iteration in the loop.
        if name == president:
            # print(i)
            pass
        else: 
            continue
        
        # ---------------------------------------------------
        # 1. Extract the date of the speech given
        # 2. Make sure the date is after Jan 20, 2021 
        # ---------------------------------------------------
        date = rows.find_element_by_class_name("date-display-single").get_attribute("content")[:10]
        date_time_obj = datetime.strptime(date, "%Y-%m-%d") # convert to date time object for easy comparison
        # If the date is before Jan 20, 2021, the program breaks out of the for and while loops and gets ready to export and finish. 
        # Here we are relying on the fact that the website has organized the speeches based on their dates. 
        if date_time_obj >= begin_date: 
            # print(date_time_obj)
            pass
        else:
            flag = False
            break

        # ---------------------------------------------------
        # Extract the title of the speech
        # ---------------------------------------------------
        title = rows.find_element_by_class_name("field-title") # extract title of the speech
        t = title.text # grab the text separately, since title is used later to grab the link
        print(t)

        # ---------------------------------------------------
        # Grab the link to the actual content of the remarks
        # ---------------------------------------------------
        link = title.find_element_by_tag_name("a").get_attribute("href") # grab the new url
        driver.get(link) # navigate to the new url
        remarks = driver.find_element_by_class_name("field-docs-content").text # extract remarks

        # ---------------------------------------------------
        # Use try and except block to deal with the case 
        # that it does not have citation or footnote
        # ---------------------------------------------------
        try: 
            citation = driver.find_element_by_class_name("ucsbapp_citation").text
        except NoSuchElementException as Exception: 
            citation = "N/A"
        try: 
            footnote = driver.find_element_by_class_name("field-docs-footnote").text
        except NoSuchElementException as Exception:
            footnote = "N/A"
        driver.back() # navigate back to the main page 
        # print(remarks[:50])
        # print(citation)
        # print(footnote)

        # ---------------------------------------------------
        # Be polite & sleep a little :) 
        # ---------------------------------------------------
        time.sleep(5)

        # ---------------------------------------------------
        # Append the row to dataframe df
        # ---------------------------------------------------
        df = df.append({"Date":date, "Title":t, "Link":link, "Remarks":remarks, "Footnote":footnote, "Citation":citation}, ignore_index=True)

    # ----------------------------------------------------------
    # Use the flag to control the process.
    # Break if already hits date prior to Jan 20, 2021
    # ----------------------------------------------------------
    if not flag: 
        break

    # ----------------------------------------------------------
    # Click the button / navigate to the next page to continue 
    # ----------------------------------------------------------
    next_page = driver.find_element_by_partial_link_text('next').get_attribute("href")
    driver.get(next_page)
    # ----------------------------------------------------------
    # Assert to make sure it is working on the correct page, and 
    # successfully navigated to the next page 
    # ----------------------------------------------------------
    assert driver.current_url.split("=")[1] == str(page_cnt-1)
    print()

# ---------------------------------------------------
# Close the driver
# ---------------------------------------------------
driver.close()

# ---------------------------------------------------
# Export to csv file 
# ---------------------------------------------------
df.to_csv("Biden_remarks.csv", index = False)

# ---------------------------------------------------
# Print a message in console to inform the users that the process is done
# ---------------------------------------------------
print("Porgram finished! \nBiden_remarks.csv has been successfully exported!")
