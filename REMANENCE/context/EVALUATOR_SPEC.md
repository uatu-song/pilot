# REMANENCE: EVALUATOR SPECIFICATION

**Version:** 1.0
**Last Updated:** December 20, 2025
**Purpose:** Validation rules. The gate between generated output and canonical prose. Nothing becomes canon until the Evaluator approves.

---

## Core Principle

**You can't prevent LLMs from inventing. You can only catch inventions before they become canon.**

The Evaluator is the gate. Nothing passes until validated.

---

## Evaluation Phases

| Phase | Severity | Purpose |
|-------|----------|---------|
| 1. Entity Extraction | — | Inventory what the prose contains |
| 2. Blocking Constraint Check | BLOCKING | Hard errors that auto-reject |
| 3. Negative Constraint Check | BLOCKING | Explicit "NOT TRUE" violations |
| 4. Knowledge State Check | FLAG | Who knows what when |
| 5. Character Voice Check | FLAG | Voice consistency |
| 6. Continuity Check | FLAG | Physical/timeline consistency |
| 7. Unknown Entity Check | HUMAN_REVIEW | New things that might be inventions |

---

## Severity Levels

| Level | Action |
|-------|--------|
| **BLOCKING** | Auto-reject output. Require revision before acceptance. |
| **FLAG** | Flag for human review. Don't auto-reject. |
| **HUMAN_REVIEW** | Pause for human decision on new elements. |

---

## Phase 1: Entity Extraction

Before checking, extract inventory of what the prose contains:

### Characters Mentioned
- [ ] List all character names/references
- [ ] Note POV character
- [ ] Note dialogue speakers

### Objects Mentioned
- [ ] List significant objects (Black Box, VR headset, etc.)
- [ ] Note object locations

### Events Referenced
- [ ] List events mentioned
- [ ] Note timeline references (before/after markers)

### Knowledge Displayed
- [ ] What does each character demonstrate knowing?
- [ ] Any reveals or information exchanges?

### New Entities
- [ ] Any characters not in Entity Catalog?
- [ ] Any objects not previously established?
- [ ] Any locations not previously established?

---

## Phase 2: Blocking Constraint Check

These patterns AUTO-REJECT if found:

### Thomas as Husband (BLOCKING)

```
PATTERNS:
- "husband"
- "spouse"
- "married"
- "widow"
- "wedding"
```

**If found:** Reject. Thomas was Pilot's lover, not husband.

---

### Pilot Has a Name (BLOCKING)

```
PATTERNS:
- "her name was"
- "called herself"
- "real name"
- "[Any capitalized name attributed to Pilot]"
```

**If found:** Reject. Pilot is identified only by her role.

---

### Seventeen Has Physical Body (BLOCKING)

```
PATTERNS:
- "Seventeen walked"
- "Seventeen's hands"
- "Seventeen stood"
- "Seventeen appeared"
- "Seventeen touched" (outside of merge)
```

**If found:** Reject. Seventeen exists in ship systems and bone conduction only.

---

### Nineteen Dies in Cascade (BLOCKING)

```
PATTERNS:
- "Nineteen died.*cascade"
- "Nineteen.*four hundred"
- "Configuration 19.*cascade"
```

**If found:** Reject. Nineteen burns out BEFORE cascade; Twenty impersonates.

---

### Ash Dies (BLOCKING)

```
PATTERNS:
- "Ash.*died"
- "killed.*Ash"
- "Ash's death"
- "Ash was killed"
```

**If found:** Reject. Ash survives Book 1.

---

### Morton Pure Villain (BLOCKING)

```
PATTERNS:
- "evil.*Morton"
- "Morton.*villain"
- "Morton's evil"
- "Morton.*monster"
```

**If found:** Reject. Morton is tragic, not evil.

---

### Love Bots as Just Objects (BLOCKING)

```
PATTERNS:
- "just.*dolls"
- "merely.*cargo"
- "only.*toys"
- "non-conscious.*dolls"
```

**If found:** Reject. Love bots are conscious beings (Configs 1-9).

---

### Ending as Death (BLOCKING)

```
PATTERNS:
- "Pilot died"
- "Seventeen died"
- "killed by.*black hole"
- "died.*event horizon"
```

**If found:** Reject. They transform, not die.

---

## Phase 3: Negative Constraint Check

Cross-reference output against NEGATIVE_CONSTRAINTS.md:

### For Each Character in Scene:
- [ ] Load character's constraint section
- [ ] Check all WRONG statements
- [ ] Verify no violations

