import sys
import time
import json
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple, Union
from game import Game, LeaderboardEntry

LEADERBOARD_FILE = "leaderboard.json"

def typewriter_effect(text: str) -> None:
    """Displays text with a typewriter animation effect.

    Args:
        text (str): The text to display.
    """
    # Animation typewriter effect for the texts
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.5)

def load_predefined_level(level: int) -> List[List[str]]:
    """Loads a predefined level from a JSON file.

    Args:
        level (int): The level to load.

    Returns:
        List[List[str]]: The grid representation of the level.
    """
    WALL = "🧱"
    GRASS = "🟩"
    EGG = "🥚"
    EMPTY_NEST = "🪹"
    FULL_NEST = "🐣"
    FRYING_PAN = "🍳"

    try:
        # Open and load the levels from a JSON file
        with open("levels.json", "r", encoding="utf-8") as file:
            levels_data = json.load(file)

        # Get the level grid
        if str(level) in levels_data["levels"]:
            os.system('clear')  # Clear the screen before showing the grid
            typewriter_effect(f"LEVEL {level}\n")
            grid = levels_data["levels"][str(level)]
        else:
            # Default to level 1 if an invalid level is provided
            print("Invalid level, loading level 1.")
            grid = levels_data["levels"]["1"]
    except FileNotFoundError:
        raise FileNotFoundError("The levels.json file was not found.")
    except json.JSONDecodeError:
        raise ValueError("The levels.json file is not properly formatted.")

    return grid

def load_special_challenge(challenge: str) -> List[List[str]]:
    """Loads a special challenge from a JSON file.

    Args:
        challenge (str): The challenge to load.

    Returns:
        List[List[str]]: The grid representation of the challenge.
    """
    WALL = "🧱"
    GRASS = "🟩"
    EGG = "🥚"
    EMPTY_NEST = "🪹"
    FULL_NEST = "🐣"
    FRYING_PAN = "🍳"

    try:
        with open("special_levels.json", "r", encoding="utf-8") as file:
            levels_data = json.load(file)

        if challenge in levels_data["special_levels"]:
            os.system('clear')
            typewriter_effect(f"SPECIAL CHALLENGE {challenge}\n")
            grid = levels_data["special_levels"][challenge]
        else:
            print("Invalid challenge, loading challenge A.")
            grid = levels_data["special_levels"]["A"]
    except FileNotFoundError:
        raise FileNotFoundError("The special_levels.json file was not found.")
    except json.JSONDecodeError:
        raise ValueError("The special_levels.json file is not properly formatted.")

    return grid

def display_grid(grid: List[List[str]], moves: List[str], remaining_moves: int, points: int) -> None:
    """Displays the game grid and related information.

    Args:
        grid (List[List[str]]): The grid representation of the current level.
        moves (List[str]): A list of previous moves.
        remaining_moves (int): The number of remaining moves.
        points (int): The player's current points.
    """
    os.system('clear')  # Clear the screen before displaying
    for row in grid:
        print(" ".join(row))
    print(f"\nPrevious moves: {' '.join(moves)}")
    print(f"Remaining moves: {remaining_moves}")
    print(f"Points: {points}\n")

