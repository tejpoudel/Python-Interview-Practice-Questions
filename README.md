#Technical Inverview Practice
#Tej Poudel - Full Stack Developer NanoDegree
# Date: Oct 13, 2017

##Project Overview
For this project, I have answered 5 technical interview questions.


##What did I Learn?
I learned where I interviewing weaknesses lie. I leanrned the techniques how do I imply the algorithm to the problems. I am also ready for the technical interview for my next job. 


##Questions
##Question 1
Given two strings `s` and `t`, determine whether some anagram of `t` is a substring of `s`. For example: if `s = "udacity"` and `t = "ad"`, then the function returns `True`. Your function definition should look like: `question1(s, t)`, and return a boolean `True` or `False`.

######Question 1 Answer
In order for `t` to be a substring of `s`, it must be true that all characters (including duplicates) in `t` are contained in `s`. In order to count the number of characters in `s`, then, we should use two hash tables to compare the components of two strings.

While it's possible to consider all permutations of t and see if any one of them is in str, this approach is inefficient: it will take O(m! n) where m = len(t) and n = len(str) . My approach is to break up the strings into lists of characters (t_list and s_list). We then only go through s_list once: if we get to a character in t, we remove this character from t_list. If after a number of such steps t_list has length zero, some order of the letter in t was contained in str and we can return True.

The time complexity of this solution is O(s) because t is smaller than s, and at the worst case s must be traversed completely. The space complexity is O(1) because there are 26 letters in the Englis alphabet.


##Question 2
Given a string `a`, find the longest palindromic substring contained in `a`. Your function definition should look like `question2(a)`, and return a string.

######Question 2 Answer
What's the space complexity here? For `bananas` (7 characters), we have to start from each character and get the substrings from there. Starting from `b` we hit each of the 6 letters after that: `ba`, `ban`, `bana`, `banan`, `banana`, `bananas`; then `a`: `an`, `ana`, `anan`, `anana`, `ananas` (5 remaining letters); next, `n`: `na`, `nan`, `nana`, `nanas` (4). There seems to be a pattern here!

A first approach could be to reverse the string so it reads backwards, list all substrings, and see which of these substrings is the longest one which appears in the original string. The approach I took searches for all palindromic centers, by going through the string only once, and when the previous and the next characters are the same (or we have a double), declare this to be the center of a palindrome. My approach treats the string much like a list, rather than a stack or a tree. It is possible that turning the string into a binary search tree, our palindromic search to find centers could be reduced to O(log(n)).

The time for this would be O(n3), because making all substrings would be O(n2) and for each one we need to perform a search O(n).


##Question 3
Given an undirected graph `G`, find the minimum spanning tree within `G`. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

```python
{'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
```
Vertices are represented as unique strings. The function definition should be `question3(G)`

######Question 3 Answer

This problem seems similar to the shortest-length problem: from a given vertex, we could look for the shortest path is to all the other vertices. However, it may be that this choice of connectivity it globally sub-optimal, i.e. that it is only optimal with regards to that particular vertex. The solution I chose makes use of sets and is similar to hierarchical clustering. We begin with each node belonging to a separate "cluster", where the clusters are in the form of sets. We then go through the list of edges, ordered by weight. Even a simple disjoint-set data structure such as disjoint-set forests with union by rank can perform O(V) operations in O(V log V) time. Thus the total time is O(E log E) = O(E log V).


##Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like `question4(T, r, n1, n2)`, where `T` is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a `1` represents a child node, `r` is a non-negative integer representing the root, and `n1` and `n2` are non-negative integers representing the two nodes in no particular order. For example, one test case might be

```python
question4([[0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [1, 0, 0, 0, 1], 
           [0, 0, 0, 0, 0]], 
          3,
          1,
          4)
```

and the answer would be `3`.

######Question 4 Answer

We can assume the input is a Binary Search Tree, the time complexity of above solution is O(h) where h is height of tree. In a binary search tree, since all descendants on either side of a node are smaller or larger than that node, we are easily able to determine what the least common ancestor of any two nodes is: it is the ancestor node whose value lies between the two chosen nodes. If the two chosen nodes are in a descendant relationship to each other, e.g. one is the child of the other, then the least common ancestor is the node preceding the parent node. To solve this problem we only need to flow down the binary search tree, and stop when we find a node that lies between the two chosen nodes or is a parent to one of the two nodes. The final runtime efficiency is O(n log(n)).


##Question 5
 Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like `question5(ll, m)`, where `ll` is the first node of a linked list and `m` is the "mth number from the end". You should copy/paste the `Node` class below to use as a representation of a node in the linked list. Return the value of the node at that position.

```python
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
``` 

######Question 5 Answer
We can simply calculate the length of the linked list and access the (length - reverse_index)th element, with a time complexity of O(n). Since linked lists don't have indices we have to traverse all the links in order to find out how long the list is. The easiest strategy is to create a LinkedList object which simultaneously constructs the linked list alongside an array that keeps track of all its values. Our solution will be therefore to first traverse the linked list to find out its length, then traverse it again, but this time only the first n-m steps, and return the value of the node we land on. This solution has time efficiency O(2 n), which is still O(n) in the length of the linked list.
