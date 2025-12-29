# SESSION HANDOFF

**Last Updated:** 2025-12-28
**Last Session:** Session 13 (In Progress)
**Status:** Style/Fight guide audit in progress — stopped after CH4

---

## BEFORE YOU BEGIN

Read these files in order:
1. `/workspaces/pilot/RESONANCE_STYLE_GUIDE.md` — **Joe's prose voice (LOAD FIRST)**
2. `/workspaces/pilot/fight_Guide.md` — **Combat writing principles**
3. `/workspaces/pilot/RESONANCE/drafting/ACT_III_MAPS.md` — Emotional arcs, callbacks, constraints
4. `/workspaces/pilot/RESONANCE/drafting/SYSTEM_PROMPT.md` — Fiction-tuned prompt

### The Drafting System (Session 12)

```bash
cd /workspaces/pilot/RESONANCE/drafting
export ANTHROPIC_API_KEY="your-key"

# Draft with opus + fight guide
python draft.py 31 -m opus --fight-guide -o ch31_draft.txt

# Draft with opus + montage guide (parallel threads)
python draft.py 32 -m opus --montage-guide -c 31 -o ch32_draft.txt
```

---

## SESSION 13 SUMMARY (Current)

**Date:** 2025-12-28

### Accomplished

1. **Chapter formatting standardized (all 34 chapters):**
   - Added missing headers (CH1-6, CH15, CH21-22)
   - Removed old metadata format (CH8-14)
   - Fixed italics `*text*` → `_text_` throughout
   - Format: blank line → CHAPTER N → blank → TITLE → blank → prose

2. **Style Guide created:** `/workspaces/pilot/RESONANCE_STYLE_GUIDE.md`
   - Syntactic signatures (fragments, em-dashes, lists)
   - Tense architecture (present for RESONANCE, past for prior events)
   - Joe's editorial sensibilities codified

