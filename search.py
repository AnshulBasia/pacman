# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    from util import Stack
    pred={}
    visited={}
    action={}
    s=Stack()
    s.push(problem.getStartState())
    path=[]
    way=[]
    while(not s.isEmpty()):
        state=s.pop()
        visited[state]=True
        if(problem.isGoalState(state)):
            print "FOUND",state
            break
        for x in problem.getSuccessors(state):
            if(x[0] not in visited):
                s.push(x[0])
                pred[x[0]]=state
                action[x[0]]=x[1]

    while(state!=problem.getStartState()):
        path.append(pred[state])
        way.append(action[state])
        state=pred[state]
    way.reverse()           # Since we want the way from source to destination
    return way
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    q=Queue()
    pred={}
    visited={}
    action={}
    path=[]
    way=[]
    q.push(problem.getStartState())
    while(not q.isEmpty()):
        state=q.pop()
        visited[state]=True
        if(problem.isGoalState(state)):
            print "FOUND",state
            break
        for x in problem.getSuccessors(state):
            if(x[0] not in visited):
                visited[x[0]]=True
                q.push(x[0])
                pred[x[0]]=state
                action[x[0]]=x[1]

    while(state!=problem.getStartState()):
        path.append(pred[state])
        way.append(action[state])
        state=pred[state]
    way.reverse()           # Since we want the way from source to destination
    return way
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    from util import PriorityQueue
    q=PriorityQueue()
    pred={}
    visited={}
    action={}
    path=[]
    way=[]
    temp=[]
    q.push(problem.getStartState(),0)
    i=0
    while(not q.isEmpty()):
        if(i==0):
            state=q.pop()
            cost=0
            i=1
        else:
            temp=q.pop()
            print temp[0]," with cost of ",temp[3]," pred is ",temp[1]
            state=temp[0]
            pred[temp[0]]=temp[1]
            action[temp[0]]=temp[2]
            cost=temp[3]
        if(problem.isGoalState(state)):
            print "FOUND",state
            break
        visited[state]=True
        for x in problem.getSuccessors(state):
            if(x[0] not in visited):
                temp=[]
                temp.append(x[0])
                temp.append(state)
                temp.append(x[1])
                temp.append(x[2]+cost)
                q.update(temp,x[2]+cost)
                
                

    while(state!=problem.getStartState()):
        path.append(pred[state])
        way.append(action[state])
        state=pred[state]
    way.reverse() 
    print path          # Since we want the way from source to destination
    return way
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
