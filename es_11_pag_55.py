x = [0, 1, 2, 3, 5, 6, 7, 8]
lung = len(x)
meta = lung // 2#divisione intera
x2 = x[:meta]
x3 = x[meta:]
x2.append(5)
print(x2)
print(x3)