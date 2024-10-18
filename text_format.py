emoji_clock_font = {
    '0': ["⬛⬛⬛", "⬛⬜⬛", "⬛⬜⬛", "⬛⬜⬛", "⬛⬛⬛"],
    '1': ["⬜⬜⬛", "⬜⬜⬛", "⬜⬜⬛", "⬜⬜⬛", "⬜⬜⬛"],
    '2': ["⬛⬛⬛", "⬜⬜⬛", "⬛⬛⬛", "⬛⬜⬜", "⬛⬛⬛"],
    '3': ["⬛⬛⬛", "⬜⬜⬛", "⬛⬛⬛", "⬜⬜⬛", "⬛⬛⬛"],
    '4': ["⬛⬜⬛", "⬛⬜⬛", "⬛⬛⬛", "⬜⬜⬛", "⬜⬜⬜"],
    '5': ["⬛⬛⬛", "⬛⬜⬜", "⬛⬛⬛", "⬜⬜⬛", "⬛⬛⬛"],
    '6': ["⬛⬛⬛", "⬛⬜⬜", "⬛⬛⬛", "⬛⬜⬛", "⬛⬛⬛"],
    '7': ["⬛⬛⬛", "⬜⬜⬛", "⬜⬜⬛", "⬜⬜⬛", "⬜⬜⬛"],
    '8': ["⬛⬛⬛", "⬛⬜⬛", "⬛⬛⬛", "⬛⬜⬛", "⬛⬛⬛"],
    '9': ["⬛⬛⬛", "⬛⬜⬛", "⬛⬛⬛", "⬜⬜⬛", "⬛⬛⬛"]
}

def format_days_left_in_emoji_clock(days_left):
    days_string = f"{days_left:03}"
    lines = ["⬜", "⬜", "⬜", "⬜", "⬜"]

    for char in days_string:
        if char in emoji_clock_font:
            for i in range(5):
                lines[i] += emoji_clock_font[char][i] + "⬜"

    return "\n".join(lines)