# sds271_final_project

## PURPOSE
We made a package that reads data and returns existing and advanced sports statistics for players in specific seasons. Our package’s focus is on returning certain statistics based on what a user inputs in their chosen function. We want to be able to return individual player statistics separately based on user input, and the specific statistic(s) the user chooses should either be ones already present in our datasets or calculated based on preexisting values from the datasets.

## CLASS ATTRIBUTES
* playerstats --> a dataframe of our dataset (NBA_Player_Stats.csv)
* league = NBA (str)

## INSTANCE ATTRIBUTES

These attributes are each a column in a our dataframe. Each row represents a player's season, where the same player can have a row for each season they've played. This data is for all players who played in the NBA's 1997-98 season to the 2021-22 seasons. 

* playerstats --> a dataframe of our dataset -- this exists as both a class and instance attribute (NBA_Player_Stats.csv)
* player --> the name of the player (str)
* position --> position on the team (str)
* season --> the season which this data is from (str)
* fg (field goals) --> the number of field goals they scored (num)
* fga (field goals attempted) --> the number of field goals they attempted (num)
* fg_percent (field goal percentage) --> the number of field goals they scored/the number they attempted (num)
* tp (three pointers) --> the number of three pointers they scored (num)
* tpa (three pointers attempted) --> the number of three pointers they attempted (num)
* tp_percent (three point percentage) --> the number of three pointers they scored/the number they attempted (num)
* ft (free throws) --> the number of free throws they scored (num)
* fta (free throws attempted) --> the number of free throws they attempted (num)
* ft_percent (free throw percentage) --> the number of free throws they scored/the number of free throws they attempted (num)
* pts (points) --> the number of points they scored over the season (num)
* ast (assists) --> the number of assists they got over the season (num)
* tov (turnovers) --> the average number of turnovers/game (num)
* mp (minutes played) --> the number of minutes they played over the whole season (num)

## METHODS

* __init__ --> the initialization function (requires a player name and a season (both strs))
* get_statistics(statistic) --> takes the name of a statistic as a str input and returns the player's statistic for that season 
* true_shooting() --> calculates and returns a player's true shooting percentage (a measure of their accuracy by comparing attempts to actual goals across different throw types). 
* efficiency() --> calculates and returns a player's effective goal percentage (similar to true shooting percentage, but weighted to accommodate the varying difficulty of each type of shot). 
* ast_tov() --> calculates and returns the player's assist to turnover ratio
* turnover_percentage() --> calculates and returns an estimate of turnovers/100 plays
* per_36_minutes(statistic) --> takes a player's statistic of any kind and returns that statistic but after a calculation that accommodates how player's play might change throughout the game. 
* visualization(statistic) --> visualizes a statistic in a time series to show the change in that statistic for the same player over all their seasons played. 
* compare_player(another_player) --> takes another player's name as a string. if the player does not exist, it will throw an error. if the player does exist, it will compare the points of the object and another_player over their individual and shared seasons. intended to compare players who have played similar seasons. 

## TESTING
Our examples of how this package can be used are in our Python Notebook. 
