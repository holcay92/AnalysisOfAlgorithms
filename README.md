# AnalysisOfAlgorithms

Design an experiment to compare different algorithms for the selection problem, i.e. finding k’th smallest element in an unsorted list of n numbers. There are following candidate methods:

In this experiment, you are asked to compare these seven methods for finding the 𝑘’th smallest element in various input lists (of various sizes and various characteristics). You have to decide on sample inputs to best clarify the performance characteristics of algorithms. While doing your emprical analysis, you may use physical unit of time, count actual number of basic operation's executions, or both. You are also expected to compare your findings with theoretical complexity values. You should provide extensive comments on your results.


(i) Sort all elements by Insertion-sort and return the 𝑘’th element in the list,

(ii) Sort all elements by Merge-sort and return the 𝑘’th element in the list,

(iii) Sort all elements by Quick-sort and return the 𝑘’th element in the list. While partitioning choose the pivot element as the first element in an array.

(iv) Apply partial selection-sort, i.e. find the minimum element 𝑘 times to find the 𝑘’th smallest element.

(v) Apply partial heap-sort, i.e. store all elements in a max-heap and apply 𝑛−𝑘 times max removal. Return the max element in the root,

(vi) Not sort the list, but apply quick select algorithm, which is based on array partitioning, as described in the class. While partitioning, choose the pivot element as the first element in an array,

(vii) Apply quick select algorithm, but this time use median-of-three pivot selection1

[project document.pdf](https://github.com/holcay92/AnalysisOfAlgorithms/files/8681142/project.document.pdf)
