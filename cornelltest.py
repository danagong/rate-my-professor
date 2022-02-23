from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time
import csv

#driverLocation = '/Users/danagong/Documents/WebDriver' #if windows
# driver = webdriver.Chrome(driverLocation) 

# open a csv file and write in the columns we want. 
# If you're running this I would reccmend renaming it so you don't overwrite the original file.
csv_file = open('cornell.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['professor', 'content', 'class_level','rating', 'date'])

# most of these are disabling/closing popups
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu"); 


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=298")

# passing in the url we want it to look at
# in this script we don't actually get anything from the main page, but there might be some useful data there
driver.get("https://www.ratemyprofessors.com/campusRatings.jsp?sid=298")

# using the wait command to close a cookie popup that the previous options didn't account for
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='big-close ccpa-close']"))).click()


button = driver.find_element_by_xpath('//div[@class = "content"]')


prof_urls = ['https://www.ratemyprofessors.com/ShowRatings.jsp?tid=202231', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=261710', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1705832',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=172666', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=56605',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=268048', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=357392', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=250633',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=203512', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1414895', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2168708',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=351709', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2290792', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=153936',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2109847', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2234527', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=136263',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2209130', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=154695','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2254913',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=180783', 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=351711','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2239807',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=64520','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=284612','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=363627',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=521940','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=809456','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1547176',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2284064','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1398171','https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2258736',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2260768'
     ]
prof_names = ['Daisy Fan','David Gries','Walker White','Graeme Bailey', 'David Schwartz','John Hopcroft',
'Charles Van Loan', 'Ramin Zabih', 'Emin Gun Sirer', 'Ashutosh Saxena', 'Michael George', 'Fred Schneider', 'Nate Foster', 'Dexter Kozen',
'Anne Bracy', 'Lorenzo Alvisi', 'Jon Kleinberg','Rachit Agarwal', 'Bart Selman', 'Kilian Weinberger','Andrew Myers', 'Ken Birman','Michael Clarkson',
'Donald Greenberg','Eva Tardos', 'Paul Chew', 'Claire Cardie','Thorsten Joachims', 'Hakim Weatherspoon','Bharath Hariharan','Robert Kleinberg',
'Haym Hirsh','Immanuel Trummer']

count = 0
for url in prof_urls:
    # using time.sleep just ensures that the entire page can load so selenium can find everything.
    time.sleep(2)
    # go to each of the urls in our list
    driver.get(url)

    # keeping track of our professor names
    name = prof_names[count]
    print(name)
    # print(url)

    # printing out the overall number of ratings for each professor.
    num_ratings = driver.find_element_by_xpath("//li[@class='TeacherRatingTabs__StyledTab-pnmswv-2 bOzrdx react-tabs__tab--selected']").text.split(" ")[0]
    # print(num_ratings)

    # calcuate how many load more buttons we need to click
    button_clicks = (int(num_ratings) - 20)/10

    
    for i in range(int(button_clicks)):
        button = driver.find_element_by_xpath('//button[@class = "Buttons__Button-sc-19xdot-1 PaginationButton__StyledPaginationButton-txi1dr-1 gjQZal"][@type="button"]')
        button.click()
        time.sleep(3)
    

    reviews = driver.find_elements_by_xpath('//div[@class = "Rating__StyledRating-sc-1rhvpxz-1 jcIQzP"]')




    for ind, review in enumerate(reviews):
    
		# initializing the dict
        review_dict = {}
        # if (review.find_element_by_xpath('.//div[@class="RatingHeader__StyledClass-sc-1dlkqw1-2 gxDIt"]')== True):
            # class_level = review.find_element_by_xpath('.//div[@class="OnlineCourseLogo__StyledLogo-qyf3kt-0 gemNec"]')[1].text
        # class_level = review.find_element_by_xpath('.//div[@class="RatingHeader__StyledClass-sc-1dlkqw1-2 gxDIt"]')[1].text

       
        class_level = review.find_element_by_xpath('.//div[@class="RatingHeader__StyledClass-sc-1dlkqw1-2 gxDIt"]').get_attribute("innerText")
        score = review.find_element_by_xpath('.//div[@class="RatingValues__StyledRatingValues-sc-6dc747-0 gFOUvY"]').get_attribute("innerText")
    
        # print(class_level)

        content = review.find_element_by_xpath('.//div[@class = "Comments__StyledComments-dzzyvm-0 gRjWel"]').text
        date = review.find_element_by_xpath('.//div[@class="TimeStamp__StyledTimeStamp-sc-9q2r30-0 bXQmMr RatingHeader__RatingTimeStamp-sc-1dlkqw1-3 BlaCV"]').get_attribute("innerText")
        # print(content)

        # assigning and writing values to our columns
        review_dict["professor"]= prof_names[count]
        review_dict["content"] = content
        review_dict["class_level"] = class_level
        review_dict["score"] = score
        review_dict["date"] = date
        writer.writerow(review_dict.values())
   
    count = count + 1
