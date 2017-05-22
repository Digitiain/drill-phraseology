$("#addSectionBtn").click(addSquad);

var squadNumber = 2

function addSquad() {
  var newSquad = '<div id="squad' + squadNumber + '"><label for="squad' + squadNumber + 'Command">Quad ' + squadNumber + ' command:</label><input type="text" class="form-control" id="squad' + squadNumber + 'Command" placeholder="Turning by numbers, RIGHT TURN - ONE"><label for="squad' + squadNumber + 'Timings">Quad ' + squadNumber + ' timings:</label> <input type="text" class="form-control" id="squad' + squadNumber + 'Timings" placeholder="ONE"><label for="squad' + squadNumber + 'Immediately">Quad ' + squadNumber + ' immediately actions:</label><input type="text" class="form-control" id="squad' + squadNumber + 'Immediately" placeholder="I forced my body through 90 degrees to the right..."></div><label for="squad' + squadNumber + 'PTN">Squad ' + squadNumber + ' points to note:</label><input type="text" class="form-control" id="squad' + squadNumber + 'PTN" placeholder="I have returned to the correct position of attention"><label for="squad' + squadNumber + 'Position">Quad ' + squadNumber + ' position:<br />("Adopt the position of...")</label><input type="text" class="form-control" id="squad' + squadNumber + 'Position" placeholder="Attention"><label for="squad' + squadNumber + 'FallIn">Squad ' + squadNumber + ' fall-in location:</label><input type="text" class="form-control" id="squad' + squadNumber + 'FallIn" placeholder="Centre">';
  $("#squads").append(newSquad);
  squadNumber += 1;
}

function printPage() {
  window.print();
}
