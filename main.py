# print statement for reference and contact.
print("**\n***\n****\n*****\n******\n*******\n"
      "This bot is coded and developed by Mr.SAFEER ABBAS.\n "
      "https://safeerabbas624.github.io/safeerabbas/\n "
      "https://github.com/SafeerAbbas624\n"
      "*******\n******\n*****\n****\n***\n**")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import pandas.errors as Error
import urllib.request
import random

# Proxies setup

def chrome_proxy() -> dict:
    wire_options = {
        "proxy": {
             "http": "http://jhujkqes-AR-AT-AU-BE-CA-CH-ES-FR-GB-GR-HU-IT-JP-MT-NL-NO-SE-UA-ZA-rotate:xgb6bc4q14ai@p.webshare.io:80/",
        "https": "http://jhujkqes-AR-AT-AU-BE-CA-CH-ES-FR-GB-GR-HU-IT-JP-MT-NL-NO-SE-UA-ZA-rotate:xgb6bc4q14ai@p.webshare.io:80/"
        }
    }

    return wire_options


options = ChromeOptions()
proxies = chrome_proxy()
driver = webdriver.Chrome(
    options=options, seleniumwire_options=proxies)

# Open and read zip file
# Opening file
# file1 = open('zip.csv', 'r')
# count = 0
# zip_code = []
#
# # Using for loop
# print("Counting Zip Codes from Zip.csv file")
# for line in file1:
#     count += 1
#     zip_code.append(line.strip())
#     print("Line{}: {}".format(count, line.strip()))
#
# # Closing files
# file1.close()

