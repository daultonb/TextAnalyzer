# KeywordFinder
A Python Program design to find the number of occurrences of keywords in a given text 

Project started: September 26th, 2019

**Goal:** To read a student's essay response and find how many times they used specific keywords pre-determined by an instructor. These keywords are to be grouped into a number of groups and the student must use keywords from each group X number of times for the essay response to be acceptable. A GUI is to be implemented for ease of access of the instructor or person assessing the text.

## 0: Updates/ What's New
---
### Update - Version 3.3 - Jan 10th, 2020:
Fixed issue with using capitalized keywords. All word comparisons are made in lowercase.

### Update - Version 3.2 - Jan 9th, 2020:
Improved documentation, added images and removed redundant files from directories. Changes to dialogues to reflect use of .csv files instead of .txt files for reading text. Created executable but file is 41MB (in zip file) and GitHub's upload limit is 25MB, so  am unable to upload. Program should be ready for testing.

### Update - Version 3.1 - Nov 23rd, 2019:
Added functionality to export to csv for usage with Canvas LMS. Now the analyzed text can be given a score and that score will be written to the csv in that assignment's column.
Pyinstaller did not like one of the modules imported for this so there is no EXE. - *To be fixed in version 3.2*

### Update - Version 3.0 - Nov 19th, 2019:
Fixed bug where text would not be entered at the bottom of the scrollable text field.
Text field where messages are inputted back and forth is now locked from editing.
Version 3.0 - with exe folder contains an .EXE file for running the program without python or dependencies installed. This was created with pyinstaller.
Added README.txt file with brief explanation of file system - *To be improved in Version 3.2.*

### Update - Version 2.5 - Nov 16th, 2019:
Fixed bug with manual entry of keyword categories. Program now adds the results of each run to the CSV file instead of overwriting. 
Also now prints whether the analyzed text passed each keyword category threshold and whether it passed all thresholds (by using the AND operator). 
Documentation has also been improved for this update.

### Update - Version 2.1 - Nov 2nd, 2019:
Program now can read and analyze text from txt files and can decifer multiple delimeted lines to provide statistics for each one individually.
Keyword Categories now have a threshold value of matches that the analyzed text must meet in order to "Pass". 
Program also can keep looping for manual text entry so that the user can continue analyzing text without having to completely reset each time.
Statistics from each run are currently lost when program is closed, this will be *accounted for in version 2.5.* 

### Update - Version 2.0 - Oct 29th, 2019:
GUI added for ease of use. GUI created using Python's Tkinter module.
Program now allows user to define names for the keyword categories.
Program also accepts either manual entry of keyword categories or accepts them from a text file ("keywords.txt").
Text to be analyzed must be manually inputted through the GUI but *Version 2.1 will account for this*.

### Update - Version 1.1 - Oct 5th, 2019:
Added user input functionality for selction of keywords
This is done using Python's built-in input() function.
The user can now enter how many keyword categories they would like and then the corresponding keywords for each of those categories.
At each point the user enters something, the input is reprinted on the screen and the program confirms it is correct.
Text to be analyzed is still read from text file.


## 1: Overview
---
This program's basic function is to analyze a given text entry for the number of occurences of groups of keywords.
This is done as follows:

#### Input files
- *"keywords.txt"* - Keyword Categories stored in a text document (can be multiple, **see 2 below**)
- *"canvasExport.csv"* - Canvas Gradebook Export to be updated with grades for essay quiz.
- *"quizExport.csv"* - Canvas Quiz Export to be used to collect the text to be analyzed.

#### Output
- The number of occurences of each of the keywords in the Keyword Categories.
- The pass/fail status (boolean) of the text for threshold of each Keyword Category.
- The pass/fail status (boolean) of ALL thresholds of Keyword Categories. ~This is denoted as a "passing" essay.
##### Output Files
- *"canvasImport.csv"* - Updated Canvas Gradebook file to be imported to Canvas to update grades based on program analysis.
- *"textAnalysis.csv"* - csv file containing the number of keywords from each Keyword Category used in each essay.

### Definitions
A **"Keyword Category"** is an object that has a *name, a threshold, and a list of keywords* associated with it.
- The **name** is the identifier for the Keyword Category.
- The **threshold** is the number of occurences of any keyword (or keywords) in that category an analyzed text must meet in order to "pass" that category.
- The **list of keywords** is a comma seperated list of words (can be multi-word keywords) that the program is to find in the text entry.

## 2: Keyword Entry
---
In the provided *"keywords.txt"* file, you are given the Keyword Category "Ways of Thinking"
It is formatted as follows:	
~~~
Line 1: Name of Keyword Category        -> Ways of Thinking
Line 2: Threshold of Keyword Category   -> 2
Line 3: List of keywords                -> critical thinking,creative thinking,design thinking
~~~

