count = 1000
packets = [200, 500, 600, 700, 450, 400, 200]
length = len(packets)
index = length-1

while index<length and index > 0 :
    while count > packets[index] :
        print("Packet moved out of queue", packets[index])
        count = count-packets[index]
        index = index -1

    print(f"Count {count} is less than packet value {packets[index]}")
    count = 1000

print("All packets are moved out of the queue")