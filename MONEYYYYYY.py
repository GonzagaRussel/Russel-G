import sys
from math import *

cash = input("how much cash?")
cost=1000


if(cash<cost):
    print("sorry you are broke")
if(cash>cost):
    wii=cash/cost
    print("nice! i can give you", wii ,"Wii console")
