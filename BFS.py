#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:46:02 2019

Contains BFS and DFS algorithms

@author: schka
"""

import DataRepresentation as dr #dr stands for data representation
p=dr.Problem()
lst=p.readProblem("Problem.xlsx")
#p.showProblem()

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
    return dr.State('not_found')
    
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
            print('BFS in ' + str(steps) + ' steps')
            return curState.name
        else:
            adjStates=[]
            adjStates=curState.children
            for key in adjStates:
                actual_child=findStateByName(key,all_states)
                if (not isMember(actual_child,visited)):
                    queue.append(actual_child)
    print('BFS in ' + str(steps) + ' steps')
    return 'Not found'

#run the search from the first state
found_state=bfs(lst[0], goal_test,lst)
print('Found state: '+found_state)

#DFS
def dfs(start, goalFunction,all_states):
    queue = [] # define an empty array
    queue.append(start) # insert an element at the end of the array
    visited = []
    steps = 0 #step counter
    #finalState = State('not_found') # for storing the finalState if found
    while(steps<maxSteps and len(queue)>0):
        curState = queue.pop(-1)
        #print(curState.name)
        visited.append(curState)
        steps=steps+1
        if (goalFunction(curState)):
            print('DFS in ' + str(steps) + ' steps')
            return curState.name
        else:
            adjStates=[]
            adjStates=curState.children
            for key in adjStates:
                actual_child=findStateByName(key,all_states)
                if (not isMember(actual_child,visited)):
                    queue.append(actual_child)
    print('DFS in ' + str(steps) + ' steps')
    return 'Not found'

#run the search from the first state
found_state=dfs(lst[0], goal_test,lst)
print('Found state: '+found_state)

