import numpy as np



def initialize(List, List_size, chrom_size, boundaries_list):
    i = 0
    for j in range(chrom_size):
            
        lower = boundaries_list[j][0]
        upper = boundaries_list[j][1]
            
        if lower == 'x':
            lower = np.random.uniform(0, upper)
            
        elif upper == 'x':
            #the upper limit is the 100% of the budget minus the upper of the previous channel
            upper = np.random.uniform(lower, 100.0-boundaries_list[j-1][1])

        boundaries_list[j] = (round(lower, 2), round(upper, 2))

    while(i < List_size):
        chrom = []
        
        for j in range(chrom_size):
            
            lower = boundaries_list[j][0]
            upper = boundaries_list[j][1]

                
            num = round(np.random.uniform(lower, upper), 2)             #generate random number between the lower and upper boundaries
            chrom.append(round(num/100.0, 2))

            
        if sum(chrom) > 1.0:                                            #make sure the budgets of all channels won't exceed the original budget
            continue
        
        List.append(chrom)
        i +=1

#the fitness is computed via multiply the investment of the channel, the ROI of the channel and the total budget (computed for all channels)
def compute_fitness(chrom, ROI_list, total_budget):
    fitness = 0.0
    for i in range(len(chrom)):
        fitness += chrom[i]*round(ROI_list[i]/100.0, 2)*total_budget
    return fitness


def tournament_selection(chrom_list, ROI_list, total_budget):
    selected_chroms = []
    i = 0
    while(i < len(chrom_list)):
        
        num1 = np.random.randint(0, len(chrom_list))
        num2 = np.random.randint(0, len(chrom_list))
        
        if num1 == num2:
            continue
        #if selected_chroms.__contains__(chrom_list[num1]) or selected_chroms.__contains__(chrom_list[num2]):
            #continue
        
        fitness1 = compute_fitness(chrom_list[num1], ROI_list, total_budget)
        fitness2 = compute_fitness(chrom_list[num2], ROI_list, total_budget)

        
        chrom = chrom_list[num1] if fitness1 > fitness2 else chrom_list[num2]
        selected_chroms.append(chrom)
        i+=1
        
    return selected_chroms
        
    
def replace(NewGen, OldGen, chrom_list, ROI_list, total_budget):
    for i in range(len(NewGen)):
        old_fitness = compute_fitness(OldGen[i], ROI_list, total_budget)
        new_fitness = compute_fitness(NewGen[i], ROI_list, total_budget)
        if new_fitness > old_fitness:
            index = chrom_list.index(OldGen[i])
            chrom_list[index] = NewGen[i]


#print(compute_fitness(np.array([2.7, 76.2, 5.6, 15.5])/100, [0.08, 0.12, 0.07, 0.11], 100))
l = []
boundaries_list = [(10, 30), (15, 25), ('x', 20), (20, 'x')]
initialize(l, 5, 4, boundaries_list)
print(l)
print(boundaries_list)
selected_chroms = tournament_selection(l, [8, 12, 7, 11], 100)
print(selected_chroms)
replace([[0.25,0.3,0.2,0.25],[0.22,0.15,0.3,0.1]], selected_chroms, l, [8, 12, 7, 11], 100)
print(l)

