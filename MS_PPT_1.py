#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


arr = []
random_arr = [0 for i in range(8)] 
serv_dur = [0 for i in range(8)] 
wait_time = [0 for i in range(8)]

print("RANDOM NUMBERS : ")

for x in range(8) : 
    
    random_arr[x] = random.randint(0,99)
    print(random_arr[x])

for x in range(8) : 
    if(random_arr[x]<40) : 
        serv_dur[x] = 45
    if(40<=random_arr[x]<55) :
        serv_dur[x] = 60
    if(55<=random_arr[x]<70) :
        serv_dur[x] = 15
    if(70<=random_arr[x]<80) :
        serv_dur[x] = 45
    if(80<=random_arr[x]<100) :
        serv_dur[x] = 15
print("  ")
print("SERVICE DURATION : ")
for x in range(8) : 
    
    
    print(serv_dur[x])

wait_time[0] = 0

for x in range(7) : 
    temp = wait_time[x] + (serv_dur[x]-30)
    
    if(temp>=0) : 
        wait_time[x+1] = wait_time[x] + (serv_dur[x]-30)
    else :
        wait_time[x+1] = 0

print(" ")
total_wait_time = 0
print("WAITING TIME : ")
for x in range(8) :
    total_wait_time += wait_time[x]
    print(wait_time[x])
    
avg_wait_time = total_wait_time/8
print(" ")
print(" ")
print("AVERAGE WAITING TIME : ")
print(avg_wait_time)


# In[ ]:





# In[ ]:




