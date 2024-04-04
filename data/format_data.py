import json

f = open("data/cleaneddata.csv","r")

lines = f.readlines()

dictionary = {}

# EDIT : went through the csv and removed all Domestic,Birds and changed them to Domestic Birds to facilitate strip() (with ctrlf)

# iterates through all the "rows" in the data
for line in lines: 
    line = line.split(",")  #splits the line into different sections of data (ex. number, location) by comma
    for attr in line:
        attr = attr.strip()
    dictionary[line[0]] = [line[1],line[2],line[3],line[4],line[5],line[6]] # adds to dictionary with the date and time as a key (to have separate data, only column with no overlap)

f.close()

f1= open("data/data.json","w")


json.dump(dictionary,f1,indent=4) #adds the data to a json file

f1.close()
