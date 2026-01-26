#Lab03-B

print("Q1")

ls=["Phil", "Oz", "Seuss", "Dre"]

doctors = []
for doc_name in ls:
    doctors.append("Dr " + doc_name)

print(doctors)


print("Q2")

ls_1=[111, 32, -9, -45, -17, 9, 85, -10]
positives = []
for n in ls_1:
    if n >= 0:
        positives.append(n)

print(positives)



print("Q3")

dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}

values_over_1000 = []
for v in dict.values():
    if v > 1000:
        values_over_1000.append(v - 500)

print(values_over_1000)

