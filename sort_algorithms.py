import print_util;

def swap(vals_to_sort, i, j):
    vals_to_sort[i], vals_to_sort[j] = vals_to_sort[j], vals_to_sort[i];

def bubble_sort(vals_to_sort, isVerbose):
    print("\nBubble Sort iterates through the array and bubbles \nthe largest # to the end of the array. It then starts from the \nbeginning of the array and repeats the process. The sorted partion builds from the end of the array to the start. \nUltimately, \nthis will yield a sorted array after n iterations of the array.")
    print_util.printBlankLine();
    
    print "START_BUBBLE_SORT: ", vals_to_sort;
    print_util.printBlankLine();
    
    arr_len = len(vals_to_sort);
    for i in range(1, arr_len):
        print_util.printIterator(i);
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
    print_util.printBlankLine();
    
    print "START_SELECTION_SORT: ", vals_to_sort;
    print_util.printBlankLine();
    arr_len = len(vals_to_sort);
    for i in range (0, arr_len-1):
        print_util.printIterator(i);
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
    print_util.printBlankLine();

    print "START_INSERTION_SORT: ", vals_to_sort;
    print_util.printBlankLine();

    arr_len = len(vals_to_sort);
    for i in range (0, arr_len):
        print_util.printIterator(i);
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
    print("\Merge Sort uses a divide and conquer approach. \nIt splits the array into halves until they cannot be split any further. \nThen it merges each array in the correct order and returns them, popping calls of the stack. \nUltimately, this will yield a merged, sorted version of the input array");
    print_util.printBlankLine();
    
    print "START_MERGE_SORT: ", vals_to_sort;
    print_util.printBlankLine();

    result = merge_recurse(vals_to_sort, isVerbose);
    print_util.printResult(result);
    print "END_MERGE_SORT";

def merge_recurse(vals_to_sort, isVerbose):
    if len(vals_to_sort) > 1:

        mid = len(vals_to_sort)//2
 
        L = vals_to_sort[:mid]
        R = vals_to_sort[mid:]

        print "L: ", L;
        print "R: ", R;
        print_util.printSeparation();
 
        merge_recurse(L, isVerbose)
        merge_recurse(R, isVerbose)

        merge(vals_to_sort, L, R);
        
    return vals_to_sort;

def merge(vals_to_sort, L, R):
    print "Merging: ", L, R;
    print_util.printBlankLine();
    i = j = k = 0;
    while i < len(L) and j < len(R):
        print "Comparing: ", L[i], R[j];
        if L[i] < R[j]:
            print "Copying into merged array: ", L[i];
            vals_to_sort[k] = L[i]
            i += 1
        else:
            print "Copying into merged array: ", R[j];
            vals_to_sort[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        print "Copying into merged array: ", L[i];
        vals_to_sort[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        print "Copying into merged array: ", R[j];
        vals_to_sort[k] = R[j]
        j += 1
        k += 1

    print_util.printBlankLine();
    print "Merged: ", vals_to_sort;
    print_util.printSeparation();