import json

f = open("data/cleaneddata.csv","r")

lines = f.readlines()

#initializes all dictionaries
dictionary = {}
dictionary["Bronx"] ={}
dictionary["Manhattan"] ={}
dictionary["Brooklyn"] ={}
dictionary["Queens"] ={}
dictionary["Staten Island"] ={}

# EDIT : went through the csv and removed all Domestic,Birds and changed them to Domestic Birds to facilitate strip() (with ctrlf)

# iterates through all the "rows" in the data
for line in lines: 
    
    line = line.split(",") #splits the line into different sections of data (ex. number, location) by comma

    # removes unnecessary formatting 
    line[6] = line[6].replace('\n',"")
    line[6]= int(line[6])
  

    #separates by borough
    if line[1] == "Brooklyn":   
        dictionary["Brooklyn"][line[0]] = [line[2],line[3],line[4],line[5],line[6]] 
    elif line[1] == "Manhattan":
        dictionary["Manhattan"][line[0]] = [line[2],line[3],line[4],line[5],line[6]]
    elif line[1] == "Queens":
        dictionary["Queens"][line[0]] = [line[2],line[3],line[4],line[5],line[6]]
    elif line[1] == "Bronx":
        dictionary["Bronx"][line[0]] = [line[2],line[3],line[4],line[5],line[6]]
    elif line[1] == "Staten Island":
        dictionary["Staten Island"][line[0]] = [line[2],line[3],line[4],line[5],line[6]]

    
f.close() 


f1= open("data/data.json","w")
json.dump(dictionary,f1,indent=4) #adds the data to a json file
f1.close()
