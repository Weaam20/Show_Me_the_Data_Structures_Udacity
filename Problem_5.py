import hashlib
import datetime


class BlockChain:
    def __init__(self):
        self.blockchain = []
        self.size = 0
        self.uniqe_data = set()

    def add_block(self, data):
        """
        this method will add block to our blockchain.
        :return: None
        """
        # if the data was empty.
        if data is None:
            return None
        if data in self.uniqe_data:
            print('Please we need a uniqe data !')
            return

        # add data to set uniqe_data
        self.uniqe_data.add(data)

        # if the block was a first block in the blockchain.
        if self.size == 0:
            self.blockchain.append(Block(data, 0))
        else:
            self.blockchain.append(Block(data, self.blockchain[self.size-1].hash))

        self.size += 1

    def __repr__(self):
        if self.size == 0:
            return "Blockchain empty"

        string = ''
        for i in range(len(self.blockchain)):
            string += "Block " + str(i+1) + "\n" + str(self.blockchain[i]) + "\n"

        return string


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):

        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return '-------------------------------------' + '\n Timestamp: ' + self.timestamp + "\n" + "Data: " +\
               self.data + "\n" + "SHA256 Hash: " + str(self.hash) \
               + "\n" + "Prev_Hash: " + str(self.previous_hash) + "\n" + '-------------------------------------'


# Test case 1
block_chain = BlockChain()

print(block_chain)
block_chain.add_block(None)
block_chain.add_block("1")
block_chain.add_block("2")
block_chain.add_block("3")
print(block_chain)
print('Block chain size: ', block_chain.size)
print('-------------------------------------')

# Test case 2
b1 = BlockChain()
print(b1)  # should print empty because there is no block in b2 chain
print('-------------------------------------')

"""
Test case 3 , If all data was identical the hash value will be the same of all blocks. --> we have to reject all
 identical data.
"""

b2 = BlockChain()
b2.add_block("one")
b2.add_block("one")
b2.add_block("one")

print(b2)  # should print the first element.
print('Block chain size: ', block_chain.size)
print('-------------------------------------')
