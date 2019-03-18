#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:46:02 2019

@author: schka
"""

import pandas as pd
import math
import unicodedata

class State:
    """ Class to represent the state"""
    name="" #State Name
    children={} # State Children (Name:Cost)   
    
    # name =state/node name, children= dictionary( child state:Cost)
    def __init__(self, name,children={}):
        self.name = name
        self.children=children.copy()


class Problem:
    """ Class to represent the problem with methods to 
    read and show the problem"""
    allStates=[]
    # initiation to copy another problem Problem(list of states)
    def __init__(self,allStates=[]):
        self.allStates=allStates

    @classmethod
    def readProblem(self,path='Problem.xlsx'):
        """ Method used to read the problem from excel file and return a list 
        of avilable states"""
        # the reader for the excel file
        try:
            df = pd.read_excel(path, sheetname='Sheet1')
        except: # if we can't open the file then return to terminate method
            print("Could not open the file")
            return None
         
        allStates=self.allStates
        # Looping on the column names to find each state
        for name in df.columns[1:]:
            i=0
            enc_name=name.encode('ascii','ignore')
            c=State(enc_name)
            #looping on the row to find each child of state
            for state in df[name]:
                if (not math.isnan(state)):
                    c.children[str(df['States'][i])]=state
                i=i+1
            allStates.append(c)
        return allStates
    
    @classmethod
    def showProblem(self):    
        """Show the nodes/states and the children"""
        for state in self.allStates:
            print (state.name)
            print (state.children)



# how to call the code
p=Problem() # Initiate object or  to copy from another "problem (list of states)"
lst=p.readProblem("Problem.xlsx")
     # if no path inserted it will search for Problem.xlsx in the local directory
     # the problem used is the one from AI lecture 3 Example 
#p.showProblem()
#Example to access the list 
#print ("first state children",lst[0].name,lst[0].children)

#implementation of BFS
     
def goal_test(s):
    goal_name=lst[len(lst)-1].name
    if s.name==goal_name:
        return True
    else:
        return False

memoryLimit = 2000
maxSteps = 50
# if we suppose that the name is like an ID
def equalStates(s1, s2):
    if s1.name==s2.name:
        return True
    else:
        return False
	
def isMember(s, lst_of_states):
	for i in range(len(lst_of_states)):
		if (equalStates(lst_of_states[i], s)):
			return True
	return False

# finding the state in all states list by name
def findStateByName(s_name,lst_states):
    for stored_s in lst_states:
        if stored_s.name==s_name:
			return stored_s
    return State('not_found')
    
#BFS
def bfs(start, goalFunction,all_states):
    queue = [] # define an empty array
    queue.append(start) # insert an element at the end of the array
    visited = []
    steps = 0 #step counter
    #finalState = State('not_found') # for storing the finalState if found
    while(steps<maxSteps and len(queue)>0):
        curState = queue.pop(0)
        #print(curState.name)
        visited.append(curState)
        steps=steps+1
        if (goalFunction(curState)):
            print(steps)
            return curState.name
        else:
            adjStates=[]
            adjStates=curState.children
            for key in adjStates:
                actual_child=findStateByName(key,all_states)
                if (not isMember(actual_child,visited)):
                    queue.append(actual_child)
    print(steps)
    return 'Not found'


found_state=bfs(lst[0], goal_test,lst)
print(found_state)



