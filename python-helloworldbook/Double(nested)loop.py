numBlocks = int(raw_input("How many lines of blocks do you want?"))
numLines = int(raw_input("How many lines of stars do you want in each block?"))
numStars = int(raw_input("how many stars do you want in each line?"))
for block in range(0, numBlocks):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print '*',
        print
    print    
