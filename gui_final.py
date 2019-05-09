# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:02:21 2019
Working with Python 2.7

Implement a GUI for running the searching algorithm comparer:
 One file can be loaded
 The BFS and DFS algorithms can be applied and compared

@author: Katalin Schaffer
"""
import BFS_and_DFS as alg
import CompareTrial as comp #for comparing the algorithms

import tkinter as tk #library for gui
from PIL import Image, ImageTk #library to convert image format
from tkFileDialog   import askopenfilename #for the menu
from difflib import SequenceMatcher


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
        #self.graph_fname="Problem.xlsx"
        self.graph_fname=""
        
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
        
        '''two buttons for displaying the result paths of the algorithms'''
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
        
        '''Text widget for compared results'''
        self.scroll_comp = tk.Scrollbar(self.root)
        self.txt_comp = tk.Text(self.root, height=10, width=50)
        self.scroll_comp.config(command=self.txt_comp.yview)
        self.txt_comp.config(yscrollcommand=self.scroll_comp.set)
        self.scroll_comp.grid(row=4, column=3, sticky=tk.N+tk.S+tk.W)
        self.txt_comp.grid(row=4, column=1,columnspan=2,sticky=tk.N+tk.S+tk.W+tk.E)
        self.txt_comp.insert(tk.END, "Compared results\nhere\n")
        
        '''Buttons to see compared results'''
        self.button_comp=tk.Button(root, text='Show compared features', width=25, command=self.comp_button)
        self.button_comp.grid(row=3, column=1,sticky=tk.W)
        self.button_comp=tk.Button(root, text='Show compared paths', width=25, command=self.pathcomp_button)
        self.button_comp.grid(row=3, column=2,sticky=tk.W)

    """FUNCTIONS FOR WIDGETS"""
    def comp_button(self):
        self.txt_comp.delete('1.0', tk.END)
        if (self.bfs_done and self.dfs_done):
            fcompname='out_comp.txt'
            comp.comparism(fcompname)
            with open(fcompname) as fc:  
               line = fc.readline()
               while line:
                   line = fc.readline()
                   self.txt_comp.insert(tk.END, line)
            fc.close()
            self.root.update_idletasks()
        
    
    
    def bfs_button(self):
        '''run BFS and show results'''
        if (self.loaded and not self.bfs_done):
            fname="graph_bfs.jpg"
            self.path_bfs=alg.algorithm_caller(self.graph_fname, 1, fname)
            outpath=reduce((lambda x, y: str(unicode(x)) + str(unicode(y))), self.path_bfs)
            self.msg_bfs.config(text="BFS: "+outpath)
            self.msg_bfs.text=("BFS: "+outpath)
              
            if (self.path_bfs):
                im=Image.open(fname)
                photo_bfs=ImageTk.PhotoImage(im)
            else:
                im=Image.open('blank.jpg')
                photo_bfs=ImageTk.PhotoImage(im)
            self.label_bfs.configure(image=photo_bfs)
            self.label_bfs.image = photo_bfs
            
            self.bfs_done=True
    
        
    def dfs_button(self):
        '''run DFS and show results'''
        if (self.loaded and not self.dfs_done):
            fname="graph_dfs.jpg"
            self.path_dfs=alg.algorithm_caller(self.graph_fname, 2, fname)
            outpath=reduce((lambda x, y: str(unicode(x)) + str(unicode(y))), self.path_dfs)
            self.msg_dfs.config(text="DFS: "+ outpath)
            self.msg_dfs.text=("DFS: "+ outpath)
        
            if (self.path_dfs):
                im=Image.open(fname)
                photo_dfs=ImageTk.PhotoImage(im)
            else:
                im=Image.open('blank.jpg')
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
            
        self.graph_fname = askopenfilename(title="Select files")
        
        fname="graph_whole.jpg"
        alg.algorithm_caller(self.graph_fname, 3, fname)
        im=Image.open(fname)
        photo_graph=ImageTk.PhotoImage(im)
    
        self.label_graph.configure(image=photo_graph)
        self.label_graph.image = photo_graph
        
    def pathcomp_button(self):
        self.txt_comp.delete('1.0', tk.END)
        if (self.bfs_done and self.dfs_done):
            a=reduce((lambda x, y: str(unicode(x)) + str(unicode(y))), self.path_bfs)
            b=reduce((lambda x, y: str(unicode(x)) + str(unicode(y))), self.path_dfs)
            s = SequenceMatcher(None, a, b)
            for tag, i1, i2, j1, j2 in s.get_opcodes():
                line=('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
                        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
                self.txt_comp.insert(tk.END,line+'\n')
            self.root.update_idletasks()
    
"""RUNNING THE GUI APPLICATION"""

if __name__ == "__main__":
    root = tk.Tk()
    app=MainApplication(root)
    root.mainloop()
    