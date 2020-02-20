import sys
import math
import random
import time
from collections import defaultdict
## needs to implement best backtracking technique
## needs to implement local search

## from stdin, takes in colors and map description


class InputReader():
    def __init__(self):
        pass

    def parseMapFromStdIn(self):
        file = sys.stdin.readlines()
        colors = []
        states = {}
        breakCount = 0
        adjacencyList = defaultdict(set)
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
                    newState = State(line)
                    states[line] = newState
                else:
                    # creates adjacency list and appends to states those that werent explicitely stated in previous breakCount
                    elements = line.split()
                    startState = elements[0] + '\n'
                    if startState not in states:
                        newState = State(startState)
                        states[startState] = newState
                    endState = elements[1] + '\n'
                    if endState not in states:
                        newState = State(endState)
                        states[endState] = newState            
                    start = states[elements[0]+'\n']
                    end = states[elements[1]+'\n']
                    adjacencyList[start].add(end)
                    adjacencyList[end].add(start)
  
        return (colors, states, adjacencyList)


#Changed is used to detect loops and accurate calculation of misplaced states
class State:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.changed = False

class Map(object):
    def __init__(self, adjacencyList,colors):
        self.map = adjacencyList
        self.colors = colors


    def hillClimbingColoring(self):
    # misplaced == number of states that are either not colored or have the same color as one of their neighbors
    # main algorithm functionality: 
    # state's start with color value from initialized state (None)
    # we iterate through adjacency list of states, for each state we change its color if changing it does not cause a violation
    # this is done until an iteration does not change the map or the number of misplaced tiles is zero.
        misplaced = len(self.map)
        changed = True
        totalChanges = 0
        # if state has not changed and we have not reached a final state we keep iterating
        while(changed and misplaced > 0):
            changed = False
            for key in self.map:
                #adds randomization to assignment of colors
                random.shuffle(self.colors)
                print(self.colors)
                for color in self.colors:
                    # only change color if there is no violation and is not stuck changing back and forth from same color
                    if color != key.color and self.checkChange(key,color) and key.changed < 100:
                        totalChanges += 1
                        if key.changed == 0:
                            misplaced -= 1
                        key.color = color
                        key.changed += 1
                        changed = True
                        break
        return (misplaced, totalChanges)

    def countColoredStates(self):
        notColored = 0
        for state in self.map:
            if state.color != None:
                notColored += 1
        return notColored

    def printMap(self):
        for state in self.map:
            print(state.name + ' ' + state.color)
       
    #checks if any the neighbors of a passed state are the same as its color
    def checkChange(self, key, color):
        neighbors = self.map[key]
        for neighbor in neighbors:
            if neighbor.color == color:
                return False
        return True


    # check correctness of full map. If any state is None or one of its neighbors is the same color as itself false is returned
    def checkValidity(self):
        for state, neighborList in self.map.items():
            for neighbor in neighborList:
                if state.color == neighbor.color or neighbor.color == None or state.color == None:
                    print(state.name, state.color , neighbor.name, neighbor.color)
                    return False
        return True

    def reset(self):
        for state in self.map:
            state.color = None
    def repeatedHillClimbing(self, times):
        # function that is called from main, takes in number of seconds to be run
        # runs hillClimbing until it finds a valid solution or it times out
        start = time.time()
        current = 0
        misplaced = float('inf')
        while((current - start) < times):
            self.reset()
            (misplaced, totalChanges) = self.hillClimbingColoring()
            if misplaced == 0:
                return (True, totalChanges)
            current = time.time()
        return (False, 0)


def main():

    # initialization code: starts timer and passes input into parser
    startTime = time.time()
    ir = InputReader()
    (colors, positions, adjacencyList) = ir.parseMapFromStdIn()

    # map creation and repeating hillClimbing call
    map = Map(adjacencyList,colors)
    (foundRes , totalChanges) = map.repeatedHillClimbing(60)
    endTime = time.time()

    # checks if map ended in a valid state and prints corresponding output
    output = map.checkValidity()
    if output:
        map.printMap()     
        print('local search successful')
        print('total changes: ', totalChanges)
    else:
        print('local search stuck in local maxima')

    print('total time to compute and print map: ' + str((endTime - startTime)))
   

if __name__ == "__main__":
    main()


