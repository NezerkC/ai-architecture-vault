"""Inspect UI Automation accessibility tree for a specific window on Windows."""

import argparse
import json
import os
import sys

# Ensure scripts folder is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import desktop_utils
import inspect_windows
import uiautomation as auto


INTERACTIVE_CONTROL_TYPES = {
    auto.ControlType.ButtonControl: "Button",
    auto.ControlType.EditControl: "Edit",
    auto.ControlType.ComboBoxControl: "ComboBox",
    auto.ControlType.CheckBoxControl: "CheckBox",
    auto.ControlType.RadioButtonControl: "RadioButton",
    auto.ControlType.TabItemControl: "TabItem",
    auto.ControlType.MenuItemControl: "MenuItem",
    auto.ControlType.ListItemControl: "ListItem",
    auto.ControlType.TreeItemControl: "TreeItem",
    auto.ControlType.HyperlinkControl: "Hyperlink",
    auto.ControlType.DocumentControl: "Document",
    auto.ControlType.TextControl: "Text",
    auto.ControlType.MenuBarControl: "MenuBar",
    auto.ControlType.ToolBarControl: "ToolBar",
    auto.ControlType.CustomControl: "Custom",
    auto.ControlType.HeaderItemControl: "HeaderItem",
    auto.ControlType.SplitButtonControl: "SplitButton",
}


def dump_ui_elements(target_control, max_depth: int = 5, interactive_only: bool = True):
    elements = []

    def walk(ctrl, current_depth: int):
        if current_depth > max_depth:
            return

        try:
            ctrl_type_id = ctrl.ControlType
            type_name = INTERACTIVE_CONTROL_TYPES.get(ctrl_type_id, ctrl.ControlTypeName)
            name = ctrl.Name.strip() if ctrl.Name else ""
            auto_id = ctrl.AutomationId.strip() if ctrl.AutomationId else ""
            class_name = ctrl.ClassName.strip() if ctrl.ClassName else ""
            rect = ctrl.BoundingRectangle

            # Check if control has valid bounds
            if rect and rect.width() > 0 and rect.height() > 0:
                is_interactive = ctrl_type_id in INTERACTIVE_CONTROL_TYPES
                
                if not interactive_only or is_interactive or name or auto_id:
                    elements.append(
                        {
                            "type": type_name,
                            "name": name,
                            "automation_id": auto_id,
                            "class_name": class_name,
                            "depth": current_depth,
                            "rect": {
                                "left": rect.left,
                                "top": rect.top,
                                "right": rect.right,
                                "bottom": rect.bottom,
                                "width": rect.width(),
                                "height": rect.height(),
                            },
                            "center": {
                                "x": rect.left + rect.width() // 2,
                                "y": rect.top + rect.height() // 2,
                            },
                        }
                    )
        except Exception:
            pass

        try:
            for child in ctrl.GetChildren():
                walk(child, current_depth + 1)
        except Exception:
            pass

    walk(target_control, 0)
    return elements


def find_target_hwnd(title_query: str = None, hwnd: int = None) -> int:
    if hwnd:
        return hwnd
    windows = inspect_windows.list_visible_windows()
    if not title_query:
        # Return foreground window
        fg = desktop_utils.user32.GetForegroundWindow()
        return fg if fg else (windows[0]["hwnd"] if windows else 0)

    for w in windows:
        if title_query.lower() in w["title"].lower():
            return w["hwnd"]
    return 0


def main():
    parser = argparse.ArgumentParser(description="Inspect UI Automation controls inside a window.")
    parser.add_argument("--hwnd", type=int, help="Target window HWND.")
    parser.add_argument("--title", type=str, help="Target window title substring.")
    parser.add_argument("--depth", type=int, default=5, help="Maximum tree traversal depth (default: 5).")
    parser.add_argument("--type", type=str, help="Filter by control type (e.g. Button, Edit, TabItem).")
    parser.add_argument("--search", type=str, help="Filter by control name/label (case-insensitive).")
    parser.add_argument("--all", action="store_true", help="Include all non-interactive elements too.")
    parser.add_argument("--json", action="store_true", help="Output raw JSON.")
    args = parser.parse_args()

    desktop_utils.attach_to_default_desktop()

    target_hwnd = find_target_hwnd(title_query=args.title, hwnd=args.hwnd)
    if not target_hwnd:
        print(f"Error: Window not found matching search criteria.", file=sys.stderr)
        sys.exit(1)

    target = auto.ControlFromHandle(target_hwnd)
    if not target or not target.Exists(0):
        print(f"Error: Could not obtain UI Automation handle for HWND {target_hwnd}.", file=sys.stderr)
        sys.exit(1)

    print(f"Inspecting: [{target.ControlTypeName}] '{target.Name}' (HWND: {target_hwnd})", file=sys.stderr)

    elements = dump_ui_elements(target, max_depth=args.depth, interactive_only=not args.all)

    if args.type:
        elements = [e for e in elements if args.type.lower() in e["type"].lower()]

    if args.search:
        elements = [e for e in elements if args.search.lower() in e["name"].lower() or args.search.lower() in e["automation_id"].lower()]

    if args.json:
        print(json.dumps(elements, indent=2, ensure_ascii=False))
        return

    print(f"\nFound {len(elements)} element(s):\n")
    print(f"{'TYPE':<14} {'CLICK (X,Y)':<14} {'BOUNDS (L,T WxH)':<22} {'NAME / AUTOMATION ID'}")
    print("-" * 90)

    for el in elements:
        c = el["center"]
        r = el["rect"]
        click_str = f"({c['x']}, {c['y']})"
        bounds_str = f"({r['left']},{r['top']} {r['width']}x{r['height']})"
        label = el["name"] if el["name"] else (f"id:{el['automation_id']}" if el["automation_id"] else "")
        label_disp = label if len(label) <= 45 else label[:42] + "..."
        indent = "  " * el["depth"]
        print(f"{el['type']:<14} {click_str:<14} {bounds_str:<22} {indent}{label_disp}")


if __name__ == "__main__":
    main()
