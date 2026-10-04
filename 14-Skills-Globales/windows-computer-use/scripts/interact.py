"""Human-like mouse and keyboard interaction engine for Windows."""

import argparse
import os
import sys
import time

# Ensure scripts folder is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import desktop_utils
import inspect_windows
import pyautogui
import pyperclip

# Configure PyAutoGUI safety and human movement defaults
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.05


def do_focus(hwnd: int = None, title: str = None) -> bool:
    desktop_utils.attach_to_default_desktop()
    if not hwnd and title:
        wins = inspect_windows.list_visible_windows()
        for w in wins:
            if title.lower() in w["title"].lower():
                hwnd = w["hwnd"]
                break

    if not hwnd:
        print(f"Error: Target window not found.", file=sys.stderr)
        return False

    success = desktop_utils.force_focus_window(hwnd)
    print(f"Focus HWND {hwnd}: {'SUCCESS' if success else 'FAILED'}")
    return success


def do_click(x: int, y: int, button: str = "left", duration: float = 0.1):
    desktop_utils.attach_to_default_desktop()
    if duration > 0:
        pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)
    else:
        pyautogui.moveTo(x, y)

    if button == "double":
        pyautogui.doubleClick(x, y)
    elif button == "right":
        pyautogui.rightClick(x, y)
    elif button == "middle":
        pyautogui.middleClick(x, y)
    else:
        pyautogui.click(x, y)
    print(f"Clicked {button} at ({x}, {y})")


def do_move(x: int, y: int, duration: float = 0.1):
    desktop_utils.attach_to_default_desktop()
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)
    print(f"Moved mouse to ({x}, {y})")


def do_drag(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5):
    desktop_utils.attach_to_default_desktop()
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button="left")
    print(f"Dragged from ({start_x}, {start_y}) to ({end_x}, {end_y})")


def do_type(text: str, press_enter: bool = False, clear_first: bool = False, use_paste: bool = True):
    desktop_utils.attach_to_default_desktop()
    if clear_first:
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.05)
        pyautogui.press("backspace")
        time.sleep(0.05)

    if use_paste:
        old_clip = pyperclip.paste()
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.05)
    else:
        pyautogui.write(text, interval=0.03)

    if press_enter:
        pyautogui.press("enter")

    print(f"Typed text ({len(text)} chars, enter={press_enter})")


def do_hotkey(keys_str: str):
    desktop_utils.attach_to_default_desktop()
    # Normalize separators: "ctrl+shift+esc" or "ctrl,shift,esc"
    keys = [k.strip().lower() for k in keys_str.replace("+", " ").replace(",", " ").split()]
    
    # Map common aliases
    key_map = {
        "win": "win",
        "cmd": "win",
        "super": "win",
        "control": "ctrl",
        "escape": "esc",
        "return": "enter",
    }
    normalized_keys = [key_map.get(k, k) for k in keys]

    if len(normalized_keys) == 1:
        pyautogui.press(normalized_keys[0])
    else:
        pyautogui.hotkey(*normalized_keys)
    print(f"Executed hotkey: {'+'.join(normalized_keys)}")


def do_scroll(clicks: int, x: int = None, y: int = None):
    desktop_utils.attach_to_default_desktop()
    if x is not None and y is not None:
        pyautogui.moveTo(x, y)
    pyautogui.scroll(clicks)
    print(f"Scrolled {clicks} clicks at ({x}, {y})")


def main():
    parser = argparse.ArgumentParser(description="Human-like Windows mouse and keyboard control.")
    subparsers = parser.add_subparsers(dest="action", required=True)

    # Focus
    p_focus = subparsers.add_parser("focus", help="Focus window by HWND or title.")
    p_focus.add_argument("--hwnd", type=int, help="Target window HWND.")
    p_focus.add_argument("--title", type=str, help="Target window title substring.")

    # Click
    p_click = subparsers.add_parser("click", help="Click at (x, y) coordinates.")
    p_click.add_argument("--x", type=int, required=True, help="X coordinate.")
    p_click.add_argument("--y", type=int, required=True, help="Y coordinate.")
    p_click.add_argument("--button", choices=["left", "right", "double", "middle"], default="left", help="Mouse button.")
    p_click.add_argument("--duration", type=float, default=0.1, help="Mouse movement duration in seconds.")

    # Move
    p_move = subparsers.add_parser("move", help="Move mouse cursor to (x, y).")
    p_move.add_argument("--x", type=int, required=True, help="X coordinate.")
    p_move.add_argument("--y", type=int, required=True, help="Y coordinate.")
    p_move.add_argument("--duration", type=float, default=0.1, help="Movement duration.")

    # Drag
    p_drag = subparsers.add_parser("drag", help="Click and drag.")
    p_drag.add_argument("--start-x", type=int, required=True)
    p_drag.add_argument("--start-y", type=int, required=True)
    p_drag.add_argument("--end-x", type=int, required=True)
    p_drag.add_argument("--end-y", type=int, required=True)
    p_drag.add_argument("--duration", type=float, default=0.5)

    # Type
    p_type = subparsers.add_parser("type", help="Type text string into active window.")
    p_type.add_argument("--text", type=str, required=True, help="Text to type.")
    p_type.add_argument("--enter", action="store_true", help="Press Enter after typing.")
    p_type.add_argument("--clear", action="store_true", help="Clear field (Ctrl+A -> Backspace) before typing.")
    p_type.add_argument("--no-paste", action="store_true", help="Type character by character instead of clipboard paste.")

    # Hotkey
    p_hotkey = subparsers.add_parser("hotkey", help="Press hotkey combination (e.g. 'ctrl+c', 'win+r', 'alt+tab').")
    p_hotkey.add_argument("--keys", type=str, required=True, help="Keys combination separated by '+' or spaces.")

    # Scroll
    p_scroll = subparsers.add_parser("scroll", help="Scroll mouse wheel.")
    p_scroll.add_argument("--clicks", type=int, required=True, help="Number of clicks (positive = up, negative = down).")
    p_scroll.add_argument("--x", type=int, help="Optional X coordinate.")
    p_scroll.add_argument("--y", type=int, help="Optional Y coordinate.")

    args = parser.parse_args()

    if args.action == "focus":
        do_focus(hwnd=args.hwnd, title=args.title)
    elif args.action == "click":
        do_click(args.x, args.y, button=args.button, duration=args.duration)
    elif args.action == "move":
        do_move(args.x, args.y, duration=args.duration)
    elif args.action == "drag":
        do_drag(args.start_x, args.start_y, args.end_x, args.end_y, duration=args.duration)
    elif args.action == "type":
        do_type(args.text, press_enter=args.enter, clear_first=args.clear, use_paste=not args.no_paste)
    elif args.action == "hotkey":
        do_hotkey(args.keys)
    elif args.action == "scroll":
        do_scroll(args.clicks, x=args.x, y=args.y)


if __name__ == "__main__":
    main()
