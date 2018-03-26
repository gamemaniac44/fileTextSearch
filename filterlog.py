#Version:  1.0
#Author:  Kyle Siler
#Program Description:  This application will receive a file path the user specifies for an input text
#file and then scans the input text file path for a matching word term or sequence and then outputs the matching
#lines to an output file in an output file path that the user specifies. If the file path of the input file the
#user entered is invalid, then output an error to the user and ask for an input filepath again.

def main():
    #by default the program will run since variable is set to true
    runAgain = True

    #by default there is no matched text data in the text document since variable is set to false
    matchedData = False

    #run the program until the user inputs a valid file path to search the text document
    while runAgain == True:

        #read the user input file path text document
        readFile = input("Please enter the file path that you want to read in:  ")

        #user specifies what file name the program should write the output to.
        #note:  the user does not have to create this filename, the program will create it automatically
        writeFile = input("Please enter the file path that you want to write the output to:  ")
        stringFind = input("What do you want to find in the first file:  ")

        #try to read the file path that the user input and write output to outputfile that user specified
        try:
            dataRead = open(readFile, "rt")
            dataWrite = open(writeFile, "w")

        #the program could not locate the filepath on the system that the user specified, so output an error              
        except:
            print ("The files you entered could not be located on the system.  Please make sure you have created the file.")

        #the filepath the user input is a valid file, so write the matched data in the scanned input file to the output file
        else:.
            #write an intial line to the output file informing the user what matching lines were found based on the word they input to search for
            dataWrite.write("These are the lines that matched the string you entered based on file:  " + readFile + "\n")

            #go through each line in the input file path and find if the search word the user input is in the input file
            #if the search word is in in the input file, write the text line to the output file
            for text in dataRead:
                if stringFind in text:
                    dataWrite.write(text)
                    matchedData = True

            #output to user that the program found matching lines and wrote the output to the user specified output file         
            if matchedData == True:
                print ("Matching lines based on string written to file:  " + writeFile)
                runAgain = False

            #no matching lines were found, so inform the user
            else:
                print ("No matching lines were found!")
                runAgain = False

            #close the files to prevent memory leaks and file reading and writing issues
            dataRead.close()
            dataWrite.close()

main()
