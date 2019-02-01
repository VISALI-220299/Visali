v=input()
print (v)
if(v=='A' or v=='a' or v=='E' or v =='e' or v=='I' or v=='i' or v=='O' or v=='o' or v=='U' or v=='u'):
	print("Vowel")
elif((v>='a' and v<='z') or (v>='A' and v<='Z')):
    print("Consonant")
else:
	print("invalid")
