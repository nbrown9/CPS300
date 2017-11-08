# Nicholas Brown
# CPS300
    
# This function returns a floating point number average
def getAverage(Sentence):
    # Count the number of characters in the sentence
    CharacterCount = (sum(len(word) for word in Sentence.split()))
    # Count the number of words in a sentence
    WordCount = len(Sentence.split())
    # Calculate average by dividing characters by number of words
    Average = CharacterCount / WordCount
    return Average

# Specify in and out files
inputFileName = input("Enter input file name: ")
outputFileName = input("Enter output file name: ")

# Open specified files to work with
workingFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'w')

# Line number counter
lineCount = 1

# Iterate through each line of text file
for line in workingFile:
    # Cast float to write as string
    toWrite = str(getAverage(line))
    # write string to text file with line number counter
    outputFile.write(str(lineCount)+' : ' +toWrite + '\n')
    # Increment counter
    lineCount+=1

# Close out files
outputFile.close()
workingFile.close()