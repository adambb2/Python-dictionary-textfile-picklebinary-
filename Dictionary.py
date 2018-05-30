"""
Adam Blake Bell

Assignment 4 Question 1

The file UN.txt  gives the data about 193 members of the United Nations. Each line of the file contains four pieces of data about a country - name, continent, population (in millions), and land area (in square miles).

Create a class named Nation with four instance variables to hold the data for a country and a method named popDensity that calculates the population density of the country. Write a program that uses the class to
create a dictionary of 193 items, where each item of the dictionary has the form name of a country: Nation object for that country Use the file un.txt to create the dictionary, and save the dictionary in a pickled binary file named
nationDict.dat  .
Also, save the class Nation in a file named nation.py

Write a program that requests the name of a U.N member country as input, and then displays infor- mation about the country.
Use a pickled binary file nationsDist.dat and the file nation.py created in part (a).

Write a program that requests the name of a continent as input, and then displays the names (in descending order) of the five most densely populated U.N member countries in that continent.
Use the pickled binary file nationsDict.dat and the file nation.py created in part (a).
"""

#import nation file containing Nation class
import nation
#from nation import popDensity

import pickle

#dictionary
#country: nation object#
#student.update({'name': 'Jane'})
#print(len(student))
#print(student.items())

def main():
    my_dict = {} #create instance of a Dictionary object
    nation_dict = {} #create instance of a Dictionary object
    my_dict = createDict() #invoke createdict method
    #print(my_dict.items())

    #create a pickle file
    output_file = open("nation.dat", "wb")
    pickle.dump(my_dict, output_file)
    output_file.close()

    #open the pickle file
    output_file = open("nation.dat", "rb")
    #get the dictionary from the pickle binary file
    nation_dict = pickle.load(output_file)
    
    #get user input for the key of the dictionary
    while True:
        try:
            countrykey = input("Please enter a country name. If the country exists within the dictionary stored in the pickle binary file then its infromation will be displayed: ")
            print(nation_dict[countrykey]._name+" is in the continent of "+nation_dict[countrykey]._continent+", has a population of "+nation_dict[countrykey]._population+"(million), and has "+nation_dict[countrykey]._area+ " square miles of land.")
        except KeyError:
            print("Invalid Country name..")
            continue
        break
      
        
    #nationobject = nation.Nation(0, 0, 0 , 0)
    #nationobject = nation_dict[countrykey]
    #area = nationobject._area()
    #print(area)
    #print(nation_dict.items())
    

    #if 'Africa' in nation_dict.values():
     #   print('YES')
    #mylist = []
    #mylist = list(nation_dict.values())
    #for x in mylist:
        #if mylist[x]._name == 'Africa':
           # print('True')
    print(" ")
    print(" ")

    continent = input("Please enter a continent. The names (in descending order) of the five most densely populated U.N member countries in that continent will be displayed if it exists in the dictionary stored in the pickle binary file: ")
    
    newlist = []
    
    #iterate thru the keys in the dictionary
    for key in nation_dict:
        nation_dict[key].popDensity()#set the population density using the method in nation class
        if nation_dict[key]._continent == continent:
            #add objects to list if they have the continent
            newlist.append(nation_dict[key])
    #print(str(newlist))

    print(" ")
    
    sortedlist = sorted(newlist, key=lambda x: float(x._density), reverse=True) #sort the list by density with largest first

    count = 0
    counta=0
    #for x in sortedlist:
        #count = count+1
        #print(x._name + " has "+x._population+" (million) people") #printing first 5 country names
        #x.popDensity()#set the population density using the method in nation class
        #if count == 5:
            #break

    print(" ")
    for x in sortedlist:
        counta = counta+1
        print(x._name + " has "+str(x._density)+" people per square mile")
        if counta == 5:
            break

    
    output_file.close()
    
    


    
def createDict():
    dictionary={}    
        #open file for reading
    with open('UN.txt', 'r') as f:
                #print(UN.name)
                #print("These are the file contents:")
                #print(" ")
                #print all lines in the file
                #for line in f:
                    #print(line, end='')
                #num_lines = sum(1 for line in open('UN.txt'))
                #print(str(num_lines))
                
                #seek may be unneccessary here
                #f.seek(0)
        #print(" ")
        #print(" ")

        count=0
                    
                    #iterates through the lines
        for line in f:
                        #line = f.readline()
                        
                        #split the line around the comma
            array = line.split(",")
            count= count+1
                        #print(str(count))

                        #try:
            nationobj = nation.Nation(array[0], array[1], array[2], array[3])
                            #print(nationobj._name)
                            #add a new nation name and object to the dictionary
            dictionary.update({nationobj._name: nationobj})
                         #print(dictionary.items())
                        #except IndexError:
                            #returns dictionary when a blank line is reached
                    #print(dictionary.items())
            #print('return reached')
                        #    return dictionary

                    #print(len(dictionary))
                    #print(dictionary.items())
    return dictionary
        

            
    
main()

            



                








