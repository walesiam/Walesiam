import pandas as pd

# Load the latest soccer match data from FiveThirtyEight
matches = pd.read_csv('https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv')

# Select relevant columns for analysis
matches_edit = matches[['date','league', 'team1', 'team2', 'spi1', 'spi2', 'prob1', 'prob2', 'score1', 'score2']]

def team_league(x, y):
    # x: team name
    # y: league name

    # Filter matches for the specified league and all major UEFA competitions
    total = matches_edit.loc[(matches_edit['league'] == y) | 
                             (matches_edit['league'] == 'UEFA Champions League') | 
                             (matches_edit['league'] == 'UEFA Europa League') | 
                             (matches_edit['league'] == 'UEFA Europa Conference League')]
    
    # Initialize columns for match outcome and points for each team
    total[['outcome', 'points1', 'points2']] = 'unknown','unknown', 'unknown'
    
    # Determine match outcomes based on scores
    # Set 'away win' if team2 scored more than team1
    total.loc[(total['score1']) < (total['score2']), 'outcome'] = 'away win'
    # Set 'home win' if team1 scored more than team2
    total.loc[(total['score1']) > (total['score2']), 'outcome'] = 'home win'
    # Set 'draw' if scores are equal
    total.loc[(total['score1']) == (total['score2']), 'outcome'] = 'draw'
    
    # Assign points based on match outcomes
    # Home team (team1) gets 3 points for a win
    total.loc[(total['score1']) > (total['score2']), 'points1'] = 3
    # Away team (team2) gets 0 points when home team wins
    total.loc[(total['score1']) > (total['score2']), 'points2'] = 0
    # Away team (team2) gets 3 points for a win
    total.loc[(total['score1']) < (total['score2']), 'points2'] = 3
    # Home team (team1) gets 0 points when away team wins
    total.loc[(total['score1']) < (total['score2']), 'points1'] = 0
    # Home team (team1) gets 1 point for a draw
    total.loc[(total['score1']) == (total['score2']), 'points1'] = 1
    # Away team (team2) gets 1 point for a draw
    total.loc[(total['score1']) == (total['score2']), 'points2'] = 1
    
    # Calculate points for the specified team (x) in the specified league (y)
    # Points from home wins in the league
    hp = total.loc[(total['league'] == y) & (total['team1'] == x) & (total['points1'] == 3)]
    hp1 = hp['points1'].sum()
    # Points from away wins in the league
    ap = total.loc[(total['league'] == y) & (total['team2'] == x) & (total['points2'] == 3)]
    ap1 = ap['points2'].sum()
    # Points from home draws in the league
    hd = total.loc[(total['league'] == y) & (total['team1'] == x) & (total['points1'] == 1)]
    hd1 = hd['points1'].sum()
    # Points from away draws in the league
    ad = total.loc[(total['league'] == y) & (total['team2'] == x) & (total['points2'] == 1)]
    ad1 = ad['points2'].sum()
    
    # Sum all points for the team in the league
    total_points = hp1 + ap1 + hd1 + ad1
    
    # --- Count Wins, Losses, Draws for the specified team (x) in the LEAGUE (y) ---
    # League home wins
    win = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == y)]
    # League away wins
    win1 = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == y)]
    # League home losses (team1 is x, outcome is away win)
    loss = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == y)]
    # League away losses (team2 is x, outcome is home win)
    loss1 = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == y)]
    # League home draws
    draw = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == y)]
    # League away draws
    draw1 = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == y)]
    
    # --- Count Wins, Losses, Draws for the specified team (x) in UEFA CHAMPIONS LEAGUE ---
    # UCL home wins
    win_ucl = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Champions League')]
    # UCL away wins
    win1_ucl = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Champions League')]
    # UCL home losses
    loss_ucl = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Champions League')]
    # UCL away losses
    loss1_ucl = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Champions League')]
    # UCL home draws
    draw_ucl = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Champions League')]
    # UCL away draws
    draw1_ucl = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Champions League')]
    
    # --- Count Wins, Losses, Draws for the specified team (x) in UEFA EUROPA LEAGUE ---
    # UEL home wins
    win_uel = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa League')]
    # UEL away wins
    win1_uel = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa League')]
    # UEL home losses
    loss_uel = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa League')]
    # UEL away losses
    loss1_uel = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa League')]
    # UEL home draws
    draw_uel = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa League')]
    # UEL away draws
    draw1_uel = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa League')]

    # --- Count Wins, Losses, Draws for the specified team (x) in UEFA EUROPA CONFERENCE LEAGUE ---
    # ECL home wins
    win_ecl = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa Conference League')]
    # ECL away wins
    win1_ecl = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa Conference League')]
    # ECL home losses
    loss_ecl = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa Conference League')]
    # ECL away losses
    loss1_ecl = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa Conference League')]
    # ECL home draws
    draw_ecl = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa Conference League')]
    # ECL away draws
    draw1_ecl = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa Conference League')]
    
    # --- Count unplayed matches (outcome is 'unknown') for the specified team (x) ---
    # Unplayed matches in the specified league
    none = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == y)]
    # Unplayed matches in UCL
    none1 = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == 'UEFA Champions League')]
    # Unplayed matches in UEL
    none2 = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == 'UEFA Europa League')]
    # Unplayed matches in ECL
    none3 = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == 'UEFA Europa Conference League')]
    
    # Print the aggregated statistics
    print (win['outcome'].count(), 'league home win')
    print (win1['outcome'].count(), 'league away win')
    print (loss['outcome'].count(), 'league home loss')
    print (loss1['outcome'].count(), 'league away loss')
    print (draw['outcome'].count(), 'league home draw')
    print (draw1['outcome'].count(), 'league away draw')
    
    print (win_ucl['outcome'].count(), 'ucl home win')
    print (win1_ucl['outcome'].count(), 'ucl away win')
    print (loss_ucl['outcome'].count(), 'ucl home loss')
    print (loss1_ucl['outcome'].count(), 'ucl away loss')
    print (draw_ucl['outcome'].count(), 'ucl home draw')
    print (draw1_ucl['outcome'].count(), 'ucl away draw')
    
    print (win_uel['outcome'].count(), 'uel home win')
    print (win1_uel['outcome'].count(), 'uel away win')
    print (loss_uel['outcome'].count(), 'uel home loss')
    print (loss1_uel['outcome'].count(), 'uel away loss')
    print (draw_uel['outcome'].count(), 'uel home draw')
    print (draw1_uel['outcome'].count(), 'uel away draw')
    
    print (win_ecl['outcome'].count(), 'ecl home win')
    print (win1_ecl['outcome'].count(), 'ecl away win')
    print (loss_ecl['outcome'].count(), 'ecl home loss')
    print (loss1_ecl['outcome'].count(), 'ecl away loss')
    print (draw_ecl['outcome'].count(), 'ecl home draw')
    print (draw1_ecl['outcome'].count(), 'ecl away draw')
    
    print(none['outcome'].count(), 'unplayed league matches')
    print(none1['outcome'].count(), 'unplayed ucl matches')
    print(none2['outcome'].count(), 'unplayed uel matches')
    print(none3['outcome'].count(), 'unplayed ecl matches')
    
    print('total points', total_points)
    
    # Return all matches involving the specified team (x) from the filtered leagues
    return total.loc[(total['team1'] == x) | (total['team2'] == x)]