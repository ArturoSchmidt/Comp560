import sys
from collections import defaultdict
## needs to implement best backtracking technique
## needs to implement local search

## from stdin, takes in colors and map description


class inputReader():
    def __init__(self):
        pass

    def parseMapFromStdIn(self):
        file = sys.stdin.readlines()
        colors = []
        mapPositions = []
        breakCount = 0
        adjacencyList = defaultdict(list)

        #read stdin line by line
        for line in file:
            #use breakCount to keep track of current section (either colors, mapPositions or adjacencyList)
            #stdin should separate sections by a new line
            #append accordingly to either group
            if line == '\n':
                breakCount += 1
            else:
                if breakCount == 0:
                    colors.append(line)
                elif breakCount == 1:
                    mapPositions.append(line)
                else:
                    elements = line.split()
                    start = elements[0]
                    end = elements[1]
                    adjacencyList[start].append(end)
  
        return (colors, mapPositions, adjacencyList)

class search:
    def __init__(self,colors, positions, adjacencyList):
        self.colors = colors
        self.positions = positions
        self.adjacencyList = adjacencyList

    def backtrack(self): 
        
        pass

    def localSearch(self):
        pass

def main():
    ir = inputReader()
    (colors, positions, adjacencyList) = ir.parseMapFromStdIn()
    print(colors)
    print(positions)
    print(adjacencyList)
if __name__ == "__main__":
    main()


