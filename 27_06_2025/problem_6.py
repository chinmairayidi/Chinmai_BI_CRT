'''
campus open MIC regestration and votiing system

problem statement:
build a system for handling regestration and voting during collage open mic event .
user register as performance or audience. audience 


'''
from collections import deque
import matplotlib.pyplot as plt
class Openmic:
    def __init__(self):
        self.performance = []
        self.audience = set()
        self.queue = deque()
        self.votes = {}
        self.voted = {}
    def register(self,name,role):
        if role == "performer" and name not in self.performance:
            self.add_performance(name)
        elif role == "audience" and name not in self.audience:
            self.audience.add(name)
            self.voted[name] = set()
    def start(self):
        while self.queue:
            p = self.queue.popleft()
            for a in self.audience:
                if p not in self.voted[a]:
                    vote = input(f"{a}, do you want to vote for {p}? (yes/no): ")
                    if vote.lower() == "yes":
                        self.votes[p] += 1
                        self.voted[a].add(p)
    def winner(self):
        max_v= max(self.votes.values())
        for p in self.votes:
            if self.votes[p] == max_v:
                print(f"winner: {p} with {max_v} votes")
    def save(self, filename="votes.txt"):
        with open(filename, "w") as f:
            for p in self.performance:
                f.write(f"{p}: {self.votes[p]}votes\n")
    def chart(self):
        names, counts = zip(*self.votes.items())
        plt.bar(names, counts)
        plt.xlabel("Performers")
        plt.ylabel("Votes")
        plt.title("---Vote counts----")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
o = Openmic()
o.register("Alice", "performer")
o.register("Bob", "performer")  
o.register("Charlie", "audience")
o.register("David", "audience")
o.start()
o.winner()
o.save()
o.chart()