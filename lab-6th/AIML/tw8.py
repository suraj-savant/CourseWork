# Define input vectors and corresponding output labels
inputs = [
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
]
labels = [1, -1, -1, -1]

w1 = w2 = bw = 0
print("dw1","\t", "dw2","\t", "db", "\t", "w1", "\t", "w2", "\t", "bw" )
for i, x in enumerate(inputs):
    dw1 = x[0] * labels[i]
    dw2 = x[1] * labels[i]
    db = labels[i]

    w1 += dw1
    w2 += dw2
    bw += db

    print(dw1,"\t", dw2,"\t", db, "\t", w1, "\t", w2, "\t", bw )

print("Learning complete")

print("\nlearning outcome for AND gate")
bias = 1
for x in inputs:
    X = x[0] * w1 + x[1] * w2 + bias * bw
    Y = 1 if X>0 else -1
    print(x, Y)