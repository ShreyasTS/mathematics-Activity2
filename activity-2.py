#Submitted by
#Shreyas Rao T S - JUPG22MCA17494 
#Activity - 2
#Given the truth values of propostitions p and q, find the truth values of the conjunction, disjunction, exclusive or, conditional statement and bidirectional of these propositions
p = int(input("Enter P: "))
q = int(input("Enter Q: "))

print("------------------")
print("Conjunction: ",p&q) # Performing AND Operation

print("Disjunction : ",p|q) # Performing OR Operation

print("XOR: ",p^q)

if p==1 and q ==0:
        print("Conditional: 0") # Performing conditional Operation
else:
    print("Conditional: 1")

print("Biconditional: ", int(not (p^q))) # Performing Bidirectional Operation
