import unittest
from Lab3_Group6.app.Lab3_Kevin_Owen import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), 3.141592653589793)
        self.assertAlmostEqual(circle_area(5.5), 95.03317777109125)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(ValueError):
            circle_area(-10)
        with self.assertRaises(ValueError):
            circle_area(-1.8364)
        with self.assertRaises(ValueError):
            circle_area('afafhbafhafshj')
        with self.assertRaises(ValueError):
            circle_area("")

    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(1,9,5), 25.0)
        self.assertAlmostEqual(trapezium_area(0,0,0), 0)
        self.assertAlmostEqual(trapezium_area(2, 7, 0), 0)
        self.assertAlmostEqual(trapezium_area(1.74, 14.94, 17.736), 147.91824)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-11,0,100)
        with self.assertRaises(ValueError):
            trapezium_area(-1.56575, 124124124, -100)
        with self.assertRaises(ValueError):
            trapezium_area(11.2442, 'abd', 6482)
        with self.assertRaises(ValueError):
            trapezium_area("","","")

    def test_ellipse_area_valid(self):
        self.assertEqual(ellipse_area(20, 15), 942.4777960769379)
        self.assertAlmostEqual(ellipse_area(0,1), 0)
        self.assertAlmostEqual(ellipse_area(1, 0), 0)
        self.assertAlmostEqual(ellipse_area(5.657, 19), 337.66780318579174)
        self.assertAlmostEqual(ellipse_area(191, 10.94271794), 6566.114397506363)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-20, "a")
        with self.assertRaises(ValueError):
            ellipse_area(-20.748, 11)
        with self.assertRaises(ValueError):
            ellipse_area(11111, -144223)
        with self.assertRaises(ValueError):
            ellipse_area(1.4774, -991)
        with self.assertRaises(ValueError):
            ellipse_area("","")

    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(11,3), 16.5)
        self.assertAlmostEqual(rhombus_area(17,0), 0)
        self.assertAlmostEqual(rhombus_area(0, 13), 0)
        self.assertAlmostEqual(rhombus_area(5.5, 13.211), 36.33025)
        self.assertAlmostEqual(rhombus_area(191, 13), 1241.5)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-1, 10000)
        with self.assertRaises(ValueError):
            rhombus_area("asaswff", 10)
        with self.assertRaises(ValueError):
            rhombus_area(-1.2614813, 10.177482)
        with self.assertRaises(ValueError):
            rhombus_area(12.7474742, -1)
        with self.assertRaises(ValueError):
            rhombus_area("","")





if __name__ == "__main__":
    unittest.main()