import sys
from Node import Node
from PriorityQueue import PriorityQueue


def Print(text):
    if text is None or len(text) == 0:
        print('invalid text.')
        print('--------------------------------------------------------------')
        return

    text_set = set()
    for i in text:
        text_set.add(i)

    if len(text_set) == 1:
        print('invalid text.')
        print('--------------------------------------------------------------')
        return

    print("The size of the data is: {}\n".format(sys.getsizeof(text)))
    print("The content of the data is: {}\n".format(text))

    encoded_data, tree = huffman_encoding(text)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    print('--------------------------------------------------------------')


# this method will print huffman tree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print('Data: ', root.data, 'Freq: ', root.frequency)
        if root.right is not None:
            print('Right: ', root.right.data)
        if root.left is not None:
            print('Left: ', root.left.data)
        inorder(root.right)

# end method inorder(root)


def generate_encoded_data(root):
    """
    :param root: is a root of huffman tree
    :return: dictionary contains all codes for each letter in the text.
    """
    return generate_encoded_data2(root, {}, '')


# helper method
def generate_encoded_data2(root, dic, code):
    if root is not None:
        # go left of the tree if root has a left child.
        if root.left is not None:
            s = code + '0'
            generate_encoded_data2(root.left, dic, s)

        # if root is a leaf node then add this letter as a key and the code as a value.
        if str(root.data).isalpha() or root.data == ' ':
            dic.update({root.data: code})

        # go left of the tree if root has a right child.
        if root.right is not None:
            s = code + '1'
            generate_encoded_data2(root.right, dic, s)

        return dic
    else:
        return None


def huffman_encoding(data):
    """
    :param data: is the text that will we encode.
    :return: encoded text as a binary and a root of huffman tree.
    """
    if len(data) == 0 or data is None:
        print('Please enter a valid data.')
        return '', None

    min_heap = PriorityQueue()
    count_dic = {}
    # count frequency of each letter and add it in count_dic as a value of the letter.
    for i in range(len(data)):
        if data[i] in count_dic:
            count_dic[data[i]] += 1
        else:
            count_dic[data[i]] = 1

    # add all element in count_dic to min_heap.
    for i, j in count_dic.items():
        new_node = Node(i, j)
        min_heap.push(new_node, new_node.frequency)

    count: int = 1

    # create huffman tree phase 1.
    while min_heap.size() >= 2:
        item_1 = min_heap.pop()
        item_2 = min_heap.pop()
        sum_frequency = item_1.frequency + item_2.frequency
        node = Node(count, sum_frequency, item_1, item_2)
        min_heap.push(node, node.frequency)
        count += 1

    # the root of huffman tree.
    root = min_heap.pop()
    # generate the Encoded Data.
    codes_ = generate_encoded_data(root)

    # create string represent encoded data.
    encoded = ''
    for char in data:
        if codes_.get(char) is not None:
            encoded += codes_.get(char)

    return encoded, root


def huffman_decoding(data, root):
    """
    :param data: is the encoded text as a binary.
    :param root: is the root of huffman tree.
    :return: the decoded data.
    """
    if len(data) == 0:
        print('Please enter a valid data.')
        return '', None

    decoded = ''
    i = 0
    curr = root
    while i < len(data):
        """
        If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if
         the current bit is 1.
        """
        if data[i] == '0':
            curr = curr.left
        else:
            curr = curr.right
        # go to the next cell of the encoded data.
        i += 1

        # if curr is leaf node then this node contain a letter.
        if curr.is_leaf():
            # add this letter to decoded data.
            decoded += curr.data
            # return and start from the root to find the next letter.
            curr = root

    return decoded


# Test case 1 -----------------------------------
a_great_sentence = 'The bird is the word'
Print(a_great_sentence)

# Test case 2 -----------------------------------
t1 = ''
Print(t1)  # will print 'invalid text'

# Test case 3 -----------------------------------
t2 = 'AAAAAB'
Print(t2)

# Test case 4 -----------------------------------
t3 = 'AAAAA'
Print(t3)   # will print 'invalid text'
