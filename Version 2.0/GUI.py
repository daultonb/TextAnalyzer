import tkinter as tk
#import tkinter.scrolledtext as scrolledtext

version = 2.0
# window dimensions
HEIGHT = 600
WIDTH = 800

# global variables
# userEntries is a list that will hold all of the user's inputs via the entry field
# counter is a counter variable used for functions that are recursively called
#   (to check how many times we have called them)
# numCat is the total number of categories (stored at userEntries[0])
# STAGE is a variable that stores what part of the program we are at.
# It is used as a "switch variable" (See getResponse documentation)
# textToBeAnalyzed is the students's text entry response.
userEntries = []
counter = 0
numCat = 0
catNames = []
kw_dicts = []
STAGE = 0
textToBeAnalyzed = ''
manual = None


#Storing the count of keywords of that category doesn't work!

# classes
class KeywordCategory:
    def __int__(self):
        name = ''
        kwList = []
        keywords = {}

    def set_name(self, name):
        self.name = name

    def set_list(self, keywords):
        self.kwList = keywords.split(',')

    def set_list_fromFile(self, keywordList):
        self.kwList = keywordList

    def set_dict(self, keywordList):
        self.keywords = dict.fromkeys(keywordList, 0)


    def getName(self):
        return self.name

    def getKeyList(self):
        return self.kwList

    def getKeywords(self):
        return self.keywords


    def print(self):
        return f'[\nName:{self.getName()}, \nlist:{self.getKeyList()}, \ndict:{self.getKeywords()},\n]' #\ntotalCount:{self.getTotal()}\n]'

    def textFileOutput(self):
        keys = ''
        keylist = self.getKeyList()
        for i in range(0, len(keylist)):
            if i != len(keylist)-1:
                keys += keylist[i] + ','
            else:
                keys += keylist[i]
        retStr = '' + self.getName() + '\n' + keys + '\n'
        return retStr

# functions
def updateText(entry):
    '''
    This function updates the user's text upon the button being pressed or the Enter/ Return key being pressed
    The entry parameter is the text that is in the entry field at the time of button press/ enter key press
    If there is no text in the entry field, it is an invalid entry.
    If there is text, it is updated into the "convo" text field and the entry field is cleared
    The function then runs the getResponse() function which is what gets the next output of the computer.
    We pass the global variable STAGE into getResponse() so that it can determine which function to go to.
    '''
    global STAGE
    if len(entry) > 0:
        convo.insert(tk.INSERT, '\nUser: ' + entry)
        userEntries.append(entry)
        user.delete(0, tk.END)
        print(f'userEntries list: {userEntries}')
        getResponse(STAGE)
    else:
        convo.insert(tk.INSERT, "\nComp: I'm sorry, that entry was invalid.")

    convo.see('end')
def getResponse(STAGE):
    '''
    This function uses the global variable STAGE which this function
    uses to determine which part or "Stage" of the program we are on.
    - Initially we need to st up the keyword categories (stage = 0)
    - Then we create dictionaries from the keyword categories (stage = 1)
    - Then we get the input text that is going to be analyzed for keywords (stage = 2)
    - Then we find all of the keywords in the text. (stage = 3)
    '''
    if STAGE == 0:
        getKeywordCats()
    elif STAGE == 1:
        createDicts()
    elif STAGE == 2:
        getTextToAnalyze()
    elif STAGE == 3:
        findAllKeywords()
