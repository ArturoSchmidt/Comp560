import sys
from collections import defaultdict
import queue
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
        for color in colors:
            color = color.rstrip('/n')
        print(colors)
        self.colors = colors
        self.positions = positions
        self.adjacencyList = adjacencyList

    def backtrack(self): 
        #sanitize data
        
        print(self.colors)
        #create a directed graph to use AC3

        #create a queue of arcs
        arcs  = queue.Queue()
        for state in self.positions:
            for adjState in self.adjacencyList[state]:
                arcs.enqueue((state, adjState))
        for arc in list(arcs.queue):
            print(arc)


        #assign each state it's possible domain
        stateDomains = {}
        for state in self.positions:
            stateDomains[state] = self.colors
        #print(stateDomains)

        

    def localSearch(self):
        pass

def main():
    ir = inputReader()
    (colors, positions, adjacencyList) = ir.parseMapFromStdIn()
    print(colors)
    print(positions)
    print(adjacencyList)
    backSearch = search(colors, positions, adjacencyList)
    backSearch.backtrack()
if __name__ == "__main__":
    main()


