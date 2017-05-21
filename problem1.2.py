

plates_am = int(input('Количество тарелок: '))
det_am = float(input('Количество моющего средства:'))

det_per_plate = 0.5

while plates_am and det_am:
    plates_am -= 1
    det_am -= det_per_plate
    print('Осталось моющего средства:', det_am)