def getKeywordCats():
    '''
    This function gets all of the keywords and keyword categories from the user.
    The categories are stored as a custom type - KeywordCategories which can store the category name,
        keyword list (array), and keyword dictionary.
    kw_list is the list of all of the KeywordCategories.
    The global variables used are: userEntries, counter, numCat, kw_dicts, and STAGE
    - userEntries is the array that stores user input so we need this to check if the input was as expected
        and to account for yes or no (Y/N) responses.
    -counter is a counter variable, in this method it is used to count which category we are currently on.
    -numCat is the number of categories the user has requested.
    -kw_list is the list of all of the KeywordCategories.
    -STAGE is only used so that we can increment it at the end of this function
    '''
    global userEntries, counter, numCat, catNames, kw_dicts, STAGE, manual
    backUp = []
    count = len(userEntries)
    print('count:',count)
    # count=0 means start, ask how many categories
    if count == 0:
        convo.insert(tk.INSERT, '\nComp: Would you like to use keywords from text file or '
                                'manual entry?(Enter "text file" or "manual entry")')

    if count == 1 and manual is None:
        if userEntries[0].lower().__contains__('manual'):
            manual = True
        elif userEntries[0].lower().__contains__('text'):
            manual = False
    if manual:
        if count == 1:
            convo.insert(tk.INSERT, '\nComp: How many keyword categories would you like?')
        # count=2 means they entered a number of categories, confirm the entry
        elif count == 2:
            try:
                numCat = int(userEntries[-1])
                convo.insert(tk.INSERT, f'\nComp: You have requested {numCat} categories, is this correct? (Y/N)')
            except ValueError:
                convo.insert(tk.INSERT, "\nComp: The number of categories must be a number.")
                for i in range(0, len(userEntries)-1):
                    backUp.append(userEntries[i])
                userEntries.clear()
                userEntries = backUp.copy()
                count -= 1
                getResponse(STAGE)
        # count=2 means that we are now naming the first category
        # unless N was entered at count=1, then we reset the list and start again.
        elif count == 3:
            if userEntries[-1].lower() == 'y':  # If the user confirmed # categories, move on
                convo.insert(tk.INSERT, f'\nComp: Enter the name of category {(counter+1)}:')
                counter += 1
            elif userEntries[(count-1)].lower() == 'n':
                userEntries.remove(userEntries[-2])
                userEntries.remove(userEntries[-1])
                counter = 0
                getResponse(STAGE)
            else:
                convo.insert(tk.INSERT, "\nComp: I'm sorry, that entry was invalid.")
                userEntries.remove(userEntries[-1])
                getResponse(STAGE)
        # This is the iterative step of asking for a category name and then confirming it,
        # So we need a generic conditional statement
        # We are selecting the name of a category unless N was entered at the previous step,
        # then we save the list up to the last category name and restart this step
        elif 3 < count < (numCat*2)+3 and counter < numCat and count % 2 != 0:
            if userEntries[-1].lower() == 'y':  # If the user confirmed # of categories or category name, move on
                print(f'catnames: {catNames}')
                convo.insert(tk.INSERT, f'\nComp: Enter the name and threshold of category {(counter+1)}:')
                counter += 1
            elif userEntries[-1].lower() == 'n':
                for i in range(0, (count-2)):
                    backUp.append(userEntries[i])
                userEntries.clear()
                userEntries = backUp.copy()
                catNames.pop()
                counter -= 1
                getResponse(STAGE)
            else:
                convo.insert(tk.INSERT, "\nComp: I'm sorry, that entry was invalid.")
                for i in range(0, len(userEntries) - 1):
                    backUp.append(userEntries[i])
                userEntries.clear()
                userEntries = backUp.copy()
                catNames.pop()
                count -= 1
                getResponse(STAGE)

        # confirmation part of above step. Only accepts 'Y' or 'N' (lower or upper case)
        # Anything else will output "Invalid entry, try again"
        elif 3 < count < (numCat*2)+3 and counter <= numCat and count % 2 == 0:
            convo.insert(tk.INSERT, f'\nComp: Category {counter} is called "{userEntries[-1]}",'
                                    f' is this correct? (Y/N)')
            catNames.append(userEntries[-1])
        # When count = 2* the number of categories + 3 that means that the user has inputted
        # all categories and confirmed, lets confirm all categories to make sure.
        elif count == (numCat*2)+3 and counter >= numCat and userEntries[-1].lower() == 'y':
            c = 1
            for i in range(3, len(userEntries)-1, 2):
                convo.insert(tk.INSERT, f'\nComp: Category {c} is named "{userEntries[i]}",')
                c += 1
            convo.insert(tk.INSERT, f'\nComp: Are these entries all correct? (Y/N):')

        # last entry is incorrect, backup list and go back
        elif count == (numCat*2) + 3 and counter >= numCat and userEntries[-1].lower() == 'n':
            catNames.pop()
            for i in range(0, len(userEntries)-2):
                backUp.append(userEntries[i])
            userEntries.clear()
            userEntries = backUp.copy()
            counter = numCat-1
            getResponse(STAGE)
        elif count > (numCat * 2) + 3:  # at this point we are creating the dictionaries
            if userEntries[-1].lower() == 'y':
                for i in range(0, len(catNames)):
                    kw_dicts.append(KeywordCategory())
                counter = 0
                manual = None
                STAGE = 1
                getResponse(STAGE)
            elif userEntries[-1].lower() == 'n':
                backUp.append(userEntries[0])
                backUp.append(userEntries[1])
                userEntries.clear()
                userEntries = backUp.copy()
                counter = 0
                getResponse(STAGE)
            else:
                convo.insert(tk.INSERT, "\nComp: I'm sorry, that entry was invalid.")
                for i in range(0, len(userEntries) - 1):
                    backUp.append(userEntries[i])
                userEntries.clear()
                userEntries = backUp.copy()
                catNames.pop()
                count -= 1
                getResponse(STAGE)
        else:
            convo.insert(tk.INSERT, "\nComp: I'm sorry, that entry was invalid.")
            for i in range(0, len(userEntries) - 1):
                backUp.append(userEntries[i])
            userEntries.clear()
            userEntries = backUp.copy()
            catNames.pop()
            count -= 1
            getResponse(STAGE)
    if not manual:
        if count == 1:
            filename = 'keywords.txt'
            convo.insert(tk.INSERT, f'\nComp: Is the filename for the keywords: "{filename}"?(Y/N)')
        if count == 2 and userEntries[-1].lower() == 'y':
            '''
            Assumed keyword file format:
            ********************************
            category 1 name
            keyword 1,keyword 2,keyword 3
            category 2 name
            keyword 1,keyword 2,keyword 3
            ...etc
            ********************************
            '''
            import re
            filename = 'keywords.txt'
            file = open(filename, 'r')
            convo.insert(tk.INSERT, f'\nComp: From File:')
            catNames = []   # stores all category names
            kwlists = []    # stores all keywords

            # for each line in the file, first line is category name
            # second line is keyword list
            for line in file:
                line = line.replace('\n', '')
                catNames.append(line)
                kwlists.append(file.readline().replace('\n', ''))

            # for the number of categories we collected from the file,
            # set the names and lists and dicts up
            for i in range(0, len(catNames)):
                kw_dicts.append(KeywordCategory())
                kw_dicts[i].set_name(catNames[i])
                kw_dicts[i].set_list(kwlists[i])
                kw_dicts[i].set_dict(kw_dicts[i].getKeyList())
                convo.insert(tk.INSERT, f'\n{kw_dicts[i].print()}')

            convo.insert(tk.INSERT, f'\nComp: Is this correct? (Y/N)')

        if count == 3 and userEntries[-1].lower() == 'y':
            manual = None
            STAGE = 2
            getResponse(STAGE)

    convo.see('end')  # makes the scrollbar keep most recent messages on screen