start_date =[]        #an empty list to store the first column
end_date = []
with open('date.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        start_date.append(row[0])
        end_date.append(row[1])
start_date = list(filter(None, start_date))
end_date = list(filter(None, end_date))
print(start_date)
print(end_date)


# Navigate to the website
url = "https://cpdocket.cp.cuyahogacounty.us/Search.aspx"
driver.get(url)
time.sleep(10)
# Find and select the "Foreclosure" option
driver.find_element(By.XPATH,'//*[@id="SheetContentPlaceHolder_rbCivilForeclosure"]').click()
# Wait for page loading
time.sleep(15)
# Terms agreement selecting yes
driver.find_element(By.XPATH, '//*[@id="SheetContentPlaceHolder_btnYes"]').click()
time.sleep(15)
# Variable for end date string 
end_date_string = 0
# For loop to loop through all zip codes one by one
for date in start_date:
    case_number = 0
    global case, case2

    # Range loop for collecting all cases against zip code in above loop
    for n in range(0, 200):

        try:

            # Dictionary for collecting data
            headings = {'Case Summary Link': [],
                        'Case Number': [],
                        'Case Title': [],
                        'Case Designation': [],
                        'Filing Date': [],
                        'Judge': [],
                        'Magistrate': [],
                        'Mediator': [],
                        'Room': [],
                        'Next Action': [],
                        'File Location': [],
                        'Last Status': [],
                        'Last Status Date': [],
                        'Last Disposition': [],
                        'Last Disposition Date': [],
                        'Prayer Amount': [],
                        'Court of Appeals Case': [],
                        'Original Case': [],
                        'Refiled Case': [],
                        'PLAINTIFF': [],
                        'DEFENDANT	(1)': [],
                        'DEFENDANT	(2)': [],
                        'DEFENDANT	(3)': [],
                        'DEFENDANT	(4)': [],
                        'DEFENDANT	(5)': [],
                        'DEFENDANT	(6)': [],
                        'DEFENDANT	(7)': [],
                        'DEFENDANT	(8)': [],
                        'DEFENDANT	(9)': [],
                        'DEFENDANT	(10)': [],
                        'ATTORNEY (1)': [],
                        'ATTORNEY (2)': [],
                        'ATTORNEY (3)': [],
                        'ATTORNEY (4)': [],
                        'ATTORNEY (5)': [],
                        'Parcel (1)': [],
                        'Street Number (1)': [],
                        'Street Name(1)': [],
                        'Address Line 2 (1)': [],
                        'City (1)': [],
                        'State (1)': [],
                        'ZIP (1)': [],
                        'Parcel (2)': [],
                        'Street Number (2)': [],
                        'Street Name(2)': [],
                        'Address Line 2 (2)': [],
                        'City (2)': [],
                        'State (2)': [],
                        'ZIP (2)': [],
                        'Parcel (3)': [],
                        'Street Number (3)': [],
                        'Street Name(3)': [],
                        'Address Line 2 (3)': [],
                        'City (3)': [],
                        'State (3)': [],
                        'ZIP (3)': [],
                        'Parcel (4)': [],
                        'Street Number (4)': [],
                        'Street Name(4)': [],
                        'Address Line 2 (4)': [],
                        'City (4)': [],
                        'State (4)': [],
                        'ZIP (4)': [],
                        'Parcel (5)': [],
                        'Street Number (5)': [],
                        'Street Name(5)': [],
                        'Address Line 2 (5)': [],
                        'City (5)': [],
                        'State (5)': [],
                        'ZIP (5)': [],

                        }

            # Wait for page loading
            time.sleep(2)
            # Again Find and select the "Foreclosure" option
            select = driver.find_element(By.XPATH, '//*[@id="SheetContentPlaceHolder_rbCivilForeclosure"]')
            select.click()
            select.click()
            select.click()
            select.click()
            select.click()
            # Wait for page loading
            time.sleep(10)

            # # Select case status to active
            # active = driver.find_element(By.XPATH, '//*[@id="SheetContentPlaceHolder_foreclosureSearch_cbStatus"]')
            # if active.is_selected():
            #     pass
            # else:
            #     active.click()
            time.sleep(2)
            # Input start filing date 
            filing_date_start = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_foreclosureSearch_txtFromDate"]')
            time.sleep(2)

            filing_date_start.clear()
            time.sleep(2)
            without_slash = date.replace("/", "")
            print(without_slash)
            filing_date_start.click()
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            filing_date_start.send_keys(Keys.ARROW_LEFT)
            time.sleep(2)
            for g in without_slash:
                print(g)
                filing_date_start.send_keys(g)
                time.sleep(0.5)


            # Input start filing end date 
            filing_date_end = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_foreclosureSearch_txtToDate"]')
            time.sleep(2)

            filing_date_end.clear()
            time.sleep(2)
            without_slash = end_date[end_date_string].replace("/", "")
            print(without_slash)
            filing_date_end.click()
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            filing_date_end.send_keys(Keys.ARROW_LEFT)
            time.sleep(2)
            for x in without_slash:
                print(x)
                filing_date_end.send_keys(x)
                time.sleep(0.5)

            # Click on Search button
            driver.find_element(By.XPATH, '/html[1]/body[1]/form[1]/div[4]/div[1]/div[10]/div[3]/div[1]/div[1]/div['
                                          '1]/div[2]/div[10]/div[1]/div[2]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr['
                                          '1]/td[1]/div[1]/table[1]/tbody[1]/tr[14]/td[2]/span[1]/input[1]').click()
            time.sleep(10)

            # Search table data getting to compere 
            search_table = driver.find_element(By.XPATH,
                                       '//*[@id="SheetContentPlaceHolder_ctl00_gvForeclosureResults"]').get_attribute('outerHTML')
            
            search_table1 = pd.read_html(search_table)
            df = search_table1[0]
            case = df.iloc[-1]['Case Number']

            # Click on case in search results
            case1 = driver.find_element(By.XPATH,
                                f'//*[@id="SheetContentPlaceHolder_ctl00_gvForeclosureResults_lbCaseNum_{case_number}"]')
            case2 = case1.text
            case1.click()
            time.sleep(8)

            # Getting Url of the page
            get_url = driver.current_url
            print(get_url)

            # Getting case summery data.
            data = driver.find_element(By.XPATH,
                                       '//*[@id="art-main"]/div/div[10]/div[3]/div/div/div[2]/div[10]/div/div['
                                       '2]/table[2]').get_attribute(
                'outerHTML')

            # Appending case summery data to dict.
            list1 = pd.read_html(data)
            list2 = list1[0][1]
            headings['Case Summary Link'] += [get_url]
            headings['Case Number'] += [list2[0]]
            headings['Case Title'] += [list2[1]]
            headings['Case Designation'] += [list2[2]]
            headings['Filing Date'] += [list2[3]]
            headings['Judge'] += [list2[4]]
            headings['Magistrate'] += [list2[5]]
            headings['Mediator'] += [list2[6]]
            headings['Room'] += [list2[7]]
            headings['Next Action'] += [list2[8]]
            headings['File Location'] += [list2[9]]
            headings['Last Status'] += [list2[10]]
            headings['Last Status Date'] += [list2[11]]
            headings['Last Disposition'] += [list2[12]]
            headings['Last Disposition Date'] += [list2[13]]
            headings['Prayer Amount'] += [list2[14]]
            headings['Court of Appeals Case'] += [list2[15]]
            headings['Original Case'] += [list2[16]]
            headings['Refiled Case'] += [list2[17]]

            # Going to parties page
            driver.find_element(By.XPATH,
                                '//*[@id="SheetContentPlaceHolder_caseHeader_lbParties"]').click()
            time.sleep(8)
            # Getting Plaintiff / Defendant data
            try:
                # Getting plaintiff data.
                data1 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '1]/td[2]/table/tbody').text

                # Appending plaintiff data into dict
                headings['PLAINTIFF'] += [data1]

                # Getting defendant 1 data.
                data2 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '2]/td[2]/table/tbody').text

                # Appending defendant 1 data into dict
                headings['DEFENDANT	(1)'] += [data2]

                # Getting defendant 2 data.
                data3 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '3]/td[2]/table/tbody').text

                # Appending defendant 2 data into dict
                headings['DEFENDANT	(2)'] += [data3]

                # Getting defendant 3 data.
                data4 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '4]/td[2]/table/tbody').text

                # Appending defendant 3 data into dict
                headings['DEFENDANT	(3)'] += [data4]

                # Getting defendent 4 data.
                data5 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '5]/td[2]/table/tbody').text

                # Appending defendant 4 data into dict
                headings['DEFENDANT	(4)'] += [data5]

                # Getting defendant 5 data.
                data6 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '6]/td[2]/table/tbody').text

                # Appending defendant 5 data into dict
                headings['DEFENDANT	(5)'] += [data6]

                # Getting defendant 6 data.
                data7 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '7]/td[2]/table/tbody').text

                # Appending defendant 6 data into dict
                headings['DEFENDANT	(6)'] += [data7]

                # Getting defendant 7 data.
                data8 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '8]/td[2]/table/tbody').text

                # Appending defendant 7 data into dict
                headings['DEFENDANT	(7)'] += [data8]

                # Getting defendant 8 data.
                data9 = driver.find_element(By.XPATH,
                                            '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                            '9]/td[2]/table/tbody').text

                # Appending defendant 8 data into dict
                headings['DEFENDANT	(8)'] += [data9]

                # Getting defendant 9 data.
                data10 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                             '10]/td[2]/table/tbody').text

                # Appending defendant 9 data into dict
                headings['DEFENDANT	(9)'] += [data10]

                # Getting defendent 10 data.
                data11 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties"]/tbody/tr['
                                             '11]/td[2]/table/tbody').text

                # Appending defendant 10 data into dict
                headings['DEFENDANT	(10)'] += [data11]

            except NoSuchElementException or Exception as E:
                print('No More Plaintiff/Defendants Data. \n All Plaintiff/Defendant Data Scraped.')
                pass

            # Getting Attorneys data
            try:
                # Getting Attorney 1 data.
                data12 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_0_grdAttyInfo_0"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                # Appending Attorney 1 data into dict
                headings['ATTORNEY (1)'] += [data12]
                print('Attorney 1 against Plaintiff data scraped')

            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Plaintiff')
                pass

            try:
                # Getting Attorney 2 data.
                data13 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_0_grdAttyInfo_0"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                # Appending Attorney 2 data into dict
                headings['ATTORNEY (2)'] += [data13]
                print('Attorney 2 against Plaintiff data scraped')

            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Plaintiff')
                pass

            try:
                # Getting Attorney 3 data.
                data14 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_0_grdAttyInfo_0"]/tbody/tr[3]/td[2]/table/tbody/tr/td/table/tbody').text

                # Appending Attorney 3 data into dict
                headings['ATTORNEY (3)'] += [data14]
                print('Attorney 3 against Plaintiff data scraped')

            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Plaintiff')
                pass

            try:
                # Getting Attorney 4 data.
                data15 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_0_grdAttyInfo_0"]/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody').text

                # Appending Attorney 4 data into dict
                headings['ATTORNEY (4)'] += [data15]
                print('Attorney 4 against Plaintiff data scraped')

            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Plaintiff')
                pass

            try:
                # Getting Attorney 5 data.
                data16 = driver.find_element(By.XPATH,
                                             '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_0_grdAttyInfo_0"]/tbody/tr[5]/td[2]/table/tbody/tr/td/table/tbody').text

                # Appending Attorney 5 data into dict
                headings['ATTORNEY (5)'] += [data16]
                print('Attorney 5 against Plaintiff data scraped')

            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Plaintiff')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 1.
                    data17 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_1_grdAttyInfo_1"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data17]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data17]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data17]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data17]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data17]
                    print('Attorney 1 against Defendant 1 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 1')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 2 data against defendant 1.
                    data18 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_1_grdAttyInfo_1"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 2 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data18]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data18]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data18]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data18]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data18]
                    print('Attorney 2 against Defendant 1 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 1')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 3 data against defendant 1.
                    data19 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_1_grdAttyInfo_1"]/tbody/tr[3]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 3 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data19]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data19]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data19]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data19]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data19]
                    print('Attorney 3 against Defendant 1 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 1')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 4 data against defendant 1.
                    data20 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_1_grdAttyInfo_1"]/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 4 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data20]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data20]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data20]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data20]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data20]
                    print('Attorney 4 against Defendant 1 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 1')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 5 data against defendant 1.
                    data21 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_1_grdAttyInfo_1"]/tbody/tr[5]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 5 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data21]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data21]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data21]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data21]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data21]
                    print('Attorney 5 against Defendant 1 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 1')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 2.
                    data22 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_2_grdAttyInfo_2"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data22]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data22]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data22]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data22]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data22]
                    print('Attorney 1 against Defendant 2 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 2')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 2 data against defendant 2.
                    data23 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_2_grdAttyInfo_2"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 2 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data23]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data23]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data23]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data23]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data23]
                    print('Attorney 2 against Defendant 2 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 2')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 3.
                    data24 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_3_grdAttyInfo_3"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data24]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data24]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data24]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data24]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data24]
                    print('Attorney 1 against Defendant 3 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 3')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 2 data against defendant 3.
                    data25 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_3_grdAttyInfo_3"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 2 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data25]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data25]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data25]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data25]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data25]
                    print('Attorney 2 against Defendant 3 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 3')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 4.
                    data26 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_4_grdAttyInfo_4"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data26]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data26]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data26]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data26]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data26]
                    print('Attorney 1 against Defendant 4 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 4')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 2 data against defendant 4.
                    data27 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_4_grdAttyInfo_4"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 2 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data27]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data27]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data27]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data27]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data27]
                    print('Attorney 2 against Defendant 4 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 4')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 5.
                    data28 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_5_grdAttyInfo_5"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data28]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data28]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data28]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data28]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data28]
                    print('Attorney 1 against Defendant 5 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 5')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 2 data against defendant 5.
                    data29 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_5_grdAttyInfo_5"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 2 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data29]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data29]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data29]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data29]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data29]
                    print('Attorney 2 against Defendant 5 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 5')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 6.
                    data35 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_6_grdAttyInfo_6"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data35]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data35]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data35]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data35]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data35]
                    print('Attorney 1 against Defendant 6 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 6')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 2 data against defendant 6.
                    data36 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_6_grdAttyInfo_6"]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 2 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data36]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data36]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data36]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data36]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data36]
                    print('Attorney 2 against Defendant 6 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 6')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 7.
                    data37 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_7_grdAttyInfo_7"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data37]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data37]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data37]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data37]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data37]
                    print('Attorney 1 against Defendant 7 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 7')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 8.
                    data38 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_8_grdAttyInfo_8"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data38]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data38]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data38]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data38]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data38]
                    print('Attorney 1 against Defendant 8 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 8')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 9.
                    data39 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_9_grdAttyInfo_9"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data39]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data39]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data39]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data39]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data39]
                    print('Attorney 1 against Defendant 9 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 9')
                pass

            try:
                if not headings['ATTORNEY (1)'] or not headings['ATTORNEY (2)'] or not headings['ATTORNEY (3)'] or not \
                        headings['ATTORNEY (4)'] or not headings['ATTORNEY (5)']:
                    # Getting Attorney 1 data against defendant 10.
                    data40 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseParties_grdCaseParties_attyInfo_10_grdAttyInfo_10"]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody').text

                    # Appending Attorney 1 data into dict
                    if not headings['ATTORNEY (1)']:
                        headings['ATTORNEY (1)'] = [data40]
                    elif not headings['ATTORNEY (2)']:
                        headings['ATTORNEY (2)'] = [data40]
                    elif not headings['ATTORNEY (3)']:
                        headings['ATTORNEY (3)'] = [data40]
                    elif not headings['ATTORNEY (4)']:
                        headings['ATTORNEY (4)'] = [data40]
                    elif not headings['ATTORNEY (5)']:
                        headings['ATTORNEY (5)'] = [data40]
                    print('Attorney 1 against Defendant 10 data scraped')

                else:
                    pass
            except NoSuchElementException or Error as E:
                print('No More Attorneys Data against Defendant 10')
                pass

            # Going to Properties page
            driver.find_element(By.XPATH,
                                '//*[@id="SheetContentPlaceHolder_caseHeader_lbProperty"]').click()
            time.sleep(8)

            # Getting Property data1.
            data30 = driver.find_element(By.XPATH,
                                         '//*[@id="SheetContentPlaceHolder_caseProperty_gvProperties"]/tbody/tr[1]/td/table').get_attribute(
                'outerHTML')

            # Appending Property data to dict.
            list1 = pd.read_html(data30)
            list2 = list1[0][1]
            headings['Parcel (1)'] += [list2[0]]
            headings['Street Number (1)'] += [list2[1]]
            headings['Street Name(1)'] += [list2[2]]
            headings['Address Line 2 (1)'] += [list2[3]]
            headings['City (1)'] += [list2[4]]
            headings['State (1)'] += [list2[5]]
            headings['ZIP (1)'] += [list2[6]]
            print('Property Data Scraped')

            try:
                # Getting Property data2.
                if not headings['Parcel (2)']:
                    data31 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseProperty_gvProperties"]/tbody/tr[2]/td/table').get_attribute(
                        'outerHTML')

                    # Appending Property data2 to dict.
                    list3 = pd.read_html(data31)
                    list4 = list3[0][1]
                    headings['Parcel (2)'] += [list4[0]]
                    headings['Street Number (2)'] += [list4[1]]
                    headings['Street Name(2)'] += [list4[2]]
                    headings['Address Line 2 (2)'] += [list4[3]]
                    headings['City (2)'] += [list4[4]]
                    headings['State (2)'] += [list4[5]]
                    headings['ZIP (2)'] += [list4[6]]
                else:
                    pass

                # Getting Property data3.
                if not headings['Parcel (3)']:
                    data32 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseProperty_gvProperties"]/tbody/tr[3]/td/table').get_attribute(
                        'outerHTML')

                    # Appending Property data3 to dict.
                    list5 = pd.read_html(data32)
                    list6 = list5[0][1]
                    headings['Parcel (3)'] += [list6[0]]
                    headings['Street Number (3)'] += [list6[1]]
                    headings['Street Name(3)'] += [list6[2]]
                    headings['Address Line 2 (3)'] += [list6[3]]
                    headings['City (3)'] += [list6[4]]
                    headings['State (3)'] += [list6[5]]
                    headings['ZIP (3)'] += [list6[6]]
                else:
                    pass

                # Getting Property data4.
                if not headings['Parcel (4)']:
                    data33 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseProperty_gvProperties"]/tbody/tr[4]/td/table').get_attribute(
                        'outerHTML')

                    # Appending Property data4 to dict.
                    list7 = pd.read_html(data33)
                    list8 = list7[0][1]
                    headings['Parcel (4)'] += [list8[0]]
                    headings['Street Number (4)'] += [list8[1]]
                    headings['Street Name(4)'] += [list8[2]]
                    headings['Address Line 2 (4)'] += [list8[3]]
                    headings['City (4)'] += [list8[4]]
                    headings['State (4)'] += [list8[5]]
                    headings['ZIP (4)'] += [list8[6]]
                else:
                    pass

                # Getting Property data5.
                if not headings['Parcel (5)']:
                    data34 = driver.find_element(By.XPATH,
                                                 '//*[@id="SheetContentPlaceHolder_caseProperty_gvProperties"]/tbody/tr[5]/td/table').get_attribute(
                        'outerHTML')

                    # Appending Property data5 to dict.
                    list9 = pd.read_html(data34)
                    list10 = list9[0][1]
                    headings['Parcel (5)'] += [list10[0]]
                    headings['Street Number (5)'] += [list10[1]]
                    headings['Street Name(5)'] += [list10[2]]
                    headings['Address Line 2 (5)'] += [list10[3]]
                    headings['City (5)'] += [list10[4]]
                    headings['State (5)'] += [list10[5]]
                    headings['ZIP (5)'] += [list10[6]]
                else:
                    pass

            except NoSuchElementException or Exception as E:
                print('No More Property Data/ All data Scraped')
                pass

            # Going to Docket page
            driver.find_element(By.XPATH,
                                '//*[@id="SheetContentPlaceHolder_caseHeader_lbDocket"]').click()
            time.sleep(8)

            for num in range(2, 500):
                try:
                    # Filing Date data extraction
                    filing_date = driver.find_element(By.XPATH,
                                                      f'//*[@id="SheetContentPlaceHolder_caseDocket_gvDocketInformation"]/tbody/tr[{num}]/td[1]').text
                    print(filing_date)
                    headings[f'Docket Filing Date ({num - 1})'] = [filing_date]

                    # Docket Party data extraction
                    Docket_party = driver.find_element(By.XPATH,
                                                       f'//*[@id="SheetContentPlaceHolder_caseDocket_gvDocketInformation"]/tbody/tr[{num}]/td[2]').text
                    print(Docket_party)
                    headings[f'Docket Party ({num - 1})'] = [Docket_party]

                    # Docket Type data extraction
                    Docket_Type = driver.find_element(By.XPATH,
                                                      f'//*[@id="SheetContentPlaceHolder_caseDocket_gvDocketInformation"]/tbody/tr[{num}]/td[3]').text
                    print(Docket_Type)
                    headings[f'Docket Type ({num - 1})'] = [Docket_Type]

                    # Docket Description data extraction
                    Docket_Description = driver.find_element(By.XPATH,
                                                             f'//*[@id="SheetContentPlaceHolder_caseDocket_gvDocketInformation"]/tbody/tr[{num}]/td[4]').text
                    print(Docket_Description)
                    headings[f'Docket Description ({num - 1})'] = [Docket_Description]

                    try:
                        # Docket Image Link extraction
                        Docket_image = driver.find_element(By.XPATH,
                                                           f'//*[@id="SheetContentPlaceHolder_caseDocket_gvDocketInformation"]/tbody/tr[{num}]/td[5]/a').get_attribute(
                            'href')

                        print(Docket_image)
                        headings[f'View Image ({num - 1})'] = [Docket_image]

                    except NoSuchElementException or Exception as E:
                        Docket_image = ''
                        headings[f'View Image ({num - 1})'] = [Docket_image]

                except NoSuchElementException or Exception as E:
                    print(f'Error: NoSuchElementException \n No More Docket Data')
                    for key in headings:
                        if not headings[key]:
                            headings[key] = ['']
                    all_data = pd.DataFrame.from_dict(headings)
                    print(all_data)
                    # Try Except condition not to get FileNotFoundError.
                    try:
                        # Opening Court cases data Excel file if present, and appending dataframe to it.
                        with pd.ExcelWriter('Court_cases_data.xlsx', mode='a', engine='openpyxl',
                                            if_sheet_exists="overlay") as writer:
                            all_data.to_excel(writer, index=False, header=False,
                                              startrow=writer.sheets['Sheet1'].max_row)
                    except FileNotFoundError:
                        # Writing new Court cases data file if not present in above code. Appending headers list also.
                        with pd.ExcelWriter('Court_cases_data.xlsx', mode='w') as writer:
                            all_data.to_excel(writer, header=True, engine='openpyxl', index=False)
                    print("appended data into Court_cases_data.xlsx file")
                    break

            case_number += 1
            if case == case2:
                print(f"No more cases agaist {date} zip code.")
                break
            else:
                pass
        except NoSuchElementException or TimeoutError or ConnectionError or ConnectionRefusedError or Exception:
            try: 
                driver.quit()
                time.sleep(2)
                options = webdriver.ChromeOptions()
                proxies = chrome_proxy()
                driver = webdriver.Chrome(
                options=options, seleniumwire_options=proxies)
                driver.get(url)
                time.sleep(10)
                # Find and select the "Foreclosure" option
                driver.find_element(By.XPATH, '//*[@id="SheetContentPlaceHolder_rbCivilForeclosure"]').click()
                # Wait for page loading
                time.sleep(15)
                # Terms agreement selecting yes
                driver.find_element(By.XPATH, '//*[@id="SheetContentPlaceHolder_btnYes"]').click()
                time.sleep(15)
                # Again Find and select the "Foreclosure" option
                select = driver.find_element(By.XPATH, '//*[@id="SheetContentPlaceHolder_rbCivilForeclosure"]')
                select.click()
                select.click()
                select.click()
                select.click()
                select.click()
                # Wait for page loading
                time.sleep(10)
            except:
                pass
                    
            
            if case == case2:
                print(f"No more cases agaist {date} zip code.")
                break
            else:
                pass

        driver.get(url)
        time.sleep(10)

    driver.get(url)
    end_date_string += 1
    time.sleep(10)
print("\n \n \n All data scraped against all zip code. please find output generated file.")
driver.quit()
#### The End of code
