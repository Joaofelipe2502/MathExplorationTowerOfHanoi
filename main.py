from stack import Stack
import random
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "TowersOfHanoi_" + str(datetime.datetime.now()) + ".csv"
filename = filename.replace(":",".")
f = open(filename, "a")
f.write("Header " + "Start Time: " + str(datetime.datetime.now()) + "\n")

#Enter number of disks

        
def play_game(known_min_moves):
  
  left_stack= Stack("Left")
  middle_stack= Stack("Middle")
  right_stack= Stack("Right")
  stacks= [left_stack,middle_stack,right_stack]
  for i in range(disk_count, 0, -1):
    left_stack.push(i)

  move_count = 0
  
  origin_stack= 0
  destination_stack= 0
  while True:

    if move_count > known_min_moves:
      print('Game exceeded known_min_moves')
      return None

    move_count += 1 
    print(f'Move: {move_count}')
    p_origin_stack = origin_stack
    p_destination_stack = destination_stack


    origin_stack= random.randint(0,2)
    destination_stack= random.randint(0,2)

    if origin_stack == p_destination_stack or p_destination_stack == origin_stack:
      next
    
    if (stacks[destination_stack].peek() == None and stacks[origin_stack].peek()!= None) or (stacks[origin_stack].peek()!= None and stacks[destination_stack].peek()!= None and (stacks[destination_stack].peek() > stacks[origin_stack].peek())) :
      stacks[destination_stack].push(stacks[origin_stack].pop())

      if stacks[2].get_size() == disk_count:
        print("Found solution in", move_count)
        return move_count
    
disk_count = int(input('Input number of disks: '))
min_moves = int(input("What is the known minimum moves? - Any solution with more moves will be discarded: "))
while True:
  result = play_game(min_moves)
  if result != None:
    if result < min_moves:
      print(result)
      exit

#Display diagram
plt.show()
