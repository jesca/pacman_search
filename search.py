# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import searchAgents

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

 
    #states will have ((coords),directionlist)
    currState=(problem.getStartState(),[])
    myStack=util.Stack()
    seen=set()
     
    while not problem.isGoalState(currState[0]):
        currCoord=currState[0]

        if currCoord not in seen:
            seen.add(currCoord)
            slist=problem.getSuccessors(currCoord)
            for s in slist:
#pop each successor onto fringe with directionlist updated
                dlist=list(currState[1])
                dlist.append(s[1])
            # print "successor", s[0], " d list", dlist
                myStack.push((s[0], dlist))
        if myStack.isEmpty():
            return []
        currState=myStack.pop()
    return currState[1]

    
                      
#first attempt with recursion (failed)
"""
def expand(problem, stack, visited):
    if stack.isEmpty():
        return stack
    coord=stack.pop()
    
    if problem.isGoalState(coord[0]):
        print "current GOAL coords, SHOULD RETURN STACK", coord[0]
        return stack    
    stack.push(coord) #push back in stack...not the right time to pop yet, popped to inspect

    if coord[0] in visited:
        x=stack.pop()
        print "already visited, popped from stack", x
        return expand(problem,stack,visited) #stack should have the visited item popped already
    visited.append(coord[0]) #append x,y coords to visited list since you're adding its children
    print "appended visited coords", coord[0]
    sList=problem.getSuccessors(coord[0])
    if len(sList)!=0:
        for s in sList:
            if s[0] not in visited:
                stack.push(s)
                print "added to stack:", s
    else:
        stack.pop()
        print "no children, pop and recurse"
    return expand(problem,stack,visited)


#updates the goal list with action items from stack; goal state on top of the stack
def rList(stack):
    finalDirections=[]
    while not stack.isEmpty():
        currState = stack.pop()
        finalDirections.append(currState[1])
        print "goal coords:", currState
    print "final directions:", finalDirections
    finalDirections.pop()
    finalDirections.reverse()
    print finalDirections
    return finalDirections
        """


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    #essentially the same as dfs with a Queue from util.py
    currState=(problem.getStartState(),[])
    myQ=util.Queue()
    seen=set()
    
    while not problem.isGoalState(currState[0]):
        currCoord=currState[0]
        if currCoord not in seen:
            slist=problem.getSuccessors(currCoord)
            for s in slist:
                #pop each successor onto fringe with directionlist updated
                dlist=list(currState[1])
                dlist.append(s[1])
                # print "successor", s[0], " d list", dlist
                myQ.push((s[0], dlist))
            seen.add(currCoord)
        if myQ.isEmpty():
            return []
        currState=myQ.pop()
            #print "final list:", currState[1]
    return currState[1]

    
    util.raiseNotDefined()


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    currState=(problem.getStartState(),[],0)
    myQ=util.PriorityQueue()
    #using a priority queue to include costs
    seen=set()
    
    while not problem.isGoalState(currState[0]):
        currCoord=currState[0]
        if currCoord not in seen:
            seen.add(currCoord)
            slist=problem.getSuccessors(currCoord)
            for s in reversed(slist):
                dlist=list(currState[1])
                dlist.append(s[1])
                combinedcost=s[2]
                combinedcost+=currState[2]
                #print s[2]
                #In UCS, you consider the cost of the entire path, not just the cost of one hop.(push combined cost onto stack) 
                myQ.push((s[0], dlist,combinedcost),combinedcost)
        if myQ.isEmpty():
            return []
        currState=myQ.pop()
#  print "final list:", currState[1]
    return currState[1]

    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    currState=(problem.getStartState(),[],0)
    myQ=util.PriorityQueue()
    #using a priority queue to include costs
    seen=set()
    
    while not problem.isGoalState(currState[0]):
        currCoord=currState[0]
        if currCoord not in seen:
            seen.add(currCoord)
            slist=problem.getSuccessors(currCoord)
            for s in reversed(slist):
                dlist=list(currState[1])
                dlist.append(s[1])
                combinedcost=s[2]
                combinedcost+=currState[2]
                #hcost doesn't get pushed back to queue. hcost = combined cost + heuristic of target node!
                hcost=combinedcost+heuristic(s[0], problem)
                #print s[2]
                #In UCS, you consider the cost of the entire path, not just the cost of one hop.(push combined cost onto stack)
                costHeurestic = combinedcost
                myQ.push((s[0], dlist,combinedcost),hcost)
        if myQ.isEmpty():
            return []
        currState=myQ.pop()
    return currState[1]

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
