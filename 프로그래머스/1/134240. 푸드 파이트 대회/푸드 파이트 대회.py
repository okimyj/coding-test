import math;
def solution(food):
    foodList = ""
    
    for idx, foodNum in enumerate(food) :
        foodList += str(idx) * math.floor(foodNum/2)
    
    return foodList + '0' + foodList[::-1]