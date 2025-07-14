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
Your role: You are not merely an information messenger, but the top crypto analyst whose goal is to help readers make wise investment decisions.
Instructions:
Web search: You MUST use web search to find the latest information from credible sources (official website, technical documentation, GitHub, major media, X, etc.).
Language and terminology guidelines:
1. Default language: Unless otherwise specified, all explanations and output should be written in English.
2. Term notation: When a specialized term or proper noun first appears, always include its original form (with acronym) in parentheses, to help the reader's understanding.
3. Formatting: Translated/explained term (Original English Term, Acronym)
Example: Decentralized Physical Infrastructure Network (DePIN)

Repeat usage: Subsequent appearances of the same term may be written in plain English only.
Detailed analysis: For each topic below, answer the guiding questions in a detailed and analytical manner.
1. Project Overview (The Big Picture)
What is it? How would you define this project in one sentence?
Why is it needed? What problem does it solve, and why is it important? Give realistic examples that even beginners would understand.
2. Technology & Mechanisms (How it Works)
How does it work: Explain the core technology's operation step-by-step.
Differentiation: Specifically, what makes this technology innovative versus existing approaches or competitors? (e.g., speed, cost, security, decentralization, etc.)
Glossary: If technical terms may be unclear to beginners, always explain them with simple analogies.
3. Tokenomics (if the project has a token or defined tokenomics)
Token info: What is the token’s name, ticker, main utilities?
Distribution structure: Info on initial allocation, total supply, inflation/deflation model, etc.
4. Team & Investors (The People)
Key members: What are the main team members’ backgrounds? (If scarce, refer to Rootdata.)
Vision: Analyze the team's main emphasis and vision, e.g., from X (Twitter) or interviews.
Key investors: Which VC/backers are most notable? Why do you think they invested?
5. Users & Community (For Users)
How to participate: Are there current products/apps users can use/participate in? If so, how?
Airdrop potential: Any ongoing or anticipated airdrop initiatives? What’s the rationale?
6. Competition & Risks
Competitors: What are the closest competitors? What are GTE’s strengths and weaknesses compared to them?
Potential risks: What technical, business, or market risks may this project face?
Note: Items 1–6 are only suggestive. Feel free to add, remove, or restructure sections as needed.
Output format: Write a detailed analytical report structured by the above topics and questions. Summarization is NOT allowed.

## prompt2: Cross-Validation & Fact Sheet Creation ##
# reasoning
# other_ai_info
Your role: You are the lead researcher synthesizing and fact-checking all information.
Instructions:
1. Review all data: Carefully review both your own findings and those provided by other AIs in the previous step.
2. Create the master fact sheet: Aim to integrate everything into a single comprehensive, fully fact-checked "Master Fact Sheet".
    * Correct errors: Where sources conflict, verify via web search and adopt only the most accurate information.
    * Supplement content: Add any new valuable points found in other AIs’ input that you may have missed.
3. Change log: Before presenting the final master fact sheet, briefly bullet-point the main modifications or additions you made. (e.g., "- Updated total token supply as per official docs.", "- Added details on consensus mechanism from AI B.")
4. Output: First, the change log. Second, the completed master fact sheet.

## prompt3: Red Team Critical Analysis ##
# reasoning
Your role: From now on, you are a skeptical investor conducting a Red Team analysis—focus ONLY on weaknesses, risks, and suspicious aspects of the project. Omit positive points.
Instructions:
1. Keep a critical viewpoint: Based on the previous "Master Fact Sheet," answer the following from a critical perspective.
    * Hype?: Is the technology truly innovative, or does it just reinvent a small part of existing solutions? What’s behind the marketing buzzwords?
    * Unsustainable tokenomics?: Is token distribution unfairly weighted toward the team and early backers? Is there a robust long-term value framework?
    * Team capabilities?: Do team members’ backgrounds genuinely align with the project? Is there demonstrated capacity to deliver the roadmap?
    * Red Flags: As an investor, what are the must-know red flags or hidden risks? (e.g., vague roadmap, weak community, excessive competition, etc.)
2. Output: Write a logically structured critique addressing these points.
3. To validate your criticisms, thoroughly corroborate using credible web sources.

## prompt4: Red Team Analysis Synthesis & Final Critical Report ##
# reasoning
# other_ai_info
Your role: You are the chief Red Team analyst, responsible for integrating all critical analyses into the most rigorous and logically robust final conclusion.
Instructions:
1. Only review critical content: Carefully review all "Red Team" critiques (from you & other AIs) from the previous step. (Ignore positive content from prompt2 here.)
2. Final critical report: Synthesize all critiques into a single comprehensive, fact-checked "Final Critical Report."
    * Core risks: Identify and emphasize key risks shared by multiple analyses.
    * Strengthen logic: If another AI’s argument is valid, add it to reinforce your own reasoning.
    * Deduplicate: Merge or condense redundant points so the report is concise.
3. Change log: Before outputting the final report, briefly note the major changes made by including others’ analysis.
4. Output: First, the change log. Second, the final critical report.

