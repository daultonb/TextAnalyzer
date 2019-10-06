'''
keywordFinder version 1.1~ See readME for changes
'''
import time

def textfile_readText(filepath):
    '''
    This code reads a textfile into a String variable so that we can use it for analysis later.
    '''
    file = open(filepath, "r")
    text = file.read()
    return text
def textfile_readKeywords(filepath):
    '''
    This method reads in the keywords from the textfile at the filepath specified.
    keywords should be written in the file as follows:
    problem solving,problem finding
    No space before or after comma but space between words is okay
    Keywords should not have hyphens, apostrophes, or and other symbolism (See findKeywords)
    The output of this method is a 2D-array of keywords.
    They are grouped by being on the same line in the text file.
    '''
    file = open(filepath, "r")
    #empty string * 5 because we have 5 "groups" of keywords
    keywords = [dict for x in range(5)]
    for i in range(0,5):
        #this line is what reads in the keywords. First remove new line character (\n)
        #then split the keywords by COMMAS *This allows two word keywords*
        keywords[i] = file.readline().replace('\n','').split(',')

    print('keywords:',keywords) #use this print statement to view the output
    return keywords
def createDictOfKeywords(keyword2DArray):
    '''
    In this function the input is the 2D-array of the keywords grouped by category
    The nested for loop adds all the keywords in every category to one array
    This is because dictionaries need the "keys" to be in a regular array not a 2D one.
    '''
    arrayOfKeywords = []
    for keywordGroup in keyword2DArray:
        for word in keywordGroup:
            arrayOfKeywords.append(word)
    #Now we make a dictionary of these keys each with an initial value of 0
    dictionary = dict.fromkeys(arrayOfKeywords, 0)

    print(dictionary)
    return dictionary
def findKeywords(text, keywordDictionary):
    '''
    re library contains the split method to split the text into regular English words.
    This means it removes commas, hyphens, apostrophes...etc.
                            ","     "-"     " ' "
    This means that the keywords cannot contain these characters
    OR something else must be used to split the text word-by-word (more difficult)
    '''
    import re
    #totalMatches keeps track of number of matches to any keyword
    totalMatches = 0
    #use the dictionary called to the method but copied because we will be updating it
    dictionary = keywordDictionary.copy()
    #this line splits the input text into individual words and puts that into an array
    #we also use the lowercase version to prevent capitalized letters from being skipped
    array = re.split('\W+',text.lower())

    for i in range(0,len(array)):
        #pulls next word to compare
        nextWord = array[i]
        #if we are not on the last word of the input text we can compare two words at a time
        #THIS IS IMPORTANT. This is how to find keywords like "design thinking"
        if i < len(array)-1:
            #next two words is just current word concatenated with a space and the next word
            nextTwoWords = nextWord+' '+array[i+1]
            #if the next two words are in our dictionary, they are a keyword
            if nextTwoWords in dictionary:
                #we increment the number at that keyword in the dictionary (so we can track KW count
                # for each word)
                dictionary[nextTwoWords] += 1
                totalMatches += 1
        '''this part just compares word by word.
            for this reason, one word keywords that are also contained in two word keywords are an issue
            Ex. "design thinking" and "thinking" cannot both be keywords because "design thinking" will be counted as 2 keywords
            because the text is being scanned for both single and double word keywords
            '''
        if nextWord in dictionary:
            #Same as above, if dictionary contains the word, it is a keyword.
            dictionary[nextWord] += 1
            totalMatches += 1
    #this lets us return both the dictionary (which now has how many times each keyword occurs)
    #and the total number of keywords.
    return dictionary, totalMatches

def ui_numKWCategories():
    '''
    This function asks the user how many keyword categories they would like
    and then waits for them to confirm it until returning
    '''
    input2 = 'n'
    while input2.lower() != 'y':
        input1 = input('How many keyword categories would you like?: ')
        input2 = input(f'You have requested {input1} categories, is this correct? (Y/N):')
    try:
        numKWCat = int(input1)
        return numKWCat

    except ValueError:
        print('Input invalid. Try again')
def ui_createDictionaries(numCat):
    '''
    This function takes the number of categories from the numKWCategories function and asks
    the user for the keywords in each category.
    This is a "Tricky" function because the list of keywords inputted by the user must match
    the EXACT syntax that the program is looking for.
    Here is the syntax:
    ex. Enter the keywords in category 1 seperated by commas and no spaces, then press enter to indicate
        the end of the list:
        -> keyword1,twoword keyword,three word keyword

        The spaces must ONLY be between the words in multi-word keywords and NOT before or after the commas.

        The function will confirm the users input at each point to aid in spelling mistakes, etc.
        Then at the end it will print out the array of key word dictionaries to confirm everything is correct.
        If the user confirms this final response, keywords will be analyzed.
    '''

    kw_dicts = []
    while True:
            for i in range(0, numCat):
                input2 = 'n'
                while input2.lower() != 'y':
                    input1 = input(f'Enter the keywords in category {(i+1)}, separated by commas and no spaces,'
                                   f' then press enter to indicate the end of list:\n')
                    input2 = input(f'The keywords in category {(i+1)} are "{input1}", is this correct? (Y/N):')
                try:
                    keywords = input1.split(',')
                    dict1 = dict.fromkeys(keywords, 0)
                    kw_dicts.append(dict1)

                except:
                    print('Entry error, try again')
            input3 = input(f'Your keywords are as follows: {kw_dicts}.\nIs this correct? (Y/N):')
            if input3.lower() == 'y':
                return kw_dicts
            else:
                kw_dicts = []

    return kw_dicts
def findAllKeywords(text, kwDictList):
    '''
    This function runs each category dictionary in our kwDictList array
    Through the exsisting findKeywords method
    It updates the count of the dictionary at each index
    and returns a count of keywords from that category
    which gets stored in the categoryCounts array.
    '''
    catgoryCounts = [0]*len(kwDictList)
    for i in range (0,len(kwDictList)):
       kwDictList[i], catgoryCounts[i] = findKeywords(text, kwDictList[i])

    return kwDictList, catgoryCounts


start = time.perf_counter_ns()
numCategories = ui_numKWCategories()
kwDictList = ui_createDictionaries(numCategories)

'''
These commented lines are from version 1.0 where all of the input came from text files- Archival comments.
As of this version, the text to be analyzed is still coming from a textfile, but this will likely change 
in version 2.0
'''
#keywordsArray is a 2D array of the keywords from the text file
#keywordsArray = textfile_readKeywords("C:/Users/dault/OneDrive/Desktop/DTQuiz_Keywords.txt")
#textFromFile will be a String holding the student's response
textFromFile = textfile_readText("C:/Users/dault/OneDrive/Desktop/DTQuiz_Q11.txt")
#keywordDict = createDictOfKeywords(keywordsArray)
#keywordsFound = findKeywords(textFromFile, keywordDict)


#This line prints the text input (to be analyzed)
#print(f'Text to be analyzed:{textFromFile}')

preproc = time.perf_counter_ns() #current time in nano seconds
preprocTimeMs = (preproc-start)/1000000 #1,000,000 ns in a ms
print(f'Pre-processing time: {preprocTimeMs}ms')

KWCountList, keywordCounts = findAllKeywords(textFromFile, kwDictList)
end = time.perf_counter_ns() #current time in nano seconds
exTime = (end-preproc)/1000000 #1,000,000 ns in a ms

print(f'List of keyword dictionary matches: {KWCountList}')
print(f'Total matches: {keywordCounts}')
print(f'Execution Time using preprocessed dictionary: {exTime}ms')
