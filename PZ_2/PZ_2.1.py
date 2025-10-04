V_still_woter = float(input("Введите скорость лодки в стоячей воде V(км/ч):"))
U_flow_river = float(input("Введите скорость течения реки U(км/ч):"))
T_lake = float(input("Введите время движения лодки поозеру T(ч):"))
T_crosscurrent = float(input("Введите время движения лодки против течения реки T(ч):"))

if U_flow_river >= V_still_woter:
    print("Ошибка, скорость течения U должна быть меньше скорости лодки V.")
    exit()

V_crosscurrent = V_still_woter - U_flow_river
S_lake = V_still_woter * T_lake
S_river = V_crosscurrent * T_crosscurrent
S_total = S_river + S_lake

print(f"Путь, пройденный лодкой по озеру: {S_lake}км")
print(f"Путь, пройденный лодкой по реке против течения:{S_river}км")
print(f"Общий путь, пройденный лодкой: {S_total}км")
