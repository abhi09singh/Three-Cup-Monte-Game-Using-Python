#!/usr/bin/env python
# coding: utf-8

# In[11]:


from random import shuffle


# In[12]:


#defining mylist 

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    


# In[13]:


#taking players guess

def player_guess():
    guess =''    #place holder for index 
    while guess not in ['0','1','2']:
        guess=input("enter the no. between 0,1,2 : ")
    return int(guess) #conversion from string to int type


# In[14]:


#matching both guesses

def check_guess(mylist,guess):
    if mylist[guess]== '0':
        print('You won')
    else :
        print('phir se try kro')
        print(mylist)


# In[15]:


#initial list
mylist=['','0','']

#shuffle it
mixed_list=shuffle_list(mylist)

#player guess
guess = player_guess()

#To check the game
check_guess(mixed_list,guess)


# In[ ]:





# In[ ]:




