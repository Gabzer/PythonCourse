#####################################
#Way to Remove at list
n = [1, 3, 5]
n.pop(1)        #remove the index = 3
n.remove(1)     #remove the number '1', index = 0 in this case
del(n[0])       #remove the index = 0
#####################################
#Modify a number of list in function
def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print list_function(n)
#####################################
#Print the elements of list
n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print_list(n)
#####################################
#Range
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0, 3, 1))  #range(start, stop, step) or (start, stop) or (stop)
#####################################
#Sum two lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Adicione sua funcao aqui
def flatten(lists):
    results = []
    for numbers in range(len(lists)):
        for i in lists[numbers]:
            results.append(i)
    return results
print flatten(n)
#####################################