
def move(action, x, y):
    if action == 'R':
        return x + 1, y
    elif action == 'L':
        return x - 1, y
    elif action == 'U':
        return x, y - 1
    elif action == 'D':
        return x, y + 1

def is_bad_zone(check_x, check_y):
    for x, y, w, h in bad_zones:
        if (x <= check_x < x + w and y <= check_y < y + h):   # распаковка кортежа
            return 1
    return 0

def beback(start_x, start_y, target_x, target_y, trip):
    x, y = start_x, start_y
    
    while x != target_x:
        if target_x > x:
            x += 1
        else:
            x -= 1
        trip.append((x, y))
    
    while y != target_y:
        if target_y > y:
            y += 1
        else:
            y -= 1
        trip.append((x, y))
    
    return x, y

def count_real_points(history):
    count = 0
    for pos in history:
        if pos is not None:
            count += 1
    return count

def get_pos_to_return(history, steps_back):
    pos_to_return = []
    temp_history = history.copy()
    
    while len(pos_to_return) < steps_back and temp_history:
        pos = temp_history.pop()
        if pos is not None:
            pos_to_return.append(pos)
    
    return pos_to_return

x, y = 1, 1
trip = []
command_history = []
bad_zones = [] 

print("введите запретные зоны в формате X,Y,W,H (пустая строка для завершения):")

while 1:
    zone_input = input()
    if zone_input == "":
        break
    
    parts = zone_input.split(',')
    if len(parts) != 4:
        print("неверный формат зоны, используйте X,Y,W,H")
        exit()

    try:
        zone_x, zone_y, w, h = map(int, parts)
    except ValueError:                                       # блок обработки исключений
        print("все значения должны быть целыми числами")
        exit()
    
    if zone_x <= 0 or zone_y <= 0 or w <= 0 or h <= 0:
        print("X, Y, W, H должны быть положительными числами")
        exit()
    
    bad_zones.append((zone_x, zone_y, w, h)) 

if is_bad_zone(x, y):
    print("робот начинает движение в запретной зоне!")
    exit()
    
print("введите команды для перемещения (например, R,4), или пустую строку для выхода:")

raw_commands = []

while 1:
    c = input()
    
    if c == "":
        break

    parts = c.split(',')

    if c[0] not in ['R', 'L', 'U', 'D', 'B']:
        print("неверная команда")
        exit()
    
    if ',' not in c and c[0] != 'B':
        print("неверный формат команды")
        exit()
    
    raw_commands.append(c)

for c in raw_commands:

    parts = c.split(',')

    if c[0] == "B":
        steps_back = 1
        
        if ',' in c:

            if len(parts) != 2:
                print("неверный формат команды")
                exit()
        
            steps_str = parts[1]
        
            if not steps_str.isdigit() or int(steps_str) <= 0:
                print("количество возвратов должно быть положительным числом")
                exit()
            
            steps_back = int(steps_str)
        
        real_points = count_real_points(command_history)
        
        if real_points < steps_back:
            print("нельзя вернуться на такое количество шагов назад")
            exit()     
        
        pos_to_return = get_pos_to_return(command_history, steps_back)

        for target_x, target_y in pos_to_return:
            x, y = beback(x, y, target_x, target_y, trip)
            
        command_history.append(None)
        continue
    
    command_history.append((x, y))
    
    action, steps_str = parts[0], parts[1]
    
    if not steps_str.isdigit() or int(steps_str) <= 0:
        print("количество шагов должно быть положительным числом")
        exit()

    steps = int(steps_str)

    check_x, check_y = x, y
    path_positions = []

    for i in range(steps):
        new_x, new_y = move(action, check_x, check_y)

        if new_x <= 0 or new_x > 100 or new_y <= 0 or new_y > 100:
            print("выход за границы поля")
            exit()
    
        if is_bad_zone(new_x, new_y):
            print("ошибка: путь проходит через запретную зону")
            exit()
    
        path_positions.append((new_x, new_y))
        check_x, check_y = new_x, new_y

    for pos in path_positions:
        x, y = pos
        trip.append(pos)

for x, y in trip:
    print(f"{x},{y}") # префикс строки