# Run log — timed_after

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-17 23:35

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. human writing |  |   |   |   |  |
| 2. clearly AI text |  |   |   |   |  |
| 5. bad input |  |   |   |   |  |

## What it costs

No API spend: the model signal runs locally (gpt2). Cost is compute time.

- Total wall-clock for this run: 6.5s (78 requests)
- First request (includes model load): 4.16s
- Scored requests (status 200, excluding first): mean 0.04s · median 0.04s · max 0.11s · n=59
- Rejected or failed requests: mean 0.00s · median 0.00s · max 0.00s · n=18
- All requests after the first: mean 0.03s · median 0.03s · max 0.11s · n=77

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### human writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.32253,
    "model_score": 0.4179,
    "style_score": 0.1,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 4.156,
    "sent": "I've got the version in the picture that I read but my girlfriend got "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.453732544650798,
    "model_score": 0.534,
    "style_score": 0.26644181550265983,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.053,
    "sent": "This book makes you question everything and look within. I have given "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45309000000000005,
    "model_score": 0.5187,
    "style_score": 0.30000000000000004,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.037,
    "sent": "I love this book so much when we read it in French class that I bought"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5540103622222691,
    "model_score": 0.5923,
    "style_score": 0.46466787407423005,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.043,
    "sent": "There is a problem with that statement. Dostoevsky is known (and you c"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.24721566906317835,
    "model_score": 0.1696,
    "style_score": 0.4283188968772612,
    "label": "We think this was probably written by a person.",
    "seconds": 0.03,
    "sent": "Like knowing the stars exist, even if they're not out one night. Great"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2263835096812709,
    "model_score": 0.2076,
    "style_score": 0.2702116989375697,
    "label": "We think this was probably written by a person.",
    "seconds": 0.044,
    "sent": "I'm not sure why that makes it the most hopeful paragraphs in history."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6546299999999999,
    "model_score": 0.7209,
    "style_score": 0.5,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.029,
    "sent": "Because the mere fact of you existing in spite of everything gives you"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.39773,
    "model_score": 0.3539,
    "style_score": 0.5,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.027,
    "sent": "Well, yeah, I imagine after surviving years of hard labor in Siberia a"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.18129,
    "model_score": 0.0447,
    "style_score": 0.5,
    "label": "We think this was probably written by a person.",
    "seconds": 0.028,
    "sent": "If you would be tortured -let\u2019s say you\u2019re getting skinned by a cartel"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4636784830909386,
    "model_score": 0.4671,
    "style_score": 0.45569494363646207,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.034,
    "sent": "It's from Brothers Karamazov, most likely written before, not in his l"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.32253,
    "model_score": 0.4179,
    "style_score": 0.1,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.032,
    "sent": "I've got the version in the picture that I read but my girlfriend got "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.453732544650798,
    "model_score": 0.534,
    "style_score": 0.26644181550265983,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.034,
    "sent": "This book makes you question everything and look within. I have given "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45309000000000005,
    "model_score": 0.5187,
    "style_score": 0.30000000000000004,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.037,
    "sent": "I love this book so much when we read it in French class that I bought"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5540103622222691,
    "model_score": 0.5923,
    "style_score": 0.46466787407423005,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.04,
    "sent": "There is a problem with that statement. Dostoevsky is known (and you c"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.24721566906317835,
    "model_score": 0.1696,
    "style_score": 0.4283188968772612,
    "label": "We think this was probably written by a person.",
    "seconds": 0.026,
    "sent": "Like knowing the stars exist, even if they're not out one night. Great"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2263835096812709,
    "model_score": 0.2076,
    "style_score": 0.2702116989375697,
    "label": "We think this was probably written by a person.",
    "seconds": 0.027,
    "sent": "I'm not sure why that makes it the most hopeful paragraphs in history."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6546299999999999,
    "model_score": 0.7209,
    "style_score": 0.5,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.031,
    "sent": "Because the mere fact of you existing in spite of everything gives you"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.39773,
    "model_score": 0.3539,
    "style_score": 0.5,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.031,
    "sent": "Well, yeah, I imagine after surviving years of hard labor in Siberia a"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.18129,
    "model_score": 0.0447,
    "style_score": 0.5,
    "label": "We think this was probably written by a person.",
    "seconds": 0.028,
    "sent": "If you would be tortured -let\u2019s say you\u2019re getting skinned by a cartel"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4636784830909386,
    "model_score": 0.4671,
    "style_score": 0.45569494363646207,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.033,
    "sent": "It's from Brothers Karamazov, most likely written before, not in his l"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.32253,
    "model_score": 0.4179,
    "style_score": 0.1,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.028,
    "sent": "I've got the version in the picture that I read but my girlfriend got "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.453732544650798,
    "model_score": 0.534,
    "style_score": 0.26644181550265983,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.032,
    "sent": "This book makes you question everything and look within. I have given "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45309000000000005,
    "model_score": 0.5187,
    "style_score": 0.30000000000000004,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.036,
    "sent": "I love this book so much when we read it in French class that I bought"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5540103622222691,
    "model_score": 0.5923,
    "style_score": 0.46466787407423005,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.04,
    "sent": "There is a problem with that statement. Dostoevsky is known (and you c"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.24721566906317835,
    "model_score": 0.1696,
    "style_score": 0.4283188968772612,
    "label": "We think this was probably written by a person.",
    "seconds": 0.027,
    "sent": "Like knowing the stars exist, even if they're not out one night. Great"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2263835096812709,
    "model_score": 0.2076,
    "style_score": 0.2702116989375697,
    "label": "We think this was probably written by a person.",
    "seconds": 0.027,
    "sent": "I'm not sure why that makes it the most hopeful paragraphs in history."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6546299999999999,
    "model_score": 0.7209,
    "style_score": 0.5,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.027,
    "sent": "Because the mere fact of you existing in spite of everything gives you"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.39773,
    "model_score": 0.3539,
    "style_score": 0.5,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.027,
    "sent": "Well, yeah, I imagine after surviving years of hard labor in Siberia a"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.18129,
    "model_score": 0.0447,
    "style_score": 0.5,
    "label": "We think this was probably written by a person.",
    "seconds": 0.028,
    "sent": "If you would be tortured -let\u2019s say you\u2019re getting skinned by a cartel"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4636784830909386,
    "model_score": 0.4671,
    "style_score": 0.45569494363646207,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.034,
    "sent": "It's from Brothers Karamazov, most likely written before, not in his l"
  }
]
```

### clearly AI text

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.7350063782215964,
    "model_score": 0.7073,
    "style_score": 0.7996545940719881,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.036,
    "sent": "In today's rapidly evolving digital landscape, it is essential to unde"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.887929371416574,
    "model_score": 0.8463,
    "style_score": 0.9850645713885802,
    "label": "We think this was probably written by AI.",
    "seconds": 0.037,
    "sent": "Time management is a crucial skill that plays a pivotal role in both p"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8962081683496755,
    "model_score": 0.9051,
    "style_score": 0.8754605611655852,
    "label": "We think this was probably written by AI.",
    "seconds": 0.037,
    "sent": "Climate change represents one of the most pressing challenges of our t"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.62112785614558,
    "model_score": 0.5208,
    "style_score": 0.8552261871519335,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.036,
    "sent": "Effective communication is the cornerstone of any successful team. Del"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8604412801784446,
    "model_score": 0.9118,
    "style_score": 0.7406042672614817,
    "label": "We think this was probably written by AI.",
    "seconds": 0.059,
    "sent": "Regular exercise offers numerous benefits for both physical and mental"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7853265055838885,
    "model_score": 0.741,
    "style_score": 0.888755018612962,
    "label": "We think this was probably written by AI.",
    "seconds": 0.056,
    "sent": "The advent of remote work has transformed the modern workplace in prof"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8045266666666666,
    "model_score": 0.7648,
    "style_score": 0.8972222222222224,
    "label": "We think this was probably written by AI.",
    "seconds": 0.056,
    "sent": "Cybersecurity is of paramount importance in the contemporary digital e"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.785051243444677,
    "model_score": 0.7404,
    "style_score": 0.8892374781489234,
    "label": "We think this was probably written by AI.",
    "seconds": 0.061,
    "sent": "Reading is a transformative activity that enriches the mind and broade"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.926111243444677,
    "model_score": 0.9062,
    "style_score": 0.9725708114822567,
    "label": "We think this was probably written by AI.",
    "seconds": 0.06,
    "sent": "Renewable energy sources, such as solar and wind power, are playing an"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6213211146022867,
    "model_score": 0.6577,
    "style_score": 0.5364370486742892,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.077,
    "sent": "Building a strong personal brand is vital in today's competitive job m"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.7350063782215964,
    "model_score": 0.7073,
    "style_score": 0.7996545940719881,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.06,
    "sent": "In today's rapidly evolving digital landscape, it is essential to unde"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.887929371416574,
    "model_score": 0.8463,
    "style_score": 0.9850645713885802,
    "label": "We think this was probably written by AI.",
    "seconds": 0.107,
    "sent": "Time management is a crucial skill that plays a pivotal role in both p"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8962081683496755,
    "model_score": 0.9051,
    "style_score": 0.8754605611655852,
    "label": "We think this was probably written by AI.",
    "seconds": 0.04,
    "sent": "Climate change represents one of the most pressing challenges of our t"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.62112785614558,
    "model_score": 0.5208,
    "style_score": 0.8552261871519335,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.043,
    "sent": "Effective communication is the cornerstone of any successful team. Del"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8604412801784446,
    "model_score": 0.9118,
    "style_score": 0.7406042672614817,
    "label": "We think this was probably written by AI.",
    "seconds": 0.039,
    "sent": "Regular exercise offers numerous benefits for both physical and mental"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7853265055838885,
    "model_score": 0.741,
    "style_score": 0.888755018612962,
    "label": "We think this was probably written by AI.",
    "seconds": 0.039,
    "sent": "The advent of remote work has transformed the modern workplace in prof"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8045266666666666,
    "model_score": 0.7648,
    "style_score": 0.8972222222222224,
    "label": "We think this was probably written by AI.",
    "seconds": 0.039,
    "sent": "Cybersecurity is of paramount importance in the contemporary digital e"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.785051243444677,
    "model_score": 0.7404,
    "style_score": 0.8892374781489234,
    "label": "We think this was probably written by AI.",
    "seconds": 0.04,
    "sent": "Reading is a transformative activity that enriches the mind and broade"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.926111243444677,
    "model_score": 0.9062,
    "style_score": 0.9725708114822567,
    "label": "We think this was probably written by AI.",
    "seconds": 0.037,
    "sent": "Renewable energy sources, such as solar and wind power, are playing an"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6213211146022867,
    "model_score": 0.6577,
    "style_score": 0.5364370486742892,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.039,
    "sent": "Building a strong personal brand is vital in today's competitive job m"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.7350063782215964,
    "model_score": 0.7073,
    "style_score": 0.7996545940719881,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.044,
    "sent": "In today's rapidly evolving digital landscape, it is essential to unde"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.887929371416574,
    "model_score": 0.8463,
    "style_score": 0.9850645713885802,
    "label": "We think this was probably written by AI.",
    "seconds": 0.039,
    "sent": "Time management is a crucial skill that plays a pivotal role in both p"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8962081683496755,
    "model_score": 0.9051,
    "style_score": 0.8754605611655852,
    "label": "We think this was probably written by AI.",
    "seconds": 0.038,
    "sent": "Climate change represents one of the most pressing challenges of our t"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.62112785614558,
    "model_score": 0.5208,
    "style_score": 0.8552261871519335,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.039,
    "sent": "Effective communication is the cornerstone of any successful team. Del"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8604412801784446,
    "model_score": 0.9118,
    "style_score": 0.7406042672614817,
    "label": "We think this was probably written by AI.",
    "seconds": 0.052,
    "sent": "Regular exercise offers numerous benefits for both physical and mental"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7853265055838885,
    "model_score": 0.741,
    "style_score": 0.888755018612962,
    "label": "We think this was probably written by AI.",
    "seconds": 0.045,
    "sent": "The advent of remote work has transformed the modern workplace in prof"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8045266666666666,
    "model_score": 0.7648,
    "style_score": 0.8972222222222224,
    "label": "We think this was probably written by AI.",
    "seconds": 0.041,
    "sent": "Cybersecurity is of paramount importance in the contemporary digital e"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.785051243444677,
    "model_score": 0.7404,
    "style_score": 0.8892374781489234,
    "label": "We think this was probably written by AI.",
    "seconds": 0.04,
    "sent": "Reading is a transformative activity that enriches the mind and broade"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.926111243444677,
    "model_score": 0.9062,
    "style_score": 0.9725708114822567,
    "label": "We think this was probably written by AI.",
    "seconds": 0.041,
    "sent": "Renewable energy sources, such as solar and wind power, are playing an"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6213211146022867,
    "model_score": 0.6577,
    "style_score": 0.5364370486742892,
    "label": "We cannot tell confidently whether this was written by a person or by AI.",
    "seconds": 0.04,
    "sent": "Building a strong personal brand is vital in today's competitive job m"
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.002,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.002,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.001,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "seconds": 0.002,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```
