# AI-Powered SEO Content Production — Research Project

> A curated research collection of expert insights on AI-powered SEO content production for B2B SaaS, gathered from 10 industry practitioners who build, test, and operate AI SEO systems.

---

## Topic

**AI-Powered SEO Content Production** — How B2B SaaS companies can leverage AI tools, workflows, and strategies to produce SEO-optimized content at scale while maintaining quality, authority, and visibility in both traditional search and AI-powered answer engines.

## Why This Topic

AI-powered SEO content production sits at the intersection of the biggest shifts in digital marketing:

1. **The rise of AI answer engines** (Google AI Overviews, ChatGPT, Perplexity) is fundamentally changing how content is discovered and consumed
2. **B2B SaaS companies** need to produce high volumes of targeted content (comparison pages, integration pages, feature pages, educational content) but often lack the resources to do it manually
3. **The quality bar is rising** — as AI makes commodity content trivially easy to produce, only expert-driven, data-backed, and genuinely valuable content will rank and be cited

This is arguably the most consequential topic in B2B marketing right now, and the gap between practitioners who understand it and those who don't is widening rapidly.

## The 10 Experts

These experts were chosen because they **practice what they teach** — they build tools, run agencies, advise major companies, and publicly share real results:

| # | Expert | Role | Why Selected |
|---|--------|------|-------------|
| 1 | **Kevin Indig** | Growth Advisor (ex-Shopify, Atlassian, G2) | Advises Reddit, Ramp, Snap on organic growth. Publishes *Growth Memo*. |
| 2 | **Jake Ward** | Founder of Byword & Contact Studios | Created the "AI SEO Heist." Builds and operates AI content tools. |
| 3 | **Ross Hudgens** | CEO of Siege Media | Runs a top content agency. Publishes data-driven AI visibility research. |
| 4 | **Eli Schwartz** | Author of *Product-Led SEO* | Former Head of SEO at SurveyMonkey. Contrarian strategic voice. |
| 5 | **Lily Ray** | VP of SEO Strategy at Amsive | Top authority on E-E-A-T, content quality, and algorithm updates. |
| 6 | **Matt Diggity** | Founder of Diggity Marketing | Known for rigorous "test everything" methodology. Evidence-based AI SEO. |
| 7 | **Julia McCoy** | AI marketing consultant (First Movers) | Built and exited a 100-person agency, then pivoted to AI content production. |
| 8 | **Bernard Huang** | Co-founder & CEO of Clearscope | Builds leading AI content optimization platform. Pioneered AEO methodology. |
| 9 | **Cyrus Shepard** | Founder of Zyppy SEO (ex-Moz) | Evidence-based tester. Former Google Quality Rater. |
| 10 | **Koray Tugberk Gubur** | Founder of Holistic SEO & Digital | Leading authority on topical authority and semantic SEO frameworks. |

See [`/research/sources.md`](research/sources.md) for detailed profiles, links, and annotations.

## What Was Collected

### YouTube Transcripts (10 videos)
Full transcripts collected via the `youtube-transcript-api` Python library (no API key required). Each transcript is from a recent (2024-2026) video featuring the expert discussing AI SEO.

📁 [`/research/youtube-transcripts/`](research/youtube-transcripts/)

| Expert | Video Title |
|--------|-------------|
| Matt Diggity | I did AI-SEO for ChatGPT and Google AI. Here's what happened |
| Ross Hudgens | AI Visibility, Data Journalism, and the Future of SEO |
| Julia McCoy | SEO with AI in 2025: The Complete Automation Manual |
| Bernard Huang | How Answer Engine Optimization (AEO) Works + AEO Playbook |
| Eli Schwartz | Product-Led SEO Still Works For AI Search |
| Cyrus Shepard | Agents are early, visibility is urgent: 2025 AI SEO |
| Jake Ward | Jake Ward Viral SEO Strategy - The SEO Heist - AMA |
| Lily Ray | Lily Ray Reveals SEO Truths in 2026: What Works Now |
| Kevin Indig | SEO in the Age of AI - Google Overviews, E-Commerce & The Future of Search |
| Koray Tugberk Gubur | Topical Authority With Koray Tugberk GUBUR |

### LinkedIn Posts (10 expert collections)
Synthesized from publicly shared LinkedIn content themes for each expert. Posts were collected via web search of their public content, organized by key themes.

📁 [`/research/linkedin-posts/`](research/linkedin-posts/)

### Other Materials
- **Cross-Expert Theme Analysis** — 8 dominant themes that emerged across all experts
- **Recommended Tools & Tech Stack** — Tools used/recommended by the experts

📁 [`/research/other/`](research/other/)

## Repository Structure

```
ai-seo-research/
├── README.md                          # This file
├── fetch_transcripts.py               # Script used to fetch YouTube transcripts
├── research/
│   ├── sources.md                     # All 10 experts with profiles and annotations
│   ├── linkedin-posts/                # LinkedIn posts organized by author
│   │   ├── kevin-indig.md
│   │   ├── jake-ward.md
│   │   ├── ross-hudgens.md
│   │   ├── eli-schwartz.md
│   │   ├── lily-ray.md
│   │   ├── matt-diggity.md
│   │   ├── julia-mccoy.md
│   │   ├── bernard-huang.md
│   │   ├── cyrus-shepard.md
│   │   └── koray-tugberk-gubur.md
│   ├── youtube-transcripts/           # Full transcripts organized by video
│   │   ├── matt-diggity-ai-seo-chatgpt-google.md
│   │   ├── ross-hudgens-ai-visibility-future-seo.md
│   │   ├── julia-mccoy-seo-ai-automation.md
│   │   ├── bernard-huang-aeo-playbook.md
│   │   ├── eli-schwartz-product-led-seo-ai.md
│   │   ├── cyrus-shepard-visibility-ai-seo.md
│   │   ├── jake-ward-seo-heist-ama.md
│   │   ├── lily-ray-seo-truths-2026.md
│   │   ├── kevin-indig-seo-age-of-ai.md
│   │   └── koray-tugberk-topical-authority.md
│   └── other/                         # Additional research materials
│       ├── cross-expert-themes.md
│       └── recommended-tools.md
```

## Collection Methods

| Content Type | Method | Tool/API |
|-------------|--------|----------|
| YouTube Transcripts | `youtube-transcript-api` Python library | No API key required — fetches from YouTube's internal endpoints |
| LinkedIn Posts | Web search synthesis | Collected via search of publicly shared content themes |
| Cross-Expert Analysis | Manual synthesis | Extracted from all collected materials |

## Key Findings Preview

The 8 dominant themes across all experts (see [`cross-expert-themes.md`](research/other/cross-expert-themes.md)):

1. **Traffic → Visibility & Citations** — New KPIs for AI search
2. **E-E-A-T as the Moat** — Human expertise differentiates in an AI world
3. **AEO + SEO = Both** — Layer GEO on traditional SEO, don't replace it
4. **Topical Authority** — Systematic coverage beats individual pages
5. **BOFU Content Resilience** — Bottom-of-funnel content survives AI disruption
6. **Programmatic Content = Product Thinking** — Value per page, not volume
7. **Brand as SEO** — Brand recognition is now a ranking factor
8. **Community Platforms Matter** — Reddit and YouTube feed AI models

## Next Steps

This research provides the raw material for building a comprehensive **AI-Powered SEO Content Production Playbook** for B2B SaaS companies. The collected transcripts, posts, and theme analysis contain enough high-signal content to develop:

- Step-by-step workflow guides
- Content production SOPs with AI integration
- Measurement frameworks for AI visibility
- Topical authority mapping methodologies
- Quality control checklists for AI content
