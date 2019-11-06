import hashlib
import time

# payload
version = (int(70015)).to_bytes(4, byteorder="little", signed=True)
services = (int(0)).to_bytes(8, byteorder="little", signed=False)
timestamp = (int(time.time())).to_bytes(8, byteorder="little", signed=True)

addr_recv_services = (int(0)).to_bytes(8, byteorder="little", signed=False)
addr_recv_ip = bytes.fromhex("127.0.0.1".encode("utf-8").hex() + ("00")*7)
addr_recv_port = (int(8333)).to_bytes(2, byteorder="big", signed=False)

addr_send_services = (int(0)).to_bytes(8, byteorder="little", signed=False)
addr_send_ip = bytes.fromhex("127.0.0.1".encode("utf-8").hex() + ("00")*7)
addr_send_port = (int(8333)).to_bytes(2, byteorder="big", signed=False)

nonce = (int(0)).to_bytes(8, byteorder="little", signed=False)
user_agent_bytes = (int(0)).to_bytes(1, byteorder="little", signed=False)
start_height = (int(0)).to_bytes(4, byteorder="little", signed=False)
relay = b'0x00'

payload = (
        version
        + services
        + timestamp
        + addr_recv_services
        + addr_recv_ip
        + addr_recv_port
        + addr_send_services
        + addr_send_ip
        + addr_send_port
        + nonce
        + user_agent_bytes
        + start_height
        + relay
        )


# header
magic_number = bytes.fromhex("f9beb4d9")
command_name = bytes.fromhex("version".encode("utf-8").hex() + ("00")*5)
payload_size = (int(len(payload))).to_bytes(4, byteorder="little", signed=False)
checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]

final_msg = (
      magic_number
      + command_name
      + payload_size
      + checksum
      + payload
)
                                           
print(final_msg.hex())