def createDicts():
    '''
    This function creates the dictionaries of the keywords that were recieved in the getKeywordCats function
    This function uses the global variables: counter, kw_dicts, and STAGE
    -counter is used to count the category we are on, similar to in getKeywordCats
    -kw_dicts is the list (array) storing the KeywordCategory objects.
    -STAGE is updated when function is done so we can change outcome of getResponse()
    '''
    global counter, kw_dicts, STAGE, userEntries
    backUp = []
    # set up dictionaries by name
    for i in range(0, len(kw_dicts)):
        kw_dicts[i].set_name(catNames[i])

    # we are not in first run of function, and previous list has been confirmed
    if 0 < counter <= len(kw_dicts) and userEntries[-2].lower() == 'y':
        keywords = userEntries[-1]
        kw_dicts[(counter - 1)].set_list(keywords)
        kw_dicts[(counter - 1)].set_dict(kw_dicts[(counter - 1)].getKeyList())

    # User made an error with one of the keywords, retry
    if 0 < counter <= len(kw_dicts) and userEntries[-1].lower() == 'n':
        for i in range(0, len(userEntries)-2):
            backUp.append(userEntries[i])
        userEntries.clear()
        userEntries = backUp.copy()
        counter -= 1
        getResponse(STAGE)
    # If previous keywords have been confirmed, move on to next
    elif counter < len(kw_dicts) and userEntries[-1].lower() == 'y':
        convo.insert(tk.INSERT, f'\nComp: Enter the keywords of the category named "{kw_dicts[counter].getName()}"'
                                f' separated by commas and NO SPACES:')
        counter += 1
    # Check that keywords are right each time
    elif counter <= len(kw_dicts):
        convo.insert(tk.INSERT, f'\nComp: The keywords of the category named "{kw_dicts[(counter-1)].getName()}"'
                                f' are {kw_dicts[(counter-1)].getKeyList()}.\nComp: Is this correct? (Y/N):')
        # If counter of categories is on the final category, increment it one more time to escape infinite loop
        if counter == len(kw_dicts):
            counter += 1

    # At this point the dictionaries are complete. Ask user if they would like  to create a backup of these keywords.
    elif counter == (len(kw_dicts)+1):
        for i in range(0, len(kw_dicts)):
            convo.insert(tk.INSERT,
                         f'\nComp: The keywords of the category named "{kw_dicts[i].getName()}"'
                         f' are {kw_dicts[i].getKeyList()}.')
            print(f'Dict #{(i+1)}: {kw_dicts[i].print()}')
        # This is to save keywords to file for later use.

        convo.insert(tk.INSERT, f'\nComp: Would you like to save these keywords '
                                f'to a text file for later use? (Y/N):')
        counter += 1
    elif counter > (len(kw_dicts)+1) and userEntries[-1].lower() == 'y':
        '''if user said yes, open and write keywords to "keywords.txt"
            format of "keywords.txt" should be:
        
            Category name 1
            Keyword 1,Keyword 2,Keyword 3
            Category name 2
            Keyword 1,Keyword 2,Keyword 3
            
            **Notice spacing between "," and "K" between each keyword!!!**
        '''
        filename = 'keywords.txt'
        file = open(filename, 'w')
        for i in range(0, len(kw_dicts)):
            # write keywords to text file using KeywordCategory class's built in method: textFileOutput
            file.write(kw_dicts[i].textFileOutput())
        convo.insert(tk.INSERT, f'\nComp: The keywords have been saved to file "{filename}".\n')
        # counter will be reused, reset it.
        counter = 0
        STAGE = 2
        getResponse(STAGE)

    # if user does not want a backup, just move to next step.
    elif counter > (len(kw_dicts) + 1) and userEntries[-1].lower() == 'n':
            convo.insert(tk.INSERT, f'\nComp: The keywords will not be saved.')
            counter = 0
            STAGE = 2
            getResponse(STAGE)
    else:
        convo.insert(tk.INSERT, f"\nComp: I'm sorry, that entry was invalid. Please try again.")
        for i in range(0, len(userEntries)-1):
            backUp.append(userEntries[i])
        userEntries.clear()
        userEntries = backUp.copy()
        counter -= 1
        getResponse(STAGE)


