a=[2,5,-5,14,8,9,-11]; b=2
print(max(sum(a[i:i+b]) for i in range(len(a)-b+1)))
