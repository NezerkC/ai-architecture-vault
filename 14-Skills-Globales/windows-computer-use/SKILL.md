---
name: windows-computer-use
description: Enables human-like interaction with Windows OS. Inspect Task Manager processes, discover active windows, analyze UI Automation accessibility trees, capture screenshots with grid overlays, and control mouse and keyboard with human-like precision.
---

# Windows Human-Like Computer Use Guide

Use this skill whenever you need to interact with the Windows desktop, analyze running processes, inspect open application windows, find UI buttons/inputs, or perform mouse and keyboard actions like a human operator.

## Architecture & Execution Engine

All helper scripts reside in:
`C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\`

The dedicated Python runtime containing all required Windows automation packages (`pywin32`, `pywinauto`, `uiautomation`, `pyautogui`, `pillow`, `psutil`) is located at:
`C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe`

Always execute the automation scripts using this dedicated Python executable.

---

## The 5-Step Operator Loop

When executing GUI tasks, always follow this cognitive loop:

```
1. OBSERVE   ───► List running processes and open windows.
2. LOCATE    ───► Inspect the UI structure or capture a screenshot with a coordinate grid.
3. FOCUS     ───► Restore and bring the target window to the foreground.
4. ACT       ───► Click elements, type text, or trigger hotkeys.
5. VERIFY    ───► Confirm the UI updated as expected before taking the next action.
```

---

## 1. Process & Window Discovery (`inspect_windows.py`)

### List All Visible Windows (with HWNDs, geometry, and foreground status)
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\inspect_windows.py"
```

### Filter Windows by Title or Process Name
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\inspect_windows.py" --title "Visual Studio Code"
```

### Inspect Top Processes (Task Manager View: CPU & Memory)
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\inspect_windows.py" --tasks
```

---

## 2. Structural UI Inspection (`inspect_ui.py`)

Always prefer structural UI inspection before blind coordinate guessing. This reads the Windows UI Automation accessibility tree and returns exact `(X, Y)` click centers for buttons, inputs, tabs, and menus.

### Inspect Interactive Controls for a Window (by Title or HWND)
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\inspect_ui.py" --title "Notepad"
```

### Search for Specific Buttons or Fields
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\inspect_ui.py" --title "Settings" --search "Bluetooth"
```

### Output Clean JSON for Programmatic Parsing
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\inspect_ui.py" --hwnd 123456 --json
```

---

## 3. Visual Observation (`capture_screen.py`)

When an application renders custom canvas/graphics (or when UI Automation is unavailable), take a screenshot.

### Full Desktop Screenshot with Coordinate Grid Overlay
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\capture_screen.py" --grid --step 100 --out "C:\Users\lolpl\.gemini\antigravity\scratch\current_desktop.png"
```

### Crop Screenshot to a Specific Window
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\capture_screen.py" --title "Fan Control" --out "C:\Users\lolpl\.gemini\antigravity\scratch\app_window.png"
```

View the generated image using `view_file` to calibrate exact targets.

---

## 4. Mouse & Keyboard Interaction (`interact.py`)

### Focus Window (brings to top and restores if minimized)
```powershell
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" focus --title "Visual Studio Code"
```

### Click Coordinates
```powershell
# Left Click
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" click --x 510 --y 780

# Right Click or Double Click
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" click --x 300 --y 450 --button right
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" click --x 300 --y 450 --button double
```

### Type Text
```powershell
# Type text and press Enter
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" type --text "Hello world" --enter

# Clear field first (Ctrl+A -> Backspace) and type
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" type --text "New text" --clear
```

### Key Combos & Shortcuts
```powershell
# Open Run dialog
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" hotkey --keys "win+r"

# Switch apps or close window
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" hotkey --keys "alt+tab"
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" hotkey --keys "alt+f4"

# Standard controls: Escape, Enter, Tab
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" hotkey --keys "esc"
```

### Scroll & Drag
```powershell
# Scroll down 5 clicks
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" scroll --clicks -5 --x 500 --y 500

# Drag from (100, 200) to (500, 200)
& "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\.venv\Scripts\python.exe" "C:\Users\lolpl\.gemini\config\skills\windows-computer-use\scripts\interact.py" drag --start-x 100 --start-y 200 --end-x 500 --end-y 200
```

---

## Best Practices & Safety Rules

1. **Hierarchy First, Vision Second**: Try `inspect_ui.py` to get exact element bounding boxes. If elements are not exposed via accessibility (e.g. Games, Electron Canvas), use `capture_screen.py --grid` and visually measure target coordinates.
2. **Always Check Focus Before Typing**: Avoid typing into the wrong active window by explicitly calling `interact.py focus` first.
3. **Verify State Transitions**: After clicking a button that should open a dialog, take a screenshot or re-run `inspect_windows.py` to confirm the action took effect before continuing.
