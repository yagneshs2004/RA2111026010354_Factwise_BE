n1=(0,3,3,5,4,4,3,5,5,4)    
n10=(0,3,6,6,5,5,5,7,6,6)   
n11=(0,6,6,8,8,7,7,9,8,8)   
n=(7,10,11) 

hundreads = (sum(n1)*9 + n10[1] + sum(n11) + sum(n10[2:])*10)*10
thousands = n[0]*9 + n[1]*99*9 + sum(n1)*100 
    
letters = hundreads + thousands + n[2]
print(letters)
