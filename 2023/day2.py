def cube(data):
    ans=0
    gameNumber = 1
    for line in data:
        gameValid = True
        line = line.replace(";"," ")
        line = line.replace(","," ")
        words = line.split()
        
        numberOfCubes = 0
        for word in words:
            if word.isnumeric():
                numberOfCubes = int(word)
            
            elif word in ["red","green","blue"]:
                # If the number of cubes exceeds a certain limit based on color, invalidate the game
                if  (word == "red" and numberOfCubes > 12) or\
                    (word == "green" and numberOfCubes > 13) or\
                    (word == "blue" and numberOfCubes > 14):
                        gameValid = False
        
        # If the game is valid, add its number to the answer
        if gameValid == True:
            ans += gameNumber

        gameNumber += 1
    return ans  

def cube2(data):
    ans = 0

    for line in data:
        gameValid = True
        line = line.replace(";"," ")
        line = line.replace(","," ")
        words = line.split()
        
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        
        numberOfCubes = 0
        for word in words:
            if word.isnumeric():
                numberOfCubes = int(word)
            
            elif word in ["red","green","blue"]:
                # Keep track of the maximum number of cubes for each color
                if word == "red" and maxRed < numberOfCubes:
                    maxRed = numberOfCubes
                    
                elif word == "green" and maxGreen < numberOfCubes:
                    maxGreen = numberOfCubes
                    
                elif word == "blue" and maxBlue < numberOfCubes:
                    maxBlue = numberOfCubes

        power = maxRed * maxGreen * maxBlue
        ans += power
    return ans

if __name__ == "__main__":
    # Read from an input file and pass the data to both functions
    f = open("input_day_2.txt", "r")  # Open the input file for reading
    data = f.readlines()  # Read all lines from the file
    f.close()  # Close the file

    print(cube(data))
    print(cube2(data))