def tilt_grid(grid: List[List[str]], direction: str) -> Union[Tuple[List[List[str]], bool, bool], Tuple[str, bool, bool]]:
    """Tilts the grid in the specified direction, moving eggs and handling game mechanics.

    Args:
        grid (List[List[str]]): The current grid representation of the game level.
        direction (str): The direction to tilt ('L', 'R', 'U', 'D').

    Returns:
        Union[Tuple[List[List[str]], bool, bool], Tuple[str, bool, bool]]:
            If the game continues:
                - Updated grid after tilting
                - A flag indicating if any egg reached a nest
                - A flag indicating if any egg moved
            If the game is lost:
                - "LOSE"
                - False (egg in nest flag)
                - A flag indicating if any egg moved
    """
    size = len(grid)
    moved = False
    egg_in_nest = False

    # Define movement offsets based on the direction
    offsets = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0),
    }

    if direction not in offsets:
        raise ValueError(f"Invalid direction '{direction}'. Must be one of 'L', 'R', 'U', 'D'.")

    row_start, row_end, row_step = (1, size - 1, 1) if direction in ['L', 'U'] else (size - 2, 0, -1)
    col_start, col_end, col_step = (1, size - 1, 1) if direction in ['U', 'L'] else (size - 2, 0, -1)

    row_range = range(row_start, row_end, row_step)
    col_range = range(col_start, col_end, col_step)

    row_offset, col_offset = offsets[direction]

    for row in row_range:
        for col in col_range:
            if grid[row][col] == "🥚":
                current_row, current_col = row, col

                while (
                    1 <= current_row + row_offset < size - 1
                    and 1 <= current_col + col_offset < size - 1
                    and grid[current_row + row_offset][current_col + col_offset] == "🟩"
                ):
                    # Move egg
                    grid[current_row][current_col], grid[current_row + row_offset][current_col + col_offset] = \
                        grid[current_row + row_offset][current_col + col_offset], grid[current_row][current_col]
                    current_row += row_offset
                    current_col += col_offset
                    display_grid(grid, [], 0, 0)
                    time.sleep(0.2)
                    moved = True

                # Check destination cell
                destination_cell = grid[current_row + row_offset][current_col + col_offset]
                if destination_cell == "🪹":
                    grid[current_row + row_offset][current_col + col_offset] = "🐣"
                    grid[current_row][current_col] = "🟩"
                    egg_in_nest = True
                elif destination_cell == "🍳":
                    return "LOSE", False, moved

    return grid, egg_in_nest, moved

def all_eggs_in_nests(grid: List[List[str]]) -> bool:
    """Checks if all eggs are in nests.

    Args:
        grid (List[List[str]]): The grid representation of the current level.

    Returns:
        bool: True if all eggs are in nests, False otherwise.
    """
    
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:  # Open the leaderboard file for writing
        json.dump(leaderboard, file)  # Write the leaderboard data as a JSON string to the file
        
def load_leaderboard() -> List[dict]:
    """Loads the leaderboard from a JSON file.

    Returns:
        List[dict]: A list of leaderboard entries.
    """
    leaderboard_file = "leaderboard.json"

    # Check if the leaderboard file exists and is not empty
    if os.path.exists(leaderboard_file):
        try:
            with open(leaderboard_file, "r", encoding="utf-8") as file:
                # Attempt to load the data as JSON
                return json.load(file)
        except json.JSONDecodeError:
            # If there's an error, print a message and return an empty list
            print("Error: Corrupted leaderboard file. Returning empty leaderboard.")
            return []
    else:
        # If the file doesn't exist, return an empty list
        print("Leaderboard file not found. Returning empty leaderboard.")
        return []

def update_leaderboard(player_name: str, score: int) -> None:
    """Updates the leaderboard with a player's score.

    If the player already exists, their highest score is kept.

    Args:
        player_name (str): The name of the player.
        score (int): The player's score to update.
    """
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as file:
            leaderboard = json.load(file)

        if not isinstance(leaderboard, dict):
            leaderboard = {}
    except (FileNotFoundError, json.JSONDecodeError):
        leaderboard = {}

    leaderboard[player_name] = max(leaderboard.get(player_name, 0), score)

    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as file:
        json.dump(leaderboard, file, indent=4)
        
def display_leaderboard() -> None:
    """Displays the leaderboard sorted by scores in descending order."""
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as file:
            leaderboard = json.load(file)

        if not isinstance(leaderboard, dict):
            print("Leaderboard data is corrupted. Resetting leaderboard.")
            leaderboard = {}
    except (FileNotFoundError, json.JSONDecodeError):
        print("No leaderboard data found. Play a game to create a leaderboard.")
        return

    if not leaderboard:
        print("Leaderboard is empty! Play a game to add scores.")
        return

    print("\nLeaderboard:")
    for player, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {score}")

