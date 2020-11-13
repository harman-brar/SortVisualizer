import sys;
import sort_algorithms;
import print_util;

args = sys.argv;

vals_to_sort = [arg for arg in args];
del vals_to_sort[0];
sort_type = vals_to_sort.pop(0);

isVerbose = vals_to_sort[0] == '-v';
if isVerbose:
    del vals_to_sort[0];

def parseInt(n):
    return int(n);

ints_to_sort = map(parseInt, vals_to_sort);

switcher = {
    'bubble_sort': sort_algorithms.bubble_sort,
    'selection_sort': sort_algorithms.selection_sort,
    'insertion_sort': sort_algorithms.insertion_sort
};

sort_fn = switcher[sort_type];

sort_fn(ints_to_sort, isVerbose);
print_util.complexityReport(sort_type);
    