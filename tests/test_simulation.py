import unittest
from src.core.simulation import WindFlow

class TestWindFlow(unittest.TestCase):

    def setUp(self):
        self.wind_flow = WindFlow(grid_size=(10, 10))

    def test_initialization(self):
        self.assertEqual(self.wind_flow.grid_size, (10, 10))
        self.assertIsNotNone(self.wind_flow.velocities)

    def test_update_velocities(self):
        initial_velocities = self.wind_flow.velocities.copy()
        self.wind_flow.update_velocities()
        self.assertNotEqual(initial_velocities.tolist(), self.wind_flow.velocities.tolist())

    def test_boundary_conditions(self):
        self.wind_flow.apply_boundary_conditions()
        # Assuming boundary conditions set velocities to zero at the edges
        self.assertTrue((self.wind_flow.velocities[0] == 0).all())
        self.assertTrue((self.wind_flow.velocities[-1] == 0).all())
        self.assertTrue((self.wind_flow.velocities[:, 0] == 0).all())
        self.assertTrue((self.wind_flow.velocities[:, -1] == 0).all())

if __name__ == '__main__':
    unittest.main()