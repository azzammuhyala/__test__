# azzammuhyala - Bro

width, height = map(int, input().split())
peta = [input()[:width] for _ in range(height)]

# simpan koordinat air yang udah di kunjungi
kunjungan = set()
# total area yang ditemukan
total = 0

def cek(x, y):
    # simpan kunjungan air
    kunjungan.add((x, y))

    #             vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv <- arah
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy

        if (
            # pastikan posisi gak keluar batas peta
            0 <= nx < width
            and 0 <= ny < height
            # pastiin posisi ini itu air
            and peta[ny][nx] == '.'
            # pastiin posisi ini belum dikunjungi
            and (nx, ny) not in kunjungan
        ):
            # cek
            cek(nx, ny)

for y in range(height):
    for x in range(width):
        if peta[y][x] == '.' and (x, y) not in kunjungan:
            cek(x, y)
            total += 1

print(total)
