import unittest
from src.visualization.plot import create_streamplot
from src.visualization.renderer import render_floor_plan

class TestVisualization(unittest.TestCase):

    def test_create_streamplot(self):
        # Test the creation of a streamplot with dummy data
        wind_vectors = [[(0, 0), (1, 1)], [(1, 1), (2, 2)]]
        fig, ax = create_streamplot(wind_vectors)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)

    def test_render_floor_plan(self):
        # Test rendering a simple floor plan
        floor_plan = {
            'walls': [(0, 0, 0, 10), (0, 10, 10, 10)],
            'windows': [(0, 5, 2, 1)]
        }
        fig, ax = render_floor_plan(floor_plan)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)

if __name__ == '__main__':
    unittest.main()