![keywords.txt](/README_imgs/Screenshots/keywords.txt.png?raw=true)

This is in the given text file, however the general form is:

Format of "keywords.txt"
```
Category name 1
Category 1 threshold
Keyword 1,Keyword 2,Keyword 3
Category name 2
Category 2 threshold
Keyword 4,Keyword 5,Keyword 6
```

**Notice spacing between "," and "K" between each keyword! This allows for multi-word keywords.
There are to be no spaces on either side of the comma (,) but there can be spaces within the keyword.**

For example:

This is acceptable 	->    `A multi word keyword,Another multi word keyword`

This is not		->    A multi word keyword , Another multi word keyword


The program will initially ask you if you would like to read keywords from a text file or manually enter them.
You may choose either option, but if you choose manual entry, you must **pay attention to the formatting** requested by the program.
You may also save the keywords entered manually to the text file for later use, as this is a function the program can do.
You may also edit the text file directly, however this is not recommended.
**All keywords will be changed to lowercase upon entry and compared with a lowercase version of the text to be analyzed.** 
This is to allow keywords to be found both anywhere in a sentence.

## 3: Using Canvas Quiz Exports to Analyze Responses
---
The quiz responses from a Canvas LMS quiz should be renamed *"quizExport.csv"* and placed in the directory **"/Version X.x/canvas/"**.

The program will ask if you have a .csv file from Canvas to read in and will be looking for this file by name, so ensure that it is spelled correctly and placed in the correct location.
The program will then ask what the **"unique string"** of the Quiz question is. This is to find the .csv file column containing the student responses.
This is necessary to ensure the text read from the .csv file is only the text that contains student responses ("essays") and not the wrong question or any of the other information canvas stores in the quiz export file. 
In the example below, I used the unique string **"Reflection Question"** at the beginning of the question.

Unique String in CSV file (opened in Excel):
![uniqueStringCSV](/README_imgs/Screenshots/UniqueStringinCSV.png?raw=true)

Unique String entered in program:
![uniqueString](/README_imgs/Screenshots/UniqueString.png?raw=true)

Once the file has been read in to the program, it will show the text repsonses that have been read in. Please read them to ensure they are correct and as expected.

## 4: Text Analysis CSV File
---
The program can generate a csv file with the number of keywords used in each Keyword Category that can be further analyzed in Excel. The program will ask if y ou would like to "save these statistics to a csv file". This file  can be found in the directory /Version X.x/lib/"textAnalysis.csv"

Format of *"textAnalysis.csv"*
```
Matches Category 1 (threshold1), Matches Category 2(threshold2), ..., Total Matches
Student 1 Matches, Student 1 Matches, ..., Student 1 TotalMatches
Student 2 Matches, Student 2 Matches, ..., Student 2 TotalMatches
```

This will give us a **excel file** formatted like this:

| Matches Category 1 (threshold1)| Matches Category 2 (threshold2) |...| Total Matches |
| ------ | ------ | ------ |------ |
 |Student 1 Matches Category 1  |Student 1 Matches Category 2  |...|Student 1 Total Matches |
 |Student 2 Matches Category 1  |Student 2 Matches Category 2  |...|Student 2 Total Matches |
 
 Example:
 ![textAnalysis](/README_imgs/Screenshots/textAnalysis.png?raw=true)

## 5: Canvas Gradebook Updates using CSV File 
---
The program can also write grades for the responses it has analyzed. To do this, two .csv files will be used. For the first file (*"canvasExport.csv"*) you must export a .csv file from your canvas gradebook. This can be done by going to the grades page on canvas and clicking Actions->Export
Exporting in Canvas:
 ![canvasExport](/README_imgs/Screenshots/CanvasExport.png?raw=true)

Once you have the Canvas Gradebook Export, **you must rename it to** ***"canvasExport.csv".*** If the file is not renamed, the program will not be able to read it. 
Once you have renamed the file, put it in the directory /Version X.x/canvas. This is where the program will be looking for it.

Exported .csv File renamed and opened in Excel:
 ![canvasExportCSV](/README_imgs/Screenshots/canvasExportCSV.png?raw=true)

The second .csv file (*"canvasImport.csv"*) will be generated by the program. It is identical to the export file (from above) with but the grades will be updated for the quiz. This will be done while the program is running.
When running the program, it will ask for a assignment name to add the grades under, this should be the name of the quiz where the essay responses came from.

Note: This program was designed to give the essay responses a pass/fail grade. Since this is the case, the grades outputted to the .csv gradebook file will be:
- "1" for pass
- "0" for fail
Canvas Import .csv File opened in Excel:
 ![canvasImportCSV](/README_imgs/Screenshots/canvasImportCSV.png?raw=true)
 
 To import this in Canvas, go to the grades page and click Actions->Import
![canvasImport](/README_imgs/Screenshots/CanvasImport.png?raw=true)
