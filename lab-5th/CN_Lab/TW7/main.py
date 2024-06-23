def crc_encode(data, divisor):
    # Append zeros to the data for the divisor length
    data += '0' * (len(divisor) - 1)
    
    # Convert data and divisor to lists for easier manipulation
    data_list = list(data)
    divisor_list = list(divisor)
    
    # Perform CRC division
    for i in range(len(data) - len(divisor) + 1):
        if data_list[i] == '1':
            for j in range(len(divisor)):
                data_list[i + j] = str((int(data_list[i + j]) + int(divisor_list[j])) % 2)
    
    # Return the CRC code (remainder)
    return ''.join(data_list[-len(divisor) + 1:])

def crc_decode(received_data, divisor):
    # Convert received data and divisor to lists for easier manipulation
    received_data_list = list(received_data)
    divisor_list = list(divisor)
    
    # Perform CRC division
    for i in range(len(received_data) - len(divisor) + 1):
        if received_data_list[i] == '1':
            for j in range(len(divisor)):
                received_data_list[i + j] = str((int(received_data_list[i + j]) + int(divisor_list[j])) % 2)
    
    # If there is no remainder, the data is correct
    if all(bit == '0' for bit in received_data_list[-len(divisor) + 1:]):
        return True
    else:
        return False

def main():
    # Input data and divisor
    data = input("Enter the data to be sent (binary): ")
    divisor = input("Enter the divisor (binary): ")

    # Encode the data with CRC
    crc_code = crc_encode(data, divisor)
    print(f"CRC Code: {crc_code}")

    #print no error codeword 
    print(f"No error codeword {data}{crc_code}")

    # Simulate transmission by introducing errors (flip some bits)
    received_data = input("Enter the received data (binary with possible errors): ")

    # Decode the received data and check for errors
    is_error = not crc_decode(received_data, divisor)

    if is_error:
        print("Error detected in the received data.")
    else:
        print("No error detected. Data is correct.")

if __name__ == "__main__":
    main()
