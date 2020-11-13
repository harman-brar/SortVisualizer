import print_util;

def bubble_sort(vals_to_sort, isVerbose):
    print("\nBubble Sort iterates through the array and bubbles \nthe largest # to the end of the array. It then starts from the \nbeginning of the array and repeats the process. The sorted partion builds from the end of the array to the start. \nUltimately, \nthis will yield a sorted array after n iterations of the array.")
    print_util.printBlankLine();
    
    print "START_BUBBLE_SORT: ", vals_to_sort;
    print_util.printBlankLine();
    
    arr_len = len(vals_to_sort);
    for i in range(1, arr_len):
        for j in range(0, arr_len-1):
            if vals_to_sort[j] > vals_to_sort[j+1]:
                print_util.highlightStep(vals_to_sort, j, j+1, isVerbose)
                vals_to_sort[j], vals_to_sort[j+1] = vals_to_sort[j+1], vals_to_sort[j];
                print_util.unHighlightStep(vals_to_sort, j, j+1, isVerbose);
            else:
                print_util.highlightStep(vals_to_sort, j, j+1, isVerbose, False);
                print_util.unHighlightStep(vals_to_sort, j, j+1, isVerbose, False);

    print "Result: ", vals_to_sort;
    
    print_util.printBlankLine();
    print ("END_BUBBLE_SORT");

def selection_sort(vals_to_sort, isVerbose):
    print("\nSelection Sort builds a sorted partition from the beginning of the array to the end. \nFor each item i, starting from 0, it scans the array for the smallest item t to swap i with.")
    print_util.printBlankLine();
    
    print "START_SELECTION_SORT: ", vals_to_sort;
    print_util.printBlankLine();
    arr_len = len(vals_to_sort);
    for i in range (0, arr_len-1):
        curr_min = i;
        for j in range(i+1, arr_len):
            print_util.highlightStep(vals_to_sort, curr_min, j, isVerbose, False);
            print_util.unHighlightStep(vals_to_sort, curr_min, j, isVerbose, False);
            
            if vals_to_sort[j] < vals_to_sort[curr_min]:
                curr_min = j;

        if curr_min != i:
            print_util.highlightStep(vals_to_sort, i, curr_min, isVerbose);
            vals_to_sort[i], vals_to_sort[curr_min] = vals_to_sort[curr_min], vals_to_sort[i];
            print_util.unHighlightStep(vals_to_sort, i, curr_min, isVerbose);

    print "Result: ", vals_to_sort;
    print_util.printBlankLine();
    print ("END_SELECTION_SORT");
