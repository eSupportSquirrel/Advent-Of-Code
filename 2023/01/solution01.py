#Solution:
# Will need to get all digits from the string. 
# Then get first digit (a) and last digit (z) from each line (l). 
# Then append them together (az). Then take az and add it to a running total (rt).
# Last, print out the running total.

#Submitted and verified as solved on 12/2/2023 at 10:58 AM CST

# get a
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

def ExtractDigits(string):
    line = ""
    for char in string:
        if char.isdigit():
            line += char
    
    return line
#end def ExtractDigits()
    

if __name__ == "__main__":
    runningTotal = 0

    #Open the file and read the lines
    inputFile = open('d:/Git Repos/AoC2023/01/input.txt', 'r')
    inputFileLines = inputFile.readlines()
    count = 0
    
    for line in inputFileLines:
        line = line.rstrip('\n')
        count += 1
        numberString = ExtractDigits(line)
        lineResults = int(FirstAndLast(numberString))
        runningTotal += lineResults
    
    print("New Calibration value is " + str(runningTotal))