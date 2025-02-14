import unittest
from ICE3_Kevin.src.temperature_sensor import process_temperatures

class TestTemperatureSensor(unittest.TestCase):

    def test_process_temperatures(self):
        #New Cases
        self.assertEqual(process_temperatures([-50]),"Min: -50.0°C, Max: -50.0°C, Avg: -50.0°C")
        self.assertEqual(process_temperatures([150]), "Min: 150.0°C, Max: 150.0°C, Avg: 150.0°C")
        self.assertEqual(process_temperatures([-49, 149]), "Min: -49.0°C, Max: 149.0°C, Avg: 50.0°C")
        self.assertRaises(Exception, process_temperatures([-60,20,160]))
        self.assertRaises(Exception, process_temperatures([20, "abc", 30]))
        self.assertRaises(Exception, process_temperatures([10, "@", -40]))
        self.assertRaises(Exception, process_temperatures([2**31 - 1, -2**31]))
        self.assertEqual(process_temperatures([50, 50, 50]), "Min: 50.0°C, Max: 50.0°C, Avg: 50.0°C")
        self.assertRaises(Exception, process_temperatures([]))

        #Cases from ICE 2
        self.assertEqual(process_temperatures([20]), "Min: 20.0°C, Max: 20.0°C, Avg: 20.0°C")
        self.assertEqual(process_temperatures([15,35]), "Min: 15.0°C, Max: 35.0°C, Avg: 25.0°C")
        self.assertRaises(Exception, process_temperatures([]))
        self.assertEqual(process_temperatures([10,-10,30]), "Min: -10.0°C, Max: 30.0°C, Avg: 10.0°C")
        self.assertEqual(process_temperatures([-50, 20, 150, 25]), "Min: -50.0°C, Max: 150.0°C, Avg: 36.25°C")
        self.assertRaises(Exception, process_temperatures([10, "abc", 30]))
        self.assertRaises(Exception, process_temperatures([2 ** 31 - 1, -2 ** 31]))
        self.assertEqual(process_temperatures([10,10,10]), "Min: 10.0°C, Max: 10.0°C, Avg: 10.0°C")
        self.assertRaises(Exception, process_temperatures(["asdf",12345,"!@#$%"]))
        self.assertRaises(Exception, process_temperatures(["Eight",9999999999999999999]))