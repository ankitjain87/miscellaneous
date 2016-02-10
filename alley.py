
class Player(object):

    def __init__(self, id):
        self.id = id
        # self.name = name
        self.score = []

    def get_score(self):
        current_score = 0
        for _score in self.score:
            if 'x' in _score:
                current_score += 10 + 10
            elif '/' in _score:
                current_score += 10 + 5
            else:
                current_score += sum(_score)
        return current_score



class Lane(object):

    def __init__(self):
        self.players = []
        self.current_frame = 0
        self.current_player = None
        self.current_strike = 0

    def add_player(self):
        id = len(self.players) + 1
        player = Player(id)
        self.players.append(player)
        return id

    def print_scores(self):
        for player in self.players:
            print 'Player %s: Score Board - %s, Total - %s' % (str(player.id), player.score, str(player.get_score()))



if __name__  == '__main__':
    lane = Lane()

    n = int(raw_input())
    for i in range(n):
        lane.add_player()

    current_frame = 1
    current_player = 0
    while True:
        x = raw_input()
        if x == '' or x is None:
            break

        if lane.current_strike == 0 and current_player + 1 > len(lane.players):
            current_player = 0
            current_frame += 1

        player = lane.players[current_player]
        if x == 'x':
            score = ['x']
            player.score.append(score)
            lane.current_strike = 0
            current_player += 1
            continue
        elif x == '/':
            player.score[-1].append('/')
            lane.current_strike = 0
            current_player += 1
            continue
        else:
            x = int(x)
            if lane.current_strike == 0:
                score = [x]
                player.score.append(score)
                lane.current_strike = 1
            else:
                player.score[-1].append(x)
                lane.current_strike = 0
                current_player += 1

    if current_player == len(lane.players):
        current_player = 0

    print 'Current frame: ', current_frame
    print 'Last Player: ', lane.players[current_player].id
    print 'Last strike: ', lane.current_strike + 1
    lane.print_scores()





# Player 1 - [2 3] [4 /] [x] [x] => 2+3 + 4+6+5 + 10+10 + 10+10 => 60
# Player 2 - [1 2] [6 0] [3 /] [x]=> 1+2 + 6+0 + 3+7+5 + 10+10 => 44
# Player 3 - [4 6] [7 /] [x] [x] => 4+6 + 7+3+5 + 10+10 + 10+10 => 65

