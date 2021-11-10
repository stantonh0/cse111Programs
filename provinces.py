
def main():
    text_list = read_list("provinces.txt")
    #print(text_list)
    text_list.pop(0)
    text_list.pop()
    alberta_num = change_AB()

    print(text_list)
    print(f"The number of times Alberta is listed is {alberta_num}.")

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open("provinces.txt", "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)
            

    # Return the list that contains the lines of text.
    return text_list

def change_AB():
    import fileinput

    with fileinput.FileInput("provinces.txt", inplace=True, backup='.bak') as file:
        alberta_num = 0
        for line in file:
            print(line.replace("AB", "Alberta"), end='')
            if line =="Alberta":
                alberta_num += 1
    return alberta_num


# Call main to start this program.
if __name__ == "__main__":
    main()