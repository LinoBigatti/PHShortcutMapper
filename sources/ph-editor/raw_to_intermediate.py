import sys
import os

CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CWD)
sys.path.insert(0, os.path.normpath(os.path.join(CWD, "..", "..")))

import shmaplib
import json

data = shmaplib.IntermediateShortcutData("Project Heartbeat Editor", "Default", os_supported=["windows", "linux"])

EXTRA_SHORTCUTS = [
    {
        "action": "note_up",
        "category": "Notes",
        "name": "Create / Change type to triangle",
        "shortcut": "W / I"
	},
    {
        "action": "note_down",
        "category": "Notes",
        "name": "Create / Change type to Cross",
        "shortcut": "S / K"
	},
    {
        "action": "note_left",
        "category": "Notes",
        "name": "Create / Change type to Square",
        "shortcut": "A / J"
	},
    {
        "action": "note_right",
        "category": "Notes",
        "name": "Create / Change type to Circle",
        "shortcut": "D / L"
	},
    {
        "action": "note_slide_left",
        "category": "Notes",
        "name": "Create / Change type to Heart / Slide Left",
        "shortcut": "Q / U"
	},
    {
        "action": "note_slide_right",
        "category": "Notes",
        "name": "Create / Change type to Heart / Slide Right",
        "shortcut": "E / O"
	},
    {
        "action": "note_slide_left_2",
        "category": "Notes",
        "name": "Create / Change type to Slide Left 2",
        "shortcut": "Shift + Q / Shift + U"
	},
    {
        "action": "note_slide_right_2",
        "category": "Notes",
        "name": "Create / Change type to Slide Right 2",
        "shortcut": "Shift + E / Shift + O"
	},
]

base_dir = os.path.dirname(__file__)
with open(base_dir + "/raw/ph_editor.json", mode="r") as f:
    shortcuts = json.load(f)

    extra_shortcut_actions = [shortcut["action"] for shortcut in EXTRA_SHORTCUTS]
    extra_shortcut_actions.append("heart_note")

    shortcuts = [shortcut for shortcut in shortcuts if not shortcut["action"] in extra_shortcut_actions]

    for shortcut in shortcuts:
        k = shortcut["shortcut"]

        data.add_shortcut("All", shortcut["name"], k, "")
        data.add_shortcut(shortcut["category"], shortcut["name"], k, "")

data.serialize(base_dir + "/intermediate/ph_editor.json")
