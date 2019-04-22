#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:51:04 2019

@author: schka

copy of the ReadingTrial by Sameh Hanna
"""

import pandas as pd
import math
import Graphing as gr
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
            enc_name=name#.encode('ascii','ignore')
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
    
    @classmethod
    def generateEdges(self):
        """ Generate/Draw the Nodes(states) and Edges (actions)
        between parents and children"""
        from_lst=[] # Starting/Parent of Edge
        to_lst=[] # Ending/Child of Edge
        color_lst=[] # List of coloring groups
        state_name=[] # List of state names
        for state in self.allStates:
            color_lst.append("normal")
            state_name.append(state.name)
            for child in state.children:
                from_lst.append(state.name)
                to_lst.append(child)
        color_lst[0]="start"
        color_lst[len(color_lst)-1]="end"
        gr.plotting([from_lst,to_lst,state_name,color_lst])
    
    @classmethod
    def plotPath(self,path=[]):
        """ Generate/Draw the Nodes(states) and Edges (actions)
        for a certain path"""
        if (len(path)==0):
            return
        from_lst=path[0:len(path)-1]
        to_lst=path[1:]
        color_lst=list(range(0,len(path))) 
        state_name=path 
        gr.plotting([from_lst,to_lst,state_name,color_lst],True)
        
        
'''
p=Problem() # Initiate object or  to copy from another "problem (list of states)"
lst=p.readProblem("Problem.xlsx")
p.showProblem()
'''