# Claude Project Tracker

**Project:** Remanence Trilogy
**Book 1:** Remanence (complete, reference material)
**Book 2:** Resonance (in progress)
**Book 3:** TBD

---

## Current Status

| Item | Status |
|------|--------|
| Book 1 Draft | Complete (~120K words) |
| Book 1 Context Engineering | Complete |
| Book 2 Chapters | 18 complete + interstitial (~34,000 words), Ch19 scaffolded |
| Book 2 Context Engineering | Active (split YAML system) |

---

## TODO: Dabble Export Workflow

**Problem:** Markdown `*italics*` in .txt files doesn't convert in Dabble's manuscript area.

**Solution needed:** Create a Python script to convert chapter .txt files to .docx with proper formatting:
- Convert `*text*` to italic runs
- Convert `**text**` to bold runs
- Convert `---` to centered scene break markers
- Preserve chapter/title structure
- Use `python-docx` library

**Workflow:**
1. Write chapters in .txt with `*italics*` markers
2. When ready for Dabble, run conversion script
3. Import .docx files into Dabble (rich text transfers correctly)

**Script location (when created):** `/workspaces/pilot/RESONANCE/scripts/convert_to_docx.py`

---

## End Session Protocol

When user says "run end session protocol":

1. **Save session reflection** to `RESONANCE/sessions/YYYY-MM-DD.md`
2. **Update this file** with:
   - Work completed
   - Decisions made
   - Open threads
   - Next steps
3. **Update arc trackers** if character states changed
4. **Note any new constraints** discovered

---

## Session Log

### 2025-12-20 — Session 1 (Complete)

**Work Completed:**
- Read complete Book 1 (Remanence, ~120K words)
- Created REMANENCE context engineering system
- Read existing RESONANCE materials (Ch 1-3, Codex, trackers)
- Wrote Chapter 4: The Convergence (~1,650 words)
- Integrated Codex v1 into HANDOFF.md
- Created character profile template
- Split character documents into profiles/ and state/
- Organized folder structure for both projects

**Session 1 Locks:**
- Elena age: 18 (was 17 during The Miracle)
- Elena experience: First major operation (NOT veteran)
- Hendricks Bomb: Elena does NOT know Hendricks shot the Child
- Thomas = Pilot's lover, NOT husband
- 287.3 Hz = frequency of consciousness
- Standard wakes from 287.3 Hz, BEFORE alien arrival

**Open Threads:**
- Brother Ash TBDs (ethnicity, sexuality) — fill before he appears
- Ash's compound physical description needed
- Book 2 ending TBD

**Session Reflection:** `/workspaces/pilot/sessions/2025-12-20_session1.md`

---

### Next Session — Pending

**Priority:**
1. Fill Brother Ash TBDs
2. Create Chapter 5 manifest
3. Write Chapter 5 (arrival at Ash's compound)
4. Update character state files

---

## Folder Structure

```
/workspaces/pilot/
├── claude.md (this file)
├── HANDOFF.md (start-of-session briefing)
├── CONTEXT_ENGINEERING_FOR_FICTION.md
├── sessions/          (session reflections — trilogy-wide)
├── RESONANCE/
│   ├── chapters/      (Ch 1-4 drafts)
│   ├── characters/
│   │   ├── profiles/  (stable identity — 4 profiles + template)
│   │   └── state/     (dynamic per-chapter — 4 states + template)
│   ├── context/       (Codex, Entity Catalog, Constraints, Evaluator)
│   └── manifests/     (session manifests)
└── REMANENCE/
    └── (Book 1 reference materials)
```

---

## Quick Reference

**Blocking Constraints (Book 2):**
- Standard does NOT know she's an android
- NO Morton telegraphing ("Morton's gift", etc.)
- Elena transports Box, does NOT hand off at NED
- Hendricks removes Regulator ALONE, in apartment
- Standard wakes from 287.3 Hz, NOT alien signal

**Character States (Ch 4 End):**
- Standard: In rover, observing, doesn't know what she is
- Hendricks: Unconscious against Black Box, bleeding out
- Elena: Driving, exhausted, tactical decision made

**The Cargo:**
- The Void (Standard) — air-gapped, carries Source Code
- The Engine (Black Box) — powers Quiet Zone, 16,749 minds
