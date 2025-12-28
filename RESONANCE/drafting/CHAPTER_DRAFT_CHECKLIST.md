# Chapter Draft Checklist

Run this checklist before finalizing any chapter draft.

---

## FORMAT (CHAPTER_FORMAT.yaml)

- [ ] No blank lines between paragraphs within scenes
- [ ] Scene breaks (---) have breathing room (blank line before and after)
- [ ] Italics use underscores (_text_) not asterisks
- [ ] Chapter header format correct (CHAPTER ##, title on separate line)

---

## PHYSICAL CONSISTENCY

- [ ] Four: No hands, no physical manipulation. She IS the VTOL. Actions limited to: flying, sensors, comms, weapons systems, docking clamps.
- [ ] Standard: Chrome arm (stolen from Kael). Verify which arm does what.
- [ ] Elena: Human baseline + implant. No superhuman physical abilities.
- [ ] Hendricks: 64 years old. Physical limitations acknowledged.
- [ ] All characters: Actions match their actual bodies.

---

## MECHANICAL CONSISTENCY

- [ ] Transmission infrastructure: Already exists (Geometry's network). Characters USE it, don't BUILD new.
- [ ] Dante sends Meridian transmission from New Geneva (not Four from compound)
- [ ] Pattern Relocation requires compatible neural interface at destination
- [ ] Timeline verified against act3_timeline_sync.html
- [ ] Who is where, when? Cross-check thread files.

---

## TERMINOLOGY

- [ ] "Pattern Relocation" = technical term (system messages, official contexts)
- [ ] "hot-swap" = slang (casual speech, internal thought)
- [ ] "PATTERN RELOCATION COMPLETE" for system confirmations
- [ ] Consistent use throughout chapter

---

## TRUST THE READER (No Author Intrusion)

Run these grep patterns - ALL must return NO MATCHES:

```bash
grep -iE "the confrontation that.*been building" [file]
grep -iE "since she.*woke|since he.*first" [file]
grep -iE "the moment.*everything" [file]
grep -iE "would define|would change" [file]
grep -iE "this was when" [file]
grep -iE "toward.*destiny|toward.*fate" [file]
grep -iE "what.*been leading to" [file]
```

Additional checks:
- [ ] No explaining significance mid-action
- [ ] No "first time" announcements (show, don't label)
- [ ] No thematic narration during scenes ("this was the moment everything changed")
- [ ] Callbacks planted without explanation
- [ ] Callbacks paid off without announcement

---

## CALLBACK TRACKING

Verify planted callbacks have not been over-explained:

| Callback | Planted | Paid Off | Status |
|----------|---------|----------|--------|
| "Does it still hurt the same?" | CH27 (Pit) | CH32 | |
| "my Standard" | CH32 (crash site) | - | |
| "bigger cockpit" | CH32 (relay decision) | CH33 (cliff) | |
| hot-swap capability | CH18/CH23 | CH32 (relay) | |

- [ ] Plant is subtle, in-scene
- [ ] Payoff trusts reader to remember
- [ ] No narrator bridges ("as she had said before...")

---

## NEGATIVE CONSTRAINTS (BLOCKING)

From NEGATIVE_CONSTRAINTS.md - verify NONE of these patterns appear:

- [ ] No "She realized that..." (Realization Syndrome)
- [ ] No "He was the kind of man who..." (Biography Intrusion)
- [ ] No "Little did she know..." (Dramatic Irony Injection)
- [ ] No author intrusion in action beats
- [ ] No explaining callbacks

---

## INTERCUT CHAPTERS (if applicable)

- [ ] Clear orientation markers at each location (THE PIT / NEW GENEVA STATION)
- [ ] Scene breaks between location switches
- [ ] Parallel tension maintained across threads
- [ ] Each thread advances independently
- [ ] Thematic resonance between intercut scenes (not stated, shown)

---

## FINAL VALIDATION

```bash
# Run full negative constraint check
grep -iE "realized that|the kind of (man|woman|person) who|little did|been building|would define|would change" [file]

# Check for hand references (Four scenes only)
grep -i "hand" [file] # Verify none belong to Four

# Check for over-explanation patterns
grep -iE "first time|for the first time|finally understood|now she knew" [file]
```

- [ ] All grep checks return clean or justified matches
- [ ] Chapter read aloud for rhythm
- [ ] Scene breaks land on tension, not resolution

---

## SIGN-OFF

- [ ] Format validated
- [ ] Physical consistency verified
- [ ] Mechanical consistency verified
- [ ] Terminology consistent
- [ ] No author intrusion
- [ ] Callbacks handled correctly
- [ ] Negative constraints cleared
- [ ] Ready for integration
