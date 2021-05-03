    # put your code here.
def word_count(filename):
    #open file
    poem = open(filename)

    #create new dictionary
    word_counts = {}

    #create for loop to look at each line
    #go through each line and split by " "
    for word in poem:
        word = word.rstrip()
        words = word.split(" ")
        word_counts[word] = word_counts.get(word, 0) + 1

    print(f"{words} {word_counts}")
    return word_counts
 

    #close file
    poem.close()

    #call the function
print(word_count("test.txt"))

