import sys;
import sort_algorithms;
import print_util;

args = sys.argv;

del args[0];
sort_type = args.pop(0);

isVerbose = args[0] == '-v';
if isVerbose:
    del args[0];

vals_to_sort = args

def parseInt(n):
    return int(n);

ints_to_sort = map(parseInt, vals_to_sort);

switcher = {
    'bubble_sort': sort_algorithms.bubble_sort,
    'selection_sort': sort_algorithms.selection_sort,
    'insertion_sort': sort_algorithms.insertion_sort,
    'merge_sort': sort_algorithms.merge_sort,
    'quick_sort': sort_algorithms.quick_sort,
    'heap_sort': sort_algorithms.heap_sort
};

sort_fn = switcher[sort_type];

sort_fn(ints_to_sort, isVerbose);
print_util.complexityReport(sort_type);
    