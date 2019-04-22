# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:42:25 2019

@author: Hemas
"""
# libraries
import pandas as pd
#import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#import DataRepresentation as dr

#p=dr.Problem() # Initiate object or  to copy from another "problem (list of states)"
#lst=p.readProblem("Problem.xlsx")
#fromToLst=p.generateEdges()

def plotting(fromToLst,path=False):
    """Function used to build the graph for all the Nodes and Edges
    inputs:
        -fromToList[0] contains the lists used to plot the nodes
        -fromToList[1] contains the lists used to plot the Edges
        -fromToList[2] contains the lists used to plot the names
        -fromToList[3] contains the lists used to plot the colors
        -path boolean to inform it is representing a path or not"""
    # Build a dataframe with lists 
    df = pd.DataFrame({ 'from':fromToLst[0], 'to':fromToLst[1]})
    df
    
    # Build your graph
    G=nx.from_pandas_edgelist(df, 'from', 'to',create_using=nx.DiGraph())
    G.nodes()
    
    #Coloring Lists ID is the state name, myvalue is the state group
    carac = pd.DataFrame({ 'ID':fromToLst[2], 'myvalue':fromToLst[3] })
    #ordering the nodes and applying the colors
    carac= carac.set_index('ID')
    carac=carac.reindex(G.nodes())
    
    carac['myvalue']=pd.Categorical(carac['myvalue'])
    carac['myvalue'].cat.codes
    
    # Plot it
    #nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.fruchterman_reingold_layout(G))
    if (not path):
        nx.draw(G, with_labels=True, node_color=carac['myvalue'].cat.codes, 
            cmap=plt.cm.Set1, arrows=True, width =1,
            node_size=500, alpha=0.5,
            linewidths=20, pos=nx.fruchterman_reingold_layout(G,scale=1000,k=1.2))
    else:
        nx.draw(G, with_labels=True, node_color=carac['myvalue'].cat.codes, 
            cmap=plt.cm.Set1, arrows=True, width =1,
            node_size=500, alpha=0.5,
            linewidths=20, pos=nx.spring_layout(G))
        
    #plt.colorbar(carac)
    plt.show()

