# Election_Analysis

## Overview of Election Audit:
The purpose of this project was to assist a board of elections employee in an election audit of the tabulated results for  U.S congression precinct in Colorado. The elections employee tasked the following:
1. Report the total number of votes cast.
2. Report the Total number of votes for each candidate.
3. Report the votes into percentages for each candidate.
4. Report the winner of the election based on popular vote.


## Election-Audit Results:

After conducting the script for the election audit, we found that the total votes in this congressional election was 369,711. The following are the results of the Election Audit:
#### Finding a county and its total vote/percentage.
- Jefferson had 38,855 which was only 10% of the total votes. 
- Arapahoe had 24,801 votes which accounted for only 6.7% of the total votes.
- Lastly, Denver received 306,055 votes which was 86.8% of the total votes.
  - The number of votes and the percentage of total votes for each county were found through this script: 

```
   for county_name in county_votes:
          # 6b: Retrieve the county vote count.
          county_vote = county_votes[county_name]
          # 6c: Calculate the percentage of votes for the county.
          vote_percentage = float(county_vote) / float(total_votes) * 100
           # 6d: Print the county results to the terminal.
          county_results = (
                  f"{county_name}: {vote_percentage:.1f}% ({county_vote:,})\n")
          print(county_results)
```    
      
- By calculating the the number of votes in each county and receiving the total votes, it was reported that Denver was the county with the largest number of votes. 
###### script for largest county vote
```
if county_vote > largest_county_voter_turnout:
            largest_county_voter_turnout = county_vote
            county_largest_amount = county_name
```            
#### Candidates and their vote count/percentage          
- Charles Casper Stockham received 85,213 votes which was 23% of the votes. 
- Raymon Anthony Doane received 11,606 votes which was 3.1% of the total votes.
- Diana DeGette received 272,892 votes which was 73.8% of the votes.
  - After receiving the results of each candidate, it is clear that Diana DeGette won the election due to her collecting 272,892 votes. The total percentage is 73.8% which is the majority of the total votes.


###### Election Results
![election_results](https://user-images.githubusercontent.com/90741799/136987982-0821f78c-7fc2-4cb3-aa6d-d5e86932bdc5.png)

## Election-Audit Summary:
 This script was very efficient for calculating a large number of data as well as creating text files to sum up the key points of the congressional election. This script can be modified into being used for other elections by using a list and a dictionary that contains the vairables that are needed for the election. Another example on how this script can be used for another election is to another set of election data that show other counties and their candidates as well as the number of voters.
###### Resources
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code, 1.47


