//http://download.basecase.com/programming-test/defender-test.pdf
//http://jsfiddle.net/j0eboygz/1/

function paddleMoves(nearestRock) {
    var y = - parseInt(Math.tan(nearestRock.radians) * nearestRock.distance)
    var moves = [];
    var pos = y < 0 ? -1 : 1;
    y = Math.abs(y);

    for (i=0; i < y; i++) {
        moves.push(pos);
    }

    for (i=0; i < (nearestRock.distance - y); i++) {
        moves.push(0);
    }

  return moves
}

defender.start(
  function notify_player(rocks, paddle_y){ 
      var moves = [];
      var nearestRock = 0;

      for (var i = 1; i < rocks.length; i++) {
          if (rocks[i].distance < rocks[nearestRock].distance) {
              nearestRock = i;
          }
      }

      return paddleMoves(rocks[nearestRock]);
  }
);