def game_loop(player_name: str):
    """Main game loop for handling gameplay and leaderboard updates."""
    def save_and_exit(points: int) -> str:
        """Handle saving the score to the leaderboard and exiting."""
        save_game = input(f"Do you wish to save your score of {points} to the leaderboard? (Y/N): ").strip().upper()
        if save_game == "Y":
            os.system('clear')
            update_leaderboard(player_name, points)
            print("Your score has been saved!\n")
        print("Returning to the main menu...")
        time.sleep(1)
        os.system('clear')
        return "QUIT"

    print("Choose a starting level (1-10): ")

    try:
        current_level = int(input().strip())
        if current_level not in range(1, 11):
            print("Invalid level choice. Defaulting to level 1.")
            current_level = 1
    except ValueError:
        print("Invalid input. Defaulting to level 1.")
        current_level = 1

    points = 0

    while True:
        try:
            grid = load_predefined_level(current_level)
        except KeyError:
            print("Congratulations! You completed all levels!")
            return save_and_exit(points)

        moves = []
        remaining_moves = 10
        history = []

        while remaining_moves > 0:
            display_grid(grid, moves, remaining_moves, points)
            move = input("Tilt the grid (L, R, U, D, type 'X' to undo, or 1 to quit): ").strip().upper()

            if move == "1":
                os.system('clear')
                confirm_quit = input("Are you sure you want to quit the game? Enter 1 to confirm or 2 to cancel: ").strip().upper()
                if confirm_quit == "1":
                    os.system('clear')
                    return save_and_exit(points)
                elif confirm_quit == "2":
                    os.system('clear')
                    print("Returning to the current level...")
                    continue

            if move == "X":
                if history:
                    grid, moves, remaining_moves, points = history.pop()
                    print("Undo successful!")
                else:
                    print("No moves to undo!")
                continue

            if move not in {'L', 'R', 'U', 'D'}:
                print("Invalid input. Please enter L, R, U, D, or X.")
                continue

            history.append(([row[:] for row in grid], moves[:], remaining_moves, points))

            result, egg_in_nest, moved = tilt_grid(grid, move)
            moves.append(move)
            remaining_moves -= 1

            if result == "LOSE":
                points -= 10
                display_grid(grid, moves, remaining_moves, points)
                print("You lose! An egg landed in a frying pan!\n")
                while True:
                    choice = input("Restart the level (R) or quit to the main menu (Q)? ").strip().upper()
                    if choice == "R":
                        os.system('clear')
                        break
                    elif choice == "Q":
                        os.system('clear')
                        return save_and_exit(points)

            if not moved:
                print("No eggs could be moved in that direction.")

            if egg_in_nest:
                points += 10 * current_level

            all_eggs_in_nests = all(cell != "🥚" for row in grid for cell in row)
            if all_eggs_in_nests:
                points += remaining_moves * current_level
                display_grid(grid, moves, remaining_moves, points)
                print(f"Congratulations! You completed Level {current_level}!\n")
                time.sleep(1)
                break

            if remaining_moves == 0:
                print("Out of moves! Game over.\n")
                os.system('clear')
                while True:
                    choice = input("Restart the level (R) or quit to the main menu (Q)? ").strip().upper()
                    if choice == "R":
                        os.system('clear')
                        break
                    elif choice == "Q":
                        os.system('clear')
                        return save_and_exit(points)

        if current_level == 10:
            os.system('clear')
            print("Congratulations! You've mastered all levels of the game!\n")
            os.system('clear')
            return save_and_exit(points)

        current_level += 1
        print(f"Proceeding to Level {current_level}...\n")

