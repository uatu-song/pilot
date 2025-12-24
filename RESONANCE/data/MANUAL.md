# RESONANCE Data System Manual

**Version:** 1.0
**Created:** 2025-12-21 (Session 4)
**Purpose:** Complete reference for the machine-queryable story canon system

---

## What This System Is

The RESONANCE Data System is a **constraint enforcement and continuity tracking system** for collaborative fiction writing. It solves three problems inherent to LLM-assisted long-form fiction:

1. **Token Window** — LLMs have bounded memory. You can't load an entire story bible every session.
2. **Statelessness** — Nothing persists between sessions. Each conversation starts fresh.
3. **Non-Determinism** — LLMs fill gaps by inventing plausible details that may contradict canon.

**The Solution:** A machine-queryable YAML database with a Python query interface. Before writing, query what you need. After writing, validate against constraints.

---

## File Structure

```
/RESONANCE/data/
├── RESONANCE_DATA.yaml    # Master canonical truth (all entities)
├── query.py               # Query and validation interface
└── MANUAL.md              # This file
```

**Related files (context documents):**
```
/RESONANCE/context/
├── CODEX_V1.md            # Thematic spine, methodology, world (prose)
├── ENTITY_CATALOG.yaml    # Legacy format (being replaced by RESONANCE_DATA.yaml)
└── NEGATIVE_CONSTRAINTS.md # Prose version of constraints
```

---

## The Master Data File

`RESONANCE_DATA.yaml` contains all canonical story elements in queryable format:

| Section | Contents |
|---------|----------|
| `meta` | Series info, book number, thesis |
| `characters` | Full profiles: demographics, knowledge states, arcs, forbidden associations, state by chapter |
| `locations` | Physical spaces with sensory details and chapter appearances |
| `objects` | Key items with tracking (e.g., revolver ammunition) |
| `events` | Plot events with timing, participants, constraints |
| `factions` | Organizations with goals, weapons, markers |
| `themes` | Thematic spine with applications |
| `arcs` | Trilogy arc and per-character arcs with beats |
| `chapter_states` | Per-chapter state snapshots (POV, location, events, endpoints) |
| `constraints` | BLOCKING and WARNING validation rules with POV awareness |
| `signatures` | Recurring motifs (frequencies, refrains, sensory markers) |

---

## Query Commands

### Character Queries

```bash
# Full character profile
python query.py character STANDARD

# Specific field
python query.py character STANDARD --field knowledge
python query.py character HENDRICKS --field state_by_chapter

# Knowledge states
python query.py knows ELENA           # What Elena knows
python query.py doesnt_know STANDARD  # What Standard doesn't know

# Forbidden associations
python query.py forbidden STANDARD    # Words/phrases to avoid

# Relationships
python query.py relationships HENDRICKS
```

### World Queries

```bash
# Locations
python query.py location CHECKPOINT
python query.py location VERTICAL_CITY

# Objects
python query.py object REVOLVER
python query.py object BLACK_BOX

# Events
python query.py event THE_HEIST
python query.py event SCAVENGER_ENCOUNTER

# Factions
python query.py faction TERMINISTS
python query.py faction THE_SKY

# Themes
python query.py theme MUTUAL_CURE
python query.py theme CONSCIOUSNESS_AS_RELATIONSHIP
```

### State Queries

```bash
# Chapter state
python query.py state 4              # Returns POV, location, events, endpoint

# Ammunition tracking
python query.py ammo                 # Revolver shots fired/remaining
```

### Discovery Queries

```bash
# Search across all entities
python query.py search "287.3"       # Find everything mentioning the frequency

# List all items in a section
python query.py list characters
python query.py list locations
python query.py list objects
python query.py list events
```

### Constraint Queries

```bash
# All blocking constraints
python query.py constraints blocking

# All warning constraints
python query.py constraints warnings

# All constraints
python query.py constraints
```

---

## Validation System

The validator checks prose against canonical constraints. It is **POV-aware** — constraints only apply to relevant POV chapters.

### Basic Validation

```bash
python query.py validate path/to/chapter.md
```

**Output:**
```
File: path/to/chapter.md
POV detected: STANDARD
Chapter detected: 4

No violations found.
```

### Verbose Validation (shows skipped constraints)

```bash
python query.py validate path/to/chapter.md --verbose
```

