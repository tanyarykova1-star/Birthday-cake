import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Основные цвета
main_dark_blue = '#0b2545'
main_black = '#000000'
main_beige = '#f5f1e9'
accent_yellow = '#ffd700'

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Параметры торта
cake_left = 5 - 1.0
cake_bottom = 4 - 1.2
cake_width = 2
cake_height = 2

# Параметры свечей
candle_positions = np.linspace(cake_left + 0.3, cake_left + cake_width - 0.3, 5)
candle_height = cake_height * 0.4  # свечи покороче
flame_radius = 0.08

# Параметры шаров
balloon_radius = 0.7  # шары побольше
balloon_centers_left = [(1.5, 6), (1, 5), (2, 4)]
balloon_centers_right = [(8.5, 6), (8, 5), (9, 4)]
balloon_colors_left = [main_dark_blue, accent_yellow, main_beige]
balloon_colors_right = [main_dark_blue, main_black, main_beige]

# Текст
text_top = 'С днём рождения, папочка!'
message = (
    "Папа, с праздником!  \n"
    "Ты всегда был примером силы и мудрости.  \n"
    "Желаю радости, тепла и уютных дней,  \n"
    "Пусть будут достигнуты все твои цели,  \n"
    "И счастье пусть всегда будет рядом!"
)
message_y = cake_bottom - 0.8  # текст чуть ниже торта

def animate(i):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Элементы рисуем поэтапно

    # 0 - квадрат торта
    if i >= 0:
        rect = plt.Rectangle((cake_left, cake_bottom), cake_width, cake_height, color=main_beige, ec=main_black, lw=3)
        ax.add_patch(rect)

    # 1-5 - свечи и пламя по очереди
    for idx, x in enumerate(candle_positions):
        if i >= 1 + idx:
            ax.plot([x, x], [cake_bottom + cake_height * 0.6, cake_bottom + cake_height * 0.6 + candle_height], color=main_dark_blue, lw=4)
            flame = plt.Circle((x, cake_bottom + cake_height * 0.6 + candle_height + flame_radius), flame_radius, color=accent_yellow)
            ax.add_patch(flame)

    # 6-11 - шары слева по очереди
    for idx, (center, color) in enumerate(zip(balloon_centers_left, balloon_colors_left)):
        if i >= 6 + idx:
            balloon = plt.Circle(center, balloon_radius, color=color, ec=main_black, lw=2)
            ax.add_patch(balloon)
            ax.plot([center[0], center[0]], [center[1] - balloon_radius, center[1] - balloon_radius - 1], color=main_black, lw=1)

    # 12-17 - шары справа по очереди
    for idx, (center, color) in enumerate(zip(balloon_centers_right, balloon_colors_right)):
        if i >= 12 + idx:
            balloon = plt.Circle(center, balloon_radius, color=color, ec=main_black, lw=2)
            ax.add_patch(balloon)
            ax.plot([center[0], center[0]], [center[1] - balloon_radius, center[1] - balloon_radius - 1], color=main_black, lw=1)

    # 18 - верхняя надпись
    if i >= 18:
        ax.text(5, 7.2, text_top, fontsize=20, ha='center', fontweight='bold', color=main_dark_blue)

    # 19 - нижняя надпись
    if i >= 19:
        ax.text(5, message_y, message, fontsize=12, ha='center', va='top', color=main_dark_blue, wrap=True)

    return []

# Интервал увеличен до 800 мс для плавного медленного рисования
anim = animation.FuncAnimation(fig, animate, frames=20, interval=800, repeat=False)
plt.show()