def how_to_play():
    # This function just involves all text and it only uses the clear screen, typewriter animation, and print function
    os.system('clear')
    typewriter_effect("Welcome to Egg Roll, Eggsecutor!\n")
    typewriter_effect("Your general mission here is to guide the eggs into their nests while avoiding frying pans, all within a limited number of moves. Here's how to play:\n")
    print('-'*40 + "\n") 

    typewriter_effect("GAMEPLAY OVERVIEW\n")
    print("The game takes place on a 2D grid with at least 4 rows and 4 columns.")
    print("Your goal is to roll eggs into empty nests to score points!")
    print("Eggs move by tilting the grid in one of four directions:")
    print("(L) Left, (R) Right, (U) Forward, (D) Backward")
    typewriter_effect("\n")

    typewriter_effect("OBJECTS IN THE GAME\n")
    print("Wall 🧱: Blocks the eggs from rolling further.")
    print("Egg 🥚: Needs to be guided into an empty nest.")
    print("Grass 🟩: An open space where eggs can roll freely.")
    print("Empty Nest 🪹: Place eggs here to score points.")
    print("Full Nest 🪺: Holds one egg and blocks others from entering.")
    print("Frying Pan 🍳: Avoid these! Eggs will cook and disappear, costing you points.")
    typewriter_effect("\n")

    typewriter_effect("RULES OF THE GAME\n")
    print("1. Tilting the Grid:")
    print("   Each move tilts the grid in one direction, and all eggs roll")
    print("   until they hit a wall, another egg, or a frying pan.")
    print("2. Scoring Points:")
    print("   Place an egg into an empty nest to gain points.")
    print("   Earn bonus points for leftover moves when the nest is filled.")
    print("3. Avoid Frying Pans:")
    print("   If an egg rolls into a frying pan, it gets cooked, and you lose points.")
    print("4. Level Completion:")
    print("   A level ends when all eggs are in nests or cooked, or when moves run out.")
    typewriter_effect("\n")

    typewriter_effect("STRATEGY TIPS\n")
    print("1. Plan ahead to minimize moves and maximize points!")
    print("2. Use walls and full nests to strategically stop eggs from rolling too far.")
    print("3. Avoid frying pans at all costs to save your points.")
    typewriter_effect("\n")

    typewriter_effect("Are you ready to tilt, roll, and nest? Let’s get cracking! 🥚🔥\n")

    print("\nPress 1 to return to the main menu.")
    choice = input("Your choice: ").strip()

    if choice == "1":
        os.system('clear')
        return True  # Indicate the user wants to return to the main menu
    else:
        print("Invalid choice. Returning to the main menu.")
        return True  # Also return True in case of an invalid choice to return to the main menu
        
def about_game():
    # same as how to play, this function just involves all text and it only uses the clear screen, typewriter animation, and print function
    os.system('clear')
    typewriter_effect("About the Game: Egg Roll v1.7.1\n")
    print('-'*40)

    typewriter_effect("Game Title: Egg Roll\n")
    print("Egg Roll is a fun and engaging puzzle game where you guide eggs into their nests while avoiding frying pans and obstacles.")
    print("Each level presents a unique challenge where careful planning and strategy are required to succeed.")
    typewriter_effect("\n")

    typewriter_effect("Developer Information\n")
    print("Game Developer: Keefe Aldwin C. Magdato")
    print("Program: 1st Year BS Computer Science student at the University of the Philippines Diliman (UP Diliman)")
    typewriter_effect("\n")

    typewriter_effect("Submission Details\n")
    print("This game was created as a submission for a Machine Problem in CS 11: Introduction to Computer Science.")
    print("The project aims to showcase the application of basic programming concepts like grids, movement, and basic game mechanics.")
    typewriter_effect("\n")

    typewriter_effect("Acknowledgments\n")
    print("Special thanks to the faculty of CS 11 for the guidance and support throughout the project!")
    print('-'*40)

    print("\nPress 1 to return to the main menu.")
    choice = input("Your choice: ").strip()

    if choice == "1":
        os.system('clear')
        return True  # Indicate the user wants to return to the main menu
    else:
        print("Invalid choice. Returning to the main menu.")
        return True  # Also return True in case of an invalid choice to return to the main menu

