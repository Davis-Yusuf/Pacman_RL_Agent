from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """

        # Your code
        pacman_coords = pacman.getPosition()
        ghost_coords = ghost.getPosition()

        if ghost.isScared():
            return Directions.STOP
        else:
            if pacman_coords[0] == ghost_coords[0]:
                if abs(pacman_coords[1] - ghost_coords[1]) <= dist:
                    if pacman_coords[1] > ghost_coords[1]:
                        return Directions.SOUTH
                    else:
                        return Directions.NORTH
                else:
                    return Directions.STOP
            elif pacman_coords[1] == ghost_coords[1]:
                if abs(pacman_coords[0] - ghost_coords[0]) <= dist:
                    if pacman_coords[0] > ghost_coords[0]:
                        return Directions.WEST
                    else:
                        return Directions.EAST
                else:
                    return Directions.STOP
            else:
                return Directions.STOP

    def getAction(self, state):
        """
        state - GameState

        Fill in appropriate documentation
        """

        # legal Pacman actions
        legal = state.getLegalPacmanActions()

        # Get the agent's state from the game state and find agent heading
        agentState = state.getPacmanState()
        ghostStates = state.getGhostStates()

        # check whether Pacman is in danger using inDanger()
        heading = None
        isDanger = False
        for ghostState in ghostStates:
            heading = self.inDanger(agentState, ghostState)
            if heading != Directions.STOP:
                isDanger = True
                break

        if heading == Directions.STOP and agentState.getDirection() == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH
        elif heading == Directions.STOP:
            heading = agentState.getDirection()

        if isDanger:
            if Directions.REVERSE[heading] in legal:
                action = Directions.REVERSE[heading]
            elif Directions.LEFT[heading] in legal:
                action = Directions.LEFT[heading]
            elif Directions.RIGHT[heading] in legal:
                action = Directions.RIGHT[heading]
            elif heading in legal:
                action = heading
            else:
                action = Directions.STOP
        else:
            left = Directions.LEFT[heading]  # What is left based on current heading
            if left in legal:
                action = left
            else:
                # No left turn
                if heading in legal:
                    action = heading  # continue in current direction
                elif Directions.RIGHT[heading] in legal:
                    action = Directions.RIGHT[heading]  # Turn right
                elif Directions.REVERSE[heading] in legal:
                    action = Directions.REVERSE[heading]  # Turn around
                else:
                    action = Directions.STOP  # Can't move!

        return action

