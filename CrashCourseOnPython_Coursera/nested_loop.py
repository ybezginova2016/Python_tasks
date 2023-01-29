# Nested Loops

# 1
for left in range(4):
    for right in range(left, 4):
        print('[' + str(left) + '|' + str(right) + ']', end=' ')
    print()
print()

# 2
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + ' vs ' + away_team)

# You got it! We want to print all possible team pairings but exclude
# those where a team would play against itself. To do that,
# we need a conditional that skips the case where both teams are the same