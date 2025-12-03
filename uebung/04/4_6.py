
f1 = (0, 0, 1, 1, 0, 1, 0, 0, 0)
f2 = (0, 1, 0, 0, 1, 0, 1, 0, 0)

for i in range(9):
    sum = 0
    s = "c_%s=\\sum_{j\\leq%s}(f_1)_j\\cdot_F (f_2)_{%s-j}&="%(i, i, i)
    cs = []
    for j in range(i + 1):
        cs.append(("%s\\cdot_F %s")%(f1[j], f2[i-j]))
        sum += (f1[j] * f2[i-j]) % 2
        sum = sum % 2
    #print(f"{s}{'+_F'.join(cs)}={sum}\\\\")
    print(sum)
