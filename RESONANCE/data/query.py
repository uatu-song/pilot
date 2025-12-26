#!/usr/bin/env python3
"""
RESONANCE Data Query System
============================
Machine-queryable interface for story canon.

Usage:
    python query.py character STANDARD
    python query.py character STANDARD --field knowledge
    python query.py location CHECKPOINT
    python query.py object REVOLVER
    python query.py event THE_HEIST
    python query.py state 4                    # Chapter 4 state
    python query.py constraints                # All blocking constraints
    python query.py validate chapter.md        # Check file against constraints
    python query.py ammo                       # Revolver ammunition status
    python query.py relationships STANDARD     # Character relationships
    python query.py knows ELENA                # What character knows
    python query.py doesnt_know STANDARD       # What character doesn't know
    python query.py book1                      # Full Book 1 (Remanence) summary
    python query.py book1 events               # Core events from Book 1
    python query.py book1 fates                # Character fates at end of Book 1
    python query.py book1 child                # What happened to the Child
    python query.py book1 hendricks            # Hendricks' Book 1 arc
    python query.py book1 miracle              # The Miracle event
    python query.py book1 constraints          # Critical constraints from Book 1
"""

import yaml
import re
import sys
import json
from pathlib import Path
from typing import Any, Optional

# Data files (split for token efficiency)
DATA_DIR = Path(__file__).parent
DATA_FILES = [
    "CORE.yaml",
    "CHARACTERS.yaml",
    "WORLD.yaml",
    "CHAPTERS.yaml",
]

# Fallback to legacy single file if split files don't exist
LEGACY_DATA_PATH = DATA_DIR / "RESONANCE_DATA.yaml"

def load_data() -> dict:
    """Load and merge all data files, or fall back to legacy single file."""
    # Check if split files exist
    split_files_exist = all((DATA_DIR / f).exists() for f in DATA_FILES)

    if split_files_exist:
        merged = {}
        for filename in DATA_FILES:
            filepath = DATA_DIR / filename
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
                if data:
                    # Deep merge - later files override earlier ones
                    for key, value in data.items():
                        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                            merged[key].update(value)
                        else:
                            merged[key] = value
        return merged
    elif LEGACY_DATA_PATH.exists():
        # Fall back to legacy single file
        with open(LEGACY_DATA_PATH, 'r') as f:
            return yaml.safe_load(f)
    else:
        raise FileNotFoundError("No data files found. Expected split files or RESONANCE_DATA.yaml")

def get_character(data: dict, char_id: str, field: Optional[str] = None) -> Any:
    """Get character data."""
    char_id = char_id.upper()
    char = data.get('characters', {}).get(char_id)
    if not char:
        return f"Character '{char_id}' not found"
    if field:
        return char.get(field, f"Field '{field}' not found")
    return char

def get_location(data: dict, loc_id: str) -> Any:
    """Get location data."""
    loc_id = loc_id.upper()
    loc = data.get('locations', {}).get(loc_id)
    if not loc:
        # Try matching by name
        for key, val in data.get('locations', {}).items():
            if loc_id.lower() in val.get('name', '').lower():
                return val
        return f"Location '{loc_id}' not found"
    return loc

def get_object(data: dict, obj_id: str) -> Any:
    """Get object data."""
    obj_id = obj_id.upper()
    obj = data.get('objects', {}).get(obj_id)
    if not obj:
        # Try matching by name
        for key, val in data.get('objects', {}).items():
            if obj_id.lower() in val.get('name', '').lower():
                return val
        return f"Object '{obj_id}' not found"
    return obj

def get_event(data: dict, event_id: str) -> Any:
    """Get event data."""
    event_id = event_id.upper()
    event = data.get('events', {}).get(event_id)
    if not event:
        # Try matching by name
        for key, val in data.get('events', {}).items():
            if event_id.lower().replace('_', ' ') in val.get('name', '').lower():
                return val
        return f"Event '{event_id}' not found"
    return event

