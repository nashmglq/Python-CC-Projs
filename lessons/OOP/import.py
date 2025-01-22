from object import Dog

hepe = Dog("Aspin", "Mabaho", "6'9")
choco = Dog("Pomy", "Sakto lang ang amoy", "6'8")


#Imagine it like we are saying that hepe (self) is using this attribute  = (self.breed = breed(we pass argue))
# So hepe is self and it uses that attribute
print(hepe.breed)
print(hepe.smell)
print(hepe.height)


print(choco.breed)
print(choco.smell)
print(choco.height)


hepe.bark()
choco.bark()
