from id_validator_module import match,matching_parts


print(f"Enter University ID's (If you're finished, enter done) :")
ID = set()
num = 1
while True:
    answer = input(f"{num} ID is :").lower()
    num += 1 
    if answer == "done" :
          break
    ID.add(answer)
for m in ID :
    x = match(m)
    y = matching_parts(m)
    print(f"""
      Input : {m}
      Matches pattern? {x}
      University ID number: {y}
""")

