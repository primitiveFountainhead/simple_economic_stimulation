#Random economic stimulation
#There are N number of people, in set P each with S number of intial sums
#They do transaction in one of m currencies, m in M
#We take two people, p1, p2 in P and toss a coin if heads give m from p2 to p1 and vice versa

import numpy as np 
import matplotlib.pyplot as plt

def interact(people, name, P):
    np.random.shuffle(name)
    for i in range(0,len(name), 2):
        x = np.random.randint(3)
        perc = P
        if x == 0 and people[name[i]] - perc > 0:
            people[name[i]] -= perc
            people[name[i+1]] += perc
        elif x == 1 and people[name[i+1]] - perc > 0:
            people[name[i+1]] -= perc
            people[name[i]] += perc
       

#money = int(input('Enter intial money:  '))
#num_of_people = int(input('Enter number of people: '))
#perc = int(input('Enter perc of transaction: '))


money = 100
num_of_people = 1000
perc = 5

people = np.ones(num_of_people, dtype= int)*money
name = np.array(range(num_of_people))

Time = 10000

for t in range(Time):
    interact(people, name,perc)

plt.hist(people, bins = 100)
plt.xlabel('Amount of Money the Person has')
plt.ylabel('Number of people')
plt.show()

#for t in range(Time):

