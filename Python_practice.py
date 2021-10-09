print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] =='Denver':
        print(counties[1])
if counties[2] != 'Jeffereson':
            print(counties[2])

counties = ["Arapahoe","Dever","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else: 
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El Paso is in the list of counties.")


#######################################################################################
 #For loop the list the county in the counties list. *print displays the county   
for county in counties:
    print(county)


#3.2.10 *I forgot to list this, thats why it wasn't running
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for loop for counties_dict
for county in counties_dict:
    print(county)

#Key() method of for loop
for county in counties_dict.keys():
    print(county)

#.values() key method: *for voters in counties_dict.values():* to get values of a dictionary *422829 *463353 *432438
#another key method: print(counties_dict[county])
#get() method: print(counties_dict.get(county)) <==== this get values/keys
for county in counties_dict:
    print(counties_dict[county])

#key-value pairs of a dictionary .items() or for key in dictionary_name.items(): print(key, value) 
#this gives both the county and number of voters or Key and Value
for county, voters in counties_dict.items():
    print(county, voters)

#printing each dictionary in voting_data we use a for loop
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    print(counties_dict)
#This is the range() method that does the same as the previos line
for i in range(len(voting_data)):
    print(voting_data[i])

#Nested for loops
for county_dict in voting_data:
    for value in counties_dict.values():
        print(value)

#To print county name from each dictionary
for county_dict in voting_data:
    print(counties_dict['county'])
#=======================================================================================================================
#original code before f str 3.2.11
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#f string 3.2.11
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


#F str method
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiple f str
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes. "
  #  f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

#The general format for a number to format it in an f-string is as follows:
    #f'{value:{width}.{precision}}'

#thousand separator for formating a number
    #f'{value:{width},.{precision}}'
#Add thousand sep. for the candidate votes & total votes then format the % votes to 2 decimal places
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.") 

