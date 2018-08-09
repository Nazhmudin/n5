file = open('Traindata1.txt', 'r')
st = file.readline()
st1 = st.split()
print(st1)
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
print(pipl)
print(apipl)
print(maxpipl)

def coltrn():
   global koltrn
   trn=0
   for k in range(kolst):
      if (trn+pipl[k]) <= vmest:
         trn=trn+pipl[k]
         pipl[k]=0
      else:
         pipl[k]=trn+pipl[k]-vmest
         break
      pass
   koltrn=koltrn+1
def prognoz(klh):
   sos='not'
   dpl=pipl
   i=0
   for i in range(0,klh):
      for j in range(kolst):
         dpl[j]=dpl[j]+apipl[j]
         if (dpl[j] < maxpipl[j]):
            pass
         else:
            sos='yes'
            break
         pass
      if sos=='yes':
         break
      pass
   return(i)

koltrn=0
for i in range(kolhours):
   print('час ',i,'   ',pipl)
   klh=kolhours-i
   print('klh=',klh,'prognoz=',prognoz(klh),sum(pipl))
   if prognoz(klh) < kolhours and 5 > vmest:
      print('час ',i,'   ',pipl)
      coltrn()
      print('час ',i,'   ',pipl)
   j=0
   print('час ',i,'   ',pipl)
   for j in range(kolst):
      pipl[j]=pipl[j]+apipl[j]
   pass
   print('час ',i,'   ',pipl)
print('количество поездов = ',koltrn)
print('github')

