
import sys
# if you put in an an invalid encoding then it spits back 'LookupError: unknown encoding: <bad value>'
script, encoding, error = sys.argv


# the main script is what kicks it all off at the end
# the script includes the language file "languages.txt" so you don't have to input it in terminal
def main(language_file, encoding, errors):
# reads one line of the languages file
    line = language_file.readline()

# an if-statement tets the truth of a variable and based on that truth run another piece of code
# this statement is testing to see if the line passed by line has anything in it (true)
# if there is nothing then it will be false and python the rest of the function (print_line and return)
    if line:
# this will call a second function to print the line, it's encoding and the errors
        print_line(line, encoding, errors)
# calling main from within main
# what this does is creates a loop because it jumps back to the top and will run over and over again
# until the if statement has an outcome of false
        return main(language_file, encoding, errors)

# the print line function encodes each line from the txt file
def print_line(line, encoding, errors):
# line.strip() strips the trailing \n from the incoming text line
    next_lang = line.strip()
# encodes the language in raw bytes
# encode requires an input for how to handle errors by setting them to be 'errors'
    raw_bytes = next_lang.encode(encoding, errors=errors)
# inverse of raw_bytes, creates the cooked version of raw_bytes by decoding it
# output of cooked_string should be the same as next_lang variable
    cooked_string = raw_bytes.decode(encoding, errors=errors)

# prints out the value of raw bytes, some seararator characters and the cooked_string to show what they look like
    print(raw_bytes, "<===>", cooked_string)

# done defining Functions
# language variable is used to run main function
# it opens open the languages.txt file and sets encoding of the file
languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
