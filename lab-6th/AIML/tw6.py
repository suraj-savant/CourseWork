dataset = [
    ([1,1],1),
    ([1,0],1),
    ([0,1],1),
    ([0,0],0)
]

def step(x):
    if x>0:
        return 1
    return 0

learning_rate = 0.2
weigth = [-0.2, 0.4]
epochs = 10

for epoch in range(epochs):
    print(f"\nAt epoch {epoch+1}")
    ip, outcome = dataset[epoch%4]
    x = ip[0] * weigth[0] + ip[1] * weigth[1]
    Y = step(x)
    error = outcome - Y
    if weigth != 0:
        weigth[0] += ip[0] * learning_rate * error
    print(f"For {ip}, expected {outcome}, computed {Y}, error {error}, weigths {weigth}")


print("Sample IO")
for ip, outcome in dataset :
    x = ip[0] * weigth[0] + ip[1] * weigth[1]
    Y = step(x)
    print(f"{ip}, {Y}")

    

    



