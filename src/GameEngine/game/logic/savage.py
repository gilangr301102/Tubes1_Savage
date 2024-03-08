import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
from collections import deque

MIN_GLOBAL_VALUE = -29
MAX_GLOBAL_VALUE = 29


class SavageLogic(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def move_position(self, current_position: Position, delta_x: int, delta_y: int):
        return Position(current_position.x + delta_x, current_position.y + delta_y)
    
    def is_coordinate_equal(self, a: Position, b: Position):
        return a.x == b.x and a.y == b.y
    
    def is_coordinate_can_tackle_by_enemy(self, current_position: Position, enemy_position: Position):
        if(current_position.x == enemy_position.x and abs(current_position.y-enemy_position.y)==1):
            return True
        elif(current_position.y == enemy_position.y and abs(current_position.x-enemy_position.x)==1):
            return True
        return False

    def is_available_to_move(self, current_position: Position, delta_x: int, delta_y: int, width: int, height: int):
        if(current_position.x + delta_x < 0 or current_position.x + delta_x >= width):
            return False
        if(current_position.y + delta_y < 0 or current_position.y + delta_y >= height):
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
        current_score_inven = board_bot.properties.diamonds
        max_global_value = current_score_inven
        max_val_dirr = [current_score_inven, current_score_inven, current_score_inven, current_score_inven]
        height = board.height
        width = board.width

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
                if(self.is_coordinate_equal(next_pos, diamond_pos)):
                    is_move[i] = True
                    max_val_dirr[i] += 1

        while len(temp_diamonds2_pos) != 0:
            diamond_pos = temp_diamonds2_pos.pop()
            for i in range(4):
                next_pos = self.move_position(current_position, self.directions[i][0], self.directions[i][1])
                if(self.is_coordinate_equal(next_pos, diamond_pos)):
                    is_move[i] = True
                    max_val_dirr[i] += 2

        while len(temp_enemy) != 0:
            enemy_pos = temp_enemy.pop()
            for i in range(4):
                next_pos = self.move_position(current_position, self.directions[i][0], self.directions[i][1])
                if(self.is_coordinate_equal(next_pos, enemy_pos.position)):
                    is_move[i] = True
                    max_val_dirr[i] += enemy_pos.properties.diamonds
                elif(self.is_coordinate_can_tackle_by_enemy(next_pos, enemy_pos.position)):
                    max_val_dirr[i] = 0

        for i in range(4):
            if(max_val_dirr[i] > max_global_value):
                max_global_value = max_val_dirr[i]
                value_move = i

        if(max_global_value == current_score_inven):
            for i in range(4):
                if(self.is_available_to_move(current_position, self.directions[i][0], self.directions[i][1], width, height)):
                    value_move = i
                    break
        
        delta_x = self.directions[value_move][0]
        delta_y = self.directions[value_move][1]

        props = board_bot.properties
        # Analyze new state
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
