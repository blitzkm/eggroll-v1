MP_Magdato

🍳 Keefe Aldwin C. MAGDATO Egg Roll Game🍳

OVERVIEW
Game Title: Egg Roll

Introduction
Welcome to Egg Roll, a fun and engaging terminal-based puzzle game. Your mission is to guide the eggs safely into their nests while avoiding frying pans and walls—all within a limited number of moves. Each level presents unique challenges that will test your planning and problem-solving skills. Are you ready to roll, Eggsecutor? Let’s crack the competition! 🐣

GRID MATERIALS
The grid is made up of six distinct tiles, each represented by an emoji:

1. Eggs (🥚): Roll continuously in the direction the grid is tilted until blocked.
2. Grass Tiles (🟩): Allow eggs to roll across them without resistance.
3. Walls (🧱): Block the path of eggs, preventing movement.
4. Frying Pans (🍳): Cook and remove any egg they touch.
5. Empty Nests (🪹): Become filled when an egg rolls into them, increasing your score.
6. Filled Nests (🪺): Act as walls but are part of the win condition.

FEATURES
1. Dynamic Gameplay: Tilt the grid to roll eggs into nests and avoid frying pans.
2. Challenging Levels: 10 levels, each progressively harder.
3. Leaderboard: Compete for the top score and track your progress.
4. Interactive Menus: Learn how to play, view your scores, and explore options.
5. Undo Feature: Use the undo feature to revert your last move if you make a mistake.
6. Save/Load Game State: Pause and resume gameplay, preserving your progress.

NEW FEATURE:
2 MODES:
1. Normal Mode: Contains 10 levels that is relatively easy and serves as the backbone of the game.
2. Special Challenges: This mode contains 3 special challenges that are unique and realtively difficult than the normal mode. It has the following challenges:
    (1) EGGXCELLENT EGGROLLER
    (2) Ma-EGGo sa HEART? 
    (3) The Amazing EGGRACE

HOW TO PLAY
1. Objective: Roll the eggs 🥚 into their nests 🪹 by tilting the grid (L, R, U, D).
2. Avoid Frying Pans 🍳: Eggs that hit frying pans are cooked, costing points.
3. Limited Moves: Plan your moves wisely to score bonus points for leftover moves.
4. Level Completion: Finish a level when all eggs are nested or when you run out of moves or eggs.

SCORING SYSTEM
Each egg that fills an empty nest awards points calculated as 10 + (number of remaining moves). The game ends when all empty nests are filled or when you run out of moves or eggs.

How to Run the Game
1. Clone or Download: Obtain the game files from the repository or download them as a ZIP archive.
2. Navigate: Open your terminal or command prompt and navigate to the folder containing eggroll.py.
3. Run the Game: Type python eggroll.py and press Enter.

Controls
1. Tilt the Grid: Use L, R, U, or D to move eggs left, right, up, or down.
2. Undo a Move: Press X to undo the last move.
3. Quit the Game: Enter 1 to exit at any time.

Code Organization and Algorithm Explanation

Code Structure
1. eggroll.py: The main game logic and user interface, responsible for running the game loop, handling user input, and updating the game state.
2. game.py: Contains the main game mechanics, integrating the leaderboard and stages. Responsible for gameplay logic.
3. test_main.py: Contains all the necessary tests for the code.
4. Unit_Test.py: Test the specific functionalities of the program.
5. levels.json: Stores predefined level layouts, including the placement of eggs, nests, walls, and frying pans.
6. leaderboard.json: Keeps track of player scores and rank.
7. Change_log.md: Shows the progress of the code and serves as journal to the coder.
8. special_levels.json: Containes all the levels in the special challenge mode


How the Algorithm Works
1. Loading Levels: The game reads the levels.json file to initialize the grid for each level.
2. User Input: The player inputs commands to tilt the grid, undo a move, or quit.
3. Grid Updates: The algorithm moves eggs in the specified direction, checking for collisions with walls, nests, and frying pans.
4. Game State Check: After each move, the algorithm checks if all eggs are in nests, if any eggs are cooked, or if moves are exhausted.
5. Scoring: Points are awarded based on the number of eggs placed in nests and the number of moves left.

Unit Tests Overview

Test Suite Details
The tests are located in test_main.py and include:

1. display_colored_message: Ensures color-coded messages display correctly.
2. load_predefined_level: Verifies that levels load properly from levels.json.
3. tilt_grid: Checks if the grid tilts in the correct direction and updates the state.
4. all_eggs_in_nests: Confirms that the game correctly identifies when all eggs are in nests.
5. save_leaderboard: Tests the saving of leaderboard data to leaderboard.json.
6. load_leaderboard: Ensures leaderboard data is loaded correctly.
7. update_leaderboard: Verifies that leaderboard scores are updated as expected.
8. display_leaderboard: Checks if the leaderboard displays properly on the screen.

Running the Tests
To run the unit tests, execute the following command in your terminal:
"python3.12 test_main.py"

These tests cover key aspects of the game's functionality:
1. Game Mechanics: Grid movement, collision detection, and scoring.
2. Data Handling: Loading and saving levels and leaderboard data.
3. User Interface: Displaying messages and leaderboards correctly.
Adding New Tests
4. To add new tests, follow the pattern of existing functions. Create a new function within test_main.py, and use Python's unittest methods such as assertEqual() and assertTrue() to validate the expected behavior.

Bonus Features
The following features have been added and should be credited for bonus points:

1. Dynamic Level Progression: New levels are unlocked as the player progresses.
2. Undo Feature: Players can undo the last move to correct mistakes.
3. Save/Load Game State: Players can save their progress and resume later.
4. Leaderboard Functionality: Tracks high scores and displays them in an interactive menu.

Running the Game
To run the unit tests, execute the following command in your terminal:

bash
Copy code
python3.12 Eggroll_MP_Extension.py


Acknowledgements
This game was developed as part of an academic project. Special thanks to my instructors and peers for their guidance and feedback.

Developer Information
Game Developer: Keefe Aldwin C. Magdato
Program: 1st Year BS Computer Science student at the University of the Philippines Diliman (UP Diliman)

Submission Details
This project was created as a submission for a Machine Problem in CS 11: Introduction to Computer Science.

LICENSE
Egg Roll is a project for educational purposes. Feel free to modify and share with proper attribution.
