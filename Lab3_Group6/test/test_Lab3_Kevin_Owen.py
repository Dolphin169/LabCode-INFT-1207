import unittest
from Lab3_Group6.app.Lab3_Kevin_Owen import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(1,9,5), 25.0)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-11,0,100)

    def test_ellipse_area_valid(self):
        self.assertEqual(ellipse_area(20, 15), 942.4777960769379)


    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-20, "a")


    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(11,3), 16.5)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-1, 10000)


if __name__ == "__main__":
    unittest.main()