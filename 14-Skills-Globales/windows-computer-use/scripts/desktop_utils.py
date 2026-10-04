"""Desktop utilities for Windows automation: DPI awareness, thread desktop attachment, and window focus management."""

import ctypes
from ctypes import wintypes
import os
import sys

# Windows API constants
DESKTOP_ALL = 0x01FF
SW_RESTORE = 9
SW_SHOW = 5
DWMWA_CLOAKED = 14

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
dwmapi = ctypes.WinDLL("dwmapi")

# Enable Per-Monitor DPI Awareness so coordinates match physical screen pixels accurately
try:
    # DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4
    user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
except Exception:
    try:
        user32.SetProcessDPIAware()
    except Exception:
        pass


def attach_to_default_desktop() -> bool:
    """Switch current thread's desktop to 'default' in WinSta0 if not already attached."""
    try:
        h_desk = user32.OpenDesktopW("default", 0, False, DESKTOP_ALL)
        if h_desk:
            return bool(user32.SetThreadDesktop(h_desk))
    except Exception:
        pass
    return False


# Automatically attach when module is imported
attach_to_default_desktop()


def is_cloaked(hwnd: int) -> bool:
    """Check if window is cloaked by Windows DWM (hidden UWP app, virtual desktop, etc.)."""
    cloaked = wintypes.DWORD()
    res = dwmapi.DwmGetWindowAttribute(
        wintypes.HWND(hwnd),
        wintypes.DWORD(DWMWA_CLOAKED),
        ctypes.byref(cloaked),
        ctypes.sizeof(cloaked),
    )
    return res == 0 and cloaked.value != 0


def get_window_rect(hwnd: int):
    """Get accurate window bounds (left, top, right, bottom, width, height)."""
    rect = wintypes.RECT()
    user32.GetWindowRect(wintypes.HWND(hwnd), ctypes.byref(rect))
    left, top, right, bottom = rect.left, rect.top, rect.right, rect.bottom
    return {
        "left": left,
        "top": top,
        "right": right,
        "bottom": bottom,
        "width": right - left,
        "height": bottom - top,
        "center_x": left + (right - left) // 2,
        "center_y": top + (bottom - top) // 2,
    }


def force_focus_window(hwnd: int) -> bool:
    """Robustly bring a window to the foreground and set input focus."""
    attach_to_default_desktop()
    if not user32.IsWindow(wintypes.HWND(hwnd)):
        return False

    # If minimized, restore it
    if user32.IsIconic(wintypes.HWND(hwnd)):
        user32.ShowWindow(wintypes.HWND(hwnd), SW_RESTORE)
    else:
        user32.ShowWindow(wintypes.HWND(hwnd), SW_SHOW)

    # Attach thread input to bypass Windows foreground lock
    current_tid = kernel32.GetCurrentThreadId()
    target_pid = wintypes.DWORD()
    target_tid = user32.GetWindowThreadProcessId(wintypes.HWND(hwnd), ctypes.byref(target_pid))

    attached = False
    if current_tid != target_tid:
        attached = bool(user32.AttachThreadInput(current_tid, target_tid, True))

    user32.BringWindowToTop(wintypes.HWND(hwnd))
    user32.SetForegroundWindow(wintypes.HWND(hwnd))
    user32.SetFocus(wintypes.HWND(hwnd))

    if attached:
        user32.AttachThreadInput(current_tid, target_tid, False)

    return user32.GetForegroundWindow() == hwnd
