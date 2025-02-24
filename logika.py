print("TABEL KEBENARAN KONJUNGSI, DISJUNGSI DAN -P OR Q")
print("________________________________________________")

print("P\t|Q\t|Q AND P\t|P OR |-P OR Q")
print("________________________________________________")

for P in [True, False]:
    for Q in [True, False]:
        Konjungsi = P and Q
        Disjungsi = P or Q
        Negasi = not -P or Q
        print(f"{P}\t{Q}\t{Konjungsi}\t{Disjungsi},\t{Negasi}")

print("__________________________________________________")
