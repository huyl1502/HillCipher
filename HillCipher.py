import numpy as np

CHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '.']

class HillCipher:

    def __init__(self, size, plaintext, ciphertext):
        self.size = size
        self.plaintext = plaintext
        self.ciphertext = ciphertext

    def padding_plaintext(self):
        pt_pad = self.plaintext
        length = len(self.plaintext)
        r = length % self.size

        if (r != 0):
            for i in range(self.size - r):
                pt_pad += '.'
        return pt_pad

    def divide_plaintext(self):
        list_plaintext_block = []

        plaintext = self.padding_plaintext()

        no_block = int(len(plaintext) // self.size)
        for i in range(no_block):
            plaintext_block = []
            for j in range(size):
                block_row = []
                e = CHARACTER.index(plaintext[i*self.size + j])
                block_row.append(e)
                plaintext_block.append(block_row)
            list_plaintext_block.append(np.array(plaintext_block))
        
        return list_plaintext_block


class Improve(HillCipher):

    def __init__(self, k1, k2, size, plaintext, ciphertext):
        super().__init__(size, plaintext, ciphertext)
        self.k1 = k1
        self.k2 = k2

    def check_key(self):
        return np.linalg.det(self.k1) & np.linalg.det(self.k2)

    def encrypt(self):
        list_ciphertext_block = []
        list_plaintext_block = self.divide_plaintext()

        for i in range(len(list_plaintext_block)):
            block = list_plaintext_block[i]
            c1 = ((self.k1).dot(block)) % 37
            
            c2 = []
            k2_pow = np.linalg.matrix_power(k2, i+1)
            for row in k2_pow:
                c2_row = []
                sum_row = 0
                for e in row:
                    sum_row += e
                r = sum_row % 37
                c2_row.append(r)
                c2.append(c2_row)

            c3 = (c1 + c2) % 37
            list_ciphertext_block.append(c3)
        
        for block in list_ciphertext_block:
            for row in block:
                self.ciphertext += CHARACTER[row[0]]

    def decrypt(self):
        pass

class Classical(HillCipher):

    def __init__(self, k, size, plaintext, ciphertext):
        super().__init__(size, plaintext, ciphertext)
        self.k = k

    def check_key(self):
        return np.linalg.det(self.k)

    def encrypt(self):
        list_plaintext_block = self.divide_plaintext()
        list_ciphertext_block = []

        for i in range(len(list_plaintext_block)):
            block = list_plaintext_block[i]
            c1 = ((self.k).dot(block)) % 37
            list_ciphertext_block.append(c1)

        for block in list_ciphertext_block:
            for row in block:
                self.ciphertext += CHARACTER[row[0]]

    def decrypt(self):
        pass

#example
k1 = np.array([[1,2,3],[3,4,5],[4,5,6]])
k2 = np.array([[0,1,2],[3,4,0],[0,0,1]])
size = 3
plaintext = "abc."
ciphertext = ""
hill_cipher = Classical(k1,size,plaintext,ciphertext)
hill_cipher.encrypt()
print(hill_cipher.ciphertext)