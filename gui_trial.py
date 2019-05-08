# -*- coding: utf-8 -*-
"""
Created on Monday Apr 29 20:10:02 2019

GUI implementation for search algorithm comparer
"""

import BFS_and_DFS as alg

import tkinter as tk #library for gui
from PIL import Image, ImageTk #library to convert image format
from tkFileDialog   import askopenfilename #for the menu

"""FUNCTIONS FOR WIDGETS"""

def bfs_button():
    '''run BFS and show results'''
    found_path=alg.bfs()
    msg_bfs.config(text=found_path)
    msg_bfs.text=("BFS:"+str(found_path))
    
    fname="graph_bfs.jpg"
    alg.p.plotPath(found_path,fname)    

    im=Image.open(fname)
    photo_bfs=ImageTk.PhotoImage(im)   
    label_bfs.configure(image=photo_bfs)
    label_bfs.image = photo_bfs

    
def dfs_button():
    '''run DFS and show results'''
    found_path=alg.dfs()
    
    msg_dfs.config(text=found_path)
    msg_dfs.text=("DFS:"+str(found_path))
    
    fname="graph_dfs.jpg"
    alg.p.plotPath(found_path,fname)    

    im=Image.open(fname)
    photo_dfs=ImageTk.PhotoImage(im)   
    label_dfs.configure(image=photo_dfs)
    label_dfs.image = photo_dfs

def OpenFile():
    '''Open files in menu'''
    #graph_file_name = askopenfilename()
    #lst = p.readProblem(graph_file_name)
    fname="graph_whole.jpg"
    alg.p.generateEdges(fname)    
    im=Image.open(fname)
    photo_graph=ImageTk.PhotoImage(im)

    label_graph.configure(image=photo_graph)
    label_graph.image = photo_graph
    

"""CREATING THE STRUCTURAL ELEMENTS"""

''' the root, main window'''
root = tk.Tk()
root.title("Search algotithm comparer")
root.geometry("1200x600")

''' deafult panel for showing the graph'''
msg_graph = tk.Message(root, text ="Graph:")
msg_graph.config(anchor="nw",bg='white',width=40)
msg_graph.grid(row=0, column=0,sticky='W')
im=Image.open('blank.jpg')
photo=ImageTk.PhotoImage(im)
label_graph = tk.Label(image=photo,anchor='nw')
label_graph.grid(row=1, column=0)

''' default message box and panel for the found paths'''
msg_bfs = tk.Message(root, text ="BFS:")
msg_bfs.config(anchor="nw",bg='white',width=40)
msg_bfs.grid(row=0, column=1)
label_bfs = tk.Label(image=photo, anchor='e')
label_bfs.image = photo
label_bfs.grid(row=1, column=1)

msg_dfs = tk.Message(root, text ="DFS:")
msg_dfs.config(anchor="nw",bg='white',width=40)
msg_dfs.grid(row=0, column=2)
label_dfs = tk.Label(image=photo, anchor='e')
label_dfs.image = photo
label_dfs.grid(row=1, column=2)

'''two buttons for displaying the result of the algorithms'''
#- they creating message and label for display the path
button_bfs = tk.Button(root, text='BFS', width=25, command=bfs_button)
button_bfs.grid(row=2, column=0)
button_dfs= tk.Button(root, text='DFS', width=25, command=dfs_button)
button_dfs.grid(row=3, column=0)

'''Menu for opening files'''
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=OpenFile)


root.mainloop()