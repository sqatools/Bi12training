list1=[[2, 1], 2, 3, [2, 4], 5, 1]
output=[]
for i in list1:
   if isinstance(i,list):
       for j in i:
           output.append(i[1])
   else:
       output.append(i)
print(output)