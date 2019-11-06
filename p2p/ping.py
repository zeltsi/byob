import random
import hashlib

# payload
nonce = (random.getrandbits(64)).to_bytes(8, byteorder="little", signed=False)

# header
magic_number = bytes.fromhex("f9beb4d9")
command_name = bytes.fromhex("ping".encode("utf-8").hex() + ("00")*8)
payload_size = (int(len(nonce))).to_bytes(4, byteorder="little", signed=False)
checksum = hashlib.sha256(hashlib.sha256(nonce).digest()).digest()[:4]

final_msg = (
        magic_number
        + command_name
        + payload_size
        + checksum
        + nonce
        )


print(final_msg.hex())
