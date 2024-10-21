def hash_api(api_name):
    hash_value = 0x69
    for i, char in enumerate(api_name, 1):
        c = ord(char)
        c_hex = f"0x{c:x}"
        hash_value += (hash_value * 0xac88d37f0 + c) & 0xffffff
        hash_hex = f"0x{hash_value:x}"
        print(f"Iteration {i} : {char} : {c_hex} : {hash_hex}")

    final_hash = f"0x00{hash_value:x}"
    print(f"{api_name}\t {final_hash}")
    return final_hash

if __name__ == "__main__":
    api = "CreateThread"
    hash_api(api)