def get_chapter_state(data: dict, chapter: int) -> Any:
    """Get state for a specific chapter."""
    key = f"ch{chapter}"
    state = data.get('chapter_states', {}).get(key)
    if not state:
        return f"Chapter {chapter} state not found"
    return state

def get_constraints(data: dict, severity: str = 'all') -> list:
    """Get constraints by severity."""
    constraints = data.get('constraints', {})
    if severity == 'all':
        result = []
        for sev in ['blocking', 'warnings']:
            result.extend(constraints.get(sev, []))
        return result
    return constraints.get(severity, [])

def get_ammunition_status(data: dict) -> dict:
    """Get revolver ammunition status."""
    revolver = data.get('objects', {}).get('REVOLVER', {})
    return {
        'capacity': revolver.get('capacity', 6),
        'remaining': revolver.get('remaining', 0),
        'shots_fired': revolver.get('ammunition', {}),
        'constraint': revolver.get('constraint', '')
    }

def get_relationships(data: dict, char_id: str) -> list:
    """Get character relationships."""
    char = get_character(data, char_id)
    if isinstance(char, str):
        return char
    return char.get('relationships', [])

def get_knowledge(data: dict, char_id: str, knows: bool = True) -> list:
    """Get what a character knows or doesn't know."""
    char = get_character(data, char_id)
    if isinstance(char, str):
        return char
    knowledge = char.get('knowledge', {})
    if knows:
        return knowledge.get('knows', [])
    return knowledge.get('doesnt_know', [])

def detect_pov(content: str) -> Optional[str]:
    """Detect POV from file content (looks for **POV:** line)."""
    # Look for POV declaration in markdown header
    pov_match = re.search(r'\*\*POV:\*\*\s*(\w+)', content, re.IGNORECASE)
    if pov_match:
        pov = pov_match.group(1).upper()
        # Normalize POV names
        pov_map = {
            'STANDARD': 'STANDARD',
            'HENDRICKS': 'HENDRICKS',
            'ELENA': 'ELENA',
            'ASH': 'ASH',
            'ELENA MARÍA ASH': 'ELENA',
            'ELENA MARIA ASH': 'ELENA',
        }
        return pov_map.get(pov, pov)
    return None

def detect_chapter(content: str) -> Optional[int]:
    """Detect chapter number from file content."""
    # Look for chapter declaration
    ch_match = re.search(r'Chapter\s*(\d+)', content, re.IGNORECASE)
    if ch_match:
        return int(ch_match.group(1))
    return None

def validate_file(data: dict, filepath: str, force_pov: str = None) -> dict:
    """Validate a file against blocking constraints (POV-aware)."""
    result = {
        'file': filepath,
        'pov_detected': None,
        'chapter_detected': None,
        'violations': [],
        'skipped': []
    }

    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        result['violations'] = [f"File not found: {filepath}"]
        return result

    # Detect POV and chapter
    pov = force_pov.upper() if force_pov else detect_pov(content)
    chapter = detect_chapter(content)
    result['pov_detected'] = pov
    result['chapter_detected'] = chapter

    constraints = get_constraints(data, 'blocking')

    for constraint in constraints:
        constraint_pov = constraint.get('pov', ['ALL'])
        constraint_chapters = constraint.get('chapters', None)

        # Check if constraint applies to this POV
        pov_applies = 'ALL' in constraint_pov or (pov and pov in constraint_pov)

        # Check if constraint applies to this chapter
        chapter_applies = constraint_chapters is None or (chapter and chapter in constraint_chapters)

        if not pov_applies or not chapter_applies:
            result['skipped'].append({
                'constraint': constraint.get('name'),
                'reason': f"POV {pov} not in {constraint_pov}" if not pov_applies else f"Chapter {chapter} not in {constraint_chapters}"
            })
            continue

        patterns = constraint.get('patterns', [])
        for pattern in patterns:
            if not pattern:  # Skip empty patterns
                continue
            try:
                if re.search(pattern, content, re.IGNORECASE):
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    result['violations'].append({
                        'constraint': constraint.get('name'),
                        'rule': constraint.get('rule'),
                        'pattern': pattern,
                        'matches': matches[:3]  # First 3 matches
                    })
            except re.error:
                # Pattern might not be valid regex, try literal
                if pattern.lower() in content.lower():
                    result['violations'].append({
                        'constraint': constraint.get('name'),
                        'rule': constraint.get('rule'),
                        'pattern': pattern,
                        'matches': ['literal match']
                    })

    return result

