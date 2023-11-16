from textblob import Word
from tkinter import *

# Initializing tkinter here
root = Tk()
root.geometry("400x300")  # width and height of GUI
root.title(" Spelling Checker ")

# Using textblob
# This class will be imported in main.py if we import from spell1.py
class Spell:
    # contructor, In main.py, while object creation we'll pass the word entered by user as parameter
    def __init__(self, text):
        self.word = Word(text)

    # This method is getting list of likely correct spellings of the word using method provided by textblob and returning it as a string
    def correctSpelling(self):
        # returns list of likely correct spellings of the word
        tempList = self.word.spellcheck()
        temp = ''
        for i in tempList:
            temp = temp+i[0]+'\n'
        return temp

    # The method spellcheck provided with textblob returns a list of likely correct spellings of the word, along with their accuracy
    # If the spelling is correct, then it returns the same word with accuracy as 1
    # This check method is using the spellcheck method and returning true if spelling of word entered is correct, else false

    def check(self):
        correct = self.word.spellcheck()[0][0]
        if (self.word == correct):
            return True
        else:
            return False

# This method will get triggered when the Check button (Initialized below) gets clicked


def takeInput():
    # This method, first clears the output screen, in case any text is already present on output screen
    Output.delete("1.0", "end")
    # Then store the text entered on input screen in Input variable.
    Input = inputText.get("1.0", "end-1c")
    # As of now, it is programmed for only single word at once.
    # So, if user enters multiple words we are considering the first word
    Input = Input.split()[0]
    # Creating an object of type Spell, more explanation about this class is present in another files.
    # We can refer to spell1.py and spell2.py files respectively, depending on which one we have imported
    s = Spell(Input)
    # This method takes Input as parameter and return True if spelling is correct else false
    if (s.check()):
        Output.insert(END, 'Correct!')
    else:
        # In case spelling is incorrect, the below method returns the likely correct spellings in the form of formatted string
        correctSpellings = s.correctSpelling()
        Output.insert(
            END, 'Incorrect!, Do you mean any of these: '+correctSpellings)


# Label is a widget provided by tkinter to display text/image on screen, it can take different parameters as you can see below.
# Try changing few and see how the GUI changes
l = Label(text="Type the word here: ", bg='#759D98',
          bd='4', font=("Times", "23", "bold"), width='40')

# Here, Text widget is initialized and assigned to the variable inputText.
# inputText is being used above, to take the word entered by user, store it in a variable and pass on to methods to check its spelling
inputText = Text(root, height=2,
                 width=40, bd='3', font=("Times", "18", "bold"))


# The button widget is initialized here, this will add a button with name Check, on cliking which the method takeInput will get triggered
Check = Button(root, height=2,
               width=20,
               text="Check",
               command=lambda: takeInput(), bg='#375F5A', fg='white', font=("Times", "14"))

# Here, the text box is initialized, where the final result after checking spelling will be displayed
Output = Text(root, height=5,
              width=40, bd='3', bg='#8C9F9D', font=("Times", "18", "bold"))


# the pack() method declares the position of widgets in relation to each other, instead of declaring the precise location of a widget
l.pack(padx=2, pady=2)
inputText.pack(padx=5, pady=5)
Check.pack(padx=2, pady=2)
Output.pack(pady=5)

# This is to call an endless loop so that the GUI window stays open until the user closes it
mainloop()