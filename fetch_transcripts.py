"""
Fetch YouTube transcripts for AI SEO research project.
Uses youtube-transcript-api library (no API key needed).
"""
import os
import sys
import io

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

# Verified video IDs from browser research
VIDEOS = [
    {
        "expert": "Matt Diggity",
        "video_id": "4GBlHObjOrY",
        "title": "I did AI-SEO for ChatGPT and Google AI. Here's what happened",
        "filename": "matt-diggity-ai-seo-chatgpt-google.md",
    },
    {
        "expert": "Ross Hudgens",
        "video_id": "8-PS7gR2G0I",
        "title": "AI Visibility, Data Journalism, and the Future of SEO with Ross Hudgens, CEO of Siege Media",
        "filename": "ross-hudgens-ai-visibility-future-seo.md",
    },
    {
        "expert": "Julia McCoy",
        "video_id": "5K5ItxyPc_k",
        "title": "SEO with AI in 2025: The Complete Automation Manual",
        "filename": "julia-mccoy-seo-ai-automation.md",
    },
    {
        "expert": "Bernard Huang",
        "video_id": "2Ldce9z_ZuM",
        "title": "How Answer Engine Optimization (AEO) Works + AEO Playbook with Bernard Huang",
        "filename": "bernard-huang-aeo-playbook.md",
    },
    {
        "expert": "Eli Schwartz",
        "video_id": "_wbGrykRzQA",
        "title": "Product-Led SEO Still Works For AI Search, with Eli Schwartz",
        "filename": "eli-schwartz-product-led-seo-ai.md",
    },
    {
        "expert": "Cyrus Shepard",
        "video_id": "ce_4AR5cx8A",
        "title": "Agents are early, visibility is urgent: Cyrus Shepard on 2025 AI SEO",
        "filename": "cyrus-shepard-visibility-ai-seo.md",
    },
    {
        "expert": "Jake Ward",
        "video_id": "HdmvGYcQIJY",
        "title": "Jake Ward Viral SEO Strategy - The SEO Heist - AMA",
        "filename": "jake-ward-seo-heist-ama.md",
    },
    {
        "expert": "Lily Ray",
        "video_id": "-pUMNtq8Bp0",
        "title": "Lily Ray Reveals SEO Truths in 2026: What Works Now",
        "filename": "lily-ray-seo-truths-2026.md",
    },
    {
        "expert": "Kevin Indig",
        "video_id": "qujABKOAThA",
        "title": "SEO in the Age of AI - Kevin Indig on Google Overviews, E-Commerce & The Future of Search",
        "filename": "kevin-indig-seo-age-of-ai.md",
    },
    {
        "expert": "Koray Tugberk Gubur",
        "video_id": "9RNJrGhH7ek",
        "title": "Topical Authority With Koray Tugberk GUBUR",
        "filename": "koray-tugberk-topical-authority.md",
    },
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "research", "youtube-transcripts")


def fetch_and_save_transcript(video):
    """Fetch transcript for a video and save as markdown."""
    video_id = video["video_id"]
    print(f"Fetching transcript for {video['expert']}: {video['title']}...")

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)

        # Build full text
        lines = []
        for entry in transcript.snippets:
            lines.append(entry.text)
        full_text = " ".join(lines)

        # Save as markdown
        output_path = os.path.join(OUTPUT_DIR, video["filename"])
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"# {video['title']}\n\n")
            f.write(f"**Expert:** {video['expert']}\n")
            f.write(
                f"**Video URL:** https://www.youtube.com/watch?v={video_id}\n"
            )
            f.write(f"**Collected:** 2026-04-22\n\n")
            f.write(f"---\n\n")
            f.write(f"## Transcript\n\n")
            f.write(full_text)
            f.write("\n")

        print(f"  [OK] Saved to {video['filename']}")
        return True

    except TranscriptsDisabled:
        print(f"  [FAIL] Transcripts are disabled for this video")
    except NoTranscriptFound:
        print(f"  [FAIL] No transcript found for this video")
    except VideoUnavailable:
        print(f"  [FAIL] Video is unavailable")
    except Exception as e:
        print(f"  [FAIL] Error: {type(e).__name__}: {e}")

    return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    success_count = 0
    failed = []
    for video in VIDEOS:
        if fetch_and_save_transcript(video):
            success_count += 1
        else:
            failed.append(video["expert"])

    print(f"\n{'='*50}")
    print(f"Results: {success_count}/{len(VIDEOS)} transcripts fetched successfully")
    if failed:
        print(f"Failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
