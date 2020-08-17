# Missionaries-and-Cannibals.py
#     A program that computes the shortest amount of moves for the Missionaries and Cannibals problem.
# by: Charles Frelund

from operator import sub, add
import constant


class Graph:
    def __init__(self, root):
        self.root = root

    def bfs(self):
        """
        Breadth-first search

        Starts with the initial state in the queue, then finds each child/successor states.
        
        Then adds each state to the path.  

        Depending on the level, will find the shortest path.
        """
        queue = [self.root]
        path = []
        for state in queue:
            if state.isFinalState():
                path = [state]
                while state.parent:
                    path.insert(0, state.parent)
                    state = state.parent
                break
            queue.extend(state.getValidStateSuccessors())
        return path


class State:
    """
    For keeping track of the game state.
    Each state represents a vertex and the edges are transitions from one state to the successor or child of the state of the game.
    """

    def __init__(self, missionaries, missionaries_max, cannibals, cannibals_max, boat_dir, valid_operators, parent=None):
        self.missionaries = missionaries  # The number of missionaries.
        self.cannibals = cannibals  # The number of cannibals.
        # The max nuber of missionaries.
        self.missionaries_max = missionaries_max
        self.cannibals_max = cannibals_max
        self.boat_dir = boat_dir  # The direction of the boat.
        self.value = (missionaries, cannibals)
        # Opperators are valid to perform action.
        self.valid_operators = valid_operators
        self.parent = parent

    # Returns the the State text, left and right sides.
    def __str__(self):
        if (self.boat_dir == constant.LEFT_SIDE):
            return '<State {}, {}, "Left Side">'.format(self.value[0], self.value[1])
        elif(self.boat_dir == constant.RIGHT_SIDE):
            return '<State {}, {}, "Right Side">'.format(self.value[0], self.value[1])
    __repr__ = __str__

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals

    def __hash__(self):
        return hash(self.value)

    def printBothSides(self):
        """
        Prints the state for each side that the cannibals, missionaires, and boat is one.
        """
        if (self.boat_dir == constant.LEFT_SIDE):
            return '<Left Side {}, {}> |__>\t\t  <Right Side {}, {}">'.format(self.value[0], self.value[1], self.missionariesOnRight(), self.cannibalsOnRight())
        elif(self.boat_dir == constant.RIGHT_SIDE):
            return '<Left Side {}, {}>\t\t <__| <Right Side {}, {}">'.format(self.value[0], self.value[1], self.missionariesOnRight(), self.cannibalsOnRight())

    def isFinalState(self):
        """
        Function to check if the current state is the final state.
        This is determined when there is no missionary or cannibal on the left side of the river bank and the boat is on the right.

        Returns a boolean value.
        """
        return self.value == (0, 0) and self.boat_dir == constant.RIGHT_SIDE

    def cannibalsOnRight(self):
        """
        Returns the number of cannibals on the right side.
        """
        return self.cannibals_max - self.cannibals

    def missionariesOnRight(self):
        """
        Returns the number of missionaries on the right side.
        """
        return self.missionaries_max - self.missionaries

    def isStateValid(self):
        """
        Function to check if the status is valid.
        For a state to be valid, the number of cannibals can never be greater than that of missionaries.

        Thus, returns a boolean value.
        """
        if(self._invalidStates() or self._cannibalsOutnumbersMissionaries()):
            return False
        else:
            return True

    def _invalidStates(self):
        """
        Auxiliary function that handles impossible cases.
        """
        return (self.missionaries < 0 or
                self.cannibals < 0 or
                self.cannibalsOnRight() < 0 or
                self.missionariesOnRight() < 0 or
                (self.boat_dir != 0 and self.boat_dir != 1))

    def _cannibalsOutnumbersMissionaries(self):
        """
        Auxiliary function that handles cases where cannibals are in greater numbers.
        """
        # cannibals > missionaries on the left
        return ((self.missionaries > 0 and self.cannibals > self.missionaries) or
                # cannibals > missionaries on the right
                (self.missionariesOnRight() > 0 and
                 self.cannibalsOnRight() > self.missionariesOnRight())
                )

    def __addTuple(self, a, b):
        """
        Auxiliary functions for tuple operations.
        """
        return tuple(map(add, a, b))

    def __subTuple(self, a, b):
        """
        Auxiliary functions for tuple operations.
        """
        return tuple(map(sub, a, b))

    def _getStateSuccessors(self):
        """
        Function that returns successor states.
        """
        successors = []
        for operator in self.valid_operators:
            if(self.boat_dir == constant.LEFT_SIDE):
                tuplex = self.__subTuple(self.value, operator)
                st = State(tuplex[0], self.missionaries_max, tuplex[1], self.cannibals_max,
                           constant.RIGHT_SIDE, self.valid_operators, parent=self)
                successors.append(st)
            elif (self.boat_dir == constant.RIGHT_SIDE):
                tuplex = self.__addTuple(self.value, operator)
                st = State(tuplex[0], self.missionaries_max, tuplex[1], self.cannibals_max,
                           constant.LEFT_SIDE, self.valid_operators, parent=self)
                successors.append(st)
        return successors

    def getValidStateSuccessors(self):
        """
        Function that returns VALID successor states.
        """
        valid_successors = []
        states = self._getStateSuccessors()
        for state in states:
            if state.isStateValid():
                valid_successors.append(state)
        return valid_successors


class MissionariesCannibals:
    def __init__(self, missionaries, cannibals, boat_size):
        """
        The problem construct: 
        First input will be the number of missionaries.
        The second input will be the number of cannibals.
        The third input will be the max number of people that can board the and traverse the boat at one time.
        """
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_size = boat_size
        self.operators = self.getOperators(self.boat_size)
        self.initial_state = State(self.missionaries, self.missionaries, self.cannibals, self.cannibals, constant.LEFT_SIDE, self.operators)

    def __str__(self):
        return '<Missionaries: {}, Cannibals: {}, Boat size: {}, Operators: {}>'.format(
            self.missionaries, self.cannibals, self.boat_size, self.operators)

    def getOperators(self, boat_size):
        """
        Function to aquire the proper amount of operaters of the boat.
        Boat size is determined at input.
        """
        operators = []
        for m in range(boat_size + 1):
            for c in range(boat_size + 1):
                if (((c != 0) or (m != 0)) and (c + m <= boat_size)):
                    operators.append((m, c))
        return operators

    def printSolution(self, path):
        """
        Prints the solution.
        """
        for s in path:
            print(s.printBothSides())

    def Search(self):
        g = Graph(self.initial_state)
        path = g.bfs()
        self.printSolution(path)


def main():
    missionaries = int(input("How many missionaires are on the river bank? "))
    cannibals = int(input("How many cannibals are on the river back? "))
    boatCapacity = int(
        input("How many occupants can the boat hold at one time? "))
    mc_problem = MissionariesCannibals(missionaries, cannibals, boatCapacity)
    mc_problem.Search()


if __name__ == "__main__":
    main()