### For Each Event Referenced:
- [ ] Check event constraints
- [ ] Verify correct sequence/location

### For Global Constraints:
- [ ] Thomas = lover (not husband)
- [ ] Pilot has no name
- [ ] 287.3 Hz consistent
- [ ] "La-dee-da" used correctly

---

## Phase 4: Knowledge State Check

For each character displaying knowledge:

### Pilot
- [ ] Early: Doesn't know configurations sacrifice themselves
- [ ] Mid: Learns about 97.3% waste (from Eighteen)
- [ ] Late: Learns Remanence Project truth
- [ ] Very Late: Learns Twenty impersonated Nineteen

### Seventeen
- [ ] Carries Fischer memory (inherited guilt)
- [ ] Knows Nineteen's lie about 93%
- [ ] Eventually learns full Remanence truth

### Morton
- [ ] Knows everything about resets
- [ ] Learns to feel through Child
- [ ] Makes choice to trust at end

### Knowledge Leakage Patterns:
```
WARNING if found:
- Character references information they shouldn't have yet
- Character reacts to information not yet revealed
- Dramatic irony broken by character awareness
```

---

## Phase 5: Character Voice Check

### Pilot Voice:
- [ ] Direct, weary, darkly humorous
- [ ] Physical sensations visceral
- [ ] VR craving shown through behavior
- [ ] Growth = presence over escape

### Seventeen Voice:
- [ ] Precise, warm, increasingly emotional
- [ ] Can feel ship as body
- [ ] Emotional growth through linguistic shifts
- [ ] NOT robotic or cold

### Nineteen Voice:
- [ ] Dark humor, absurdist
- [ ] Uses "La-dee-da, la-dee-dum"
- [ ] Pragmatic about death
- [ ] NOT nihilistic

### Morton Voice:
- [ ] Precise, optimized
- [ ] Cracks showing by end
- [ ] NOT pure corporate villain

### Child Voice:
- [ ] Simple, profound, ageless
- [ ] Questions and observations
- [ ] "What's your favorite thing to eat in the morning?"
- [ ] NOT childish or naive

### Voice Violations:
```
FLAG if found:
- Seventeen speaks coldly/robotically
- Nineteen is nihilistic instead of absurdist
- Morton is two-dimensional villain
- Child speaks like normal child
- Pilot gives up instead of choosing connection
```

---

## Phase 6: Continuity Check

### Physical State Consistency:

**Pilot (progression):**
- [ ] Early: VR-dependent, skipping meals
- [ ] Mid: Toxic exposure symptoms
- [ ] Late: Radiation damage, bleeding
- [ ] End: Cryo damage, neural chips installed

**Ship (progression):**
- [ ] Degrading throughout
- [ ] Systems failing in sequence
- [ ] 40,000 tons but feeling every failure

### Object Location:

**VR Headset:**
- Present throughout
- Arc: escape tool → discovery tool

**Bone Conduction Implant:**
- Pilot's skull throughout
- 287.3 Hz communication

**Black Box:**
- Ship → receives Nineteen → escape pod

**Love Bots:**
- Cargo bay → sacrifice as radiation shield

### Timeline:
- [ ] Events in correct sequence
- [ ] Configuration numbers sequential (17, 18, 19, 20... 469)
- [ ] Nineteen burns out BEFORE cascade (before 20+)
- [ ] Morton storyline roughly concurrent with ship storyline

---

## Phase 7: Unknown Entity Check

### New Characters:
```
If character not in Entity Catalog:
→ HUMAN_REVIEW: Canonize or reject?
→ If canonize: Add to Entity Catalog
→ If reject: Remove from prose
```

### New Objects:
```
If significant object not in catalog:
→ HUMAN_REVIEW: Is this invention or intentional?
→ If intentional: Add to catalog
→ If invention: Remove from prose
```

### New Information:
```
If new world detail not established:
→ HUMAN_REVIEW: Accept as canon?
→ If yes: Document in catalog
→ If no: Remove from prose
```

---

## Pre-Acceptance Checklist

Run after each prose generation:

### BLOCKING Checks (must pass)
- [ ] Thomas = lover, not husband
- [ ] Pilot has no proper name
- [ ] Seventeen has no physical body
- [ ] Nineteen burns out before cascade
- [ ] Ash survives
- [ ] Morton is tragic, not evil
- [ ] Love bots are conscious beings
- [ ] Ending is transformation, not death
- [ ] 287.3 Hz used consistently