def main_menu():
    os.system('clear')

    # Define the menu options that will be presented to the user
    menu_items = ["(1) Play",  # Option to start the game
                  "(2) How to Play",  # Option to display game instructions
                  "(3) Leaderboard",  # Option to view the leaderboard
                  "(4) About",  # Option to display game information
                  "(5) Exit"]  # Option to exit the game

    while True:
        print('-' * 40)                   
        typewriter_effect("EGG ROLL v1.7.1\n")
        typewriter_effect("Ready to roll, Eggsecutor? 🥚🔥 Let’s crack the competition!\n")
        print('-' * 40)

        for item in menu_items:
            typewriter_effect(item + "\n")
        print('-' * 40)
        # Prompt the user for input to choose an option
        choice = input('Please enter your choice: ').strip()

        if choice == "1":  # Play
            os.system('clear')
            player_name = input("Enter your name: ").strip()
            os.system('clear')

            if not player_name:  # Default to 'Player' if no name is entered
                print("Name cannot be empty! Defaulting to 'Player'.")
                player_name = "Player"

            typewriter_effect(f"Welcome, {player_name}! Get ready to roll...\n")
            time.sleep(1)
            os.system('clear')

            result = game_loop(player_name)  # Pass the player's name to game_loop
            if result == "QUIT":  # If the player chooses to quit during the game
                continue  # Return to the main menu
            
        elif choice == "2":  # How to Play
            os.system('clear')
            print("\n" + "-" * 40)
            typewriter_effect("Entering How to Play...\n")
            print("-" * 40 + "\n")
            time.sleep(1)
            os.system('clear')
            if how_to_play():  # Assuming this function exists
                continue  # Return to the main menu if the user presses 1
            
        elif choice == "3":  # Show leaderboard
            os.system('clear')
            print("\n" + "-" * 40)
            display_leaderboard()  # Assuming this function exists
            print("\n" + "-" * 40)
            input("Press Enter to return to the main menu...")
            os.system('clear')
            
        elif choice == "4":  # About Game
            os.system('clear')
            print("\n" + "-" * 40)
            typewriter_effect("Entering About Game...\n")
            print("-" * 40)
            time.sleep(1)
            os.system('clear')
            if about_game():  # Assuming this function exists
                continue  # Return to the main menu
            
        elif choice == "5":  # Exit
            os.system('clear')
            typewriter_effect("Thank you for playing Egg Roll! Goodbye!\n")
            break  # Exit the program
            
        else:  # Invalid choice
            os.system('clear')
            typewriter_effect("Invalid choice. Please try again.\n")
            time.sleep(1)
            os.system('clear')
   
main_menu()  # Start the game






''' UNIT TEST'''

from game import Game, GameState, Tile
from typing import List

def test_game_initialization():
    """Test the initialization of the Game class."""
    game = Game()
    assert isinstance(game.leaderboard, dict), "Leaderboard should be initialized as a dictionary."
    assert isinstance(game.levels, dict), "Levels should be initialized as a dictionary."

def test_load_level():
    """Test loading a predefined level."""
    game = Game()
    game.load_levels()
    level = game.get_level(1)
    assert isinstance(level, list), "Loaded level should be a list of lists."
    assert len(level) > 0, "Loaded level should have a grid."

def test_save_and_load_leaderboard():
    """Test saving and loading the leaderboard."""
    game = Game()
    test_leaderboard = {"Alice": 150, "Bob": 200}
    game.leaderboard = test_leaderboard
    game.save_leaderboard()

    game.load_leaderboard()
    assert game.leaderboard == test_leaderboard, "Leaderboard should be saved and loaded correctly."

def test_update_leaderboard():
    """Test updating the leaderboard with a new score."""
    game = Game()
    game.add_leaderboard_entry("TestPlayer", 300)
    assert game.leaderboard["TestPlayer"] == 300, "Player's score should be updated in the leaderboard."
    game.add_leaderboard_entry("TestPlayer", 250)
    assert game.leaderboard["TestPlayer"] == 300, "Player's score should not decrease."

def test_check_victory():
    """Test the victory condition."""
    grid: List[List[Tile]] = [
        [Tile.GRASS, Tile.GRASS, Tile.GRASS],
        [Tile.GRASS, Tile.EMPTY_NEST, Tile.GRASS],
        [Tile.GRASS, Tile.GRASS, Tile.GRASS]
    ]
    state = GameState(grid=grid)
    assert all(cell != Tile.EGG for row in state.grid for cell in row), "Victory condition should return True when all eggs are in nests."

def test_tilt_grid():
    """Test tilting the grid in different directions."""
    grid = [
        [Tile.GRASS, Tile.GRASS, Tile.GRASS, Tile.GRASS],
        [Tile.GRASS, Tile.EGG, Tile.GRASS, Tile.EMPTY_NEST],
        [Tile.GRASS, Tile.GRASS, Tile.GRASS, Tile.GRASS]
    ]
    state = GameState(grid=grid)
    game = Game()

    # Placeholder for tilt logic in update_game_state
    new_state = game.update_game_state(state, "L")
    assert isinstance(new_state, GameState), "Game state should be updated correctly."

if __name__ == "__main__":
    test_game_initialization()
    test_load_level()
    test_save_and_load_leaderboard()
    test_update_leaderboard()
    test_check_victory()
    test_tilt_grid()
    print("All tests passed!")
