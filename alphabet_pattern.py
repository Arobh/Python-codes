n=int(input('Enter the number: '))
bridge=[chr(65+i) for i in range (n)]
bridge_rev=[bridge[i] for i in range (len(bridge)-1)]
bridge_rev.reverse()
full_bridge=bridge+bridge_rev

#print(full_bridge)
for i in range(n):
   for j in full_bridge:
      print(j,end=' ')
   print('\n')
   full_bridge[i+n-1]=' '
   full_bridge[len(full_bridge)-n-i]=' ' 
