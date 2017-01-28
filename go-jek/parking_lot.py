import sys


class Slot(object):
    '''Parking slot with attributes id, level, registration no, level.'''
    def __init__(self, slot_id, reg_no, color, level=1):
        self.id = slot_id
        self.level = level
        self.reg_no = reg_no
        self.color = color


class ParkingLot(object):
    '''Parking lot class, with basic functionalities.'''
    empty_slots = []
    filled_slots = []

    def __init__(self, size):
        self.size = size
        for i in range(size, 0, -1):
            self.empty_slots.append(i)
        print "Created parking lot with %s slots" % str(size)

    def park(self, reg_no, color):
        '''Park the vehicle in the available slot.

        Args:
            reg_no: Vehicle registration number.
            color: Color of the vehicle.

        Returns:
            String: returns a message.
        '''
        if len(self.empty_slots) == 0:
            return "Sorry, parking lot is full."

        slot_id = self.empty_slots.pop()
        slot = Slot(slot_id, reg_no, color)
        self.filled_slots.append(slot)

        return "Allocated slot number: %s" % str(slot_id)

    def get_slot_no_based_on_color(self, color):
        '''Returns slot numbers of all slots where a car of a particular color is parked.

        Args:
            color: Color of the vehicle.

        Returns:
            List: Returns a list of slot ids.
        '''
        slots = []
        for i in self.filled_slots:
            if i.color == color:
                slots.append(str(i.id))

        slots = sorted(slots)
        return ", ".join(slots)

    def get_reg_no_based_on_color(self, color):
        '''Retuns registration numbers of all cars of a particular color.

        Args:
            color: Color of the vehicle.

        Returns:
            List: Returns a list of registration nos.
        '''
        reg_nos = []
        for i in self.filled_slots:
            if i.color == color:
                reg_nos.append(i.reg_no)

        reg_nos = sorted(reg_nos)
        return ", ".join(reg_nos)

    def get_slot_no(self, reg_no):
        '''Returns slot number in which a car with a given registration number is parked.

        Args:
            reg_no: Registration number of the vehicle.

        Returns:
            int: Slot id where the car is parked.
        '''
        for i in self.filled_slots:
            if i.reg_no == reg_no:
                return i.id

        return "Not found."

    def get_slot_id_index(self, slot_id):
        for i, j in enumerate(self.filled_slots):
            if j.id == slot_id:
                return i
        return -1

    def leave_slot(self, slot_id):
        '''Unpark the car from the slot.

        Args:
            slot_id: Slot id in the parking lot.

        Returns:
            String: Returns a message.
        '''
        if slot_id not in self.empty_slots:
            self.filled_slots.pop(
                self.get_slot_id_index(slot_id))
            self.empty_slots.append(slot_id)
            self.empty_slots = sorted(self.empty_slots, reverse=True)
            return "Slot number %s is free." % str(slot_id)
        else:
            return "No car parked in the slot %s" % str(slot_id)

    def parking_lot_status(self):
        '''Status of a parking lot at any given time.'''
        print "Slot No.", "\tRegistration No.", "\tColor"
        self.filled_slots = sorted(self.filled_slots, key=lambda slot: slot.id)
        for i in self.filled_slots:
            print "\t".join([str(i.id), i.reg_no, i.color])


def execute_command(parking_lot, command):
    if command[0] == 'create_parking_lot':
        parking_lot = ParkingLot(int(command[1]))
    elif command[0] == 'park':
        print parking_lot.park(command[1], command[2])
    elif command[0] == 'leave':
        print parking_lot.leave_slot(int(command[1]))
    elif command[0] == 'status':
        parking_lot.parking_lot_status()
    elif command[0] == 'registration_numbers_for_cars_with_colour':
        print parking_lot.get_reg_no_based_on_color(command[1])
    elif command[0] == 'slot_number_for_registration_number':
        print parking_lot.get_slot_no(command[1])
    elif command[0] == 'slot_numbers_for_cars_with_colour':
        print parking_lot.get_slot_no_based_on_color(command[1])
    else:
        print "Command not found"

    return parking_lot


def run_program(file_name=None):
    parking_lot = None
    try:
        if file_name:
            f = open(file_name, 'r')
            lines = f.readlines()
            for line in lines:
                command = line.strip().split(' ')
                parking_lot = execute_command(parking_lot, command)
        else:
            while True:
                print "Input:"
                command = raw_input().strip().split(' ')
                parking_lot = execute_command(parking_lot, command)

    except Exception as ex:
        if not parking_lot:
            print "Parking lot not created"
        else:
            print "Some problem in the command", command


if __name__  == '__main__':
    file_name = None
    if len(sys.argv) == 2:
        file_name = sys.argv[1]

    run_program(file_name)
