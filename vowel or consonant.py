a=input( )
if (a>="a" and a<="z") or (a>="A" and a<="Z"):
  list=["a","e","i","o","u","A","E","I","O","U"]
  
  if a in list:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
