
from posixpath import split
import functools as fn

test_str = [
    "1000\n",
    "2000\n",
    "3000\n",
    "\n",
    "4000\n",
    "\n",
    "5000\n",
    "6000\n",
    "\n",
    "7000\n",
    "8000\n",
    "9000\n",
    "\n",
    "10000"
]

def calorie_count(list_of_strings:list):
    carriers = list(map(lambda x:(x.strip()),list_of_strings))
    carriers2 = fn.reduce(lambda x,y: x +y , carriers, [0])
    print(carriers2)



#Common Code.
def run_day(list_of_strings:list):
    calorie_count(list_of_strings)

#test
run_day(test_str)