def generate_table(n):
    table = f"table {n}:\n"
    for i in range(1,11):
        table += f"{n}*{i}={n*i}\n"
        table += "\n"  # add new line

    with open("table.txt","a") as f:
         f.write(table)

with open("table.txt","w") as f:
           #f.write(table)
           pass
for i in range(2,21):
    generate_table(i)