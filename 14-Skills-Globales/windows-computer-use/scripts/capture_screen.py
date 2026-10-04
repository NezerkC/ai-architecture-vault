"""Capture desktop or window screenshots with optional coordinate grid overlay."""

import argparse
import os
import sys

# Ensure scripts folder is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import desktop_utils
import inspect_windows
from PIL import Image, ImageDraw, ImageFont, ImageGrab


def draw_coordinate_grid(image: Image.Image, step: int = 100) -> Image.Image:
    """Overlay a light coordinate grid with labels on the screenshot."""
    img = image.copy().convert("RGBA")
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    w, h = img.size

    # Draw vertical lines
    for x in range(0, w, step):
        draw.line([(x, 0), (x, h)], fill=(255, 0, 0, 90), width=1)
        draw.text((x + 2, 2), str(x), fill=(255, 0, 0, 220))

    # Draw horizontal lines
    for y in range(0, h, step):
        draw.line([(0, y), (w, y)], fill=(255, 0, 0, 90), width=1)
        draw.text((2, y + 2), str(y), fill=(255, 0, 0, 220))

    return Image.alpha_composite(img, overlay).convert("RGB")


def capture_screenshot(
    hwnd: int = None,
    title: str = None,
    output_path: str = None,
    add_grid: bool = False,
    grid_step: int = 100,
) -> str:
    desktop_utils.attach_to_default_desktop()

    crop_box = None
    if title or hwnd:
        target_hwnd = inspect_ui.find_target_hwnd(title_query=title, hwnd=hwnd) if "inspect_ui" in sys.modules else hwnd
        if not target_hwnd and title:
            wins = inspect_windows.list_visible_windows()
            for w in wins:
                if title.lower() in w["title"].lower():
                    target_hwnd = w["hwnd"]
                    break

        if target_hwnd:
            rect = desktop_utils.get_window_rect(target_hwnd)
            # Ensure valid box
            if rect["width"] > 0 and rect["height"] > 0:
                crop_box = (
                    rect["left"],
                    rect["top"],
                    rect["right"],
                    rect["bottom"],
                )

    screenshot = ImageGrab.grab(bbox=crop_box, all_screens=True)

    if add_grid:
        screenshot = draw_coordinate_grid(screenshot, step=grid_step)

    if not output_path:
        default_dir = os.path.join(os.environ.get("USERPROFILE", "."), ".gemini", "antigravity", "scratch")
        os.makedirs(default_dir, exist_ok=True)
        output_path = os.path.join(default_dir, "desktop_screenshot.png")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    screenshot.save(output_path, "PNG")
    return os.path.abspath(output_path)


def main():
    parser = argparse.ArgumentParser(description="Capture desktop or window screenshots.")
    parser.add_argument("--hwnd", type=int, help="Capture specific window HWND.")
    parser.add_argument("--title", type=str, help="Capture specific window by title substring.")
    parser.add_argument("--out", type=str, help="Output file path (PNG).")
    parser.add_argument("--grid", action="store_true", help="Overlay coordinate grid on image.")
    parser.add_argument("--step", type=int, default=100, help="Grid step in pixels (default: 100).")
    args = parser.parse_args()

    out_file = capture_screenshot(
        hwnd=args.hwnd,
        title=args.title,
        output_path=args.out,
        add_grid=args.grid,
        grid_step=args.step,
    )
    print(f"Screenshot saved to: {out_file}")


if __name__ == "__main__":
    main()
