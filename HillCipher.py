from math import gcd
import time
import numpy as np

CHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '.']

MOD = 37
class HillCipher:

    def __init__(self, size, plaintext, ciphertext):
        self.size = size
        self.plaintext = plaintext.lower()
        self.ciphertext = ciphertext.upper()

    def padding_text(self, text):
        t_pad = text.lower()
        length = len(text)
        r = length % self.size

        if (r != 0):
            for i in range(self.size - r):
                t_pad += '.'
        return t_pad

    def divide_text(self, text):
        list_text_block = []

        p_text = self.padding_text(text)

        no_block = int(len(p_text) // self.size)
        for i in range(no_block):
            text_block = []
            for j in range(self.size):
                block_row = []
                e = CHARACTER.index(p_text[i*self.size + j])
                block_row.append(e)
                text_block.append(block_row)
            list_text_block.append(np.array(text_block))
        
        return list_text_block

    def inverse_key(self, K):
        dK = int(np.linalg.det(K))
        idK = pow(dK,-1,MOD)
        Pk = dK*np.linalg.inv(K)
        Pk = np.around(Pk)
        Pk = Pk.astype(int)
        for i in range(len(Pk)):
            for j in range(len(Pk[i])):
                if Pk[i][j] < 0:
                    Pk[i][j] += MOD
        
        return idK*Pk % MOD

class Improve(HillCipher):

    def __init__(self, K1, K2, size, plaintext, ciphertext):
        super().__init__(size, plaintext, ciphertext)
        self.K1 = K1
        self.K2 = K2

    def check_key(self):
        det_K1 = np.linalg.det(self.K1)
        det_K2 = np.linalg.det(self.K2)

        if det_K1 != 0 and gcd(det_K1, MOD) == 1: 
            check_K1 = True 
        else:
            check_K1 = False
        if det_K2 != 0 and gcd(det_K2, MOD) == 1:
            check_K2 = True
        else:
            check_K2 = False
        return check_K1 & check_K2

    def encrypt(self):
        start = time.time()
        list_ciphertext_block = []
        list_plaintext_block = self.divide_text(self.plaintext)

        for i in range(len(list_plaintext_block)):
            block = list_plaintext_block[i]
            C1 = ((self.K1).dot(block)) % MOD
            
            C2 = []
            K2_pow = np.linalg.matrix_power(self.K2, i+1)
            for row in K2_pow:
                C2_row = []
                sum_row = 0
                for e in row:
                    sum_row += e
                r = sum_row % MOD
                C2_row.append(r)
                C2.append(C2_row)

            C3 = (C1 + C2) % MOD
            list_ciphertext_block.append(C3)
        
        for block in list_ciphertext_block:
            for row in block:
                self.ciphertext += CHARACTER[row[0]].upper()
        
        end = time.time()
        return end - start
        
    def decrypt(self):
        start = time.time()
        list_plaintext_block = []
        list_ciphertext_block = self.divide_text(self.ciphertext)
        iK1 = self.inverse_key(self.K1)

        for i in range(len(list_ciphertext_block)):
            block = list_ciphertext_block[i]

            C2 = []
            K2_pow = np.linalg.matrix_power(self.K2, i+1)
            for row in K2_pow:
                C2_row = []
                sum_row = 0
                for e in row:
                    sum_row += e
                r = sum_row % MOD
                C2_row.append(r)
                C2.append(C2_row)
            
            C1 = block - C2
            C3 = iK1.dot(C1) % MOD
            list_plaintext_block.append(C3)

        for block in list_plaintext_block:
            for row in block:
                self.plaintext += CHARACTER[int(row[0])]

        end = time.time()
        return end - start

class Classical(HillCipher):

    def __init__(self, K, size, plaintext, ciphertext):
        super().__init__(size, plaintext, ciphertext)
        self.K = K

    def check_key(self):
        det_K = np.linalg.det(self.K)
        if det_K != 0 and gcd(det_K, MOD) == 1:
            check = True
        else:
            check = False
        return check

    def encrypt(self):
        start = time.time()
        list_plaintext_block = self.divide_text(self.plaintext)
        list_ciphertext_block = []

        for block in list_plaintext_block:
            C1 = ((self.K).dot(block)) % MOD
            list_ciphertext_block.append(C1)

        for block in list_ciphertext_block:
            for row in block:
                self.ciphertext += CHARACTER[row[0]].upper()

        end = time.time()
        return end - start

    def decrypt(self):
        start = time.time()
        list_plaintext_block = []
        list_ciphertext_block = self.divide_text(self.ciphertext)
        iK = self.inverse_key(self.K)
        
        for block in list_ciphertext_block:
            C1 = (iK.dot(block)) % MOD
            list_plaintext_block.append(C1)

        for block in list_plaintext_block:
            for row in block:
                self.plaintext += CHARACTER[int(row[0])].lower()

        end = time.time()
        return end - start
'''
#example improve
k1 = np.array([[1,2,3],[3,5,5],[4,5,6]])
k2 = np.array([[0,1,2],[3,4,0],[0,0,1]])
size = 3
#encrypt improve
plaintext1 = "huyne"
ciphertext1 = ""
encrypt_improve = Improve(k1,k2,size,plaintext1,ciphertext1)
time_encrypt_improve = encrypt_improve.encrypt()
print(time_encrypt_improve)
print("Encrypt Improve: " + encrypt_improve.ciphertext)
#decrypt improve 
plaintext2 = ""
ciphertext2 = "L0O1R4"
decrypt_improve = Improve(k1,k2,size,plaintext2,ciphertext2)
time_decrypt_improve = decrypt_improve.decrypt()
print("Decrypt Improve: " + decrypt_improve.plaintext)

#example classical
k = np.array([[1,2,3],[3,5,5],[4,5,6]])
size = 3
#encrypt classical
plaintext3 = "huyne"
ciphertext3 = ""
encrypt_classical = Classical(k,size,plaintext3,ciphertext3)
time_encrypt_classical = encrypt_classical.encrypt()
print("Encrypt Classical: " + encrypt_classical.ciphertext)
#Decrypt classical
plaintext4 = ""
ciphertext4 = "ITNSR3"
decrypt_classical = Classical(k,size,plaintext4,ciphertext4)
time_decrypt_classical = decrypt_classical.decrypt()
print("Decrypt Improve: " + decrypt_classical.plaintext)'''