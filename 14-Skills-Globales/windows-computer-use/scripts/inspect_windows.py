"""Inspect active top-level windows and processes on Windows."""

import argparse
import ctypes
from ctypes import wintypes
import json
import os
import sys

# Ensure scripts folder is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import desktop_utils
import psutil

user32 = ctypes.windll.user32
WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)


def get_process_info(pid: int) -> dict:
    try:
        proc = psutil.Process(pid)
        return {
            "name": proc.name(),
            "cpu_percent": proc.cpu_percent(interval=None),
            "memory_mb": round(proc.memory_info().rss / (1024 * 1024), 1),
            "exe": proc.exe() if hasattr(proc, "exe") else "unknown",
        }
    except Exception:
        return {"name": "unknown", "cpu_percent": 0.0, "memory_mb": 0.0, "exe": "unknown"}


def list_visible_windows():
    desktop_utils.attach_to_default_desktop()
    foreground_hwnd = user32.GetForegroundWindow()
    windows = []

    h_desk = user32.OpenDesktopW("default", 0, False, desktop_utils.DESKTOP_ALL)

    def enum_cb(hwnd, _):
        if not user32.IsWindow(hwnd) or not user32.IsWindowVisible(hwnd):
            return True

        length = user32.GetWindowTextLengthW(hwnd)
        if length == 0:
            return True

        buf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buf, length + 1)
        title = buf.value.strip()
        if not title:
            return True

        if desktop_utils.is_cloaked(hwnd):
            return True

        rect = desktop_utils.get_window_rect(hwnd)
        if rect["width"] <= 10 or rect["height"] <= 10:
            return True

        pid_dw = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid_dw))
        pid = pid_dw.value

        pinfo = get_process_info(pid)

        windows.append(
            {
                "hwnd": hwnd,
                "hex_hwnd": hex(hwnd),
                "title": title,
                "pid": pid,
                "process": pinfo["name"],
                "cpu_percent": pinfo["cpu_percent"],
                "memory_mb": pinfo["memory_mb"],
                "is_foreground": hwnd == foreground_hwnd,
                "rect": rect,
            }
        )
        return True

    proc = WNDENUMPROC(enum_cb)
    if h_desk:
        user32.EnumDesktopWindows(h_desk, proc, 0)
    else:
        user32.EnumWindows(proc, 0)

    return windows


def list_top_processes(limit: int = 15):
    procs = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]):
        try:
            mem = round(p.info["memory_info"].rss / (1024 * 1024), 1) if p.info["memory_info"] else 0.0
            procs.append(
                {
                    "pid": p.info["pid"],
                    "name": p.info["name"],
                    "cpu_percent": p.info["cpu_percent"] or 0.0,
                    "memory_mb": mem,
                }
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    procs.sort(key=lambda x: x["memory_mb"], reverse=True)
    return procs[:limit]


def main():
    parser = argparse.ArgumentParser(description="Inspect active windows and Task Manager processes on Windows.")
    parser.add_argument("--json", action="store_true", help="Output raw JSON.")
    parser.add_argument("--title", type=str, help="Filter windows by title (case-insensitive substring).")
    parser.add_argument("--process", type=str, help="Filter windows by process name (case-insensitive substring).")
    parser.add_argument("--tasks", action="store_true", help="Show top resource-consuming processes (Task Manager view).")
    args = parser.parse_args()

    if args.tasks:
        procs = list_top_processes()
        if args.json:
            print(json.dumps(procs, indent=2, ensure_ascii=False))
            return
        print(f"\nTop {len(procs)} Processes (Task Manager View):\n")
        print(f"{'PID':<8} {'PROCESS':<30} {'MEMORY (MB)':<14} {'CPU %'}")
        print("-" * 60)
        for p in procs:
            print(f"{p['pid']:<8} {p['name']:<30} {p['memory_mb']:<14.1f} {p['cpu_percent']:.1f}%")
        return

    windows = list_visible_windows()

    if args.title:
        windows = [w for w in windows if args.title.lower() in w["title"].lower()]

    if args.process:
        windows = [w for w in windows if args.process.lower() in w["process"].lower()]

    if args.json:
        print(json.dumps(windows, indent=2, ensure_ascii=False))
        return

    print(f"\nFound {len(windows)} visible window(s) on desktop:\n")
    print(
        f"{'HWND':<10} {'PID':<8} {'PROCESS':<22} {'FOREGROUND':<12} {'GEOMETRY (L,T WxH)':<22} {'TITLE'}"
    )
    print("-" * 110)

    for w in windows:
        fg = "[ACTIVE]" if w["is_foreground"] else ""
        r = w["rect"]
        geom = f"({r['left']},{r['top']} {r['width']}x{r['height']})"
        t = w["title"] if len(w["title"]) <= 45 else w["title"][:42] + "..."
        safe_t = t.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode(sys.stdout.encoding or 'utf-8')
        print(f"{w['hwnd']:<10} {w['pid']:<8} {w['process']:<22} {fg:<12} {geom:<22} {safe_t}")


if __name__ == "__main__":
    main()
