### Day 1: September 18, 2018

**Today's Focus**: Reading txt files in Python

My answer to a code challenge from [Practice Python](http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html)

**Details**:

- Explored various ways to read a file in Python

- I used Counter from the Collections module to calculate the number of images in the file. 

**Link to work**: [Github](days/01)

----
### Day 2: September 19, 2018

**Today's Focus**: Web scraping using Python and Beautiful Soup

**Details**:

- In preperation for a future project, I reviewed several tutorials and learned the basics for how to scrape websites using beautiful soup.

**Link to work**: [Github](days/02)

----
### Day 3: September 20, 2018

**Today's Focus**: Created a script to backup and clear out my downloads directory.

**Link to work**: [Github](days/03)

----
### Day 4: September 21, 2018

**Today's Focus**: Python coding challenge that required me to import voting results from a csv file. My task was to create a Python script that analyzes the votes and calculates the winner.

**Link to work**: [Github](days/04)

----
### Day 5: September 22, 2018

**Today's Focus**: Finished completing the Python coding challenge from yesterday. I solved the challenge using two different solutions.

- I initially iterated over a for loop and += 1 to calculate the totals. 
- I then imported Counter from the collections module to return the same results. Counter required me to use a lot less code then what I used at first. Counter returns a dictionary and calculates the totals very easily.

**Link to work**: [Github](days/04)

----
### Day 6: September 23, 2018

**Today's Focus**: I followed an [AWS Blog Post](https://aws.amazon.com/blogs/aws/new-amazon-connect-and-amazon-lex-integration/) and successfully recreated a workflow with Amazon Connect, Lex, Lambda and DynamoDB. 

- I learned how to debug an AWS Lambda fucntion by enabling DEBUG level logging, which allowed me to view the logs with AWS Cloudwatch.
- I also learned how to use Amazon Connect and Amazon Lex.

**Link to work**: [Github](days/06)

----
### Day 7: September 24, 2018

**Today's Focus**: Played around with the Javascript SPA from the [AWS Blog Post](https://aws.amazon.com/blogs/aws/new-amazon-connect-and-amazon-lex-integration/) and enabled Twilio integration with the Amazon Lex bot that I created. The SPA calls DynamoDB directly and uses Amazon Cognito to manage the access to the database.

**Link to work**: [Github](days/06)

----
### Day 8: September 25, 2018

**Today's Focus**: Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

**Link to work**: [Github](days/08)

----
### Day 9: September 26, 2018

**Today's Focus**: I continued to work on the code challenge from yesterday. I used doctest to test the script that I made yesterday. Doing so allowed me to see several use cases that I did not account for. My script initially counted a word twice depending on if it contained a capital letter or punctuation mark. Armed with the new information, I proceeded to add a function that removed all of the punctuation from the string before calling the function that counts the number of words. 

**Link to work**: [Github](days/08)

----
### Day 10: September 27, 2018

**Today's Focus**: The goal is to design, implement and test a program which allows the user to search a subset of the books which have appeared in the New York Times best seller lists. The program requires me to solve the problem by using file processing, lists and strings in Python.

**Link to work**: [Github](days/10)

----
### Day 11: September 28, 2018

**Today's Focus**: I added 3 new functions and finished the code challenge from yesterday.

**Link to work**: [Github](days/10)

----
### Day 12: September 29, 2018

**Today's Focus**: Worked on a GDP and Income related project from the [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/). Learned why you should add try/exception statements when opening a file.

**Link to work**: [Github](days/12)

----
### Day 13: September 30, 2018

**Today's Focus**: Continued working on the GDP and Income related project. I used the string format method to print out a large table with several columns. The process is easy but very time consuming. I promised myself that I would never do it again.

I also added a function that finds the max value in a dictionary. This was a little tricky because dictionaries are not typically sorted. I was able to find the max value by using a list comprehension and the sorted function.

**Link to work**: [Github](days/12)

----
### Day 14: October 1, 2018

**Today's Focus**: I learned how to use Pytest today. Using Pytest and TDD helped me to see gaps in my code. I created a testcase for a script that checks to see if a string is a palindrome.

**Link to work**: [Github](days/14)

----
### Day 15: October 2, 2018

**Today's Focus**: Played around with requests and the OpenWeather API.

**Link to work**: [Github](days/15)

----
### Day 16: October 3, 2018

**Today's Focus**: Completed three code challenges that were associated with string manipulation.

**Link to work**: [Github](days/16)

----
### Day 17: October 4, 2018

**Today's Focus**: Began working on a document retrieval project from [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/06_Dictionaries/DocRetrieval/)

**Link to work**: [Github](days/17)

----
### Day 18: October 5, 2018

**Today's Focus**: Continued to work on a document retrieval project from [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/06_Dictionaries/DocRetrieval/). Started to learn about how to add sets as values in a dictionary.

