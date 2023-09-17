class player:

  def play(self):
    print("the player is laying cricket")


class batsman(player):

  def play(self):
    print("the basman is batting")


class bowler(player):

  def play(self):
    print("the bowler is bowling")


bat = batsman()
bow = bowler()

bat.play()
bow.play()
