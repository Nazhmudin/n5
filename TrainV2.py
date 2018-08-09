file = open('Traindata1.txt', 'r')
st = file.readline()
st1 = st.split()
kolst = int(st1[0])
kolhours = int(st1[1])
vmest = int(st1[2])
std=[]
for i in range(kolst):
   st=file.readline()
   st1 = st.split()
   st1[0]=int(st1[0])
   st1[1]=int(st1[1])
   st1[2]=int(st1[2])
   std.append(st1)
pipl=[std[0][0]]
apipl=[std[0][1]]
maxpipl=[std[0][2]]
i=1
for i in range(1,kolst):
    pipl.append(std[i][0])
    apipl.append(std[i][1])
    maxpipl.append(std[i][2])

def coltrn():
   global koltrn
   k=0
   trn=0
   while k < kolst:
      if (trn+pipl[k]) <= vmest:
         trn=trn+pipl[k]
         pipl[k]=0
      else:
         pipl[k]=trn+pipl[k]-vmest
         break
      k=k+1
   koltrn=koltrn+1
def prognoz(klh):
   sos='not'
   dpl=pipl
   i=1
   while i < klh:
      j=0
      while j < kolst:
         dpl[j]=dpl[j]+apipl[j]
         if (dpl[j] < maxpipl[j]):
            pass
         else:
            sos='yes'
            break
         j=j+1
      if sos=='yes':
         break
      i=i+1
   return(i)
i=0
koltrn=0
for i in range(kolhours):
   klh=kolhours-i
   if prognoz(klh) < kolhours:
      coltrn()
   j=0
   for j in range(kolst):
      pipl[j]=pipl[j]+apipl[j]
   pass
print(koltrn)