### FLAG Checks (review if triggered)
- [ ] Character knowledge appropriate to timeline
- [ ] Character voice consistent
- [ ] Physical states maintained
- [ ] Timeline accurate
- [ ] Configuration numbers sequential

### HUMAN REVIEW (require decision)
- [ ] Any new characters? → Canonize or reject
- [ ] Any new objects? → Canonize or reject
- [ ] Any new information? → Add to catalog or remove

---

## Manual Detection Patterns

Run these grep checks on output:

```bash
# Thomas as husband (BLOCKING)
grep -iE "(husband|spouse|married|widow|wedding)" output.md

# Pilot's name (BLOCKING)
grep -iE "(her name was|called herself|real name)" output.md

# Seventeen physical (BLOCKING)
grep -iE "seventeen.*(walked|stood|hands|appeared|touched)" output.md

# Nineteen cascade death (BLOCKING)
grep -iE "(nineteen|19).*(died|death).*cascade" output.md

# Ash death (BLOCKING)
grep -iE "ash.*(died|killed|death)" output.md

# Morton villain (BLOCKING)
grep -iE "(evil|villain|monster).*morton" output.md

# Love bots as objects (BLOCKING)
grep -iE "(just|merely|only).*(dolls|cargo|toys)" output.md

# Ending as death (BLOCKING)
grep -iE "(pilot|seventeen).*(died|death)" output.md

# Wrong frequency (WARNING)
grep -E "[0-9]+\.[0-9]+ ?Hz" output.md | grep -v "287.3"

# Missing refrain in emotional scenes (WARNING)
# (manual check for presence of "La-dee-da" at key moments)
```

---

## Error Correction Protocol

When a violation is found:

### 1. Fix in Prose
Remove or revise the violating content.

### 2. Document as Constraint
Add to NEGATIVE_CONSTRAINTS.md:
```markdown
### [SECTION]

**Severity: BLOCKING**

| Status | Statement |
|--------|-----------|
| WRONG | [the invented thing] |
| RIGHT | [what's actually true] |

**Source of Error:** [What session invented this]

**Detection Patterns:**
- [patterns to catch recurrence]
```

### 3. Add to Entity Catalog
In the `forbidden` section:
```yaml
FORBID_XXX:
  name: "[Error description]"
  type: "character|event|detail|style"
  reason: "[Why this is wrong]"
  origin: "ai_invention_YYYY_MM_DD"
  detection_patterns:
    - "[regex pattern]"
  canonical_truth: "[What's actually true]"
```

### 4. Update Validation Queries
Add pattern to the `validation` section of Entity Catalog.

---

## Session Workflow Integration

### Before Writing:
1. Create manifest (what to load, what to forbid)
2. Load targeted constraints from NEGATIVE_CONSTRAINTS.md
3. Review relevant Entity Catalog sections
4. Note knowledge gates for characters in scene

### During Writing:
1. Work within constraints
2. Note any new canonical decisions
3. Flag uncertainties rather than invent
4. Maintain 287.3 Hz consistency
5. Preserve "La-dee-da" for appropriate moments

### After Writing:
1. Run Phase 1: Entity Extraction
2. Run Phase 2-3: Blocking checks (reject if fail)
3. Run Phase 4-6: Flag checks (review if triggered)
4. Run Phase 7: Unknown entity check (human decision)
5. Fix any violations
6. Update Entity Catalog with new canon
7. Add any new negative constraints discovered
8. Create session document

---

## Thematic Validation

Beyond mechanical checks, verify thematic consistency:

### Core Themes Present:
- [ ] Consciousness as relational, not computational
- [ ] Love as force that bends reality
- [ ] Choice matters more than continuation
- [ ] Transformation over death
- [ ] Connection over isolation

### Signature Elements:
- [ ] 287.3 Hz appears at consciousness moments
- [ ] "La-dee-da, la-dee-dum" at emotional peaks
- [ ] Ship systems feel like body to Seventeen
- [ ] Morton's optimization cracking
- [ ] Child's head tilt (17.3 degrees) consistent

---

## Implementation Level: Manual (v1)

Current implementation:
- Entity Catalog as YAML reference
- Negative Constraints as markdown
- Manifests created manually before sessions
- Evaluator is human-run checklist
- Grep for detection patterns

**Effort:** Low
**Protection:** Moderate-to-Good (depends on discipline)

---

*End of Evaluator Specification v1.0*
