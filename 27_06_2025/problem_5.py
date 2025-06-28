'''
design  a backend system to manage multiplayer game tournament,players redister play matches, and earn points, the system should rank them ,handle
tiebreaker and stimulate knockout roundds
----------------------------------------------------------
player registration within unique username
match results entry and automatic points updater
leaderboard sorted by scores
simulate knockout using recursion
export match history
----------------------------------------------------------
tech stack:
core python(list,dict,tuples)
oop(player,match,tournament classes)
recursion(knockout simultaion)
sorting algorithm(leaderboard)
file handliing(history logs)
optional:pandas for final score export
'''
import random
class player:
    def __init__ (self, username):
        self.username = username
        self.points = 0
class match:
    def __init__(self, player1, player2, winner):
        self.player1 = player1
        self.player2 = player2
        self.winner = winner
        if winner == player1:
            player1.points += 3
        elif winner == player2:
            player2.points += 3
        else:
            player1.points += 1
            player2.points += 1
class tournament:
    def __init__(self):
        self.players = {}
        self.history = []
    def register_player(self, username):
        if username not in self.players:
            self.players[username] = player(username)
            print(f"Player {username} registration is successful.")
        else:
            print(f"Username {username} was already taken.")
    def add_match_result(self,username1,username2, winner_username):
        if username1 in self.players and username2 in self.players:
            player1 = self.players[username1]
            player2 = self.players[username2]
            if winner_username == player1.username:
                winner = player1
            elif winner_username == player2.username:
                winner = player2
            else:
                print("the given username is invalid.")
                return
            match_result = match(player1, player2, winner)
            self.history.append(match_result)
            print(f"match result: {player1.username} vs {player2.username}, Winner: {winner.username}")
        else:
            print("players not registered.")
    def display_leaderboard(self): 
        sorted_players = sorted(self.players.values(), key=lambda p: p.points, reverse=True)
        for i, player in enumerate(sorted_players, start=1):
            print(f"{i}. {player.username} - {player.points} points")
    def simulate_knockout(self, players_list=None,round_num=1):
        if players_list is None:
            players_list = list(self.players.values())
        if len(players_list) % 2 != 0:
            print("even number of players are required .")
            return
        winners = []
        for i in range(0, len(players_list), 2):
            p1 = players_list[i]
            p2 = players_list[i + 1]
            winner =random.choice([p1, p2])
            winners.append(winner)
            self.add_match_result(p1, p2, winner) 
        if len(winners) ==1:
            print(f"champions: {winners[0].username}")
        else:
            self.simulate_knockout(winners, round_num + 1)
    def export_history(self, filename="match_history.txt"):
        with open(filename, "w") as f:
            for match in self.history:
                f.write(f"{match.player1.username} vs {match.player2.username}, Winner: {match.winner.username}\n")
                print(f"Match history exported to {filename}")
t= tournament()
t.register_player("alice")
t.register_player("bob")
t.register_player("charlie")
t.register_player("dave")
t.add_match_result("alice", "bob", "alice")
t.add_match_result("charlie", "dave", "charlie")
t.display_leaderboard()
t.simulate_knockout()
t.export_history("match_history.txt")