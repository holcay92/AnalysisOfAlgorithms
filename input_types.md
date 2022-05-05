1- insertion sort worst case: descending order
                best case: ascending order
                
2- Merge sort

worst case:In order to generate the worst case of merge sort,
the merge operation that resulted in above sorted array should result in maximum comparisons.
In order to do so, the left and right sub-array involved in merge operation should store alternate elements of sorted array.
i.e. left sub-array should be {1,3,5,7} and right sub-array should be {2,4,6,8}.
Now every element of array will be compared at-least once and that will result in maximum comparisons.
We apply the same logic for left and right sub-array as well. For array {1,3,5,7},
the worst case will be when its left and right sub-array are {1,5} and {3,7}
respectively and for array {2,4,6,8} the worst case will occur for {2,4} and {6,8}.
              
best case:The idea is to consider the case when array is already sorted. Before merging,
just check if arr[mid] > arr[mid+1], because we are dealing with sorted subarrays.
This will lead us to the recursive relation T(n) = 2*T(n/2) + 1 which can be resolved by the master’s theorem,
so T(n) = n.


3- quick sort worst case: select the biggest or the smallest element as pivot descending order
                
best case: always picks the middle element as pivot

4- partial heap-sort 
worst case: The worst case for heap sort might happen when all elements in the list are distinct.
best case: The best case for heapsort would happen when all elements in the list to be sorted are identical

5- partial selection-sort

worst case: descending order
best case: ascending order
                
6- Quick select

  worst case: ?
  
  best case: k'th element is the pivot
  
  
