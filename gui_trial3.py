# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:02:21 2019

@author: Otthon
"""
import BFS_and_DFS as alg

import tkinter as tk #library for gui
from PIL import Image, ImageTk #library to convert image format
#from tkFileDialog   import askopenfilename #for the menu


class MainApplication(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        """logical variables for consistency"""
        self.loaded=False
        self.bfs_done=False
        self.dfs_done=False
        """Saved paths"""
        self.path_dfs=[];
        self.path_bfs=[];
        
        """CREATING THE STRUCTURAL ELEMENTS"""
    
        ''' the root, main window'''
        self.root.title("Search algotithm comparer")
        self.root.geometry("1400x700")
        
        ''' deafult panel for showing the graph'''
        self.msg_graph = tk.Message(root, text ="The graph:")
        self.msg_graph.config(anchor="nw",bg='white', aspect=1000)
        self.msg_graph.grid(row=0, column=0,sticky='W')
        im=Image.open('blank.jpg')
        photo=ImageTk.PhotoImage(im)
        self.label_graph = tk.Label(image=photo,anchor='nw')
        self.label_graph.grid(row=1, column=0)
        
        ''' default message box and panel for the found paths'''
        self.msg_bfs = tk.Message(root, text ="BFS:")
        self.msg_bfs.config(anchor="nw",bg='white', aspect=1000)
        self.msg_bfs.grid(row=0, column=1)
        self.label_bfs = tk.Label(image=photo, anchor='e')
        self.label_bfs.image = photo
        self.label_bfs.grid(row=1, column=1)
        
        self.msg_dfs = tk.Message(root, text ="DFS:")
        self.msg_dfs.config(anchor="nw",bg='white', aspect=1000)
        self.msg_dfs.grid(row=0, column=2)
        self.label_dfs = tk.Label(image=photo, anchor='e')
        self.label_dfs.image = photo
        self.label_dfs.grid(row=1, column=2)
        
        '''two buttons for displaying the result of the algorithms'''
        #- they creating message and label for display the path
        self.button_bfs = tk.Button(root, text='BFS', width=25, command=self.bfs_button)
        self.button_bfs.grid(row=2, column=0)
        self.button_dfs= tk.Button(root, text='DFS', width=25, command=self.dfs_button)
        self.button_dfs.grid(row=3, column=0)
        
        '''Menu for opening files'''
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)
        
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open...", command=self.OpenFile)

    """FUNCTIONS FOR WIDGETS"""
    
    
    def bfs_button(self):
        '''run BFS and show results'''
        if (self.loaded and not self.bfs_done):
            found_path=alg.bfs()
            self.path_bfs=found_path
            self.msg_bfs.config(text="BFS: "+str(found_path))
            self.msg_bfs.text="BFS:"+str(found_path)
            
            fname="graph_bfs.jpg"
            alg.p.plotPath(found_path,fname)    
        
            im=Image.open(fname)
            photo_bfs=ImageTk.PhotoImage(im)   
            self.label_bfs.configure(image=photo_bfs)
            self.label_bfs.image = photo_bfs
            self.bfs_done=True
    
        
    def dfs_button(self):
        '''run DFS and show results'''
        if (self.loaded and not self.dfs_done):
            found_path=alg.dfs()
            self.path_dfs=found_path
            
            self.msg_dfs.config(text="DFS:"+str(found_path))
            self.msg_dfs.text=("DFS:"+str(found_path))
            
            fname="graph_dfs.jpg"
            alg.p.plotPath(found_path,fname)    
        
            im=Image.open(fname)
            photo_dfs=ImageTk.PhotoImage(im)   
            self.label_dfs.configure(image=photo_dfs)
            self.label_dfs.image = photo_dfs
            self.dfs_done=True
    
    def OpenFile(self):
        '''Open files in menu'''
        if (self.loaded):
            self.bfs_done=False
            self.dfs_done=False
        else:
            self.loaded=True
        #graph_file_name = askopenfilename()
        #lst = p.readProblem(graph_file_name)
        fname="graph_whole.jpg"
        alg.p.generateEdges(fname)    
        im=Image.open(fname)
        photo_graph=ImageTk.PhotoImage(im)
    
        self.label_graph.configure(image=photo_graph)
        self.label_graph.image = photo_graph
        
    


if __name__ == "__main__":
    root = tk.Tk()
    app=MainApplication(root)
    root.mainloop()