**Link to work**: [Github](days/17)

----
### Day 19: October 6, 2018

**Today's Focus**: Completed a code challenge from [Pybites](https://codechalleng.es/bites/7/) I learned enough about datetime to know that I should import a library if I need to do a lot of work with datetime. 

**Link to work**: [Pybites](https://codechalleng.es/bites/7/)

----
### Day 20: October 7, 2018

**Today's Focus**: Completed a code challenge that required me to find an element that appears once in an array where every other element appears more than once. This was the first time that I can recall using the list.count() method.

The method count() returns count of how many times obj occurs in list.

----
### Day 21: October 8, 2018

**Today's Focus**: Created my first class using Python. I will be using the  Google Maps API to get a route between cities. [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/08_ClassDesign/GoogleMap/Project11.pdf)

**Link to work**: [Github](days/21)

----
### Day 22: October 9, 2018

**Today's Focus**: I continued working on the Google Maps API project. I created and played around with the __str__ and __repr__ methonds.  [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/08_ClassDesign/GoogleMap/Project11.pdf)

**Link to work**: [Github](days/21)

----
### Day 23: October 10, 2018

**Today's Focus**: I continued working on the Google Maps API project. I added a method to the Tour class called distance. I ended up using the params keyword argruement of the requests module to build the url for the API call.   [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/08_ClassDesign/GoogleMap/Project11.pdf)

**Link to work**: [Github](days/21)

----
### Day 24: October 11, 2018

**Today's Focus**: Continued working on the Google Maps API project. [MSU Python Projet Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/08_ClassDesign/GoogleMap/Project11.pdf)

**Link to work**: [Github](days/21)

----
### Day 25: October 12, 2018

**Today's Focus**: Completed 3 coding challenges on coderbyte.

----
### Day 26: October 13, 2018

**Today's Focus**: Completed coding excersise from the Practical Programming book. The excersise gave me the opportunity to practice creating classes.

**Link to work**: [Github](days/26)

----
### Day 27: October 14, 2018

**Today's Focus**: Completed a coding challenge on coderbyte.

----
### Day 28: October 15, 2018

**Today's Focus**: Worked through a tutorial from a class on [Talkpython](https://training.talkpython.fm/courses/details/python-language-jumpstart-building-10-apps). I learned about static methods and how to model csv data using a Class.

----
### Day 29: October 16, 2018

**Today's Focus**: Started to work on a project to scrape the addresses from the Delaware County Sheriff Sale website. The goal is to plot the addresses on a map. Since the addresses are embedded within a table, I got a chance to use Beautiful Soup and Pandas to scrape the data from the website.

**Link to work**: [Github](days/29)

----
### Day 30: October 17, 2018

**Today's Focus**: Continued to work on my web scraping project. I used Geocoder to find the latitude and longitude of the addresses. I also used gmplot to plot the lat/lng on a map.

**Link to work**: [Github](days/29)

----
### Day 31: October 18, 2018

**Today's Focus**: Completed my web scraping project. I was able to write a program that scraped addresses from a website, retrieved the latitude and longitude for each address and plotted the coordinates on map.

**Link to work**: [Github](days/29)

----
### Day 32: October 19, 2018

**Today's Focus**: I added try/except clauses to my web scraping project.
**Link to work**: [Github](days/29)

----
### Day 33: October 20, 2018

**Today's Focus**: 
* Completed a coding challenge and added a try/except statement to the solution.
* I also completed a Coderbyte coding challenge.
  
**Link to work**: [Github](days/33)

----
### Day 34: October 21, 2018

**Today's Focus**: 
* Completed 2 code challenges on coderbyte.
  
----
### Day 35: October 22, 2018

**Today's Focus**: I learned how to read and manipulate excel files by using openpyxl. I read and used a script from "Automate the Boring Stuff" to reinforce what I had learned from reading online.

**Link to work**: [Github](days/35)

----
### Day 36: October 23, 2018

**Today's Focus**: Played around with [gspread](https://github.com/burnash/gspread), which is a Python library that gives you the ability to interact with the Google Sheets API.

**Link to work**: [Github](days/36)

----
### Day 37: October 24, 2018

**Today's Focus**: I added three new functions to my project that is using gspread to interact with the google sheets api. One of the functions required me to create a dictionary with a list as the value. I also used calender module from the standard library for the first time.

**Link to work**: [Github](days/36)

----
### Day 38: October 25, 2018

**Today's Focus**: Updated the main() section of my gspread project. I got more practice with functions and try/except statements.

**Link to work**: [Github](days/36)

----
### Day 39: October 26, 2018

**Today's Focus**: I learned a lot today by playing with Flask, Twilio, Zappa and Python. Zappa is very easy to use and allows you to push web based applications to AWS using by using a combination of AWS Lambda and AWS API Gateway. I setup Twilio to call the URL that Zappa provides to you after it finishes deploying your resources.

**Link to work**: [Github](days/39)

----
### Day 40: October 27, 2018

**Today's Focus**: I used Plotly and Mapbox to create a scatterplot of addresses.

**Link to work**: [Github](days/40)

----
### Day 41: October 28, 2018

**Today's Focus**: I used textblob to parse an article from CNN. TextBlob is a library for natural language processing, or NLP. I retrieved noun phrases and perform sentiment anlaysis on the txt.

**Link to work**: [Github](days/41)

----
### Day 42: October 29, 2018

**Today's Focus**: Created a new repository and created documentation for my web scraping project.

**Link to work**: [Github](sheriff-sale-web-scraper)

----
### Day 43: October 30, 2018

**Today's Focus**: I walked through a few tutorials for the argparse module, which is the recommended command-line parsing module in the Python standard library. I was surprised how easy argparse made it to create a cli program.

**Link to work**: [Github](days/43)

----
### Day 44: October 31, 2018

**Today's Focus**: I used argparse and shutil to create a CLI program that copies a file from a source to a destination directory.

**Link to work**: [Github](days/44)

----
### Day 45: November 1, 2018

**Today's Focus**: Explored additional use cases with shutil. I updated my cp cli script to be able to copy folders as well as files.

**Link to work**: [Github](days/44)

----
### Day 46: November 2, 2018

**Today's Focus**: Played around with tutorials and code that described the difference between linear search and binary search.
* Time Complexity of Linear Search is O(n), where n is the number of elements in the list.
* Time Complexity of Binary Search is O(log n).

**Link to work**: [Github](days/46)

----
### Day 47: November 3, 2018

**Today's Focus**: Worked through a tutorial that allowed me to use Python, IFTT, and Telgram. 

**Link to work**: [Github](days/47)

----
### Day 48: November 4, 2018

**Today's Focus**: Played with a few different libraries that give you the ability to easily print data into a table. I settled on a library called tabulate. It was easy to use, and gave me the ability to print from a iterable. 

**Link to work**: [Github](days/48)

----
### Day 49: November 5, 2018

**Today's Focus**: Completed two challenges on Coderbyte.

----
### Day 51: November 7, 2018

**Today's Focus**: Completed a project euler coding challenge.

----
### Day 52: November 8, 2018

**Today's Focus**: I started to work on creating a hangman game using Python.

**Link to work**: [Github](days/52)

----
### Day 53: November 9, 2018

**Today's Focus**: Continued to work on hangman game.

**Link to work**: [Github](days/52)

----
### Day 54: November 10, 2018

**Today's Focus**: Worked through a tutorial that used Pygal to create a bar chart.

**Link to work**: [Github](days/54)

----
### Day 55: November 11, 2018

**Today's Focus**: Walked through a few tutorials in my Learning Python book. I learned how default, keyword, and keyword-only arguments are used in Python functions.

**Link to work**: [Github](days/55)

----
### Day 56: November 12, 2018

**Today's Focus**: Played around with a data set that I received from data.gov. I used csv.DictReader to read the data.

**Link to work**: [Github](days/56)

----
### Day 57: November 13, 2018

**Today's Focus**: Refactored some of the code associated with the data set that I received from data.gov. Doing so allowed me to practice list comprehensions.

**Link to work**: [Github](days/57)

----
### Day 58: November 14, 2018

**Today's Focus**: Played around with Flask-Restful.

**Link to work**: [Github](days/58)

----
### Day 59: November 15, 2018

**Today's Focus**: Played around with jsonify and updated the API to build a dictionary that gets added to the list. jsonify is then used to return the list that contains the dictionary. I was also able to figure out how to parse parameters to Flask when calling the API.

**Link to work**: [Github](days/58)

----
### Day 60: November 16, 2018

**Today's Focus**: Completed a coding challenge on CodingBat.

----
### Day 61: November 18, 2018

**Today's Focus**: Created a simple calculator with Python.

**Link to work**: [Github](days/61)

----
### Day 62: November 19, 2018

**Today's Focus**: Played around with recursive functions.

**Link to work**: [Github](days/62)

----
### Day 63: November 21, 2018

**Today's Focus**: Played around with Qt for Python.

**Link to work**: [Github](days/63)

----
### Day 64: November 23, 2018

**Today's Focus**: Read about Classes and Class inheritance. I created 3 classes to simulate the transactions associated with a banking application.

**Link to work**: [Github](days/64)

----
### Day 65: November 24, 2018

**Today's Focus**: Completed 3 coding challenges on HackerRank.

----
### Day 66: November 25, 2018

**Today's Focus**: I worked on a coding challenge from Pybit.es. I pulled tweets using Tweepy. I created a Class and several methods to parse the data. I learned how adding __len__ and __getitem__ gives me the ability to slice and iterate over the data.

**Link to work**: [Github](days/66)

----
### Day 67: November 26, 2018

**Today's Focus**: Completed a code challenge on HackerRank.

----
### Day 68: November 27, 2018

**Today's Focus**: Used Dataclasses and dataclass-csv to parse data from a csv. Using dataclasses and dataclass-csv is a lot easier than using named tuples to describe the data that is in a csv.

**Link to work**: [Github](days/68)

----
### Day 69: November 28, 2018

**Today's Focus**: Completed a coding challenge on Hackerank.

----
### Day 70: November 29, 2018

**Today's Focus**: Walked through a few tutorials related to Dash. I learned that Dash apps are composed two parts. The first part is the "layout" of the app and it describes what the application looks like. The second part describes the interactivity of the application.

* The following components are used to determine what the graph will look like:
    *  [dash_core_components](https://dash.plot.ly/dash-core-components)
    *  [dash_html_components](https://dash.plot.ly/dash-html-components)

**Link to work**: [Github](days/70)

----
### Day 72: December 1, 2018

**Today's Focus**: I completed a coding challenge from Pybit.es. I learned how to use pyperclip to copy contents from my clipboard.

https://pybit.es/codechallenge54.html

**Link to work**: [Github](days/72)

----
### Day 73: December 2, 2018

**Today's Focus**: Played around with ipdb, which is a Python Debugger. I used it to troubleshoot an issue I was having with a library that I was using.

**Link to work**: [Github](days/68)

----
### Day 74 December 3, 2018

**Today's Focus**: I used Python classes to begin creating a Rock, Paper Scissors game. I plan to complete the program over the next 2 days.

**Link to work**: [Github](days/74)

----
### Day 75 December 4, 2018

**Today's Focus**: Used Python dataclasses to create the classes for my Rock, Paper Scissor game. Learned how to use dataclass.field to to retrieve a value from a function that resides outside of the class. 

**Link to work**: [Github](days/74)

----
### Day 76 December 6, 2018

**Today's Focus**: Created a program that reads all of the data associated with 52 csv files and writes the data into one file. First time using the append 'a' keyword arguement with the open command.

**Link to work**: [Github](days/76)

----
### Day 77 December 7, 2018

**Today's Focus**: Through testing, I learned that my script would throw a UnicodeDecodeError when it encountered bad data, so I added a try/except statement to catch, print and pass the error. 

**Link to work**: [Github](days/76)

----
### Day 78 December 8, 2018

**Today's Focus**: Learned how to parse an excel-tabulated txt file with Python. 

**Link to work**: [Github](days/78)

----
### Day 79 December 10, 2018

**Today's Focus**: I started on a project that will result in the creation of an API Wrapper for the [International Space Station API](http://api.open-notify.org)

**Link to work**: [Github](days/79)

----
### Day 80 December 11, 2018

**Today's Focus**: Added an additional method to my API Wrapper project.

**Link to work**: [Github](days/79)

----
### Day 81 December 12, 2018

**Today's Focus**: Continued making updates to my API Wrapper project. I added an additional method and also learned how to manipulate instance variables when using dataclasses (__post_init__).

**Link to work**: [Github](days/79)

----
### Day 82 December 13, 2018

**Today's Focus**: I added an additional Class to my API Wrapper project.

**Link to work**: [Github](days/79)

----
### Day 83 December 14, 2018

**Today's Focus**: I added an additional method to my API Wrapper project.

**Link to work**: [Github](days/79)

----
### Day 84 December 15, 2018

**Today's Focus**: Learned how to correctly have a child dataclass inherit from a parent dataclass. When you have multiple classes trying to inherit from one another, you need to pay attention to which variables contain default values. 

If a class variable contains a default value, all variables after that must comtain a default value. 

**Link to work**: [Github](days/79)

----
### Day 85 December 16, 2018

**Today's Focus**: I'm working on a project from the Building Restful Python Web Services book. The project will give me the opportunity to learn how to build REST services using Flask-RESTful.

**Link to work**: [Github](days/85)

----
### Day 86 December 17, 2018

**Today's Focus**: Completed the Chapter 5 project from the Building Restful Python Web Services book. I learned how to create a CRUD API using Flask-RESTful. 
* Created a model to represent and persist messages
* Learned to configure serialization of messages into JSON representations
* Wrote classes that represent resources and process the different HTTP requests

**Link to work**: [Github](days/85)

----
### Day 87 December 18, 2018

**Today's Focus**: Learned how to use a more modern stack (flask-rest-api, marshmellow, webargs) to create a REST API.
* Using webargs and marshmellow reduced the amount of code that needed to be written.
* First time using a blueprint in Flask 
  
----
### Day 88 December 19, 2018

**Today's Focus**: Completd a coding challenge on HackeRank.