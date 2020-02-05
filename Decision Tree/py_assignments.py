import dtree as d
import monkdata as m
#%% Assignment 1
#Calculate the entropy of each training set
print('Entropy for MONK-1 training set: ' + str(d.entropy(m.monk1)))
print('Entropy for MONK-2 training set: ' + str(d.entropy(m.monk2)))
print('Entropy for MONK-3 training set: ' + str(d.entropy(m.monk3)))
#This is done by firstly importing the monk dataset and dtree, then 
#calling d.entropy function with the training set as input

#%% Assignment 3
#Calculate the information gain for each attribute of every MONK training set
def gain(dataset):
    dict_monk = {
            "A1": d.averageGain(dataset,m.attributes[0]),
            "A2": d.averageGain(dataset,m.attributes[1]),
            "A3": d.averageGain(dataset,m.attributes[2]),
            "A4": d.averageGain(dataset,m.attributes[3]),
            "A5": d.averageGain(dataset,m.attributes[4]),
            "A6": d.averageGain(dataset,m.attributes[5])
            }
    return dict_monk

print('Information Gain for the MONK-1 attributes ' + str(gain(m.monk1)))
print('Information Gain for the MONK-2 attributes ' + str(gain(m.monk2)))
print('Information Gain for the MONK-3 attributes ' + str(gain(m.monk3)))
#%% Assignment 5
#Compute the train and test set errors for the three Monk datasets for the full datasets
monk_1_tree = d.buildTree(m.monk1,m.attributes)
print('The error for MONK-1 training set ' + str(d.check(monk_1_tree,m.monk1)))
print('The error for MONK-1 test set ' + str(d.check(monk_1_tree,m.monk1test)))

monk_2_tree = d.buildTree(m.monk2,m.attributes)
print('The error for MONK-2 training set ' + str(d.check(monk_2_tree,m.monk2)))
print('The error for MONK-2 test set ' + str(d.check(monk_2_tree,m.monk2test)))

monk_3_tree = d.buildTree(m.monk3,m.attributes)
print('The error for MONK-3 training set ' + str(d.check(monk_3_tree,m.monk3)))
print('The error for MONK-3 test set ' + str(d.check(monk_3_tree,m.monk3test)))

#%% Assignment 7
import dtree as d
import monkdata as m
import numpy as np
import matplotlib.pyplot as plt
#Partition is pasted into d.tree
def evalu(tree, val_set,test_set):
    prune = d.allPruned(tree)
    temp_store = 0
    index = 0
    for i in range(0,len(prune)):
        check = d.check(prune[i],val_set)
        
        if check > temp_store:
            temp_store = check
            index = i
            
    best_tree = prune[index]
    check_perf = d.check(best_tree, test_set)
    error = 1 - check_perf
    return error

def init(fractions):
    error_ave_1 = []
    error_ave_3 = []
    for frac in fractions:
        error_temp_1 = []
        error_temp_3 = []

        for i in range(0,1000):
            monk1train, monk1val = d.partition(m.monk1,frac)
            monk_1_tree = d.buildTree(monk1train,m.attributes)
            error_temp_1.append(evalu(monk_1_tree,monk1val,m.monk1test))
            
            monk3train, monk3val = d.partition(m.monk3,frac)
            monk_3_tree = d.buildTree(monk3train,m.attributes)
            error_temp_3.append(evalu(monk_3_tree,monk3val,m.monk3test))
            
        
        error_ave_1.append(np.mean(error_temp_1))
        error_ave_3.append(np.mean(error_temp_3))
    return error_ave_1, error_ave_3
                



if __name__ == "__main__":

    fractions = [0.3,0.4,0.5,0.6,0.7,0.8]    



    error_ave_1,error_ave_3 = init(fractions)
    plt.figure()
    plt.plot(fractions, error_ave_1)
    plt.xlabel('Fractions')
    plt.ylabel('Mean error')
    plt.title('Mean error versus fractions, MONK-1')
    
    plt.figure()
    plt.plot(fractions, error_ave_3)
    plt.xlabel('Fractions')
    plt.ylabel('Mean error')
    plt.title('Mean error versus fractions, MONK-3')






























