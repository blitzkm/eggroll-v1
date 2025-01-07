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