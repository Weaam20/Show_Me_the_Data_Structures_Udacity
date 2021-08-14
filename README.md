# Project 2 | Show Me the Data Structures

## Description 
In this project, we will answer the six questions. The questions cover a variety of topics related to the data structures we have learned in this course.
We will write up a clean and efficient answer in Python.

## Questions 

**Problem 1 | LRU Cache :**

In this problem, our goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least 
recently used entry when the cache memory reaches its limit. For the current problem, we have to design LRU with a data structure that can search, insert and delete in O(1). 
In this problem, I used two data structures a  dictionary and a doubly-linked list why? dictionary for fast lookup and doubly-linked list for insert and delete in O(1).

**Problem 2 | Finding Files (Recursion) :**

In this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c". I used DFS to search in the directory
once I find any file that ends with ".c" I will add it to my solution.

**Problem 3 | Huffman Coding (Data Compression) :**

In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the
transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, we have to implement the logic
for both encoding and decoding. In the first phase we have to build the Huffman Tree we will recive a message we have to compression it but how? 


  ### Encoding 
  **Phase 1 | Build the Huffman Tree :**
  
      A Huffman tree is built in a bottom-up approach by useing Priority queue
     
      - First, you determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.

      - Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require
      to pop-out the node having the lowest frequency. Therefore, you build and sort a list of nodes in the order lowest to highest frequencies.
      
      - Pop-out two nodes with the minimum frequency from the priority queue.
      
      - Create a new node with a frequency which equals to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, 
      and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly
      created node back into the priority queue.
      
      - Repeat steps #3 and #4 until you have a single element left in the priority queue. 
      
  **Phase 2 | Generate the Encoded Data :** 
 
      - Based on the Huffman tree, generate a unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to 
      the leaf node.
      
  ### Decoding 
      Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data
 
      - Declare a blank decoded string.
      - Pick a bit from the encoded data, traversing from left to right.
      - Start traversing the Huffman tree from the root.
      
        - If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
        - If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
        
      - Repeat steps #2 and #3 until the encoded data is completely traversed.
      
**Problem 4 | Active Directory :** 

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We have to write a function that provides an efficient look up of whether the user is in a group.

**Problem 5 | Blockchain :** 

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time 
when the block was created, and text strings as data. In this problem we have to implement blockchain.

**Problem 6 | Union and Intersection :** 

In this problem, We have to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. 
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. We will receive two linked lists and we have 
to find the union and intersection items between these lists.
