class SearchProblem:
    def __init__(self):
        pass

    def getStartState(self):
        pass

    def isGoalState(self, state):
        pass

    def getSuccessors(self, state):
        pass

    def getCostOfActions(self, actions):
        pass

import util

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
    """
    from util import Stack
    
    fringe = Stack()
    fringe.push((problem.getStartState(), []))
    visited = set()
    
    while not fringe.isEmpty():
        current_state, actions = fringe.pop()
        
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited:
            visited.add(current_state)
            for successor, action, stepCost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                fringe.push((successor, new_actions))
    
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    
    fringe = Queue()
    fringe.push((problem.getStartState(), []))
    visited = set()
    
    while not fringe.isEmpty():
        current_state, actions = fringe.pop()
        
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited:
            visited.add(current_state)
            for successor, action, stepCost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                fringe.push((successor, new_actions))
    
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = {}
    
    while not fringe.isEmpty():
        current_state, actions = fringe.pop()
        
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited or problem.getCostOfActions(actions) < visited[current_state]:
            visited[current_state] = problem.getCostOfActions(actions)
            for successor, action, stepCost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                cost = problem.getCostOfActions(new_actions)
                fringe.push((successor, new_actions), cost)
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = {}
    
    while not fringe.isEmpty():
        current_state, actions = fringe.pop()
        
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited or problem.getCostOfActions(actions) < visited[current_state]:
            visited[current_state] = problem.getCostOfActions(actions)
            for successor, action, stepCost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                cost = problem.getCostOfActions(new_actions) + heuristic(successor, problem)
                fringe.push((successor, new_actions), cost)
    
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
