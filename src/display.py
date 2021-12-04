#!/usr/bin/env python3

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import ST7789 as ST7789

# Display HAT Mini
display = ST7789.ST7789(
    height=240,
    width=320,
    rotation=180,
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    spi_speed_hz=60 * 1000 * 1000,
    offset_left=0,
    offset_top=0,
)

WIDTH = display.width
HEIGHT = display.height

BG_COLOR = "black"
FG_COLOR = "white"

OK_COLOR = "green"
COOL_COLOR = "blue"
WARNING_COLOR = "orange"
DANGER_COLOR = "red"

PADDING = 10

LABEL_FONT_SIZE = 20
VALUE_FONT_SIZE = 35

SCRIPT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
FONT_PATH = str(SCRIPT_DIR / "fonts/Michroma/Michroma-Regular.ttf")

LABEL_FONT = ImageFont.truetype(FONT_PATH, LABEL_FONT_SIZE)
VALUE_FONT = ImageFont.truetype(FONT_PATH, VALUE_FONT_SIZE)


def monitor_image(
    label_1: str,
    value_1: str,
    value_color_1: str,
    label_2: str,
    value_2: str,
    value_color_2: str,
    label_3: str,
    value_3: str,
    value_color_3: str,
    label_4: str,
    value_4: str,
    value_color_4: str,
) -> Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)

    draw = ImageDraw.Draw(image)

    # Cross in the centre
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    draw.line((center_x, PADDING, center_x, HEIGHT - PADDING), fill=FG_COLOR, width=2)
    draw.line((PADDING, center_y, WIDTH - PADDING, center_y), fill=FG_COLOR, width=2)

    # Draw text
    label_1_anchor = (PADDING, PADDING)
    value_1_anchor = (PADDING, (center_y // 2) - (VALUE_FONT_SIZE // 2))
    draw.text(label_1_anchor, label_1, fill=FG_COLOR, font=LABEL_FONT)
    draw.text(value_1_anchor, value_1, fill=value_color_1, font=VALUE_FONT)

    label_2_anchor = (center_x + PADDING, PADDING)
    value_2_anchor = (center_x + PADDING, (center_y // 2) - (VALUE_FONT_SIZE // 2))
    draw.text(label_2_anchor, label_2, fill=FG_COLOR, font=LABEL_FONT)
    draw.text(value_2_anchor, value_2, fill=value_color_2, font=VALUE_FONT)

    label_3_anchor = (PADDING, center_y + PADDING)
    value_3_anchor = (PADDING, center_y + (center_y // 2) - (VALUE_FONT_SIZE // 2))
    draw.text(label_3_anchor, label_3, fill=FG_COLOR, font=LABEL_FONT)
    draw.text(value_3_anchor, value_3, fill=value_color_3, font=VALUE_FONT)

    label_4_anchor = (center_x + PADDING, center_y + PADDING)
    value_4_anchor = (
        center_x + PADDING,
        center_y + (center_y // 2) - (VALUE_FONT_SIZE // 2),
    )
    draw.text(label_4_anchor, label_4, fill=FG_COLOR, font=LABEL_FONT)
    draw.text(value_4_anchor, value_4, fill=value_color_4, font=VALUE_FONT)

    return image


# Initialize display
display.begin()

image = monitor_image(
    "Oil",
    "50 °C",
    OK_COLOR,
    "Coolant",
    "30 °C",
    COOL_COLOR,
    "Exhaust",
    "45 °C",
    WARNING_COLOR,
    "Turbo",
    "120 °C",
    DANGER_COLOR,
)
display.display(image)
