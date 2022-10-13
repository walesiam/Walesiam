import pandas as pd
matches = pd.read_csv('https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv')
matches_edit = matches[['date','league', 'team1', 'team2', 'spi1', 'spi2', 'prob1', 'prob2', 'score1', 'score2']]
def team_league(x, y):
    total = matches_edit.loc[(matches_edit['league'] == y) | (matches_edit['league'] == 'UEFA Champions League') 
                        | (matches_edit['league'] == 'UEFA Europa League') | (matches_edit['league'] == 'UEFA Europa Conference League')]
    total[['outcome', 'points1', 'points2']] = 'unknown','unknown', 'unknown'
    away = total.loc[(total['score1']) < (total['score2']), 'outcome'] = 'away win'
    home = total.loc[(total['score1']) > (total['score2']), 'outcome'] = 'home win'
    draw = total.loc[(total['score1']) == (total['score2']), 'outcome'] = 'draw'
    ph = total.loc[(total['score1']) > (total['score2']), 'points1'] = 3
    phl = total.loc[(total['score1']) > (total['score2']), 'points2'] = 0
    pa = total.loc[(total['score1']) < (total['score2']), 'points2'] = 3
    pal = total.loc[(total['score1']) < (total['score2']), 'points1'] = 0
    phd = total.loc[(total['score1']) == (total['score2']), 'points1'] = 1
    pad = total.loc[(total['score1']) == (total['score2']), 'points2'] = 1
    hp = total.loc[(total['league'] == y) & (total['team1'] == x) & (total['points1'] == 3)]
    hp1 = hp['points1'].sum()
    ap = total.loc[(total['league'] == y) & (total['team2'] == x) & (total['points2'] == 3)]
    ap1 = ap['points2'].sum()
    hd = total.loc[(total['league'] == y) & (total['team1'] == x) & (total['points1'] == 1)]
    hd1 = hd['points1'].sum()
    ad = total.loc[(total['league'] == y) & (total['team2'] == x) & (total['points2'] == 1)]
    ad1 = ad['points2'].sum()
    total_points = hp1 + ap1 + hd1 + ad1
    win = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == y)]
    win1 = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == y)]
    loss = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == y)]
    loss1 = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == y)]
    draw = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == y)]
    draw1 = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == y)]
    win_ucl = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Champions League')]
    win1_ucl = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Champions League')]
    loss_ucl = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Champions League')]
    loss1_ucl = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Champions League')]
    draw_ucl = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Champions League')]
    draw1_ucl = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Champions League')]
    win_uel = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa League')]
    win1_uel = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa League')]
    loss_uel = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa League')]
    loss1_uel = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa League')]
    draw_uel = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa League')]
    draw1_uel = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa League')]
    win_ecl = total.loc[(total['team1'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa Conference League')]
    win1_ecl = total.loc[(total['team2'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa Conference League')]
    loss_ecl = total.loc[(total['team1'] == x) & (total['outcome'] == 'away win') & (total['league'] == 'UEFA Europa Conference League')]
    loss1_ecl = total.loc[(total['team2'] == x) & (total['outcome'] == 'home win') & (total['league'] == 'UEFA Europa Conference League')]
    draw_ecl = total.loc[(total['team1'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa Conference League')]
    draw1_ecl = total.loc[(total['team2'] == x) & (total['outcome'] == 'draw') & (total['league'] == 'UEFA Europa Conference League')]
    none = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == y)]
    none1 = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == 'UEFA Champions League')]
    none2 = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == 'UEFA Europa League')]
    none3 = total.loc[((total['team1'] == x) | (total['team2'] == x)) & (total['outcome'] == 'unknown') & (total['league'] == 'UEFA Europa Conference League')]
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
    return total.loc[(total['team1'] == x) | (total['team2'] == x)]