import unittest
from eggroll import (
    load_predefined_level,
    tilt_grid,
    all_eggs_in_nests,
    save_leaderboard,
    load_leaderboard,
    update_leaderboard,
    display_leaderboard,
)

class GameLogicTests(unittest.TestCase):

    def test_load_predefined_level(self):
        """Test loading a predefined level."""
        level = 1
        grid = load_predefined_level(level)
        assert isinstance(grid, list), "Grid should be a list"
        assert len(grid) > 0, "Grid should not be empty"
        assert all(isinstance(row, list) for row in grid), "Each row should be a list"

    def test_tilt_grid(self):
        """Test tilting the grid in a direction."""
        grid = [["🟩", "🟩", "🟩"],
                ["🟩", "🥚", "🟩"],
                ["🟩", "🟩", "🟩"]]
        result, egg_in_nest, moved = tilt_grid(grid, 'L')
        assert moved, "Grid should have moved"
        assert not egg_in_nest, "No egg should be in a nest"
        assert grid[1][0] == "🥚", "Egg should move to the left"

    def test_all_eggs_in_nests(self):
        """Test if all eggs are in nests."""
        grid_with_eggs = [["🟩", "🟩", "🟩"],
                          ["🟩", "🥚", "🟩"],
                          ["🟩", "🟩", "🟩"]]
        grid_without_eggs = [["🟩", "🟩", "🟩"],
                             ["🟩", "🪹", "🟩"],
                             ["🟩", "🟩", "🟩"]]
        assert not all_eggs_in_nests(grid_with_eggs), "Should return False for grid with eggs"
        assert all_eggs_in_nests(grid_without_eggs), "Should return True for grid without eggs"

class LeaderboardTests(unittest.TestCase):

    def test_save_leaderboard(self):
        """Test saving leaderboard data."""
        leaderboard = {"Player1": 100}
        save_leaderboard(leaderboard)
        saved_data = load_leaderboard()  # Reload to verify
        assert saved_data == leaderboard, "Saved data should match the input"

    def test_load_leaderboard(self):
        """Test loading leaderboard data."""
        leaderboard = load_leaderboard()
        assert isinstance(leaderboard, dict), "Leaderboard should be a dictionary"
        assert "Player1" in leaderboard, "Leaderboard should contain Player1"

    def test_update_leaderboard(self):
        """Test updating leaderboard with a new score."""
        update_leaderboard("Player2", 150)
        leaderboard = load_leaderboard()
        assert leaderboard["Player2"] == 150, "Player2's score should be updated to 150"

    def test_display_leaderboard(self):
        """Test displaying the leaderboard."""
        leaderboard = {"Player1": 100, "Player2": 150}
        save_leaderboard(leaderboard)
        display_leaderboard()  # Manually verify display output

if __name__ == "__main__":
    unittest.main()


