# -*- coding: utf-8 -*-
"""
Created on Monday Apr 29 20:10:02 2019

GUI implementation for search algorithm comparer
"""
"""Copy from BFS_and_DFS.py"""
import DataRepresentation as dr #dr stands for data representation
import ProfTrial
p=dr.Problem()
lst=p.readProblem("Problem.xlsx")

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

#reconstruation of the path based on the saved key - value pairs during search
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
    
#BFS
@ProfTrial.Profile_Decoder
def bfs(start, goalFunction,all_states):
    #dict for backtracking the found path
    #key: the state, value: from where we got there
    from_dict=dict()
    #the from value for the starting state key
    #it helps ending the becktracking
    from_state='START'
    from_dict[start.name]=from_state
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
            ls=path_backtracking(from_dict,from_state,curState)
            #return curState.name
            return ls
        else:
            adjStates=[]
            adjStates=curState.children
            for key in adjStates:
                actual_child=findStateByName(key,all_states)
                #the new member should not be in the visited list and also in the queue
                if (not isMember(actual_child,visited) and not isMember(actual_child,queue)):
                    queue.append(actual_child)
                    from_dict[actual_child.name]=curState.name
    print('BFS in ' + str(steps) + ' steps')
    return 'Not found'

#DFS
@ProfTrial.Profile_Decoder
def dfs(start, goalFunction,all_states):
    from_dict=dict()
    from_state='START'
    from_dict[start.name]=from_state
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
    print('DFS in ' + str(steps) + ' steps')
    return 'Not found'

"""STARTING GUI IMPLEMENTATION"""
import tkinter as tk #library for gui
from PIL import Image, ImageTk #library to convert image format

"""functions at button click"""
def bfs_button():
    found_path=bfs(lst[0], goal_test,lst)
    msg = tk.Message(root, text =found_path)
    msg.config(anchor="nw",bg='white',width=40)
    msg.pack()
    fname="graph_bfs.jpg"
    p.plotPath(found_path,fname)
    
    #canvas_width = 440
    #canvas_height = 400
    #canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    #canvas.pack()
    im=Image.open(fname)
    photo=ImageTk.PhotoImage(im)
    #canvas.create_image(20,20, anchor="nw", image=photo)
    
    label = tk.Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()
    
def dfs_button():
    found_path=dfs(lst[0], goal_test,lst)
    msg = tk.Message(root, text =found_path)
    msg.config(anchor="nw",bg='white',width=80)
    msg.pack()
    fname="graph_dfs.jpg"
    p.plotPath(found_path,fname)
    
    #canvas_width = 440
    #canvas_height = 400
    #canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    #canvas.pack()
    im2=Image.open(fname)
    photo2=ImageTk.PhotoImage(im2)
    #canvas.create_image(20,20, anchor="nw", image=photo)
    
    label2 = tk.Label(image=photo2)
    label2.image = photo2 # keep a reference!
    label2.pack()


"""creating and running gui""" 
root = tk.Tk()
root.title("Search algotithm comparer")
#two buttons - they creating message and label for display the path
button = tk.Button(root, text='BFS', width=25, command=bfs_button)
button.pack()
button2= tk.Button(root, text='DFS', width=25, command=dfs_button)
button2.pack()

root.mainloop()