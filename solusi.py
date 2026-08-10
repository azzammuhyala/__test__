# azzammuhyala - Bro

width, height = map(int, input().split())
peta = [input()[:width] for _ in range(height)]

kunjungan = set()
total = 0

def cek(x, y):
    kunjungan.add((x, y))

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy

        if (
            0 <= nx < width
            and 0 <= ny < height
            and peta[ny][nx] == '.'
            and (nx, ny) not in kunjungan
        ):
            cek(nx, ny)

for y in range(height):
    for x in range(width):
        if peta[y][x] == '.' and (x, y) not in kunjungan:
            cek(x, y)
            total += 1

print(total)
