"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        # Criterion 1: at most 1 of 10 human texts labelled high-confidence AI.
        # ⚠️ These are stand-ins in a casual human voice. Swap in paragraphs you
        # actually wrote — this criterion is meaningless with someone else's prose.
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I've got the version in the picture that I read but my girlfriend got me a gorgeous hardback copy that I haven't touched.",
            "This book makes you question everything and look within. I have given it to people close to me along with a copy of The Prophet by Kahlil Gibran.",            
            "I love this book so much when we read it in French class that I bought a copy – but it’s been so many years and I really would need to brush up on my French to reread it 😂 It’s time!",
            "There is a problem with that statement. Dostoevsky is known (and you can see this in the books) for giving voice to a lot of different political and philosophical ideas through his characters. Assuming that he thinks A because one of his characters said A is not a sound way to asses his own voice.",
            "Like knowing the stars exist, even if they're not out one night. Great writer.",
            "I'm not sure why that makes it the most hopeful paragraphs in history. Surely there are more inclusive paragraphs written.",
            "Because the mere fact of you existing in spite of everything gives you hope that you are still able to change things for the better.",
            "Well, yeah, I imagine after surviving years of hard labor in Siberia a person might come out the other side quite resilient.",
            "If you would be tortured -let’s say you’re getting skinned by a cartel - most people would rather not exist tho",
            "It's from Brothers Karamazov, most likely written before, not in his last three months, as he didn't wrote the novel the night before publishing it. And it's not his voice, but Dimitri's."
        ],
    },
    {
        # Criterion 2: mean score of clearly-AI texts >= 0.20 above mean of the
        # human texts. The human side is the "my own writing" scenario above,
        # so compare its mean combined score against this one in the report.
        "name": "clearly AI text",
        "criterion": 2,
        "texts": [
            "In today's rapidly evolving digital landscape, it is essential to understand the multifaceted implications of artificial intelligence. Furthermore, organizations must leverage innovative solutions to foster sustainable growth. In conclusion, a holistic approach is paramount to navigating these challenges effectively.",
            "Time management is a crucial skill that plays a pivotal role in both personal and professional success. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can enhance their productivity. Moreover, effective time management contributes to reduced stress and improved well-being.",
            "Climate change represents one of the most pressing challenges of our time. It is important to note that its effects are far-reaching, impacting ecosystems, economies, and communities worldwide. Therefore, collaborative action across all sectors is imperative to ensure a sustainable future for generations to come.",
            "Effective communication is the cornerstone of any successful team. Delving into its key components, we can identify active listening, clarity, and empathy as essential elements. Additionally, fostering an environment of trust and transparency can significantly elevate collaboration and drive meaningful results.",
            "Regular exercise offers numerous benefits for both physical and mental health. First, it strengthens the cardiovascular system. Second, it improves mood by releasing endorphins. Third, it enhances sleep quality. Overall, incorporating exercise into one's daily routine is a valuable investment in long-term well-being.",
            "The advent of remote work has transformed the modern workplace in profound ways. On one hand, it offers flexibility and eliminates commuting. On the other hand, it presents challenges related to communication and work-life balance. Ultimately, organizations should adopt a balanced, adaptive strategy tailored to their unique needs.",
            "Cybersecurity is of paramount importance in the contemporary digital era. As threats continue to evolve, businesses must implement robust security measures, including multi-factor authentication, regular audits, and employee training. By taking a proactive stance, organizations can safeguard their valuable data and maintain stakeholder trust.",
            "Reading is a transformative activity that enriches the mind and broadens perspectives. Whether one engages with fiction or non-fiction, the benefits are manifold: improved vocabulary, enhanced empathy, and sharpened critical thinking. It is therefore advisable to cultivate a consistent reading habit.",
            "Renewable energy sources, such as solar and wind power, are playing an increasingly significant role in the global energy transition. These technologies offer a clean, sustainable alternative to fossil fuels. Moreover, continued innovation and investment will be instrumental in accelerating widespread adoption.",
            "Building a strong personal brand is vital in today's competitive job market. By showcasing expertise, maintaining a consistent online presence, and engaging authentically with a network, professionals can unlock new opportunities. In summary, a well-crafted personal brand serves as a powerful catalyst for career advancement.",
        ],
    },
    {
        # Criterion 3: every label (human / unsure / ai) reachable across the run.
        # Spread of inputs: clearly AI, clearly human, and genuinely borderline
        # (human-written but polished/formal, and AI-ish text with a personal edge).
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "In today's rapidly evolving digital landscape, it is essential to leverage innovative solutions. Furthermore, a holistic approach is paramount. In conclusion, organizations must foster sustainable growth through collaborative, forward-thinking strategies.",
            "ok so I totally forgot my umbrella AGAIN and got soaked lol. my shoes are still squelching. anyway the cafe was fine, the barista remembered my order which was weirdly nice",
            "The committee reviewed the proposal and concluded that the budget was reasonable, although several timelines required clarification. We recommend a follow-up meeting to address the outstanding concerns before approval is granted.",
            "I've always believed that learning a second language changes how you think. When I started Spanish, I was embarrassed constantly. Over time, though, I noticed that I became more patient with myself, and that patience carried over into other parts of my life.",
            "Moving to a new city can be both exciting and daunting. There are new streets to learn, new people to meet, and new routines to build. Still, I found that the small things, like a favorite coffee shop, made the place feel like home.",
        ],
    },
    # Criterion 4: appeals (5 appeals, each logged append-only with content ID,
    # creator ID, reasoning and under_review status).
    # NOT expressible here: an appeal needs a content_id returned by a prior
    # /submit, then a POST to the appeal endpoint, then a check of the audit log.
    # Tested by hand (or by extending run_eval.py) — state which in the write-up.
    {
        # Criterion 5: missing, empty, or overlong text -> client error, no
        # detector decision, rejection logged. Raw bodies, sent as written.
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
