import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
from collections import deque

# MIN_GLOBAL_VALUE = -29
MAX_GLOBAL_VALUE = 28


class SavageLogic(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def move_position(self, current_position: Position, delta_x: int, delta_y: int):
        return Position(current_position.y + delta_y,current_position.x + delta_x)
    
    def compute_distance(self, current_position: Position, destination_position: Position):
        return abs(current_position.x - destination_position.x) + abs(current_position.y - destination_position.y)
    
    def is_coordinate_equal(self, a: Position, b: Position):
        return a.x == b.x and a.y == b.y
    
    def status_coordinate_on_enemy(self, current_position: Position, enemy_position: Position):
        distance = self.compute_distance(current_position, enemy_position)
        if(distance==1): # Can be tackled by enemy
            return -1
        elif(distance==0): # Can tackle enemy
            return 1
        else:
            return 0 # Nothing
    
    def is_valid_coordinate(self, current_position: Position, width: int, height: int):
        if(current_position.x < 0 or current_position.x >= width):
            return False
        if(current_position.y < 0 or current_position.y >= height):
            return False
        return True

    def next_move(self, board_bot: GameObject, board: Board):
        value_move = -1
        temp_teleport_pos = []
        temp_diamond_button_pos = deque()
        temp_diamonds1_pos = deque()
        temp_diamonds2_pos = deque()
        temp_enemy = deque()
        base_game_pos = None
        current_position = board_bot.position
        current_id = board_bot.id
        props = board_bot.properties
        current_diamond = props.diamonds
        candidate_next_diamond = current_diamond
        max_val_dirr = [current_diamond, current_diamond, current_diamond, current_diamond]
        height = board.height
        width = board.width
        total_value_objektif = [0, 0, 0, 0]

        if props.diamonds == 5:
            # Move to base
            base = board_bot.properties.base
            self.goal_position = base
            delta_x, delta_y = get_direction(
                current_position.x,
                current_position.y,
                self.goal_position.x,
                self.goal_position.y,
            )
            return delta_x, delta_y

        # Store each component items in the board to decrease the time complexity checking
        for i in board.game_objects:
            if(i.type == "TeleportGameObject"):
                temp_teleport_pos.append(i.position)
            elif(i.type == "DiamondButtonGameObject"):
                temp_diamond_button_pos.append(i.position)
            elif(i.type == "DiamondGameObject"):
                if(i.properties.points == 1):
                    temp_diamonds1_pos.append(i.position)
                else:
                    temp_diamonds2_pos.append(i.position)
            elif(i.type == "BaseGameObject"):
                base_game_pos = i.position
            elif(i.type == "BotGameObject"):
                if(i.id != current_id):
                    temp_enemy.append(i)
        is_move = [False, False, False, False]

        while len(temp_diamonds1_pos) != 0:
            diamond_pos = temp_diamonds1_pos.pop()
            for i in range(4):
                next_pos = self.move_position(current_position, self.directions[i][0], self.directions[i][1])
                if(self.is_valid_coordinate(next_pos, width, height)):
                    distance = self.compute_distance(next_pos, diamond_pos)
                    if(distance==0):
                        is_move[i] = True
                        if(props.diamonds + 1 <= 5):
                            max_val_dirr[i] = current_diamond + 1
                    else:
                        value = MAX_GLOBAL_VALUE-distance
                        if(value > total_value_objektif[i]):
                            total_value_objektif[i] = value


        while len(temp_diamonds2_pos) != 0:
            diamond_pos = temp_diamonds2_pos.pop()
            for i in range(4):
                next_pos = self.move_position(current_position, self.directions[i][0], self.directions[i][1])
                if(self.is_valid_coordinate(next_pos, width, height)):
                    distance = self.compute_distance(next_pos, diamond_pos)
                    if(distance==0):
                        is_move[i] = True
                        if(props.diamonds + 2 <= 5):
                            max_val_dirr[i] = current_diamond + 2
                    else:
                        value = MAX_GLOBAL_VALUE-distance
                        if(value > total_value_objektif[i]):
                            total_value_objektif[i] = value

        while len(temp_enemy) != 0:
            enemy = temp_enemy.pop()
            for i in range(4):
                next_pos = self.move_position(current_position, self.directions[i][0], self.directions[i][1])
                if(self.is_valid_coordinate(next_pos, width, height)):
                    if(enemy.properties.diamonds>0):
                        status_on_enemy = self.status_coordinate_on_enemy(next_pos,enemy.position)
                        if(status_on_enemy==1):
                            is_move[i] = True
                            max_val_dirr[i] += enemy.properties.diamonds
                        elif(status_on_enemy==-1):
                            max_val_dirr[i] = 0

        for i in range(4):
            if(max_val_dirr[i] > candidate_next_diamond):
                candidate_next_diamond = max_val_dirr[i]
                value_move = i

        if(candidate_next_diamond == current_diamond):
            temp_value_max = total_value_objektif[0]
            value_move = 0
            for i in range(1,4):
                if(temp_value_max < total_value_objektif[i]):
                    temp_value_max = total_value_objektif[i]
                    value_move = i
            if(current_diamond>0):
                distance_to_base = self.compute_distance(base_game_pos,current_position)
                if(MAX_GLOBAL_VALUE-temp_value_max > distance_to_base):
                    delta_x, delta_y = get_direction(
                                            current_position.x,
                                            current_position.y,
                                            distance_to_base.x,
                                            distance_to_base.y,
                                        )
                    return delta_x, delta_y
        
        delta_x = self.directions[value_move][0]
        delta_y = self.directions[value_move][1]

        return delta_x, delta_y
