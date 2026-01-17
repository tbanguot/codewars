def mine_location(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]:
                return [i, j]
​
    return []