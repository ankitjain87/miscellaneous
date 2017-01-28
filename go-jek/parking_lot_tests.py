import unittest

from parking_lot import ParkingLot


class TestParkingLot(unittest.TestCase):

    def test_park(self):
        parking_lot = ParkingLot(6)
        self.assertEqual(
            parking_lot.park('KA-01-HH-1234', 'Red'),
            'Allocated slot number: 1')
        self.assertEqual(
            parking_lot.park('KA-01-HH-5678', 'Black'),
            'Allocated slot number: 2')

    def test_get_reg_no_based_on_color(self):
        parking_lot = ParkingLot(6)
        parking_lot.park('KA-01-HH-1234', 'Blue')
        parking_lot.park('KA-01-HH-5678', 'White')
        self.assertEqual(
            parking_lot.get_reg_no_based_on_color('White'), 'KA-01-HH-5678')

    def test_get_slot_no(self):
        parking_lot = ParkingLot(6)
        parking_lot.park('KA-01-HH-1234', 'Blue')
        parking_lot.park('KA-01-HH-5678', 'White')
        self.assertEqual(parking_lot.get_slot_no('KA-01-HH-5678'), 2)

    def test_get_slot_no_based_on_color(self):
        parking_lot = ParkingLot(6)
        parking_lot.park('KA-01-HH-8675', 'Black')
        self.assertEqual(
            parking_lot.get_slot_no_based_on_color('Black'), '1')

    def test_leave_slot(self):
        parking_lot = ParkingLot(6)
        parking_lot.park('KA-01-HH-8675', 'Black')
        self.assertEqual(parking_lot.leave_slot(1), 'Slot number 1 is free.')

if __name__ == '__main__':
    unittest.main()