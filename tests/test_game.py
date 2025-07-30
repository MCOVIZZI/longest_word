 def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False


    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched
