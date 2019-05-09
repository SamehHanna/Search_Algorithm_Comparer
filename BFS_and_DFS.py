#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:46:02 2019

Contains BFS and DFS algorithms in a function, which also can run them 
and return their results.

@author: Katalin Schaffer
"""

import DataRepresentation as dr #dr stands for data representation
import ProfTrial

def algorithm_caller(problem_fname, alg_number,fname_outplot):
    """
    problem_fname: name of the excel file representing the graph
    
    There are 3 options of returned results (choosed by giving alg_numb=1/2/3)
    if alg_number=1, then runs BFS and create the image about the path
    if 2 then run DFS and create the image about the path
    if 3 then create the image about the whole graph
    
    (the name of the created file is given as fname_outplot input argument)
    """
    """Reading the problem file"""
    p=dr.Problem()
    lst=p.readProblem(problem_fname)
    """if 3 then create the image about the whole graph and return"""
    if (alg_number==3):
        p.generateEdges(fname_outplot)
        return
    
    """IMPLEMENTATION OF THE ALGORITHMS"""
    maxSteps = 50 # for preventing to run too much time e.g. stucked in loop
    """Used helper functions"""
    def goal_test(s):
        goal_name=lst[len(lst)-1].name
        if s.name==goal_name:
            return True
        else:
            return False
        
    def equalStates(s1, s2): # if we suppose that the name is like an ID
        if s1.name==s2.name:
            return True
        else:
            return False
    	
    def isMember(s, lst_of_states):
    	for i in range(len(lst_of_states)):
    		if (equalStates(lst_of_states[i], s)):
    			return True
    	return False
    
    '''finding the state in all states list by name'''
    def findStateByName(s_name,lst_states):
        for stored_s in lst_states:
            if stored_s.name==s_name:
                return stored_s
        return dr.State('not_found')
    
    '''reconstruation of the path based on the saved key - value pairs
        during search'''
    def path_backtracking(fromDict,startValue,goalState):
        path=[]
        path.append(goalState.name)
        for i in range(0,len(fromDict)):
            val=fromDict.get(path[0],None)
            if val==None or val==startValue:
                return path
            else:
                path.insert(0,val)
        return path
        
    """BFS"""
    @ProfTrial.Profile_Decoder
    def bfs(start=lst[0], goalFunction=goal_test,all_states=lst,printres=False):
        '''dict for backtracking the found path'''
        '''key: the state, value: from where we got there'''
        from_dict=dict()
        '''the from value for the starting state key, it helps ending the becktracking'''
        from_state='START'
        from_dict[start.name]=from_state
        queue = [] # define an empty array
        queue.append(start) # insert an element at the end of the array
        visited = []
        steps = 0 #step counter
        while(steps<maxSteps and len(queue)>0):
            curState = queue.pop(0)
            visited.append(curState)
            steps=steps+1
            if (goalFunction(curState)):
                if printres : print('BFS in ' + str(steps) + ' steps')
                ls=path_backtracking(from_dict,from_state,curState)
                return ls
            else:
                adjStates=[]
                adjStates=curState.children
                for key in adjStates:
                    actual_child=findStateByName(key,all_states)
                    '''the new member should not be in the visited list and also in the queue'''
                    if (not isMember(actual_child,visited) and not isMember(actual_child,queue)):
                        queue.append(actual_child)
                        from_dict[actual_child.name]=curState.name
        if printres : print('BFS in ' + str(steps) + ' steps')
        return 'Not found'
    
    """If 1st option (BFS) was choosen then run the search from the first state"""
    if (alg_number==1):
        found_path_bfs=bfs(lst[0], goal_test,lst)
        p.plotPath(found_path_bfs,fname_outplot)
        #print(found_path_bfs)
        return found_path_bfs
    
    """DFS"""
    @ProfTrial.Profile_Decoder
    def dfs(start=lst[0], goalFunction=goal_test,all_states=lst,printres=False):
        from_dict=dict()
        from_state='START'
        from_dict[start.name]=from_state
        queue = [] # define an empty array
        queue.append(start) # insert an element at the end of the array
        visited = []
        steps = 0 #step counter
        while(steps<maxSteps and len(queue)>0):
            curState = queue.pop(-1)
            visited.append(curState)
            steps=steps+1
            if (goalFunction(curState)):
                if printres : print('DFS in ' + str(steps) + ' steps')
                ls=path_backtracking(from_dict,from_state,curState)
                return ls
            else:
                adjStates=[]
                adjStates=curState.children
                for key in sorted(adjStates.keys(), reverse=True):
                    actual_child=findStateByName(key,all_states)
                    if (not isMember(actual_child,visited)):
                        queue.append(actual_child)
                        from_dict[actual_child.name]=curState.name
        if printres : print('DFS in ' + str(steps) + ' steps')
        return 'Not found'
    
    """If 2nd option (DFS) was choosen then run the search from the first state"""
    if (alg_number==2):
        found_path_dfs=dfs(lst[0], goal_test,lst)
        p.plotPath(found_path_dfs,fname_outplot)
        #print(found_path_dfs)
        return found_path_dfs
