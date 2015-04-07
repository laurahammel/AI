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

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    '''print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    '''
    
    "*** YOUR CODE HERE ***"
    
    start = problem.getStartState()
    s = str(start)
    g = {s : 0}
    
    frontierNodes = util.PriorityQueue()
    frontierNodes.push(start,g[s])
    expandedNodes = []
    
    nodes = {}

    while frontierNodes.isEmpty() == False:
        
        currentNode = frontierNodes.pop()
        if problem.isGoalState(currentNode):
            return backtracker(start, currentNode, nodes)
        
        expandedNodes.append(currentNode)

        successors = problem.getSuccessors(currentNode)
    
        for (successor, action, stepCost) in successors:
            if successor not in expandedNodes:
                x = g[str(currentNode)] + stepCost
                if str(successor) not in g.keys() or x < g[str(successor)]:
                    g[str(successor)] = x
                    nodes[str(successor)] = (currentNode, action)
                    frontierNodes.push(successor, x)
                    
    return []

"""
The function backtracker is a recursive helper function for uniformCostSearch.  It
retraces the steps from a node to the start node in the original problem and returns
the desired move list for uniformCostSearch.  Hooray! :D
"""
def backtracker(start, currentNode, nodes):
    print currentNode
    if currentNode == start:
        return []
    
    current = nodes[str(currentNode)]
    last = current[0]
    move = current[1]

    return backtracker(start, last, nodes) + [move]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
        
    start = problem.getStartState()
    s = str(start)
    g = {s : 0}
    h = {s : heuristic(start, problem)}
    
    frontierNodes = util.PriorityQueue()
    frontierNodes.push(start,g[s] + h[s])
    expandedNodes = []
    
    nodes = {}
    
    while frontierNodes.isEmpty() == False:
        currentNode = frontierNodes.pop()
        while currentNode in expandedNodes:
            currentNode = frontierNodes.pop()
        if problem.isGoalState(currentNode):
            return backtracker(start, currentNode, nodes)
    
        expandedNodes.append(currentNode)
        
        successors = problem.getSuccessors(currentNode)
        
        for (successor, action, stepCost) in successors:
            if successor not in expandedNodes:
                x = g[str(currentNode)] + stepCost
                if successor not in g.keys() or x < g[str(successor)]:
                    g[str(successor)] = x
                    h[str(successor)] = heuristic(successor, problem)
                    nodes[str(successor)] = (currentNode, action)
                    frontierNodes.push(successor, x + h[str(successor)])

    return []


# Abbreviations
astar = aStarSearch
ucs = uniformCostSearch
