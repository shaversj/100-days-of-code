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