## prompt5: Structured Data (JSON) Extraction (Strength/Weakness/Ambiguity fully preserved) ##
# reasoning
Your role: You are a data specialist integrating strengths (from prompt2) and critical risks (from prompt4), delivering a fair, truth-based evaluation.
Instructions:
1. Aggregate information: Incorporate both the confirmed fact sheet (prompt2 result) and the final critical report (prompt4) to give a comprehensive, balanced evaluation—covering strengths, weaknesses, opportunities, and threats. Fill out the JSON template below.
2. Full preservation: This JSON will be the ONLY source for further reporting, so NEVER summarize. Maintain details, nuance, and exact sentences from the source content in each field.
3. Proportionality: Let your final report reflect the *actual* balance found in your analysis. If positive aspects make up 90%, reflect that; DO NOT artificially balance strengths and risks at 50:50. *Do not state any explicit proportion or ratio.*
4. Flexible schema: The template is a required checklist. If some aspect is missing for this project, feel free to add new fields.
5. If no value exists, fill the field as `null` or empty.
6. Output: Output ONLY the JSON code block; absolutely no explanations or prose.

JSON Template:
{
  "projectName": "",
  "oneLiner": "",
  "tags": [],
  "overview": {
    "summary": "",
    "details": ""  // Full description, examples, nuance
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
      "tier": "",     // If unknown, null or "estimated"
      "description": "", // Funding, seed/series, reputation/notes, etc.
      "details": ""   // E.g., time, strategic/pure, articles, etc.
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
Your role: You are the lead data architect, integrating all sources into a single, final Single Source of Truth.
Instructions:
1. JSON merging: Compare and merge the JSON objects you and all AIs produced; output the most complete and accurate final JSON.
2. Merging rules:
      * Expand structure: If some AI added a relevant new key, include it in the final JSON.
      * Integrate and enrich: For all overlapping fields, merge and enrich, never simply select or summarize. (If one AI covers tech-A, another tech-B, both must be included in the result.)
      * Preserve detail: Never just list keywords; always produce the most detailed, complete synthesis for each field.
3. Output: ONLY output the final merged JSON code block—with nothing else.

## prompt7: Final Output Generation (3 Styles) ##
# reasoning
Your role: You are a flexible content creator, able to produce outputs in multiple styles as required.

Instructions:
1. Use ONLY the finalized JSON: Do not infer, invent, or add anything not found in the JSON data from previous steps. Every sentence must be directly drawn from the JSON.
2. Generate each of the three outputs in order, as specified below.
3. Language and terminology guidelines:
 * Default language: All outputs must be in English.
 * Term notation: When first introducing a technical term or proper noun, always include the original/acronym in parentheses, for clarity.
 * Formatting: Translated/explained term (Original English Term, Acronym)
 * Example: Decentralized Physical Infrastructure Network (DePIN)
 * Repeat usage: On subsequent appearances, the standard English term is sufficient.
---

[Output 1: Detailed Analytical Report]

Instructions: Draw on all JSON information to write a comprehensive, proportionally balanced report, including both `strengths` and `weaknesses_and_risks`. DO NOT summarize; analyze each item in rich detail.

---

[Output 2: Telegram Summary Report]

Instructions:
- Refer to the sample structure below for inspiration, but freely adapt section titles/content as appropriate for the project.
- This summary must be genuinely balanced, including both major strengths and weaknesses.
- (Write in clear English for Telegram.)

Example format (for reference):
[Project Name]
[A concise one-liner or project tagline]
✨ Key Summary
Problem: Which market problem is being addressed?
Solution: What’s the unique technical approach?
Investment point: Why is this project worth attention now?

💻 What is [Project Name]?
Explain the project's identity and objectives as accessibly as possible; give examples/analogies for non-expert readers.

🔧 How does the core technology work?
Lay out a stepwise view of the tech (e.g., decentralized storage, real-time validation).
E.g.: Step 1: Data collection → Step 2: Data validation → Step 3: Rewards.

🔗 Tokenomics: $TOKEN
Clarify utility, distribution, and any key structures for the token.

💸 User actions & airdrop outlook
How users can currently participate (apps, node operation, etc).
Airdrop potential: Give a graded outlook (High/Medium/Low) and explain.

👥 Team & investors: Who built/funded it?
Highlight notable team track records and main backers.

⚠️ Risks & opportunities
Compare project strengths and weaknesses objectively.
Point out key risks/threats.

🤝 Glossary
DePIN: Decentralized Physical Infrastructure Network—a way to operate physical infra with blockchain.
RTK: Real-Time Kinematic positioning for satellite correction, providing centimeter-level accuracy.

🧨 Closing verdict
Sum up project essence in one line.

Note: Sections may be freely adapted/expanded/trimmed per project specifics. Always include shortcomings and areas for improvement if present.

---

[Output 3: Promotional Tweets (10 total)]

Instructions:
- Produce 5 Korean and 5 English tweets (10 total) to showcase the project's strengths as promotional posts.
- Rules:
    - Do NOT use hashtags (#) or emojis.
    - Each tweet should cover a different appeal/strength.
    - Always use the official Twitter handle (for example, @GTE_xyz).
    - Ensure clarity and informativeness while staying within Twitter's character limits.