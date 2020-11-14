import print_util;

def swap(vals_to_sort, i, j):
    vals_to_sort[i], vals_to_sort[j] = vals_to_sort[j], vals_to_sort[i];

def bubble_sort(vals_to_sort, isVerbose):
    print("\nBubble Sort iterates through the array and bubbles \nthe largest # to the end of the array. It then starts from the \nbeginning of the array and repeats the process. The sorted partion builds from the end of the array to the start. \nUltimately, this will yield a sorted array after n iterations of the array.")
    print_util.gap();
    
    print "START_BUBBLE_SORT: ", vals_to_sort;
    print_util.gap();
    
    arr_len = len(vals_to_sort);
    for i in range(1, arr_len):
        print_util.printIterator(i, isVerbose);
        for j in range(0, arr_len-1):
            if vals_to_sort[j] > vals_to_sort[j+1]:
                print_util.highlightStep(vals_to_sort, j, j+1, isVerbose)
                swap(vals_to_sort, j, j+1);
                print_util.unHighlightStep(vals_to_sort, j, j+1, isVerbose);
            else:
                print_util.highlightStep(vals_to_sort, j, j+1, isVerbose, False);
                print_util.unHighlightStep(vals_to_sort, j, j+1, isVerbose, False);

    print_util.printResult(vals_to_sort);
    print ("END_BUBBLE_SORT");

def selection_sort(vals_to_sort, isVerbose):
    print("\nSelection Sort builds a sorted partition from the beginning of the array to the end. \nFor each item i, starting from 0, it scans the array for the smallest item t to swap i with.")
    print_util.gap();
    
    print "START_SELECTION_SORT: ", vals_to_sort;
    print_util.gap();

    arr_len = len(vals_to_sort);
    for i in range (0, arr_len-1):
        print_util.printIterator(i, isVerbose);
        curr_min = i;
        for j in range(i+1, arr_len):
            print_util.highlightStep(vals_to_sort, i, j, isVerbose, False);
            print_util.unHighlightStep(vals_to_sort, i, j, isVerbose, False);

            if vals_to_sort[j] < vals_to_sort[curr_min]:
                curr_min = j;

        if curr_min != i:
            print_util.highlightStep(vals_to_sort, i, curr_min, isVerbose);
            swap(vals_to_sort, i, curr_min);
            print_util.unHighlightStep(vals_to_sort, i, curr_min, isVerbose);

    print_util.printResult(vals_to_sort);
    print ("END_SELECTION_SORT");

def insertion_sort(vals_to_sort, isVerbose):
    print("\nInsertion Sort builds a sorted partition from the beginning of the array to the end. \nFor each item i, it swaps i with any item that precedes i in the array that is bigger than i.")
    print_util.gap();

    print "START_INSERTION_SORT: ", vals_to_sort;
    print_util.gap();

    arr_len = len(vals_to_sort);
    for i in range (0, arr_len):
        print_util.printIterator(i, isVerbose);
        for j in range (0, i):
            print_util.highlightStep(vals_to_sort, j, i, isVerbose, False);
            print_util.unHighlightStep(vals_to_sort, j, i, isVerbose, False);
            if vals_to_sort[i] < vals_to_sort[j]:
                print_util.highlightStep(vals_to_sort, j, i, isVerbose);
                swap(vals_to_sort, i, j);
                print_util.unHighlightStep(vals_to_sort, j, i, isVerbose);

    print_util.printResult(vals_to_sort);
    print "END_INSERTION_SORT";

def merge_sort(vals_to_sort, isVerbose):
    print("\nMerge Sort uses a divide and conquer approach. \nIt splits the array into halves until they cannot be split any further. \nThen it merges each array in the correct order and returns them, popping calls of the stack. \nUltimately, this will yield a merged, sorted version of the input array");
    print_util.gap();
    
    print "START_MERGE_SORT: ", vals_to_sort;
    print_util.gap();

    result = merge_recurse(vals_to_sort, isVerbose);
    print_util.printResult(result);
    print "END_MERGE_SORT";

def merge_recurse(vals_to_sort, isVerbose):
    if len(vals_to_sort) > 1:

        mid = len(vals_to_sort)//2
 
        L = vals_to_sort[:mid]
        R = vals_to_sort[mid:]

        print_util.printIfVerbose("L: " + str(L), isVerbose);
        print_util.printIfVerbose("L: " + str(R), isVerbose);
        print_util.printSeparation(isVerbose);
 
        merge_recurse(L, isVerbose)
        merge_recurse(R, isVerbose)

        merge(vals_to_sort, L, R, isVerbose);
        
    return vals_to_sort;

def merge(vals_to_sort, L, R, isVerbose):
    print_util.printIfVerbose("Merging: " + str(L) + ", " + str(R), isVerbose);
    print_util.printBlankLine(isVerbose);
    i = j = k = 0;
    while i < len(L) and j < len(R):
        print_util.printIfVerbose("Comparing: " + str(L[i]) + ", " + str(R[j]), isVerbose);
        if L[i] < R[j]:
            print_util.printIfVerbose("Copying into merged array: " + str(L[i]), isVerbose);
            vals_to_sort[k] = L[i]
            i += 1
        else:
            print_util.printIfVerbose("Copying into merged array: " + str(R[j]), isVerbose);
            vals_to_sort[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        print_util.printIfVerbose("Copying into merged array: " + str(L[i]), isVerbose);
        vals_to_sort[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        print_util.printIfVerbose("Merging: " + str(L) + ", " + str(R), isVerbose);
        vals_to_sort[k] = R[j]
        j += 1
        k += 1

    print_util.printBlankLine(isVerbose);
    print_util.printIfVerbose("Merging: " + str(L) + ", " + str(R), isVerbose);
    print_util.printSeparation(isVerbose);

def quick_sort(vals_to_sort, isVerbose):
    print("\nQuickSort uses a divide and conquer approach. \nAt each step, it makes sure the chosen pivot (always the last element in this implementation) \nis always in a spot where all elements to the left are smaller, and to the right are larger. \nQuicksort is generally more efficient than other sorting algorithms because \nits inner loop can be implemented efficiently on most architectures.");
    print_util.gap();
    
    print "START_QUICK_SORT: ", vals_to_sort;
    print_util.gap();

    quick_recurse(vals_to_sort, 0, len(vals_to_sort)-1, isVerbose);

    print_util.printResult(vals_to_sort);
    print "END_QUICK_SORT";

def quick_recurse(arr, low, high, isVerbose):
    if low < high: 

        pi = partition(arr, low, high, isVerbose); 
        print_util.printIfVerbose("Partitioning Index: " + str(pi), isVerbose);

        print_util.printIfVerbose("Array to partition and sort " + str(arr[:pi]), isVerbose);
        quick_recurse(arr, low, pi-1, isVerbose) 
        print_util.printIfVerbose("Array to partition and sort " + str(arr[pi:]), isVerbose);
        quick_recurse(arr, pi+1, high, isVerbose)     

def partition(arr, low, high, isVerbose):
    i = low-1; 
    pivot = arr[high];
    print_util.printSeparation(isVerbose);
    print_util.printIfVerbose("Pivot Value: " + str(pivot), isVerbose);
  
    for j in range(low , high): 
        if arr[j] < pivot:
            i = i+1 
            print_util.highlightStep(arr, j, i, isVerbose);
            swap(arr, i , j);
            print_util.unHighlightStep(arr, j, i, isVerbose);
  
    print_util.highlightStep(arr, i+1, high, isVerbose);
    swap(arr, i+1, high);
    print_util.unHighlightStep(arr, i+1, high, isVerbose);
    return i+1; 
