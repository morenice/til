from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt_aes_text(key, data: str):
    """
    Advanced Encrypt Standard
     - symmetric key encryption
    """
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    print('text: {0}'.format(data))
    print('ciphertext: {0}'.format(ciphertext.hex()))
    print('tag: {0}'.format(tag.hex()))
    print('nonce: {0}'.format(cipher.nonce.hex()))

    return {
        'nonce':cipher.nonce.hex(),
        'tag': tag.hex(),
        'ciphertext': ciphertext.hex()
    }

def decrypt_aes_text(key, nonce, tag, ciphertext):
    """
    Advanced Encrypt Standard
     - symmetric key decryption
    """
    ciphertext = bytes.fromhex(ciphertext)
    nonce = bytes.fromhex(nonce)
    tag = bytes.fromhex(tag)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print('decrpyt: {0}'.format(data.decode('utf-8')))


if __name__ == "__main__":
    # AES 16 byte key
    #
    key = 'Q9=1@Ad*iKq1(*&m'.encode('utf-8')
    #key = get_random_bytes(16)

    result = encrypt_aes_text(key, '1')
    decrypt_aes_text(key, result['nonce'], result['tag'], result['ciphertext'])
    print('')

    result = encrypt_aes_text(key, '1a')
    decrypt_aes_text(key, result['nonce'], result['tag'], result['ciphertext'])
    print('')

    result = encrypt_aes_text(key, '123456aab')
    decrypt_aes_text(key, result['nonce'], result['tag'], result['ciphertext'])
    print('')

    result = encrypt_aes_text(key, 'Qaf12bp1[]34&*5@512$3aax!@#1')
    decrypt_aes_text(key, result['nonce'], result['tag'], result['ciphertext'])
    print('')

