# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:06:20 2019

@author: Hemas
"""

import cProfile
import functools
import pstats


def Profile_Decoder(func):
    @functools.wraps(func)
    def profile_fun(*args, **kwargs):
        # Generating the profiler object
        pr=cProfile.Profile()
        pr.enable()
        # runnign the profiler
        out=pr.runcall(func,*args, **kwargs)
        # generte the stats file with the algorithm name
        pr.dump_stats(str(func.__name__))
        pr.disable()
        
        # openeing the states and transforming it to a readable format then saving it
        with open(func.__name__ +"_output.txt", "w") as fh:	
            output_stat = pstats.Stats(func.__name__,stream=fh)
            #sorting by number of runs and limiting to the important calls
            output_stat.strip_dirs().sort_stats(0).print_stats('BFS_and_DFS')

        #return the value after running the function 
        return out
    return profile_fun