def get_forbidden(data: dict, char_id: str) -> dict:
    """Get forbidden associations for a character."""
    char = get_character(data, char_id)
    if isinstance(char, str):
        return char
    return char.get('forbidden', {})

def get_theme(data: dict, theme_id: str) -> Any:
    """Get theme data."""
    theme_id = theme_id.upper()
    theme = data.get('themes', {}).get(theme_id)
    if not theme:
        # Try matching by name
        for key, val in data.get('themes', {}).items():
            if theme_id.lower().replace('_', ' ') in val.get('name', '').lower():
                return val
        return f"Theme '{theme_id}' not found"
    return theme

def get_faction(data: dict, faction_id: str) -> Any:
    """Get faction data."""
    faction_id = faction_id.upper()
    faction = data.get('factions', {}).get(faction_id)
    if not faction:
        # Try matching by name
        for key, val in data.get('factions', {}).items():
            if faction_id.lower() in val.get('name', '').lower():
                return val
        return f"Faction '{faction_id}' not found"
    return faction

def search(data: dict, query: str) -> list:
    """Search across all entities for a term."""
    results = []
    query_lower = query.lower()

    for section in ['characters', 'locations', 'objects', 'events', 'factions', 'themes']:
        for key, val in data.get(section, {}).items():
            val_str = str(val).lower()
            if query_lower in val_str:
                results.append({
                    'section': section,
                    'key': key,
                    'name': val.get('name', val.get('canonical_name', key))
                })

    return results

