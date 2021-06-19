import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

plaintext = b'Attack at dawn'
key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)
CipherText = cipher.encrypt(plaintext)

ct = b64encode(CipherText).decode('utf-8')

#result = json.dumps({'CipherText':CipherText})
print(ct)