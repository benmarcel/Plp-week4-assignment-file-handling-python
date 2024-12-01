def fileHandler(filename):
    file = open(filename, 'r') # this opens the file in a read mode
    document = file.read() # this reads the file
    print(document) # this displays the read file in the console

    open(filename, 'a').write('\n we are the word') # appends some new content to the file
    newDocs = open(filename, 'r').read()
    print(newDocs)

    return 'File modified successfully'

print(fileHandler('./document.txt'))

# file = open('./document.txt', 'r').readlines()

# for let in file:
#     print(let)
