# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:47:50 2019

@author: Sameh Hanna

"""
import pandas as pd
import math

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
p.showProblem()
#Example to access the list 
print ("first state children",lst[0].name,lst[0].children)
