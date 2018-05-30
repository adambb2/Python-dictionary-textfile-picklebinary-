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

class Nation:
    
    #set the values for a new Nation
    def __init__(self, name, continent, population, area):
        self._name = name
        self._continent = continent
        self._population = population
        self._area = area
        #start the pop density at o
        self._density = float(0)

      #method to calcualte population density  
    def popDensity(self):
        ## Calculate population desnity of a nation
        self._density = round((float(self._population)*1000000)/float(self._area),2)
        #round( (float(self._population*1000000)) / float(self._area), 2)

    