def getTextToAnalyze():
    '''
    This function is for getting the (student's) text to be analyzed for keywords
    It uses the global variables: textToBeAnalyzed, counter, userEntries, and STAGE
    -textToBeAnalyzed is a string that stores the student's text after it has been entered into
        the textfield by the user
    -counter is a counter variable to count how many times we have called this function
    -userEntries is the list (array) that stores the users text entries.
    -STAGE is to be updated on the last run of the function so that we can go to the next step
    '''
    global textToBeAnalyzed, counter, userEntries, STAGE, kw_dicts, manual
    backUp = []
    print(f'counter:{counter}')
    if counter == 0:
        convo.insert(tk.INSERT, f'\nComp: Would you like to manually enter the text to be analyzed,'
                                f' or read from text file? (Enter manual entry or text file).')
        counter += 1
    elif counter == 1 and manual is None:
        if userEntries[-1].lower().__contains__('manual'):
            manual = True
            counter += 1
        elif userEntries[-1].lower().__contains__('text'):
            manual = False
            counter += 1
        else:
            convo.insert(tk.INSERT, f'\n\nComp: That entry was invalid.')
    if manual:
        print('Manual= True, counter:', counter)
        if counter == 2:
            convo.insert(tk.INSERT, f'\n\nComp: Please paste the text into the textbox '
                                    f'below and press Enter when finished.\n')
            counter += 1
        elif counter == 3:
            textToBeAnalyzed = userEntries[-1]
            convo.insert(tk.INSERT, f'\n\nComp: You entered:\n"{textToBeAnalyzed}"'
                                    f'\n\nComp: Is this correct? (Y/N)')
            counter += 1

        elif counter == 4 and userEntries[-1].lower() == 'y':
            convo.insert(tk.INSERT, f'\n\nComp: Text Analysis:\n*********************************************\n')
            kw_dictList, categoryCounts = findAllKeywords(textToBeAnalyzed, kw_dicts)
            for i in range(0, len(kw_dictList)):
                convo.insert(tk.INSERT, f'\nCategory:"{kw_dicts[i].getName()}",'
                                        f' Total keywords found: {categoryCounts[i]}'
                                        f'\nOccurrences of each Keyword: {kw_dictList[i]}\n')
            convo.insert(tk.INSERT, f'\n****************************************************')

            return kw_dictList, categoryCounts

        elif counter == 4 and userEntries[-1].lower() == 'n':
            for i in range(0, len(userEntries)-2):
                backUp.append(userEntries[i])
            userEntries.clear()
            userEntries = backUp
            counter = 2
            getResponse(STAGE)

        elif counter == 5:
            # TODO: Reset program if user has more text to analyze
            convo.insert(tk.INSERT, f'\nComp: Is there more text you would like to analyze?')
            counter += 1
    if not manual:
        # TODO: Read textToAnalyze from text file - possibly multiple that are delimited.
        convo.insert(tk.INSERT, f'\nComp: Reading from text file not yet implemented.')


