numLines = int(raw_input("How many lines of stars do you want?"))
numStars = int(raw_input("How many stars perline do you want?"))
for line in range(0, numLines):
    for star in range(0, numStars):
        print '*',
    print    
    
