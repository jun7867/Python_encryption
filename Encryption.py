import random
import sys
#Encryption funtion
def Encryption(filename,password):
   #filename.enc !!
  
  outfname=filename.replace('.txt','.enc')
  keyname=filename.replace('.txt','.key')
  try:
    f=open(filename,'r')
  except IOError as err:
    print("I/O error: {0}".format(err))
    sys.exit()

  full=f.read()
  set_full=list(set(full))
  set_full.sort()

  base_s= list(range(len(set_full)))
  random.shuffle(base_s)
  z=dict(zip(set_full,base_s))

  print(z)
  try:
    outf=open(outfname,'w')
  except IOError as err:
    print("I/O error: {0}".format(err))
    sys.exit()
  #write .enc file
  for q in full:
    outf.write(str(z[q])+' ')
  print(".enc file complete!")

  #filename.key !!
  pass_uni=password.encode()
  sum=0
  for i in pass_uni:
    sum=sum+i #sum password unicode
  new_key=[]
  new_value=[]
  #new_key is key_uni+pass_uni
  for key in z.keys():
    key_uni=key.encode()
    for i in key_uni:
      new_key.append(i+sum) #101?
  
  for value in z.values():
    new_value.append(value+sum)
  new_z=dict(zip(new_key,new_value))

  try:
    keyfile=open(keyname,'w')
  except IOError as err:
    print("I/O error: {0}".format(err))
    sys.exit()
    
  for i in range(len(new_value)):
    keyfile.write(str(new_key[i])+" "+str(new_value[i])+" ")

  f.close()
  outf.close()
  keyfile.close()

#Decryption function
def Decryption(filename,password):
  try:
    keyname=filename.replace('.enc','.key')
    decname=filename.replace('.enc','.dec')
    keyfile=open(keyname,'r')

    pass_uni=password.encode()
    sum=0
    for i in pass_uni:
      sum=sum+i #sum password unicode
    key_full=keyfile.read()
    key_split=key_full.split()
    new_key=[]
  
    for i in key_split:
      k=int(i)-sum
      new_key.append(k)
   
    count=0
    new_key2=[]
    new_value2=[]
    for i in new_key:
      if(count%2==0):
        chri=chr(i)
        new_key2.append(chri)
      else:
        new_value2.append(i)
      count=count+1
  
    #new_key2 is decrypt key
    z=dict(zip(new_value2,new_key2))
    print(z)

    encfile=open(filename,'r')
    full_enc=encfile.read()
    full_enc_split=full_enc.split()
    g=[]
    for i in full_enc_split:
      for k in z.keys():
        if int(i)==int(k):
          dec=z.get(k)
          g.append(dec)
    #g is dec intent
    decfile=open(decname,'w')
    for i in range(len(g)):
      decfile.write(g[i])

    keyfile.close()
    encfile.close()
    decfile.close()
  except ValueError as err:
    print("it is not .enc file or password range error".format(err))
    sys.exit()
  except KeyError as err:
    print("key error: {0}".format(err))
    sys.exit()
  except IOError as err:
    print("I/O error: {0}".format(err)) 

#Main function!!!~!!!!
#1 explain program

print("Hello~ This program is Encryption/Descryption ")

#2 Ask the user choose
while(1):
  choose=input("Select number 1 or 2(1-Encryption, 2-Decryption): ")
  if choose.isdecimal():
    if int(choose)==1 or int(choose) ==2:
      break
  else:
    print("Wrong input! only 1 or 2")

#3 Ask the user to enter filename
fp=input("Input file name: ")
try:
  inf = open(fp)
    #4 Ask password
  while(1):
    password=input("input password! : ")
    if not password or password.isspace():
      print("Wrong input")
    else:
      if ' ' in password:
        print("Not space!")
      elif len(password)!=4:
        print("Input only 4 character: ")
      else:
        break
  if int(choose) ==1 :
    Encryption(fp,password)
  else:
    Decryption(fp,password)

  inf.close()
  

except IOError as err:
    print("I/O error: {0}".format(err))
  




  