def format_output(result: Any) -> str:
    """Format output for display."""
    if isinstance(result, (dict, list)):
        return yaml.dump(result, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return str(result)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    data = load_data()
    command = sys.argv[1].lower()

    if command == 'character':
        if len(sys.argv) < 3:
            print("Usage: python query.py character <ID> [--field <field>]")
            return
        char_id = sys.argv[2]
        field = None
        if '--field' in sys.argv:
            idx = sys.argv.index('--field')
            if idx + 1 < len(sys.argv):
                field = sys.argv[idx + 1]
        result = get_character(data, char_id, field)
        print(format_output(result))

    elif command == 'location':
        if len(sys.argv) < 3:
            print("Usage: python query.py location <ID>")
            return
        result = get_location(data, sys.argv[2])
        print(format_output(result))

    elif command == 'object':
        if len(sys.argv) < 3:
            print("Usage: python query.py object <ID>")
            return
        result = get_object(data, sys.argv[2])
        print(format_output(result))

    elif command == 'event':
        if len(sys.argv) < 3:
            print("Usage: python query.py event <ID>")
            return
        result = get_event(data, sys.argv[2])
        print(format_output(result))

    elif command == 'state':
        if len(sys.argv) < 3:
            print("Usage: python query.py state <chapter_number>")
            return
        result = get_chapter_state(data, int(sys.argv[2]))
        print(format_output(result))

    elif command == 'constraints':
        severity = 'all'
        if len(sys.argv) > 2:
            severity = sys.argv[2]
        result = get_constraints(data, severity)
        print(format_output(result))

    elif command == 'validate':
        if len(sys.argv) < 3:
            print("Usage: python query.py validate <filepath> [--pov STANDARD|ELENA|HENDRICKS]")
            return
        filepath = sys.argv[2]
        force_pov = None
        if '--pov' in sys.argv:
            idx = sys.argv.index('--pov')
            if idx + 1 < len(sys.argv):
                force_pov = sys.argv[idx + 1]

        result = validate_file(data, filepath, force_pov)

        print(f"File: {result['file']}")
        print(f"POV detected: {result['pov_detected']}")
        print(f"Chapter detected: {result['chapter_detected']}")
        print()

        if result['violations']:
            print("VIOLATIONS FOUND:")
            print(format_output(result['violations']))
        else:
            print("No violations found.")

        if '--verbose' in sys.argv and result['skipped']:
            print("\nSkipped constraints (not applicable to this POV/chapter):")
            for s in result['skipped']:
                print(f"  - {s['constraint']}: {s['reason']}")

    elif command == 'ammo':
        result = get_ammunition_status(data)
        print(format_output(result))

    elif command == 'relationships':
        if len(sys.argv) < 3:
            print("Usage: python query.py relationships <character_id>")
            return
        result = get_relationships(data, sys.argv[2])
        print(format_output(result))

    elif command == 'knows':
        if len(sys.argv) < 3:
            print("Usage: python query.py knows <character_id>")
            return
        result = get_knowledge(data, sys.argv[2], knows=True)
        print(format_output(result))

    elif command == 'doesnt_know':
        if len(sys.argv) < 3:
            print("Usage: python query.py doesnt_know <character_id>")
            return
        result = get_knowledge(data, sys.argv[2], knows=False)
        print(format_output(result))

    elif command == 'forbidden':
        if len(sys.argv) < 3:
            print("Usage: python query.py forbidden <character_id>")
            return
        result = get_forbidden(data, sys.argv[2])
        print(format_output(result))

    elif command == 'theme':
        if len(sys.argv) < 3:
            print("Usage: python query.py theme <theme_id>")
            return
        result = get_theme(data, sys.argv[2])
        print(format_output(result))

    elif command == 'faction':
        if len(sys.argv) < 3:
            print("Usage: python query.py faction <faction_id>")
            return
        result = get_faction(data, sys.argv[2])
        print(format_output(result))

    elif command == 'search':
        if len(sys.argv) < 3:
            print("Usage: python query.py search <term>")
            return
        result = search(data, sys.argv[2])
        print(format_output(result))

    elif command == 'list':
        if len(sys.argv) < 3:
            print("Usage: python query.py list <section>")
            print("Sections: characters, locations, objects, events, factions, themes")
            return
        section = sys.argv[2]
        if section in data:
            items = list(data[section].keys())
            print(format_output(items))
        else:
            print(f"Section '{section}' not found")

    elif command == 'book1':
        # Get Book 1 summary - key facts from Remanence needed for Book 2
        book1 = data.get('book_1', {})
        if len(sys.argv) > 2:
            # Specific subsection
            subsection = sys.argv[2].lower()
            if subsection == 'events':
                result = book1.get('core_events', {})
            elif subsection == 'fates':
                result = book1.get('character_fates', {})
            elif subsection == 'objects':
                result = book1.get('objects', {})
            elif subsection == 'signatures':
                result = book1.get('signatures', {})
            elif subsection == 'constraints':
                result = book1.get('constraints', [])
            elif subsection == 'child':
                result = book1.get('core_events', {}).get('the_child', {})
            elif subsection == 'hendricks':
                result = {
                    'shot_child': book1.get('core_events', {}).get('hendricks_shoots_the_child', {}),
                    'fate': book1.get('character_fates', {}).get('hendricks', {})
                }
            elif subsection == 'miracle':
                result = book1.get('core_events', {}).get('the_miracle', {})
            else:
                result = f"Unknown subsection: {subsection}. Options: events, fates, objects, signatures, constraints, child, hendricks, miracle"
        else:
            result = book1
        print(format_output(result))

    else:
        print(f"Unknown command: {command}")
        print(__doc__)

if __name__ == '__main__':
    main()
