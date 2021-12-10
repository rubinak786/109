import random
import statistics
import plotly.figure_factory as ff
dice_result= []
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
mean =sum(dice_result)/len(dice_result)  
std_deviation= statistics.stdev(dice_result)
print("mean is",mean)
print("stdev is",std_deviation)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
print("median is",median)
print("mode is",mode)
fig =ff.create_distplot([dice_result],["result"],show_hist=False)
fig.show()

