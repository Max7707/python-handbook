first_name = 'Петя'
second_name = 'Вася'
third_name = 'Толя'
first_speed = int(input())
second_speed = int(input())
third_speed = int(input())

if first_speed < second_speed:
    first_name, second_name = second_name, first_name
    first_speed, second_speed = second_speed, first_speed
    
if first_speed < third_speed:
    first_name, third_name = third_name, first_name
    first_speed, third_speed = third_speed, first_speed
if second_speed < third_speed:
    second_name, third_name = third_name, second_name
    second_speed, third_speed = third_speed, second_speed

print(f"{first_name: ^24}")
print(f"{second_name: ^8}{" ": ^16}")
print(f"{" ": ^16}{third_name: ^8}")
print(f"{"II": ^8}{"I": ^8}{"III": ^8}")