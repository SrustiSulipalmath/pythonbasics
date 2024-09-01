number_grid = [    #4rows 3 columns
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

#nested for loops

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)