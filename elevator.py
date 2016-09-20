class Lift(object):

    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.direction = None # "UP", "DOWN"
        self.current_floor = 0
        self.up_queue = []
        self.down_queue = []
        self.state = 'STOPPED' # "RUNNING


    def add_new_request(self, direction, floor_no):
        if direction == "UP":
            self.up_queue.append(floor_no)
            self.up_queue = sorted(self.up_queue)
        else:
            self.down_queue.append(floor_no)
            self.down_queue = sorted(self.down_queue)

        if not self.direction:
            self.direction = direction

        if self.state == "STOPPED":
            self.state = "RUNNING"
            self.run()


    def find_next_stop(self):
        if self.direction == "UP":
            for i, j in enumerate(self.up_queue):
                if j >= self.current_floor:
                    return i, "UP"

            if self.down_queue:
                self.direction = "DOWN"
                return len(self.down_queue)-1, "DOWN"
            if self.up_queue:
                self.direction = "DOWN"
                return 0, "DOWN"
        else:
            for i, j in enumerate(self.down_queue):
                if j <= self.current_floor:
                    return i, "DOWN"

            if self.up_queue:
                self.direction = "UP"
                return 0, "UP"
            if self.down_queue:
                self.direction = "UP"
                return 0, "UP"

        self.state = "STOPPED"
        return None


    def run(self):
        while self.up_queue or self.down_queue:
            if self.state == "RUNNING":
                next_stop = self.find_next_stop()
                if next_stop:
                    if next_stop[1] == "UP":
                        pop = self.up_queue.pop(next_stop[0])
                    else:
                        pop = self.down_queue.pop(next_stop[0])

                    self.current_floor = pop
                    print pop, self.direction




lift = Lift(1, 10)
floors = [(2, "UP"), (5, "UP"), (2, "DOWN"), (6, "UP"), (7, "UP"), (5, "DOWN")]
# result - 2, 5, 6, 7, 5, 2
for i, j in floors:
    lift.add_new_request(j, i)

lift.run()
