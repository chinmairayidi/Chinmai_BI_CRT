'''
you have attended a skill development program training for 15 days on python programming lanuage

TASK:
write a program to give the details report of 15 days python training which includes
1.Day
2.Topics covered
3.Efficiency (rate of efficanccy & grip on topics learnt on a scale of 5)
4.number of ssignment questions solved
5.number of hackerrank questions solved
6.Rating achived on hackerrank for the particuar day
7.certifications completeed(include name of certificates)
8.duration of class
9.rate the session on scale of 5

i]   1-being worst
ii]  2-being bad
iii] 3-good
iv]  4-verygood
v]   5-Excellent

'''

class training_report:
    def __init__(self,day,topic,efficiency,solved_assignments,hacker_rank_que_solved,hackerrank_achivements,certifications,duration,rating):
        self.day = day
        self.topics =topic
        self.efficiency=efficiency
        self.assignments_solved =solved_assignments
        self.hackerrank_questions=hacker_rank_que_solved
        self.hackerrank_rating =hackerrank_achivements
        self.certifications =certifications
        self.duration =duration
        self.session_rating =rating

    def display(self):
        print(f"--- Day {self.day}---")
        print(f"Topics Covered: {self.topics}")
        print(f"Efficiency on Scale of 5: {self.efficiency}")
        print(f"number of assignments solved: {self.hackerrank_questions}")
        print(f"Hackerrank rating:{self.hackerrank_rating}")
        print(f"certifications {self.certifications}")
        print(f"Duration of Class: {self.duration}")
        print(f"Session_Rating (1-being Worst to 5-Excellent): {self.session_rating}")
        
training =[
training_report(1, "Introduction to Python", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(2,"Variables, Data Types", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(3, "Introduction to Python, Variables, Data Types", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(4, "opertaors", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(5, "variables", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(6, "loops", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(7, "conditional statements", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(8, "string", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(9, "operating systems", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(10, "conctructers", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(11, "self", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(12, "hackerrank problems", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(13, "list,tuples,dict,sets", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(14, ".........", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
training_report(15, ".........", 4, 5, 3, "Silver", ["Basics of Python - Great Learning"], 2, 4),
]

for report in training:
    report.display()