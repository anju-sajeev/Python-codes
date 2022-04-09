import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

matches = pd.read_csv(r"archive\matches.csv")
deliveries= pd.read_csv(r"archive\deliveries.csv")
print(matches.shape)

#question 1
no_of_matches_played_per_year=matches.groupby(['season'])['winner'].count()

print(no_of_matches_played_per_year)

#question 2
year=input("Enter year")

wins_teams=matches.groupby(['season','winner'])['id'].nunique()

wins_teams.unstack().plot(kind='bar', stacked=True, figsize=(15,10)) 
plt.title(str('Number of matches wins by each teams in each seasons').upper())
plt.xlabel(str('Years').upper())
plt.ylabel(str('matches counts').upper())
plt.xticks(rotation=45)
plt.show()

#question 4

matches.rename(columns = {'id':'match_id'}, inplace = True)
merged=deliveries.merge(matches, how="left", on='match_id')
bowled = merged[(merged['dismissal_kind']=='bowled')]
bowlers_wickets = bowled.groupby(['season','bowler'])['dismissal_kind'].count()
bowlers_wickets.sort_values(ascending = False, inplace = True)
blr=bowlers_wickets[:10]