**Output:**
```
File: path/to/chapter.md
POV detected: ELENA
Chapter detected: 2

No violations found.

Skipped constraints (not applicable to this POV/chapter):
  - Standard's nature: POV ELENA not in ['STANDARD']
  - Machine words in Standard POV: POV ELENA not in ['STANDARD']
```

### Force POV (override auto-detection)

```bash
python query.py validate path/to/chapter.md --pov STANDARD
```

### How POV Detection Works

The validator looks for this pattern in the markdown:
```markdown
**POV:** Standard
```

It normalizes variations:
- `Standard` → `STANDARD`
- `Elena María Ash` → `ELENA`
- `Hendricks` → `HENDRICKS`

---

## Constraint Types

### BLOCKING Constraints

**Auto-reject if violated.** These are canon-breaking errors.

| ID | Name | POV | Description |
|----|------|-----|-------------|
| CON_001 | Standard's nature | STANDARD | She doesn't know she's an android |
| CON_002 | Morton telegraphing | ALL | Don't hint at Standard's origin |
| CON_003 | Black Box handoff | ALL | Elena transports, doesn't hand off at NED |
| CON_004 | Regulator removal | ALL | Hendricks removes it alone, in apartment |
| CON_005 | Awakening trigger | ALL | Standard wakes from 287.3 Hz, not aliens |
| CON_006 | Elena experience | ALL | First operation, age 18, not veteran |
| CON_007 | Hendricks Bomb | ELENA | Elena doesn't know Hendricks shot the Child |
| CON_008 | Machine words | STANDARD | No tech vocabulary in her internal narration |
| CON_009 | Revolver ammo | ALL | Only 2 shots remaining (manual tracking) |
| CON_010 | Standard self-reference | STANDARD | Can't think of herself as machine |

### WARNING Constraints

**Flag for human review.** Not auto-reject, but worth checking.

| ID | Name | POV | Description |
|----|------|-----|-------------|
| WARN_001 | Hendricks interiority | HENDRICKS (Ch 3) | Minimize internal narration |
| WARN_002 | Superhuman strength | STANDARD | Her strength should cost her |

---

## Character Knowledge States

Critical for preventing knowledge leakage.

### Standard — What She Doesn't Know
```bash
python query.py doesnt_know STANDARD
```
- She is an android
- Morton created her
- She carries the Source Code for Mortality
- Why Hendricks isn't surprised by her
- Why the scanner read empty
- Why she didn't fall during the Correction Frequency

### Elena — What She Doesn't Know
```bash
python query.py doesnt_know ELENA
```
- What Standard is
- That Standard is air-gapped
- **Hendricks shot the Child** (THE BOMB — dramatic reveal pending)

---

## Object Tracking

### Revolver Ammunition

```bash
python query.py ammo
```

| Shot | Target | Location |
|------|--------|----------|
| 1 | The Child | Remanence |
| 2 | Scavenger leader | Resonance Ch 4 |
| 3 | Scavenger woman | Resonance Ch 4 |
| 4 | Scavenger (gut-shot) | Resonance Ch 4 |
| 5 | REMAINING | — |
| 6 | REMAINING | — |

**Constraint:** Two bullets for the rest of the book. No convenient reloads for 300-year-old ammunition.

---

## Chapter State Tracking

```bash
python query.py state 4
```

Returns:
```yaml
title: The Descent
pov: Standard
tense: Present
location: Stairwell
characters_present: [STANDARD, HENDRICKS, SCAVENGERS]
events: [SCAVENGER_ENCOUNTER]
ends_with: Standard carrying Hendricks into the dark
word_count: 1400
```

---

## Workflow: Before Writing

1. **Query character knowledge states**
   ```bash
   python query.py knows STANDARD
   python query.py doesnt_know STANDARD
   ```

2. **Query forbidden associations**
   ```bash
   python query.py forbidden STANDARD
   ```

3. **Query relevant constraints**
   ```bash
   python query.py constraints blocking
   ```

4. **Check previous chapter state**
   ```bash
   python query.py state 4
   ```

5. **Check object tracking**
   ```bash
   python query.py ammo
   ```

---

## Workflow: After Writing

1. **Run validation**
   ```bash
   python query.py validate chapter.md
   ```

2. **If violations found:** Fix prose, re-validate

3. **If clean:** Update data file with new state
   - Add new events
   - Update character knowledge (if something is revealed)
   - Update object tracking (if ammo used, items moved, etc.)
   - Update chapter_states section

---

## Updating the Data File

