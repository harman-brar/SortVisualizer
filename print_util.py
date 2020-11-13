def highlightStep(vals_to_sort, l, r, isVerbose, isSwap=True):
    if not isVerbose:
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
        'selection_sort': "O(n^2) time | O(1) space"
    };

    print "==================|   Complexity Report:   " + switcher[sort_type] + "     |==================";

def printBlankLine():
    print "\n";