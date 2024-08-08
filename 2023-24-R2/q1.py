mass = int(input())
speed = int(input())
height = int(input())

ke = 0.5 * mass * speed**2
gpe = mass * 10 * height

print(f"{ke+gpe:.1f}")

