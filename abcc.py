with open('abcc.txt') as file:
    a = file.readline()
    q = [list(map(str, row.split())) for row in file.readlines()]
    q_f = a.split()

print("Q: ")
print(q)
print("F: ")
print(q_f)

with open('test_abcc.txt') as file:
    test_strs = [list(map(str, row.split())) for row in file.readlines()]

#print(test_strs)
E = ['a','b','c','d']

for i in test_strs:
    current_str = list(i[0])
    current_state = 0
    good_condition = 0
    for j in current_str:
        for var in range(len(E)):
            if j == E[var]:
                current_state = q[int(current_state)][var]
                #print(current_state)
    print(current_str)
    for d in range(len(q_f)):
        if int(current_state) == int(q_f[d]):
            good_condition += 1
    if good_condition > 0:
        print("True")
    else:
        print("False")
