# open the newfile.txt in read mode. causes error if no such file exists.
with open("exampleFiles/newfile.txt", "x") as fileptr:
    print(fileptr)

    if fileptr:
        print("File created successfully")
