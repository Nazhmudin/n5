file = open('Traindata2.txt', 'r')
st = file.readline()
st1 = st.split()
print(st1)
kolst = int(st1[0])
kolhours = int(st1[1])
vmest = int(st1[2])
i=0
std=[]
while i < kolst:
   st=file.readline()
   st1 = st.split()
   st1[0]=int(st1[0])
   st1[1]=int(st1[1])
   st1[2]=int(st1[2])
   print(st1)
   std.append(st1)
   i=i+1
pipls=[std[0][0]]
apipls=[std[0][1]]
maxpipls=[std[0][2]]
i=1
while i < kolst:
    pipls.append(std[i][0])
    apipls.append(std[i][1])
    maxpipls.append(std[i][2])
    i=i+1
print(pipls,apipls,maxpipls)
i=0
koltrn=0
while i < kolhours:
   print('час ',i,'   ',pipls)
   j=0
   while j < kolst:
      if (pipls[j]+apipls[j]) > maxpipls[j]:
         k=0
         trn=0
         while k < kolst:
            if (trn+pipls[j]) <= vmest:
               trn=trn+pipls[j]
               pipls[j]=0
            else:
               pipls[j]=trn+pipls[j]-vmest
               break
            k=k+1
         koltrn=koltrn+1
         j=0
         continue
      j=j+1
   j=0
   while j < kolst:
      pipls[j]=pipls[j]+apipls[j]
      j=j+1
   i=i+1
print('час ',i,'   ',pipls)
print('количество поездов = ',koltrn)
