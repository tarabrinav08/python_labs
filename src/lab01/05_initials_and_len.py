fio = input ("ФИО: ")
parts = fio.split()

initials = parts[0][0] + parts[1][0] + parts[2][0]
clean = " ".join(parts)

print(f"Инициалы {initials.upper()}.")
print(f"Длина (символов): {len(clean)}")

