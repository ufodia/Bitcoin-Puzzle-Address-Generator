import random
import os
from bitcoin import *

def generate_keys_addresses_and_percentage(start, end):
    with open("bitcoin__puzzle_addresses.txt", "w") as file:
        for i in range(start, end + 1):
            min_range = 2 ** (i - 1)
            max_range = 2 ** i - 1
            private_key = random.randint(min_range, max_range)
            private_key_hex = hex(private_key)[2:]  # Convert to hexadecimal and remove '0x'

            # Convert the hex private key back to integer before encoding to WIF
            private_key_int = int(private_key_hex, 16)
            wif_encoded_private_key = encode_privkey(private_key_int, 'wif_compressed')

            # Calculate the percentage position of the private key in the range
            if min_range == max_range:
                percentage = 100.0
            else:
                percentage = ((private_key - min_range) / (max_range - min_range)) * 100

            # Generate public key and address
            public_key = privtopub(wif_encoded_private_key)
            address = pubtoaddr(public_key)

            # Write to file: index, private key in hex, percentage, address
            file.write(f"{i}, {private_key_hex}, {address}, {percentage:.6f}%\n")

generate_keys_addresses_and_percentage(1, 160)
