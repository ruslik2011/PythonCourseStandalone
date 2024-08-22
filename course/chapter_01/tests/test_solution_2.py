import ast
from ast import Assign

with open('course/chapter_01/solutions/solution_2.py', 'r') as file:
        tree = ast.parse(file.read())
        
for e in tree.body:
    print(isinstance(e, Assign))
