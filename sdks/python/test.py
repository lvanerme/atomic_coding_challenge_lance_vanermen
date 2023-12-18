import unittest
import client

class TestGetMove(unittest.TestCase):
  def test_get_move_returns_a_valid_move(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 1, 0, 0, 0], 
             [0, 0, 0, 1, 1, 0, 0, 0], 
             [0, 0, 0, 2, 1, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual(client.get_move(2, board), [2, 3])

  # Test that player is checking all possible pieces to take
  def test_aggregate_pieces_taken(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 1, 0, 0, 0], 
             [0, 0, 0, 0, 1, 2, 0, 0], 
             [0, 0, 0, 1, 2, 0, 2, 0], 
             [0, 2, 2, 2, 1, 2, 2, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0]]
    # Client should return [4,7] because it has 4 pieces to take diaganolly and horizontally
    self.assertEqual(client.get_move(1, board), [4, 7])

    board = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 1, 0, 0, 0], 
             [0, 0, 0, 0, 1, 0, 0, 0], 
             [0, 0, 0, 1, 2, 0, 2, 0], 
             [0, 2, 2, 2, 1, 2, 2, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0]]
    # Client should return [4,7] because it has 4 pieces to take diaganolly and horizontally
    self.assertEqual(client.get_move(1, board), [4, 0])

  # Test that player will take a corner over other moves
  def test_corner_move(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 2, 0, 0, 0, 0], 
             [0, 0, 0, 2, 0, 0, 0, 0], 
             [0, 0, 0, 2, 0, 0, 0, 0], 
             [0, 0, 0, 1, 1, 0, 0, 0], 
             [0, 0, 1, 0, 0, 0, 0, 0], 
             [0, 2, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual(client.get_move(1, board), [7, 0])

    board = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 2, 0, 0, 0, 2], 
             [0, 0, 0, 2, 0, 0, 0, 1], 
             [0, 0, 0, 2, 0, 0, 0, 0], 
             [0, 0, 0, 1, 1, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual(client.get_move(1, board), [0, 7])

class TestPrepareResponse(unittest.TestCase):
  def test_prepare_response_returns_a_valid_response(self):
    self.assertEqual(client.prepare_response([2, 3]), b'[2, 3]\n')

if __name__ == '__main__':
  unittest.main()
