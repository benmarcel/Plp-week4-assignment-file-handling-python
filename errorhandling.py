file = input('enter file path or name')



def readFile():
    try:
        with open(file, "r") as openedFile:
             read = openedFile.read()
        print(read);
    
    except FileNotFoundError:
        print('file does not exist! please check file name or path.');
    finally:
        print('operation carried out successfully!');


readFile()


