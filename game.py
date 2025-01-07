import json
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict

LEADERBOARD_FILE = "leaderboard.json"
LEVELS_FILE = "levels.json"

class Tile(str, Enum):
    """Represents different types of tiles in the game grid."""
    WALL = "🧱"
    GRASS = "🟩"
    EGG = "🥚"
    EMPTY_NEST = "🪹"
    FULL_NEST = "🐣"
    FRYING_PAN = "🍳"

@dataclass
class LeaderboardEntry:
    """Represents an entry in the leaderboard."""
    name: str
    score: int

@dataclass
class GameState:
    """Represents the state of the game."""
    grid: List[List[Tile]]
    moves: List[str] = field(default_factory=list)
    remaining_moves: int = 10
    points: int = 0

@dataclass
class Game:
    """Handles the game mechanics, leaderboard, and levels."""
    leaderboard: Dict[str, int] = field(default_factory=dict)
    levels: Dict[int, List[List[Tile]]] = field(default_factory=dict)

    def __post_init__(self):
        self.load_leaderboard()
        self.load_levels()

    def load_leaderboard(self) -> None:
        """Loads the leaderboard from a file."""
        if os.path.exists(LEADERBOARD_FILE):
            try:
                with open(LEADERBOARD_FILE, "r", encoding="utf-8") as file:
                    self.leaderboard = json.load(file)
            except json.JSONDecodeError:
                self.leaderboard = {}
        else:
            self.leaderboard = {}

    def save_leaderboard(self) -> None:
        """Saves the leaderboard to a file."""
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as file:
            json.dump(self.leaderboard, file, indent=4)

    def add_leaderboard_entry(self, name: str, score: int) -> None:
        """Adds an entry to the leaderboard."""
        self.leaderboard[name] = max(score, self.leaderboard.get(name, 0))
        self.save_leaderboard()

    def load_levels(self) -> None:
        """Loads the levels from a file."""
        if os.path.exists(LEVELS_FILE):
            try:
                with open(LEVELS_FILE, "r", encoding="utf-8") as file:
                    levels_data = json.load(file).get("levels", {})
                    self.levels = {
                        int(level): [[Tile(cell) for cell in row] for row in grid]
                        for level, grid in levels_data.items()
                    }
            except json.JSONDecodeError:
                self.levels = {}
        else:
            self.levels = {}

    def get_level(self, level_id: int) -> List[List[Tile]]:
        """Gets the grid for a specific level."""
        return self.levels.get(level_id, [])

    def update_game_state(self, state: GameState, move: str) -> GameState:
        """Updates the game state based on a move."""
        # This should implement the actual grid movement logic
        return state
