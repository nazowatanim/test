'''extracts the specific column information of 'ps aux' command with pandas'''
#test code
import psutil
import subprocess
import os
import pandas as pd
# print (p.USER)

output_lines= [s.split() for s in os.popen("ps aux").read().splitlines()]
df=pd.DataFrame(output_lines)
#print(df)
df1=df.iloc[1:,2]
df2=df.iloc[1:,1]
for i in df2:
    p=psutil.Process(i)
    print(p.cpu_percent())
#print(df1)
sum=0
for i in df1:
    #print(i)
    i=float(i)
    sum=sum+i
print(sum)
#print (output_lines)
def test():
    l = []
    j = []
    k = []
    for line in output_lines:
        one = line[2]
        two = line[1]#test
        three = line[3]#test
        l.append(one)
        j.append(two)#test
        k.append(three)#test
    #print(l)

# print (j)
# print(k)


test()


