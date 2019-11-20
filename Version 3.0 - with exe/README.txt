Hello! Welcome to the README file for Keyword Finder version 3.0

0:Overview:
~~~~~~~~
This program's basic function is to analyze a given text entry for the number of occurences of groups of keywords.
This is done as follows:
2 inputs 
-Keyword Categories (can be multiple, in one file)
-Text to be analyzed (can be mulitple, in one file)
1 output
-The number of occurences of all of the words in the Keyword Category.

A "Keyword Category" is an object that has a name, a threshold, and a list of keywords associated with it.

-The name is the identifier for the Keyword Category.
-The threshold is the number of occurences of keywords in that category an analyzed text must meet in order to pass.
-The list of keywords is a comma seperated list of words (can be multiple word keywords) that the program is to find in the text entry.

1: Keyword Entry:
~~~~~~~~~~~~~~~~~

In the provided "keywords.txt" file, you are given the Keyword Category "Ways of Thinking"
It is formatted as follows:					   Inside text file
								  *****************************************************
Line 1: Name of Keyword Category      				-> Ways of Thinking
Line 2: Threshold of Keyword Category 				-> 2
Line 3: List of keywords associated with that Keyword Category  -> critical thinking,creative thinking,design thinking
								   ...
 								  *****************************************************

This is in the given text file, however the general form is:

Format of "keywords.txt"
***************************************
Category name 1
Category 1 threshold
Keyword 1,Keyword 2,Keyword 3
Category name 2
Category 2 threshold
Keyword 4,Keyword 5,Keyword 6
****************************************

Notice spacing between "," and "K" between each keyword! This allows for multi-word keywords.
There are to be no spaces on either side of the comma (,) but there can be spaces within the keyword.

For example:

This is acceptable 	->    A multi word keyword,Another multi word keyword

This is not		->    A multi word keyword , Another multi word keyword


The program will initially ask you if you would like to read keywords from a text file or manually enter them.
You may choose either option, but if you choose manual entry, you must pay attention to the formatting requested by the program.
You may also save the keywords entered manually to the text file for later use, as this is a function the program can do.
You may also edit the text file directly, however this is not recommended.


2: Text for Analysis Entry:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The text that is to be analyzed is stored in the text file "textToBeAnalyzed.txt".

In the provided file, you will see two long text entries seperated by a new line with an asterisk (*)
This is the delimeter character. It seperates two text entries that are being read into the program.


Assumed textToBeAnalyzed file format:
****************************************************************
Text that someone has wrote where we are looking for keywords...
*
Second piece of text that we are analyzing for keywords
****************************************************************

The text entry can also be split across multiple lines, as long as the asterisk is used to seperate two text entries.


3: CSV File Export:
~~~~~~~~~~~~~~~~~~~

The program can export the results of the text analysis to a CSV (Comma Seperated Value) file for further analysis using Excel. 
The program will export the number of occurences of all the keywords of the Keyword Category, not the occurences of each specific keyword.


Format of "textAnalysis.csv"
***********************************************************************************
Matches Category 1 (threshold1), Matches Category 2(threshold2), ..., Total Matches
Text 1 Matches, Text 1 Matches, ..., Text 1 TotalMatches
Text 2 Matches, Text 2 Matches, ..., Text 2 TotalMatches
**********************************************************************************
                
This will give us an excel file like this:
************************************************************************************************
| Matches Category 1 (threshold1) | | Matches Category (threshold2) |      | Total Matches |
----------------------------------- ---------------------------------      -----------------
     | Text 1 Matches C1  |              | Text 1 Matches C2  |        | Text 1 Total Matches |
     ----------------------              ----------------------        ------------------------
     | Text 2 Matches C1  |              | Text 2 Matches C2  |        | Text 2 Total Matches |
     ----------------------              ----------------------        ------------------------
************************************************************************************************
