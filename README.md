# KeywordFinder
A Python Program design to find the number of occurrences of keywords in a given text 

Project started: September 26th, 2019

**Goal:** To read a student's essay response and find how many times they used specific keywords pre-determined by an instructor. These keywords are to be grouped into a number of groups and the student must use keywords from each group X number of times for the essay response to be acceptable. A GUI is to be implemented for ease of access of the instructor or person assessing the text.

**Update - Version 3.0 - Nov 19th, 2019:**
---
Fixed bug where text would not be entered at the bottom of the scrollable text field.
Text field where messages are inputted back and forth is now locked from editing.
Version 3.0 - with exe folder contains an .EXE file for running the program without python or dependencies installed. This was created with pyinstaller.
Added README.txt file with brief explanation of file system - *To be improved in Version 3.1.*

**Update - Version 2.5 - Nov 16th, 2019:**
---
Fixed bug with manual entry of keyword categories. Program now adds the results of each run to the CSV file instead of overwriting. 
Also now prints whether the analyzed text passed each keyword category threshold and whether it passed all thresholds (by using the AND operator). 
Documentation has also been improved for this update.

**Update - Version 2.1 - Nov 2nd, 2019:**
---
Program now can read and analyze text from txt files and can decifer multiple delimeted lines to provide statistics for each one individually.
Keyword Categories now have a threshold value of matches that the analyzed text must meet in order to "Pass". 
Program also can keep looping for manual text entry so that the user can continue analyzing text without having to completely reset each time.
Statistics from each run are currently lost when program is closed, this will be *accounted for in version 2.5.*

**Update - Version 2.0 - Oct 29th, 2019:**
---
GUI added for ease of use. GUI created using Python's Tkinter module.
Program now allows user to define names for the keyword categories.
Program also accepts either manual entry of keyword categories or accepts them from a text file ("keywords.txt").
Text to be analyzed must be manually inputted through the GUI but *Version 2.1 will account for this*.

**Update - Version 1.1 - Oct 5th, 2019:**
---
Added user input functionality for selction of keywords
This is done using Python's built-in input() function.
The user can now enter how many keyword categories they would like and then the corresponding keywords for each of those categories.
At each point the user enters something, the input is reprinted on the screen and the program confirms it is correct.
Text to be analyzed is still read from text file.
