'''
VIGNAN CAMPUS MAP 
each building in a collage campus is a node , and walkable paths are edges 

----------------------------------------------------------------------------------
represent the campus using an adjecent list
check if theres path from the library to the auditorium using BFS
list all buildings that are that are directly connected to the admin block
use DFS to visit all reachable buildings from the main gate 
find if there are any disconncted buildings(buildings not connected to campus)

'''
campus = {
    "main_gate": ["admin_block"],
    "admin_block": ["main_gate", "library", "canteen", "engineering_block"],
    "library": ["admin_block", "auditorium"],
    "canteen": ["admin_block", "hostel"],
    "auditorium": ["library"],
    "engineering_block": ["admin_block", "science_block"],
    "science_block": ["engineering_block"],
    "hostel": ["canteen"],
}
def bfs(start, target):
    visited = set()
    queue = [start]
    while queue:
        b = queue.pop(0)
        if b == target:
            return True
        if b not in visited:
            visited.add(b)
            queue += [n for n in campus[b] if n not in visited]
    return False
def dfs(start,visited =None):
    if visited is None:
        visited = set()
    if start in visited:
        return
    print(start,end=' ')
    visited.add(start)
    for neighbor in campus[start]:
        dfs(neighbor, visited)
def disconnected():
    visited = set()
    dfs(next(iter(campus)))  # Start DFS from an arbitrary node
    return set(campus.keys() - visited)

#adjecent list
print("campus map:")
for b , n in campus.items():
    print(f"{b} -> {', '.join(n)}")
print("\n 2.path from library to auditorium exists: ")
print("yes" if bfs("library", "auditorium") else "no")
print("\n3.buildings directly connected to admin block:")
print(campus["admin block"])
print("\n4.DFS from main gate:")
dfs("main_gate")
print()
print("\n5.Disconnected buildings:")
d = disconnected()
print("d if d else 'no disconnected buildings'")
