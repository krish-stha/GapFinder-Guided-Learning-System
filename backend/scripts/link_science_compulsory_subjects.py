# -*- coding: utf-8 -*-
"""
Phase 1b (this session's platform-overhaul plan): after phase4_cleanup
stripped all synthetic filler from 91/38's compulsory subjects (English/
Compulsory English, नेपाली, सामाजिक अध्ययन / Social Studies), those subjects
are now empty and need real content. Rather than re-authoring from
scratch, this links the ALREADY-authored real content from 209/210 (see
scripts/content/grade{11,12}_{english,nepali,social_studies}.py) back into
91/38's matching chapters - the reverse direction of the earlier (now-
superseded) link_common_subjects.py, which tried to go 91/38 -> 209/210
before an audit found 91/38's source content was 100% synthetic junk.

Chapter-name comparison (live, 2026-08-09) found:
  - English: 91<->209 (42/42) and 38<->210 (37/37) match EXACTLY - pure
    exact-name linking via link_existing(), zero gaps.
  - नेपाली: 91<->209 12/13 match, 38<->210 11/14 match - a handful of
    91/38-only chapters (नेपाली व्याकरण, व्यावसायिक पत्र, Orientation and
    Feedback) have no 209/210 counterpart - link what matches, list the
    rest as needing fresh authoring.
  - सामाजिक अध्ययन / Social Studies: ZERO exact-name matches (91/38 use
    short topic names, 209/210 prefix "एकाइ N" unit numbers and often
    append an English translation) despite being the SAME curriculum
    topics - this is a genuine formatting difference, not a content
    difference. Per this script's design rule (never fuzzy-match live -
    only exact names, or a human-reviewed fixed table), the pairing below
    was built by a human reading both full chapter lists side by side
    (see scratchpad/social_studies_full.txt from this session) and is a
    FIXED, reviewed table - not computed by any string-similarity
    heuristic. Chapters left out of the table (Syllabus, Orientation and
    Feedback, and 1-2 genuinely unique topics) are reported as needing
    fresh authoring or are meta/administrative and may not need content.

Reuses chapters_under_subject / _link_chapter_questions from
link_common_subjects.py rather than reimplementing the same walk/upsert
logic.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal
from app import models
from scripts.link_common_subjects import chapters_under_subject, _link_chapter_questions, link_existing


# course_38 Social Studies chapter_id -> course_210 सामाजिक... chapter_id
# and course_91 सामाजिक अध्ययन chapter_id -> course_209 सामाजिक... chapter_id.
# Human-reviewed 2026-08-09 (see module docstring). Chapters not listed
# here have no confident pairing and are left for fresh authoring.
SOCIAL_STUDIES_91_TO_209 = {
    24065: 35081,  # अर्थ्तन्त्र विकास <-> एकाइ १०: अर्थतन्त्र र विकास
    24058: 35075,  # जीवनोपयोगी सीप <-> एकाइ: ३ जीवनोपयोगी सीप
    24064: 35079,  # बस्ती, जनसङ्ख्या र विकास <-> एकाइ ९ (same phrase)
    24060: 35065,  # भूगोल र सामाजिक सम्बन्ध <-> एकाइ ५ (same phrase + EN suffix)
    24061: 35063,  # विश्वको इतिहास <-> एकाइ ६ (same phrase)
    24063: 35073,  # संविधान र नागरिक चेतना <-> एकाइ ८ ...सचेतना (spelling variant)
    24056: 34915,  # समजिक अध्ययन तथा जीवनोपयोगी शिक्षाको अवधारणा <-> एकाइ १ (typo: समजिक->सामाजिक)
    24062: 35071,  # सामाजिक पहिचान र विविधता र वर्ग विभाजन <-> एकाइ ७ (same phrase, comma)
    24066: 35077,  # स्वास्थ सेवा र समाजिक विकास <-> एकाइ ११ ...स्वास्थ्य... (spelling variant)
}
SOCIAL_STUDIES_38_TO_210 = {
    18844: 34699,  # एकाइ १ (already exact-name-equal, included for completeness)
    18855: 34744,  # एकाइ १० (exact)
    18856: 34742,  # एकाइ ११ (EN suffix + spacing only)
    18845: 34704,  # एकाइ २ (spelling variants + EN suffix)
    18847: 34706,  # एकाइ ३ (exact)
    18848: 34720,  # एकाइ ४ (exact)
    18850: 34736,  # एकाइ ५ (exact)
    18851: 34738,  # एकाइ ६ (exact)
    18852: 34734,  # एकाइ ७ (विभिधता typo -> विविधता + EN suffix)
    18853: 34702,  # एकाइ ८ (चेतना -> सचेतना + EN suffix)
    18854: 34740,  # एकाइ ९ (exact)
}


def link_by_explicit_pairs(target_to_source: dict) -> dict:
    db = SessionLocal()
    linked = {}
    for target_id, source_id in target_to_source.items():
        target = db.get(models.Section, target_id)
        source = db.get(models.Section, source_id)
        n_new, n_total = _link_chapter_questions(db, source_id, target_id)
        linked[f"{target_id} ({target.name})"] = {
            "source_chapter_id": source_id, "source_name": source.name,
            "questions_linked_new": n_new, "questions_available": n_total,
        }
    db.commit()
    db.close()
    return {"linked": linked, "chapters_linked": len(linked)}


if __name__ == "__main__":
    results = {}

    # English: exact-name match, zero gaps expected
    results["91_english_link"] = link_existing(target_subject_id=35113, source_subject_id=37491)  # 91 Compulsory English <- 209 English
    results["38_english_link"] = link_existing(target_subject_id=18072, source_subject_id=37534)   # 38 English <- 210 English

    # नेपाली: exact-name match for most chapters
    results["91_nepali_link"] = link_existing(target_subject_id=23982, source_subject_id=34310)    # 91 नेपाली <- 209 नेपाली
    results["38_nepali_link"] = link_existing(target_subject_id=11494, source_subject_id=34298)     # 38 नेपाली <- 210 नेपाली

    # सामाजिक अध्ययन / Social Studies: human-reviewed explicit pairing
    results["91_social_studies_link"] = link_by_explicit_pairs(SOCIAL_STUDIES_91_TO_209)
    results["38_social_studies_link"] = link_by_explicit_pairs(SOCIAL_STUDIES_38_TO_210)

    print(json.dumps(results, indent=2, ensure_ascii=False, default=str))

    report_path = Path(__file__).parent / "reports" / "phase1b_link_compulsory.json"
    report_path.write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"\nSaved to {report_path}")
