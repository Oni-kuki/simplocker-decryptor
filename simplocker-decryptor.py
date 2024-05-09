from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad

class AesCrypt:
    def __init__(self, key):
        self.key = SHA256.new(key.encode()).digest()
        self.iv = b'\x00' * 16  

    def decrypt(self, input_file, output_file):
        with open(input_file, 'rb') as f_in:
            cipher_text = f_in.read()
        decryptor = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        plain_text = unpad(decryptor.decrypt(cipher_text), AES.block_size)
        with open(output_file, 'wb') as f_out:
            f_out.write(plain_text)

# Usage :
key = "SPECIFIC-KEY" 
aes = AesCrypt(key)

# Decrypt file
aes.decrypt("ENCRYPTED.enc", "DECRYPTED.XX")