3. **Style + Fight Guide audit started:**
   - CH2 revised (Elena's tactical competence, compression)
   - CH3 audited (tense shift intentional, typos fixed)
   - CH4 audited (clean — bookends, fight works)

### Joe's Editorial Sensibilities (captured)

- **Trust the reader implicitly** — Don't explain emotional beats
- **Density is a feature** — Compression does the work
- **Voice trumps technical polish** — Trust the ear
- **Intentional repetition stays** — If it sounds right, defend it
- **Tense is architectural** — CH3's past→present shift is design, not drift

### Resume From

**CH5 (THE QUEUE)** — Continue style/fight guide audit

---

## SESSION 12 SUMMARY

**Date:** 2025-12-27

### Accomplished

1. **Act III Timeline HTML created** — `/workspaces/pilot/RESONANCE/ACT_III_TIMELINE.html`
   - Five phases mapped with parallel threads
   - All character rows with beat-by-beat tracking
   - Notes section with thematic breakdowns

2. **All chapter scaffolds updated (27-33):**
   - Matrioshka Brain colonization mechanics
   - The Softing (border defense Elena disables)
   - Role swap: Elena disables defense, Hendricks finds Standard
   - Black Box location (throne room)
   - Dante stays at New Geneva
   - Humans join the fight
   - Four's death (the cost is real)

3. **The Brawl finalized (Ch 31):**
   - Dual deception: Both hide weapons
   - The sermon: "Morton at least had the decency to fuck what he built—"
   - Ash KNEW about Morton and Standard — hypocrisy exposed
   - Ceramic blade (killed Morton) stabs Hendricks
   - Hendricks falls out window

4. **Standard's Escape finalized (Ch 27):**
   - Kael visits — implied sexual danger, explicit physical
   - She clocks punches too hard — he's enhanced (TERMINIST HYPOCRISY)
   - Tears off his RIGHT arm with her legs
   - Attaches it to her stump: "Good thing I'm Standard."

5. **The Three Arms Progression:**
   - Original → taken by Ash (violation)
   - Kael's → stolen in escape (survival)
   - Sister's → given freely (gift)

6. **Waystation Callback (Ch 32):**
   - 40,000 Template 3s — catharsis
   - "Where's the jacket I loaned you?"
   - Sister gives Standard her own arm: "Appearances, right?"

7. **Drafting System Built:**
   - `draft.py` — API drafting script
   - `SYSTEM_PROMPT.md` — Fiction-tuned prompt
   - `ACT_III_MAPS.md` — Emotional arcs, callbacks, negative constraints
   - Chapter 1 as style exemplar (auto-included)
   - Fight guide + Montage guide (optional flags)

---

## NEGATIVE CONSTRAINTS (DO NOT)

### Pacing:
- ❌ Compress confrontations into single paragraphs
- ❌ Skip transitions (teleportation problem)
- ❌ Rush Four's death
- ❌ Jam all Ash confrontations together

### Character:
- ❌ Make Ash stupid (his fear is legitimate)
- ❌ Let Hendricks explain himself
- ❌ Resolve Standard's consciousness question
- ❌ Thesis statements in dialogue

### Action:
- ❌ Blow-by-blow choreography
- ❌ Action-movie survival without cost
- ❌ Fights that don't reveal character

### Structure:
- ❌ Explain plan in dialogue (discover through execution)
- ❌ Hand-wave colonization mechanics
- ❌ Miss battlefronts
- ❌ Forget refugees picking up weapons (thesis goes both ways)

---

## CALLBACKS THAT MUST PAY OFF

| Setup | Payoff |
|-------|--------|
| "Does it still hurt the same?" (Ch 27) | Ch 32 (Standard vs Ash) |
| Ceramic blade killed Morton | Ch 31 (stabs Hendricks) |
| "I'll keep the engine warm" (Ch 30) | Ch 33 (Four's death) |
| Waystation jacket | Ch 32 (sister callback) |
| "You think that machine loves you?" (Ch 31) | Ch 32 (family saves each other) |
| Ch 1 chest point (shutdown) | Ch 33 ("It's okay") |
| Bullet 5 | Ch 32 (Ash) |
| Bullet 6 | Ch 33 (Standard) |
| Three arms progression | Ch 27 → 31 → 32 |
| "Good thing I'm Standard" | Ch 27 (escape) + Ch 32 (40K sisters) |

---

## REVOLVER JOURNEY

| Shot | Target | Meaning |
|------|--------|---------|
| 1 | The Child | First sin |
| 2-4 | Scavengers | Survival |
| 5 | Ash | Contract fulfilled |
| 6 | Standard | Door opened |

---

## CHARACTER EMOTIONAL ARCS (Act III)

### HENDRICKS
- **Arc:** Transactional isolation → chosen family → paying the cost
- **Key Shift:** The bullet meant for himself becomes the gift that frees her

### STANDARD
- **Arc:** "Am I real?" → "It doesn't matter" → "I offer anyway"
- **Key Shift:** Her nature (machine) is her advantage, not her curse

### ELENA
- **Arc:** Performing daughter → active resistance → receiving grace
- **Key Shift:** She gets to choose (android life with Dante) what her mother never could

### FOUR
- **Arc:** Protector → sacrifice → "engine warm" made literal
- **Key Shift:** She becomes the bridge. Then Standard takes over. Four is gone.

### ASH
- **Arc:** Prophet → exposed → refuses gift → dies refusing
- **Key Shift:** Never learns Standard is Marisol. Dies without knowing.

---

## KEY FILES

| Purpose | Path |
|---------|------|
| **Drafting** | |
| Script | `/workspaces/pilot/RESONANCE/drafting/draft.py` |
| System Prompt | `/workspaces/pilot/RESONANCE/drafting/SYSTEM_PROMPT.md` |
| Maps | `/workspaces/pilot/RESONANCE/drafting/ACT_III_MAPS.md` |
| Timeline | `/workspaces/pilot/RESONANCE/ACT_III_TIMELINE.html` |
| **Scaffolds** | |
| Ch 27 | `/workspaces/pilot/RESONANCE/chapters/RESONANCE_CH27_SCAFFOLD.txt` |
| Ch 31 | `/workspaces/pilot/RESONANCE/chapters/RESONANCE_CH31_SCAFFOLD.txt` |
| Ch 32 | `/workspaces/pilot/RESONANCE/chapters/RESONANCE_CH32_SCAFFOLD.txt` |
| Ch 33 | `/workspaces/pilot/RESONANCE/chapters/RESONANCE_CH33_SCAFFOLD.txt` |
| **Style** | |
| Style Guide | `/workspaces/pilot/RESONANCE_STYLE_GUIDE.md` |
| Fight Guide | `/workspaces/pilot/fight_Guide.md` |
| Montage Guide | `/workspaces/pilot/Montage_Style_Guide.md` |
| Ch 1 (exemplar) | `/workspaces/pilot/RESONANCE/chapters/RESONANCE_CH1_RUDE_AWAKENING.txt` |
| Ch 20 (exemplar) | `/workspaces/pilot/RESONANCE/chapters/RESONANCE_CH20_IN_PLAIN_SIGHT.txt` |

---

## THE THESIS

> "What if they offer something we don't deserve?"

And now: What if we prove worthy of it?

The gift creates the worthiness. The offering transforms the recipient.

---

## MANUSCRIPT STATUS

| Ch | Status |
|----|--------|
| 1-34 | Complete (~65K words) |

**Full manuscript exists.** Style/fight guide audit in progress (stopped after CH4).

---

*Ready to draft. Make it hurt. Make it matter.*
