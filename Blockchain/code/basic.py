import hashlib

# 1. hash the following texts using sha256
str1 = "Hello"
str2 = "안녕"
str3 = "Firm A Send 1 BTC to Firm B"

result = hashlib.sha256(str1.encode())


# 2. Build the block first block that contains upper texts
class block:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.blockData = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()


block_1 = block('block_1', [str1, str2, str3])

print(f"Q2 - 1 : {block_1.blockData} \n")

print(f"Q2 - 2 : {block_1.blockHash} \n")

# 3. Build the second block tha contains the first vlock hash
str4 = "Firm C send 3 BTC to Firm D"
str5 = "Firm C send 5 BTC to Firm D"

block_2 = block(block_1.blockHash, [str4, str5])

print(f"Q3 - 1 : {block_2.blockData} \n")
print(f"Q3 - 2 : {block_2.blockHash} \n")


# Build a BlockChain

class blockChain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(block("0", ["Genesis Block"]))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.blockHash
        self.chain.append(block(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i+1} : {self.chain[i].blockData}\n")
            print(f"Data {i+1} : {self.chain[i].blockHash}\n")

    @property
    def last_block(self):
        return self.chain[-1]


myBlock = blockChain()
myBlock.create_block_from_transaction([str1, str2])
myBlock.display_chain()
