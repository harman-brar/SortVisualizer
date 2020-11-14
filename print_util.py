def highlightStep(vals_to_sort, l, r, isVerbose, isSwap=True):
    if not isVerbose:
        return;
    if l == r:
        return;

    if isSwap:
        vals_to_sort[l] = str(vals_to_sort[l]) + " ->";
        vals_to_sort[r] = "<- " + str(vals_to_sort[r]);
    else:
        vals_to_sort[l] = "*" + str(vals_to_sort[l]) + "*";
        vals_to_sort[r] = "*" + str(vals_to_sort[r]) + "*";
    print(vals_to_sort);

def unHighlightStep(vals_to_sort, l, r, isVerbose, isSwap=True):
    """ Orginal l and r are now swapped """
    if not isVerbose:
        return;
    if l == r:
        return;

    if isSwap:
        vals_to_sort[l] = int(vals_to_sort[l][3:]);
        vals_to_sort[r] = int(vals_to_sort[r][:-3]);
    else:
        vals_to_sort[l] = int(vals_to_sort[l][1: -1]);
        vals_to_sort[r] = int(vals_to_sort[r][1: -1]);
    print ""

def complexityReport(sort_type):
    switcher = {
        'bubble_sort': "O(n^2) time | O(1) space",
        'selection_sort': "O(n^2) time | O(1) space",
        'insertion_sort': "O(n^2) time | O(1) space",
        'merge_sort': "O(nlogn) time | O(n) space",
        'quick_sort': "Worst: O(n^2), Avg: O(nlogn) time | O(logn) space",
        'heap_sort': "O(nlogn) time | O(1) space"
    };

    print "==================|   Complexity Report:   " + switcher[sort_type] + "     |==================\n";

def printBlankLine(isVerbose):
    if not isVerbose:
        return;
    print "\n";

def gap():
    print "";

def printResult(sorted_array):
    gap();
    print "Result: ", sorted_array;
    gap();

def printSeparation(isVerbose):
    if not isVerbose:
        return;
    print "----------------------------"

def printIterator(i, isVerbose):
    if not isVerbose:
        return;
    print "i = " + str(i);
    printSeparation(isVerbose);

def printIfVerbose(str, isVerbose):
    if isVerbose:
        print str;
