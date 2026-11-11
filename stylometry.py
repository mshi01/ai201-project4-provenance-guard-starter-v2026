"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    stock_ai_word_rate       how often stock AI words ("furthermore", "crucial") appear
    first_person_rate        how often the writer says I / my / we

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

MAX_ANALYSIS_CHARS = 100_000


def _analysis_text(text: str) -> str:
    """Return a bounded string for the inexpensive style measures."""
    if not isinstance(text, str) or not text:
        return ""
    return text[:MAX_ANALYSIS_CHARS]


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    bounded_text = _analysis_text(text)
    lengths = [len(words(sentence)) for sentence in sentences(bounded_text)]
    lengths = [length for length in lengths if length > 0]
    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean_length if mean_length else 0.0


STOCK_AI_WORDS = frozenset("""
    furthermore moreover additionally therefore ultimately overall essential
    crucial pivotal paramount holistic leverage foster multifaceted landscape
    imperative significantly effectively sustainable innovative however
    important notably
""".split())

FIRST_PERSON_WORDS = frozenset({"i", "my", "me", "we", "our"})


def stock_ai_word_rate(text: str) -> float:
    """
    Stock AI words per 100 words. Higher means more AI-ish.

    Words like "furthermore", "crucial" and "holistic" are over-represented in
    generated prose. Blind spot: formal human writing uses them too, and
    swapping a few words defeats it.
    """
    tokens = words(_analysis_text(text))
    if not tokens:
        return 0.0
    return sum(t in STOCK_AI_WORDS for t in tokens) / len(tokens) * 100


def first_person_rate(text: str) -> float:
    """
    First-person words (I, my, me, we, our) per 100 words. Higher means more
    human — the style signal flips it.
    """
    tokens = words(_analysis_text(text))
    if not tokens:
        return 0.0
    return sum(t in FIRST_PERSON_WORDS for t in tokens) / len(tokens) * 100


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    bounded_text = _analysis_text(text)
    if not bounded_text:
        return 0.0

    spread = sentence_length_spread(bounded_text)
    stock = stock_ai_word_rate(bounded_text)
    first_person = first_person_rate(bounded_text)

    # Each component is scaled to 0-1, with higher values meaning more AI-like.
    # Reference rates (per 100 words) come from calibration on sample texts:
    # stock words ~0 for human vs ~6 for AI; first person ~4 vs ~0.5.
    low_spread = 1.0 / (1.0 + spread)
    stock_words = min(stock / 4.0, 1.0)
    no_first_person = 1.0 - min(first_person / 4.0, 1.0)

    return 0.2 * low_spread + 0.4 * stock_words + 0.4 * no_first_person


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"stock_ai_word_rate       {stock_ai_word_rate(text)}")
    print(f"first_person_rate        {first_person_rate(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
