# Open file    
fileHandler = open ("samplelog.txt", "r")
# Get list of all lines in file
listOfLines = fileHandler.readlines()
# Close file 
fileHandler.close()

list = []

# Iterate over the lines
for line in listOfLines:
    if "INK" in line:
        words = line.split()
        #print(words)
        list.append(words[7])

for listitem in list:
    print (listitem)

list.sort()

for listitem in list:
    print (listitem)