When canon changes, update `RESONANCE_DATA.yaml`:

### Adding a new event
```yaml
events:
  NEW_EVENT:
    id: "EVT_XXX"
    name: "Event Name"
    chapter: N
    participants: [CHARACTER_IDS]
    outcome: "What happened"
```

### Updating character knowledge
```yaml
characters:
  STANDARD:
    knowledge:
      knows:
        - "New thing she learned"  # Add here
      learns:
        new_knowledge: { chapter: N }  # Track when learned
```

### Tracking ammunition
```yaml
objects:
  REVOLVER:
    ammunition:
      shot_5: { target: "New target", book: "Resonance", chapter: N }
    remaining: 1  # Decrement
```

### Adding chapter state
```yaml
chapter_states:
  ch5:
    title: "Chapter Title"
    pov: "CHARACTER"
    tense: "Present"
    location: "LOCATION_ID"
    characters_present: [IDS]
    events: [EVENT_IDS]
    ends_with: "Final beat"
    word_count: NNNN
```

---

## Key Constraints to Remember

### Standard POV Rules
- **Never** use: robot, machine, android, servo, chassis, circuit, processor, reboot, malfunction
- **Never** have her realize what she is before the reveal
- **Do** use clinical/computational framing ("structural integrity," percentages, precise measurements)
- **Do** show tells the reader notices but she doesn't

### Elena POV Rules
- She is 18, not a veteran
- This heist is her FIRST major operation
- She does NOT know Hendricks shot the Child (this is a dramatic bomb)
- Present tense (the Box is recording)

### Hendricks POV Rules
- Minimize interiority in Chapter 3 opening
- Show through action, not internal narration
- Post-Regulator: shaking, gray, weak — not strong or steady

### Global Rules
- Don't telegraph Standard's origin ("Morton's gift," "Morton sent")
- Elena transports the Box, doesn't hand it off at NED
- Standard wakes from 287.3 Hz, not alien signal
- Revolver has 2 shots remaining

---

## Signatures and Motifs

Query these for thematic consistency:

```yaml
signatures:
  frequencies:
    resonance: "287.3 Hz"
    correction: "Alien dissonance frequency"

  refrains:
    book_1: "La-dee-da, la-dee-dum"
    its_okay: "Appears twice in Ch 2"

  sensory:
    void: "What Elena feels around Standard — absence, not silence"
    hum: "287.3 Hz — subliminal pressure in Sky territory"

  objects:
    thunder: "Connects to gunshot, Child's death, Hendricks' trauma"
    revolver: "Antique, dismissed as junk, kills precisely"
```

---

## Quick Reference Card

```bash
# Before writing Standard POV
python query.py forbidden STANDARD
python query.py doesnt_know STANDARD

# Before writing Elena POV
python query.py doesnt_know ELENA
python query.py character ELENA --field operation_status

# Check continuity
python query.py state [previous_chapter]
python query.py ammo

# After writing
python query.py validate chapter.md

# Find anything
python query.py search "term"
```

---

## Troubleshooting

### "POV detected: None"
The validator couldn't find `**POV:** CharacterName` in the file. Either:
- Add the POV declaration to the file header
- Use `--pov CHARACTER` to force it

### False positives
If a constraint fires incorrectly:
1. Check if the constraint's POV scope is correct
2. Check if the pattern is too broad
3. Update the constraint in `RESONANCE_DATA.yaml`

### Missing data
If a query returns "not found":
1. Check the exact ID/name spelling
2. Try `python query.py search "partial_term"` to find it
3. Add the missing entity to `RESONANCE_DATA.yaml`

---

## Philosophy

This system embodies the **Context Engineering for Fiction** methodology:

1. **You don't load everything** — Query only what's needed for the current scene
2. **Validate before accepting** — Output doesn't become canon until it passes
3. **Document what's NOT true** — Negative constraints prevent inventions more effectively than positive statements
4. **The Evaluator is the gate** — Nothing passes until validated

The key insight: **You can't prevent LLMs from inventing. You can only catch inventions before they become canon.**

---

## For New Sessions

If you're a new Claude instance starting a session:

1. Read `/workspaces/pilot/HANDOFF.md` first
2. Query the current chapter state: `python query.py state [last_chapter]`
3. Query character knowledge before writing any POV
4. Validate all prose before saving
5. Update the data file when canon changes

**The system is the source of truth. When in doubt, query it.**

---

*End of Manual*
