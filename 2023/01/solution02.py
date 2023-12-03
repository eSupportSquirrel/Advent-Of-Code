#Solution:
# Will need to get all digits from the string.
#   There will need to be a method for evaluating the text-based spelling for
#   each digit.
# Then get first digit (a) and last digit (z) from each line (l). 
# Then append them together (az). Then take az and add it to a running total (rt).
# Last, print out the running total.

#Submitted and verified as solved on 12/2/2023 at 10:58 AM CST

#Gets the first (a) and last (b) character of a string, then returns them as (ab) format
def FirstAndLast(string):
    for i in range(len(string)):
        # If it is the first character of the string then print it.
        if i == 0:
            first = string[i]
        # If it is the last character of the stringthen also print it.
        if i == len(string) - 1:
            last = string[i]
        
    return (first + last)
#end def FirstAndLast()

#Extracts digits from the given string
def ExtractDigits(string):
    string = CheckForSpelledDigit(string)
    digits = ''
    for char in string:
        if char.isdigit():
            digits += char

    return digits
#end def ExtractDigits()

#Checks for digits spelled out, calls CheckForIncorrectSpelledDigit()
def CheckForSpelledDigit(string):
    string = string.lower()
    string = CheckForIncorrectSpelledDigit(string)
    string = string.replace("one", "1")
    string = string.replace("two", "2")
    string = string.replace("three", "3")
    string = string.replace("four", "4")
    string = string.replace("five", "5")
    string = string.replace("six", "6")
    string = string.replace("seven", "7")
    string = string.replace("eight", "8")
    string = string.replace("nine", "9")

    return string
#end def CheckForSpelledDigit()

#Checks SPECIFICALLY for misspelled digits
def CheckForIncorrectSpelledDigit(string):
    string = string.replace("twone", "twoone")
    string = string.replace("fiveight", "fiveeight")
    string = string.replace("eightwo", "eighttwo")
    string = string.replace("nineight", "nineeight")

    return string
#end def CheckForIncorrectSpelledDigit()

if __name__ == "__main__":
    runningTotal = 0

    #Open the file and read the lines
    inputFile = open('d:/Git Repos/AoC2023/01/input.txt', 'r')
    inputFileLines = inputFile.readlines()
    
    for line in inputFileLines:
        line = line.rstrip('\n')
        numberString = ExtractDigits(line)
        lineResults = int(FirstAndLast(numberString))
        runningTotal += lineResults  
    print("New Calibration value is " + str(runningTotal))