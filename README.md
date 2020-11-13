# SortVisualizer
Visualizer script that prints steps for common sort algorithms given any input array of integers,

## Getting started
Running on the cmd line: 

Pass in sorting algorithm name (separated by underscore) and space separated list of numbers to sort.

Eg.

    python sort_setup.py bubble_sort 3 2 1 4 6 1 8
   

## Displaying steps
Steps taken by the algorithms can be displayed by setting the verbose flag "-v"

Eg. 

    python sort_setup.py selection_sort -v 3 2 1 4

![Selection Sort Results Image](https://github.com/harman-brar/SortVisualizer/blob/master/assets/readme_sel_sort.png?raw=true)


## Further Information

**Asterisk**: * n *, where n is an element of the array, means it is a subject of the current step

**Directional arrow**: n -> or <- n indicates a swap at the current step and the direction in which the element is going to be moved