def findAllKeywords(text, kw_dicts):
    '''
    This function runs each category dictionary in our kwDictList array
    Through the existing findKeywords method
    It updates the count of the dictionary at each index
    and returns a count of keywords from that category
    which gets stored in the categoryCounts array.
    '''
    kwDictList = ['']*len(kw_dicts)
    categoryCounts = [0]*len(kw_dicts)
    for i in range(0, len(kw_dicts)):
        kwDictList[i] = kw_dicts[i].getKeywords()

    for i in range(0, len(kwDictList)):
        kwDictList[i], categoryCounts[i] = findKeywords(text, kwDictList[i])

    return kwDictList, categoryCounts


def findKeywords(text, keywordDictionary):
    '''
    re library contains the split method to split the text into regular English words.
    This means it removes commas, hyphens, apostrophes...etc.
                            ","     "-"     " ' "
    This means that the keywords cannot contain these characters
    OR something else must be used to split the text word-by-word (more difficult)
    '''
    import re
    # totalMatches keeps track of number of matches to any keyword
    totalMatches = 0
    # use the dictionary called to the method but copied because we will be updating it
    dictionary = keywordDictionary.copy()
    # this line splits the input text into individual words and puts that into an array
    # we also use the lowercase version to prevent capitalized letters from being skipped
    array = re.split('\W+',text.lower())

    for i in range(0,len(array)):
        # pulls next word to compare
        nextWord = array[i]
        # if we are not on the last word of the input text we can compare two words at a time
        # THIS IS IMPORTANT. This is how to find multi-word keywords like "design thinking"
        if i < len(array)-1:
            # next two words is just current word concatenated with a space and the next word
            nextTwoWords = nextWord+' '+array[i+1]
            # if the next two words are in our dictionary, they are a keyword
            if nextTwoWords in dictionary:
                # we increment the number at that keyword in the dictionary (so we can track KW count
                # for each word)
                dictionary[nextTwoWords] += 1
                totalMatches += 1
        '''this part just compares word by word.
            for this reason, one word keywords that are also contained in two word keywords are an issue
            Ex. "design thinking" and "thinking" cannot both be keywords because "design thinking" will be counted as 2 keywords
            because the text is being scanned for both single and double word keywords
            '''
        if nextWord in dictionary:
            # Same as above, if dictionary contains the word, it is a keyword.
            dictionary[nextWord] += 1
            totalMatches += 1
    # this lets us return both the dictionary (which now has how many times each keyword occurs)
    # and the total number of keywords.
    return dictionary, totalMatches

