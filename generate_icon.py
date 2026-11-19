import struct
import zlib

def create_png(width, height, pixels):
    def chunk(name, data):
        c = struct.pack('>I', len(data)) + name + data
        return c + struct.pack('>I', zlib.crc32(c[4:]) & 0xffffffff)
    
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    
    raw = []
    for row in pixels:
        raw.append(0)  # filter type
        for r, g, b in row:
            raw.extend([r, g, b])
    
    compressed = zlib.compress(bytes(raw), 9)
    
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', ihdr)
    png += chunk(b'IDAT', compressed)
    png += chunk(b'IEND', b'')
    return png

W, H = 128, 128

# Background color: dark navy #1a1a2e
BG = (26, 26, 46)
# Accent: bright cyan/teal
ACC = (0, 212, 255)
# White
WH = (255, 255, 255)

pixels = [[BG] * W for _ in range(H)]

cx, cy = W // 2, H // 2

# Draw a rounded square border (card shape)
margin = 12
radius = 16
for y in range(H):
    for x in range(W):
        in_rect = margin <= x <= W - margin and margin <= y <= H - margin
        # rounded corners check
        corners = [
            (margin + radius, margin + radius),
            (W - margin - radius, margin + radius),
            (margin + radius, H - margin - radius),
            (W - margin - radius, H - margin - radius),
        ]
        in_corner = False
        for (cx2, cy2) in corners:
            if abs(x - cx2) > radius and abs(y - cy2) > radius:
                # We're in a corner area
                dx = min(abs(x - (margin + radius)), abs(x - (W - margin - radius)))
                dy = min(abs(y - (margin + radius)), abs(y - (H - margin - radius)))
                if x < margin + radius or x > W - margin - radius:
                    if y < margin + radius or y > H - margin - radius:
                        dx = min(abs(x - (margin + radius)), abs(x - (W - margin - radius)))
                        dy = min(abs(y - (margin + radius)), abs(y - (H - margin - radius)))
                        if dx*dx + dy*dy > radius*radius:
                            in_corner = True
                            break
        if in_rect and not in_corner:
            pixels[y][x] = (40, 40, 72)

# Draw sparkle (4-pointed star) in cyan
# Center of canvas
star_cx, star_cy = cx, cy - 10
arm_len = 22
arm_width = 4

for y in range(H):
    for x in range(W):
        dx = x - star_cx
        dy = y - star_cy
        # Vertical arm
        if abs(dx) <= arm_width and abs(dy) <= arm_len:
            pixels[y][x] = ACC
        # Horizontal arm
        if abs(dy) <= arm_width and abs(dx) <= arm_len:
            pixels[y][x] = ACC
        # Diagonal thin arms
        if abs(dx - dy) <= 2 and abs(dx) <= arm_len // 2:
            pixels[y][x] = (180, 240, 255)
        if abs(dx + dy) <= 2 and abs(dx) <= arm_len // 2:
            pixels[y][x] = (180, 240, 255)

# Draw "AI" text as pixel blocks below sparkle
# Simple pixel font for "AI"
# A
letter_A = [
    "  XXX  ",
    " X   X ",
    " XXXXX ",
    " X   X ",
    " X   X ",
]
# I
letter_I = [
    " XXXXX ",
    "   X   ",
    "   X   ",
    "   X   ",
    " XXXXX ",
]

def draw_letter(letter, start_x, start_y, color):
    for row_i, row in enumerate(letter):
        for col_i, ch in enumerate(row):
            if ch == 'X':
                px = start_x + col_i * 2
                py = start_y + row_i * 2
                for dy2 in range(2):
                    for dx2 in range(2):
                        nx, ny = px + dx2, py + dy2
                        if 0 <= nx < W and 0 <= ny < H:
                            pixels[ny][nx] = color

draw_letter(letter_A, cx - 20, cy + 20, WH)
draw_letter(letter_I, cx + 4, cy + 20, WH)

png_data = create_png(W, H, pixels)
with open('icon.png', 'wb') as f:
    f.write(png_data)
print("icon.png created successfully")
