import numpy as np
import random as r

# In this module 2-point crossover and non-(uniform) mutation will be implemented

pc = r.uniform(0.4, 0.7)    #probability of crossover
pm = r.uniform(0.001, 0.3)  #Probability of mutation

def two_point_crossover(x1, x2):
    # X1: first parent chromosome
    # X2: Second parent Chromosome

    p1 = int(r.uniform(1, len(x1)-1))   # First crossover point 
    p2 = int(r.uniform(1, len(x1)-1))   # Second crossover point

    # if two points are identical re-generate them
    # Hint : it will be a strange accident if p1 equals p2 after re-generation
    if (p1 == p2):
        p1 = int(r.uniform(1, len(x1)-1))
        p2 = int(r.uniform(1, len(x1)-1))
        
    # Crossover indicator
    rc = r.uniform(0, 1)

    
    print(p1, p2)
    print(rc, pc)
    if (rc <= pc):
        # Perform Crossover
        if (p1 < p2):       # Where point1 < point 2
            temp = x1[p1:p2+1]
            x1[p1:p2+1] = x2[p1:p2+1]
            x2[p1:p2+1] = temp
        else :              # Where point 1 > point 2
            temp[p2:p1+1] = x1[p2:p1+1]
            x1[p2:p1+1] = x2[p2:p1+1]
            x2[p2:p1+1] = temp
        return list([x1, x2])
    else:
        #NO Crossover
        return list([x1, x2]) # Return Parents without Change



def uniform_mutation(chrom, LU_list):
    # chrom: chromosome which it's fitness lower than the other selected 

    Delta = None  # Delta var which indicates xnew

    # LU_list : lower and upper bound list passed from another function
                # to make sure the sequence is safe

    # first step : calculate delta lower and delta upper for each gene
    
    for i in range(0, len(chrom)):
        rm = r.uniform(0,1)    
        if (rm <= pm):
            # Calculating delta lower and delta upper
            lb, ub = LU_list[i]
            delta_lo = chrom[i] - lb
            delta_hi = ub - chrom[i]
            r1 = r.uniform(0,1)
            if (r1 <= 0.5):
                Delta = delta_lo
                r2 = r.uniform(0, Delta)
                chrom[i] = chrom[i] - r2
            else :
                Delta = delta_hi
                r2 = r.uniform(0, Delta)
                chrom[i] = r2 - chrom[i]             
    return chrom     


def nonuniform_mutation(chrom, LU_list, t, T):
    # Like uniform mutation but value of mutation is calculated another way
    # t : Current Generation
    # T : max number of generations
    
    Y = None # Delta indicator
    for i in range(0, len(chrom)):
        rm = r.uniform(0,1)    
        if (rm <= pm):
            # Calculating delta lower and delta upper
            lb, ub = LU_list[i]
            delta_lo = chrom[i] - lb
            delta_hi = ub - chrom[i]
            r1 = r.uniform(0,1)
            if (r1 <= 0.5):
                Y = delta_lo
                ra = r.uniform(0,1)
                b = r.uniform(0.5, 5.5)
                mut_fun = Y * (1-ra)**(1-t/T)**b
                #print(mut_fun)
                chrom[i] = chrom[i] - mut_fun
            else :
                Y = delta_hi
                ra = r.uniform(0,1)
                b = r.uniform(0.5, 5.5)
                mut_fun = Y * (1-ra)**(1-t/T)**b
                #print(mut_fun)
                chrom[i] = mut_fun - chrom[i]             
    return chrom   

#print(uniform_mutation([0.08, 0.12, 0.07, 0.11], [(2.7,58),(20.5,38),(5,18),(10,30)]))
#print(two_point_crossover([0.1, 0.5, 0.6, 0.3, 0.2, 0.56, 0.11]
#                         ,[1, 5, 6, 3, 2, 56, 11]))
#print(nonuniform_mutation([0.08, 0.12, 0.07, 0.11], [(2.7,58),(20.5,38),(5,18),(10,30)], 2, 7))


                ### Debugged AND TESTED ###
