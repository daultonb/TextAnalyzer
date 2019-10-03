def readFromTextFile(filepath):
    '''
    This code reads a textfile into a String variable so that we can use it for analysis later.
    '''
    file = open(filepath, "r")
    text = file.read()
    return text
def readKeywordsFromTextFile(filepath):
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
    keywords = [""]*5
    for i in range(0,5):
        #this line is what reads in the keywords. First remove new line character (\n)
        #then split the keywords by COMMAS *This allows two word keywords*
        keywords[i] = file.readline().replace('\n','').split(',')

    print(keywords) #use this print statement to view the output
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

import time
start = time.perf_counter_ns()
#textFromFile will be a String holding the student's response
textFromFile = readFromTextFile("C:/Users/dault/OneDrive/Desktop/DTQuiz_Q11.txt")
#keywordsArray is a 2D array of the keywords from the text file
keywordsArray = readKeywordsFromTextFile("C:/Users/dault/OneDrive/Desktop/DTQuiz_Keywords.txt")

#matchesArray = [0]*len(keywordsArray) #this is meant to count the keyword count from each category- Not implemented yet
keywordDict = createDictOfKeywords(keywordsArray)
preproc = time.perf_counter_ns() #current time in nano seconds
preprocTimeMs = (preproc-start)/1000000 #1,000,000 ns in a ms
print(f'Pre-processing time: {preprocTimeMs}ms')
keywordsFound = findKeywords(textFromFile, keywordDict)
end = time.perf_counter_ns() #current time in nano seconds
exTime = (end-preproc)/1000000 #1,000,000 ns in a ms
print(f'Dict of keyword matches: {keywordsFound[0]}')
print(f'Total matches: {keywordsFound[1]}')
print(f'Execution Time using preprocessed dictionary: {exTime}ms')