def getColour(field, colourmode):
    '''
    FFFFFF is the hex colour for white, 000000 is the hex color for black
    darkmode is white text on black background
    lightmode is black text on white background
    field is what they are colouring, bg = background colour
    txt is all text in the program
    '''
    if colourmode == 'dark':
        if field == 'bg':
            return '#000000'
        elif field == 'txt':
            return '#FFFFFF'
        elif field == 'scrl':
            return '#423F3F'
    if colourmode == 'light':
        if field == 'bg':
            return '#FFFFFF'
        elif field == 'txt':
            return '#000000'


window = tk.Tk()

colourmode = 'light'
bgcolour = getColour('bg', colourmode)
textcolour = getColour('txt', colourmode)
scrlcolour = getColour('scrl', colourmode)

'''
# Code from: https://stackoverflow.com/questions/23836000/can-i-change-the-title-bar-in-tkinter/23836427
# Code for making title bar black - optional for later
def move_window(event):
    window.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
window.overrideredirect(True)
window.geometry('700x700+350+80')
titleBar = tk.Frame(window, bg=bgcolour, relief='raised', bd=0)
closeBtn = tk.Button(titleBar, text='X', command=lambda: window.destroy())
titleBar.pack(expand=1, fill='x')
closeBtn.pack(side='right')
titleBar.bind('<B1-Motion>', move_window)
'''

window.title(f'KeywordFinder v{version}')


canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH, bg=bgcolour)
#background_image = tk.PhotoImage(file='landscape.png')
#background_label = tk.Label(window, image=background_image)
#background_label.place(relwidth=1, relheight=1)

canvas.pack()

header_frame = tk.Frame(window, bg=bgcolour, bd=6)
header_frame.place(anchor='n', relx=0.5, rely=0.01, relwidth=0.98, relheight=0.15)

title = tk.Label(header_frame, text='Keyword Finder', font=('Times', 50), bg=bgcolour, fg=textcolour)
title.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.6)

middle_frame = tk.Frame(window, bg='#000000', bd=6)
middle_frame.place(relx=0.01, rely=0.17, relwidth=0.98, relheight=0.6)

# code from: https://stackoverflow.com/questions/17657212/how-to-code-the-tkinter-scrolledtext-module
scrollbar = tk.Scrollbar(middle_frame)
convo = tk.Text(middle_frame, width=10, height=10, wrap="word",
                yscrollcommand=scrollbar.set,
                borderwidth=0, bg=bgcolour, fg=textcolour, font=16, )
convo.insert(tk.INSERT, f'Comp: Welcome to KeywordFinder Version {version}.')
convo.see(tk.END)
getResponse(STAGE)
scrollbar.config(command=convo.yview)
scrollbar.pack(side="right", fill="y")
convo.pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(window, bg=bgcolour, bd=6)
lower_frame.place(anchor='sw', relx=0.01, rely=0.99, relwidth=0.98, relheight=0.11)

user = tk.Entry(lower_frame, bg=bgcolour, font=40, fg=textcolour)
user.place(relx=0, rely=0.2, relwidth=0.7, relheight=0.7)
user.bind('<Return>', lambda event: updateText(user.get()))

button = tk.Button(lower_frame, text='Send', font=('Times', 12), bg=bgcolour, fg=textcolour, command=lambda: updateText(user.get()))
button.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.7)


window.mainloop()
