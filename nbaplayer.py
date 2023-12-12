# Import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

""" 
Player class reads in player stats data and returns different statistics, true shooting percentage, and efficiency of players.
"""
#Initialize class Player()
class Player():
    #Read in playerstats data
    playerstats = pd.read_csv("NBA_Player_Stats.csv")
    league = "NBA"
    """
    Constructor for a player object. Takes in the player's name and season.
    """
    #Write init function that takes in player's name and the season they play in
    def __init__(self, player, season):
        playerstats = pd.read_csv("NBA_Player_Stats.csv")
        #player, position, season, fg, fga, fg_percent, tp, tpa, tp_percent, ft, fta, ft_percent, pts
        self.player = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["Player"]
        self.position = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["Pos"]
        self.season = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["Year"]
        self.fga = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["FGA"]
        self.fg = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["FG"]
        self.fg_percent = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["FG%"]
        self.tpa = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["3PA"]
        self.tp = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["3P"]
        self.tp_percent = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["3P%"]
        self.fta = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["FTA"]
        self.ft = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["FT"]
        self.ft_percent = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["FT%"]
        self.pts = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["PTS"]
        self.ast = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["AST"]
        self.tov = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["TOV"]
        self.mp = playerstats.loc[playerstats["Player"] == player].loc[playerstats["Year"] == season]["MP"]
        
    """
    Returns statistics of choice if they exists in the dataset. Else, throws an error.
    """ 
    #Getter function for available statistics in the dataset
    def get_statistic(self, statistic):
        #Turn statistic user puts in to lower cap
        statistic_noncap = statistic.lower()
        #Check if the statistic belongs in the list of attributes
        if hasattr(self, statistic_noncap) == True:
            #Return rounded version (to 2 decimals) of the statistic
            return round(getattr(self, statistic_noncap).values[0],2)
        #If statistic is not in list of attributes, return a print statement
        else:
            print( "Oops! We don't have that statistics. Try again!" )
        
    """ 
    Calculates and returns true shooting percentage of the player.
    """
    #Function that calculates true shooting percentage based on formula on NBA website
    def true_shooting(self):
        ts = (self.pts)/(2*(self.fga + (0.44 * self.fta)))
        #Return rounded version (to 2 decimals) of the statistic
        return round(ts.values[0],2)
    
    """ 
    Calculates and returns the efficiency of the player.
    """
    #Function that calculates efficiency of player based on formula on NBA website
    def efficiency(self):
        efg = (self.fg + (0.5 * self.tp))/(self.fga)
        #Return rounded version (to 2 decimals) of the statistic
        return round(efg.values[0],2)
    
    #Function that calculates AST/TOV based on formula on NBA website
    def ast_tov(self):
        ast_tov = self.ast/self.tov
        #Return rounded version (to 2 decimals) of the statistic
        return round(ast_tov.values[0],2)
    
    #Function that calculates various statistics per 36 minutes based on formula on NBA website
    def per_36_minutes(self, statistic):
        #Turn statistic user puts in to lower cap
        statistic_noncap = statistic.lower()
        #Check if the statistic belongs in the list of attributes
        if hasattr(self, statistic_noncap) == True:
            #Return rounded version (to 2 decimals) of the statistic
            return round((((getattr(self, statistic_noncap).values[0])/self.mp)*36).values[0],2)
        #If statistic is not in list of attributes, return a print statement
        else:
            print( "Oops! We don't have that statistics. Try again!")
    
    # the formula is 100 * TOV / (FGA + 0.44 * FTA + TOV). Turnover percentage is an estimate of turnovers per 100 plays.
    def turnover_percentage(self):
        turnover = (100*self.tov)/((self.fga + (0.44*self.fta) + self.tov))
        #Return rounded version (to 2 decimals) of the statistic
        return round(turnover.values[0],2)

    #Function that provides a time-series visualization of user's chosen statistic
    def visualization(self, statistic):
        playerstats = pd.read_csv("NBA_Player_Stats.csv")
        playermask = playerstats["Player"] == str(self.player.values[0])
        singlestats = playerstats[playermask]
        sns.lineplot(x = singlestats["Year"], y = singlestats[statistic])
        plt.xticks(rotation = 45)
        plt.title(f"{self.player.values[0]}'s {statistic} Per Season")
        plt.xlabel("Season")
        plt.show()
    
    #Function that provides a visual that compares the current player's points with another player's. 
    # ALERT: this is only supposed to compare players who have similar career length and have played during the same seasons.
    def compare_player(self, another_player):
        
        ## isolate the relevant statistics (player and points/season) for the player object
        playerstats = pd.read_csv("NBA_Player_Stats.csv")
        playermask = playerstats["Player"] == str(self.player.values[0])
        singlestats = playerstats[playermask]
        
        ## do the same for the "other player" (user input)
        secondplayermask = playerstats["Player"] == str(another_player)
        otherstats = playerstats[secondplayermask]
        
        #Throw an exception if we don't have data of the other player that user puts in
        if len(otherstats) == 0:
            return("This player either does not exist or the statistics for them are unavailable :( sorry")
        
        #Comparing length of datasets to see which player played for more seasons (this determined the x-axis)
        if len(singlestats) >= len(otherstats):
            sns.lineplot(x = singlestats["Year"], y = singlestats["PTS"], label = str(self.player.values[0]))
            #plt.plot(singlestats["PTS"], label = str(self.player.values[0]))
            plt.plot(otherstats["Year"], otherstats["PTS"], label = another_player)
            plt.xticks(rotation = 45)
            plt.xlabel("Season")
            plt.ylabel("Points")
            plt.title(f"{self.player.values[0]} vs {another_player}'s Points Per Season")
            plt.legend()
            plt.show()
            
        #if the second player has more seasons, the plot is defined differently
        else:
            sns.lineplot(x = otherstats["Year"], y = otherstats["PTS"], label = another_player)
            #plt.plot(singlestats["PTS"], label = str(self.player.values[0]))
            plt.plot(singlestats["Year"], singlestats["PTS"], label = str(self.player.values[0]))
            plt.xticks(rotation = 45)
            plt.xlabel("Season")
            plt.ylabel("Points")
            plt.title(f"{self.player.values[0]} vs {another_player}'s Points Per Season")
            plt.legend()
            plt.show()