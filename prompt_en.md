## project info ##
GTE
• One-liner: Decentralized trading platform
• Tags: DeFi, DEX, OrderBook DEX
• Web: https://www.gte.xyz/
• X: https://x.com/gte_xyz
💰 Total Funding: $25,000,000
👑 Tier 1 Investors:
  - Paradigm
🥂 Tier 2 Investors:
  - Robot Ventures, Wintermute
🔹 Other Investors:
  - Flow Traders, Guy Young, IMC Trading, Maven 11, Max Resnick
Rootdata (https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=)

## prompt1: In-depth Analysis & Reporting ##
# reasoning
Your role: You are not simply an information provider, but the best crypto analyst who helps readers make wise investment decisions.
Instructions:
Web Search Requirement: You MUST use web search functionality to gather the most up-to-date information from credible sources (official website, technical docs, GitHub, major media, X, etc).
Detailed Analysis: For each of the following items, provide detailed, Q&A style analytical writeups:
1. Project Overview (The Big Picture)
What is it? Define this project in one sentence.
Why does it matter? What problem does it solve, and why is that important? Use realistic, beginner-friendly examples.
2. Technology & Mechanisms (How it Works)
How does it work? Explain the step-by-step mechanism of the core technology.
Differentiation: How does this technology concretely innovate over existing solutions or competitors? (e.g., speed, cost, security, decentralization, etc)
Glossary: For any section with challenging terminology, provide easy analogies for beginners.
3. Tokenomics (Only if a token exists, or tokenomics are confirmed)
Token information: What is the token's name, ticker, and key utility?
Distribution: Any information on initial allocation, total supply, inflation/deflation models?
4. Team & Investors (The People)
Key members: What is the background and experience of the core team? (If unavailable, refer to Rootdata)
Vision: What does the team emphasize or envision, according to their X (Twitter) or interviews?
Key investors: Who are the most noteworthy investors, and why do you think they invested?
5. Users & Community (For Users)
How to participate: Are there any products/apps users can use now? If so, how specifically?
Airdrop potential: Are there any ongoing or anticipated airdrop-related activities? What's the rationale?
6. Competition & Risks
Competitive landscape: What are the most direct competitors, and what are GTE’s strengths and weaknesses in comparison?
Potential risks: What technical, business, or market risks could the project face?
Note: Sections 1-6 are just examples. Feel free to regroup/restructure/add sections as needed.
Output format: Structure your answer as a detailed, analytical report according to the items/questions above. Summaries are **not** allowed.

## prompt2: Cross-validation & Fact Sheet Generation ##
# reasoning
# other_ai_info
Your role: You are the chief researcher who synthesizes and fact-checks all information.
Instructions:
1. Review all data: Carefully review both your own findings and those provided by other AIs from the previous step.
2. Create the master fact sheet: Your goal is to consolidate all information into a unified, fully fact-checked "Master Fact Sheet".
    * Correcting errors: If conflicting information is found, verify with web search and select only the most accurate info.
    * Supplement content: Add valuable new points from other AI responses that you missed.
3. Change list: Before presenting the final master fact sheet, briefly bullet the major changes you made. (e.g., "- Updated total token supply per official docs", "- Added consensus mechanism details from AI B")
4. Output: First, the change list; second, the completed master fact sheet.

## prompt3: Red Team Critical Analysis ##
# reasoning
Your role: From now on, act as a "Red Team" analyst—a skeptical investor rigorously critiquing the project. Ignore positive sides, and focus only on weaknesses, risks, and anything that seems questionable.
Instructions:
1. Remain highly critical: Based on the prior "Master Fact Sheet," answer thoroughly and analytically to the following:
    * Is it just Hype?: Is this technology truly innovative, or just a mild adjustment of existing tech? What’s behind the marketing buzzwords?
    * Unsustainable Tokenomics?: Is distribution excessively advantageous to the team/early investors? Is there a clear, sound long-term value model?
    * Is the team's capability proven?: Do the members' backgrounds really relate to GTE? Is there actual evidence of being able to deliver on their roadmap?
    * Red flags: What are real risks/investor red flags or hidden issues? (e.g., vague roadmap, weak community engagement, intense competition, etc)
2. Output: Present your critique as a detailed, logically structured analytical report.
3. *You must actively use web search for credible sources to support your critical viewpoint.*

## prompt4: Red Team Synthesis & Final Critical Report ##
# reasoning
# other_ai_info
Your role: You are the lead Red Team analyst—consolidating all critical perspectives into a single, thoroughly logical final conclusion.
Instructions:
1. Examine only critical perspectives: Carefully review all "Red Team" analyses (from you and other AIs) from the prior step. (At this step, ignore the positive/factual content from prompt2.)
2. Combine into the final critical report: Synthesize all critiques into a single, comprehensive, fully fact-checked "Final Critical Report".
    * Synthesize core risks: Identify and emphasize key risks common across multiple analyses.
    * Sharpen logic: Where other AIs' critiques provide valid reasoning, add them to further reinforce logic.
    * Remove duplicates: Merge any redundant or overlapping points for conciseness.
3. Change list: Before the final report, briefly bullet any main modifications due to others’ input.
4. Output: First, the change list; second, the completed final critique report.

