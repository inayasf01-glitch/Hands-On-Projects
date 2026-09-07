from pathlib import Path
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY was not found. Check your .env file."
    )

client = genai.Client(api_key=API_KEY)

MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
]


def analyze_architecture(file_path):
    proposal = Path(file_path).read_text(encoding="utf-8")

    prompt = f"""
You are assisting an enterprise architecture review team.

Analyze the following architecture change proposal.

Your role is advisory. Do not make a final approval decision.

Return exactly these four sections:

ARCHITECTURE SUMMARY
Provide a concise summary of the proposed change.

POTENTIAL RISKS
Identify potential technical, security, operational, integration, scalability,
or governance risks that an architect should consider. Do not invent facts.
If the proposal does not provide enough information to assess a risk, say so.

REVIEW QUESTIONS
Provide specific questions an enterprise architect should ask before approving
or implementing the change.

SUGGESTED REVIEW FOCUS
Identify the areas that deserve the most attention during human architecture
review.

Keep the analysis concise, specific, and grounded only in the proposal.

Architecture Change Proposal:
------------------------------
{proposal}
------------------------------
"""

    last_error = None

    for model in MODELS:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                return response.text

            except errors.APIError as error:
                last_error = error

                if error.code not in (429, 500, 502, 503, 504):
                    raise

                wait_time = 2 ** attempt
                print(
                    f"Temporary Gemini API error ({error.code}) "
                    f"using {model}. Retrying in {wait_time}s..."
                )

                time.sleep(wait_time)

    raise RuntimeError(
        f"Gemini analysis failed after retries. Last error: {last_error}"
    )


if __name__ == "__main__":
    result = analyze_architecture(
        "monitored_files/customer_platform_v2.txt"
    )

    print("\nAI-ASSISTED ARCHITECTURE REVIEW")
    print("--------------------------------")
    print(result)
