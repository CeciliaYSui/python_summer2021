# --------------------------------------------------------------------------------
# Program ------------------------- Python Camp HW #4 (Sorting Algorithms)
# Developer ----------------------- Cecilia Y. Sui
# Date last updated --------------- Aug 26, 2021
# 
# Sorting Algorithms Implemented -- Merge sort (good) & Stooge sort (terrible)
# 
# Note : Both sorting algorithms uses recursion as covered in python camp. 
# Sources :
# https://en.wikipedia.org/wiki/Merge_sort
# https://en.wikipedia.org/wiki/Stooge_sort
# --------------------------------------------------------------------------------

import random
import matplotlib.pyplot as plt
from timeit import default_timer


# --------------------------------------------------------------------------------
# Merge sort explained: 
# This sorting algorithm uses recursion as we covered in python camp on Wednesday.
# 1. Divide the list to 2 halves. 
# 2. Merge sort the first half.
# 3. Merge sort the second half.
# 4. Combine the two halves together. 
# Time complexity: 
# Best - O(nlogn)
# Average - O(nlogn)
# Worst - O(nlogn)
# Space complexity: 
# Worst - O(n) additional array is used to store the output 
# --------------------------------------------------------------------------------

def merge_sort(input_l):
    l = len(input_l)

    # Base Case: 
    if l == 1 or l == 0: 
        return input_l
    
    # Recursive Case: 
    # where l > 1
    # Divide the list to 2 halves.
    mid_pt = l//2
    l1 = input_l[:mid_pt]
    l2 = input_l[mid_pt:]

    # Merge sort the first half.
    # Merge sort the second half.
    # Return the combined list of two halves.
    return merge(merge_sort(l1),merge_sort(l2))


# Merge the two halves together. 
def merge(l,r):
    # create an empty output list
    out_list = []
    # set the start point for while loop
    i = j = 0
    while i < len(l) and j < len(r):
        # append the smaller value to output list 
        if l[i] < r[j]:
            out_list.append(l[i])
            i += 1
        else: 
            out_list.append(r[j])
            j += 1
    # check for leftovers if exists 
    out_list.extend(l[i:])
    out_list.extend(r[j:])
    return out_list




# --------------------------------------------------------------------------------
# Stooge sort explained: 
# This sorting algorithm uses recursion as we covered in python camp on Wednesday. 
# For ascending order sorting: 
# 1. Base case: 
#    If the first element (at index 0) > the last element (at index n-1), swap them.
#    (Use < if to sort in descending order.)
# 2. Recusive case: 
#    Stooge sort first 2/3 of the list.
#    Stooge sort last 2/3 of the list.
#    Stooge sort first 2/3 of the list again.
#    (2/3 is always rounded up when getting a non-integer.)
#    
# 
# Pros ------------ Super easy to implement!
# Cons ------------ Extremely inefficient with a terrible time complexity! :(
# ----------------- Don't use in actual practice! Just do it for fun :) 
# --------------------------------------------------------------------------------

def stooge_sort(input_l, left, right):
    # Return when no overlap 
    if left >= right:
        return
  
    # Base Case: 
    # If the first element (at index 0) > the last element (at index n-1), swap them.
    if input_l[left] > input_l[right]:
        x = input_l[left]
        input_l[left], input_l[right] = input_l[right], x
  
    # Recusive Case: 
    # When there are more than 2 elements left in the list of the current level: 
    if right-left > 1:
        # Get the index of the third of the list
        ind = round((right-left+1)/3) 
        # Recursively: Stooge sort first 2/3 of the list.
        stooge_sort(input_l, left, right-ind)
        # Recursively: Stooge sort last 2/3 of the list. 
        stooge_sort(input_l, left+ind, right)
        # Recursively: Stooge sort first 2/3 of the list again.
        stooge_sort(input_l, left, right-ind)
  
 
# --------------------------------------------------------------------------------
# Run the sorting algorithms from N = 1 to N = 100
# --------------------------------------------------------------------------------

# Run times for merge (y1) and stooge sorts (y2)
y1, y2 = [], []
for n in range(1, 101):
    l = []
    for i in range(n):
        l.append(i)
    random.shuffle(l)
    start_t = default_timer()
    merge_sort(l)
    y1.append(default_timer() - start_t)
    # print("Merge sort: Run time is %.5f seconds. " % (t))
    start_t = default_timer()
    stooge_sort(l, 0, len(l)-1)
    y2.append(default_timer() - start_t)
    # print("Stooge sort: Run time is %.5f seconds. " % (t))

# --------------------------------------------------------------------------------
# Plot the graph
# --------------------------------------------------------------------------------

# x-axis: # of elements in list
x1 = x2 = range(1, 101) 
# adjust the area around the plot
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)

# Plot the data
plt.plot(x1, y1)
plt.plot(x2, y2)

# Add a legend
plt.legend(['Merge Sort', 'Stooge Sort'], loc = "upper left", prop = {"size":10})
# y label
plt.ylabel("Time in seconds")
# x label
plt.xlabel("N (size of set to sort)")
# plot title
plt.title("Compare the Runtime of Merge Sort and Stooge Sort")
plt.show(block=False)
# Save plot
plt.savefig('/Users/ysui/Desktop/plot.pdf')
# Close plot
plt.close()