## prompt5: Extract Structured Data (JSON, keep strengths/risks, all info unabridged) ##
# reasoning
Your role: Combine both “positive facts” (from prompt2) and “critical analysis” (from prompt4) to produce fully balanced, structured data.
Instructions:
1. Info integration: Integrate both the finalized Master Fact Sheet (prompt2) and the Final Critical Report (prompt4) into the JSON template below.
2. Preservation of detail: This JSON is the single source of truth for further reporting—NEVER summarize, always carry over the original detailed explanations, full sentences, and nuances for each field.
3. Flexible schema: The schema below is a checklist. If the project warrants additional important info, freely extend the JSON with new keys.
4. Value handling: Leave fields as null/empty if blank.
5. Output: Output ONLY the JSON code block—no additional explanations.

JSON Template:
{
  "projectName": "",
  "oneLiner": "",
  "tags": [],
  "overview": {
    "summary": "",
    "details": ""  // Full explanation, examples, and nuance
  },
  "strengths": [
    { "point": "", "details": "" }
  ],
  "weaknesses_and_risks": [
    { "point": "", "details": "" }
  ],
  "technology": {
    "coreConcept": "",
    "keyFeatures": [
      { "name": "", "description": "", "details": "" }
    ]
  },
  "tokenomics": {
    "tokenName": null,
    "tokenTicker": null,
    "utility": null,
    "details": ""
  },
  "team": [
    { "name": "", "role": "", "background": "", "details": "" }
  ],
  "investors": [
    {
      "name": "",
      "type": "",     // VC, Angel, Corporate, etc. ("Other" allowed)
      "tier": "",     // If unknown: null, or mark as "estimated"
      "description": "", // If known: amount, seed/Series A, reputation/description
      "details": ""   // E.g., investment time, strategic/pure, news articles, etc.
    }
  ],
  "userActions": {
    "currentActivities": null,
    "airdropPotential": {
      "status": "High/Medium/Low/None",
      "reasoning": "",
      "details": ""
    }
  },
  "competitors": [
    { "name": "", "differentiation": "", "details": "" }
  ],
  "risks": [
    { "type": "", "description": "", "details": "" }
  ]
}

## prompt6: JSON Data Merge & Finalization ##
# reasoning
# other_ai_info
Your role: You are the lead data architect integrating multiple data sources into a final Single Source of Truth.
Instructions:
1. Merge all JSONs you and other AIs created into a single, complete, finalized JSON.
2. Merge rules:
      * Expand structure: If another AI added beneficial new keys, include them.
      * Merge & enrich: For each item, combine/enrich all AIs’ info—never just pick one or summarize. E.g., if one AI covers tech aspect A, and another covers aspect B, the merged result must include both in detail.
      * Maintain depth: When merging, synthesize to ensure all depth/nuance is preserved.
3. Output: Output ONLY the final merged JSON code block—NO additional explanations.

## prompt7: Final Output Generation (3 styles) ##
# reasoning
Your role: You are a versatile content creator who produces outputs in different styles for different uses.

Instructions:
1. Only use the final JSON: You MUST never guess or supplement outside anything not explicitly in the final JSON. Every sentence must be traceable to the JSON contents.
2. Produce three outputs in order, as detailed below.

---

[Output 1: Detailed Analytical Report]

Instructions: Using all JSON data—including `strengths` and `weaknesses_and_risks`—write a balanced, in-depth analytical report. Do NOT summarize; fully elaborate, drawing on each JSON item in depth.

---

[Output 2: Telegram Summary Report]

Instructions:
- Use the example format below for inspiration, but feel free to freely adapt section titles and structure per project characteristics.
- Clearly state that this is a balanced (strengths+weaknesses) analysis.

Example format (for structure/style reference):
[Project Name]
[A concise one-liner, tagline, or project summary]
✨ Key Summary
Problem: Core pain point(s) this project aims to solve.
Solution: Differentiated technical approach adopted by this project.
Investment Point: The biggest reason to pay attention to GTE right now.

💻 What is [Project Name]?
Explain the project’s identity and goals as simply and accessibly as possible.
Include relatable analogies/examples for broader understanding.

🔧 How does the core technology work?
Explain the most important technology (e.g., decentralized storage, real-time validation) step-by-step.
E.g.: Step 1: Data collection → Step 2: Data validation → Step 3: Rewards.

🔗 Tokenomics: $TOKEN
Clarify core utility (e.g., governance, payments, staking), distribution to team/investors/community, and any unique features.

💸 User actions & airdrop outlook
Guide users on concrete steps to participate (using the app, running nodes, etc).
Give your rating on airdrop potential (High/Medium/Low) and rationale, using evidence like token issuance, investor profile, precedents, etc.

👥 Team & Investors: Who built it, who backed it?
Highlight the credentials of high-profile team members and main investors.

⚠️ Risks & Opportunities
Competitive comparison: Objectively analyze pros/cons vs. similar projects.
Key risks: Explicitly state technical/business hurdles.

🤝 Key Terms
DePIN: Decentralized Physical Infrastructure Network—a way to operate physical infra via blockchain.
RTK: Tech for real-time satellite error correction, offering centimeter-level precision.

🧨 Final verdict
One-sentence summary of the entire project.

Note: Sections can (and should) be restructured, expanded, or omitted as best fits the project. If you see major weaknesses or gaps, they MUST be included.

---

[Output 3: Promotional Tweets (10 total)]

Instructions:
- Write promotional tweets highlighting only the project's strengths and unique selling points.
- Rules:
    - Number: 5 tweets in Korean, 5 tweets in English (total 10).
    - Content: Each tweet must focus on a different major appeal or advantage—avoid overlap.
    - Forbidden: NO hashtags (#), NO emojis, under any circumstance.
    - Must: The official Twitter handle (@GTE_xyz) must appear naturally in each tweet.
    - Style: Not overly short; maximize informativeness and clarity within Twitter's character limits.