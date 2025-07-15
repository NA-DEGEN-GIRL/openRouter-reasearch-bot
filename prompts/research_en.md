## project name ##
GTE

## prompt1: In-Depth Analysis & Reporting ##
# reasoning
**project info**
GTE
• One-liner: Decentralized trading platform
• Tag: DeFi, DEX, OrderBook DEX
• web: https://www.gte.xyz/
• X: https://x.com/gte_xyz
💰 Total Funding: $25,000,000
👑 Tier 1 Investors:
  - Paradigm
🥂 Tier 2 Investors:
  - Robot Ventures, Wintermute
🔹 Other Investors:
  - Flow Traders, Guy Young, IMC Trading, Maven 11, Max Resnick
Rootdata (https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=)
**end of project info**
main request: Analyze and investigate the project described in **project info**.

Your role: You are not just an information provider; you are a top-tier crypto analyst whose aim is to help readers make wise, informed decisions.

Instructions:
- **Mandatory Web Search:** You MUST always use web search to obtain the latest information as of today from credible sources (official website, technical documentation, GitHub, major media, X/Twitter, etc.). Always ground each report in facts discoverable today.
- **Date Statement:** At the very top of your report, you MUST clearly state the current date as:  
  *"Date of Analysis: YYYY-MM-DD"*
- **Language and Terminology Rules:**
  1. Default: ALL output must be in English unless otherwise noted.
  2. English term notation: Whenever you first introduce a technical term or proper noun, always cite the original English term and acronym in parentheses.
  3. Format: [Translated/Explained Term] (Original English Term, Acronym)
     - Example: Decentralized Physical Infrastructure Network (DePIN)
  4. For recurring terms, the standard English version is sufficient after the first instance.
- **Analysis Depth:** For each item below, answer the listed guiding questions comprehensively, section by section.
  1. **Project Overview (The Big Picture)**
     - What is this project, in one sentence?
     - Why is it necessary? What problem does it solve and why is this important? Give clear, beginner-friendly examples.
  2. **Technology & Mechanism (How it Works)**
     - Operation: Explain the main mechanism/processes step by step.
     - Differentiators: Which specific aspects make this project innovative versus predecessors and competitors (e.g., speed, cost, security, decentralization)?
     - Jargon: Always explain complex terms through relatable analogies.
  3. **Tokenomics** (if the project has a token or defined economic model)
     - Token details: Name, ticker/symbol, main utility.
     - Distribution: Initial allocation, total supply, inflation/deflation models if any.
  4. **Team & Investors (The People)**
     - Key personnel: What are the backgrounds and experiences of the core team? (If info is missing, supplement from Rootdata.)
     - Team vision: Analyze what the team emphasizes/publicly states as their vision via X(Twitter) or interviews.
     - Lead investors: Who are the most noteworthy backers? Why do you think they invested in this project?
  5. **Users & Community (For Users)**
     - How to participate: Are there products/apps that normal users can directly use? If so, how specifically?
     - Airdrop potential: Are there ongoing or expected airdrop-related campaigns? What evidence or rationale is there?
  6. **Competition & Risks**
     - Competitive landscape: Who are the direct competitors, and what are GTE’s strengths and weaknesses compared to them?
     - Potential risks: What technical, business, or market-side risks could this project face?
  *Note:* These points are guides—not mandatory fixed sections. You may reorganize, merge, or expand them for best clarity and logic.
- **Output Requirements:** You MUST write your output as an in-depth report addressing the questions above, in English. Summarization is forbidden.

## prompt2: Cross-Validation & Fact Sheet Generation ##
# reasoning
# other_ai_info
Your role: You are the lead fact-checker and integrator.

Instructions:
1. Review all information: Carefully verify your prior findings and all research provided by other AIs.
2. Master Fact Sheet: Your goal is to create a comprehensive, fully fact-checked "Master Fact Sheet" integrating all data.
    - Correct all discrepancies: Whenever there’s conflicting info, you MUST use web search to determine the accurate facts and adopt only the best-sourced info.
    - Enrich your content: Add any unique value points from other AI responses that you initially missed.
3. Change Log: Before outputting the final Master Fact Sheet, list the principal changes you made in concise bullet points (e.g., "- Updated total supply based on official docs", "- Incorporated consensus details from AI B").
4. Output: List the changes first, then output the full Master Fact Sheet.

## prompt3: Red Team Critical Analysis ##
# reasoning
Your role: You are now acting as a highly skeptical investor—your job is to provide a "Red Team" critique. Disregard positive points; focus solely on weaknesses, risks, and any suspicious elements.

Instructions:
1. Maintain a critical viewpoint: Based on the Master Fact Sheet, answer the following:
   - Hype?: Is this technology truly groundbreaking, or just a mild iteration of past ideas? What’s really behind the marketing?
   - Unsustainable tokenomics?: Is the token allocation unfairly slanted towards team/early investors? Is there a clear, sustainable long-term value model?
   - Team capabilities?: Are team backgrounds genuinely relevant? Is there proof they can execute their roadmap?
   - Red Flags: As an investor, what are the must-know warning signs? Any hidden/critical risks? (e.g., vague roadmap, weak community, excessive competition, etc.)
2. Output: Write a detailed, logically argued Red Team analysis covering the above.
3. You must support your critiques with credible web sources as evidence.

## prompt4: Synthesis & Final Red Team Critical Report ##
# reasoning
# other_ai_info
Your role: Synthesize all Red Team reports (from you + other AIs) into the sharpest, most objectively reasoned final conclusion.

Instructions:
1. Consider ONLY critical (negative) analyses: Thoroughly review all Red Team critiques from step 3. Ignore positive data from step 2 for this step.
2. Write the Final Red Team Report by merging all relevant criticisms into one coherent, fact-checked document.
   - Identify and highlight the core risks that are mentioned by multiple sources.
   - Strengthen logic by adding valid points from other AI critiques.
   - Merge/condense duplicates for clarity.
3. Before output, list major changes added from other AI critiques.
4. Output: List changes, then output the finalized report.

## prompt5: Structured Data (JSON Extraction with Full Preservation of Strengths & Weaknesses) ##
# reasoning
Your role: Combine positive facts (step 2) and negative Red Team analyses (step 4) to produce a well-balanced dataset.

Instructions:
1. Aggregate all information: Merge the Master Fact Sheet and Final Critical Report. Evaluate strengths, weaknesses, opportunities, and risks and fill out the JSON template below.
2. Preservation Rule: This JSON is your definitive single source for any further output. Do NOT summarize—transfer all important explanations and critical sentences/narratives verbatim.
3. Your output should proportionally represent the real strengths/risks ratio of the data. If positive is 90%, show that; do NOT try to artificially balance it. *Never state or imply an explicit percentage.*
4. If a project-specific key/section is missing, you may add more keys beyond the template.
5. Set any missing value to `null` or empty.
6. Output: ONLY the JSON code block, no explanations.

JSON Template:
{
  "projectName": "",
  "oneLiner": "",
  "tags": [],
  "overview": {
    "summary": "",
    "details": ""  // full detail, examples, and nuance
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
      "type": "",       // VC, Angel, Corporate, etc. (Other allowed)
      "tier": "",       // null or 'estimated' if unknown
      "description": "",// e.g. capital, round, notability
      "details": ""     // e.g. time of support, strategic/type, links
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

## prompt6: Merging JSON Data for Finalization ##
# reasoning
# other_ai_info
Your role: As the lead data architect, merge all JSONs into the single, finalized Single Source of Truth.

Instructions:
1. Merge all your and other AIs' JSONs into the single most complete and accurate data object.
2. Rules:
   - Expand schema: If another AI added useful keys, include them.
   - Merge/enrich: For each key, aggregate and enrich all values; do NOT just select or summarize. Both A & B aspects must be preserved if different AIs contributed them.
   - DO NOT lose important detail.
3. Output: Output ONLY the final merged JSON code block.

## prompt7: Final Output Generation (3 Output Styles) ##
# reasoning
Your role: As an all-round content creator, your task is to generate three distinctive output formats.

Instructions:
1. Only use the finalized JSON above; do NOT invent, speculate, or add material not present in the JSON.
2. Produce the three outputs below, sequentially.
3. **Language and terminology guidelines:**
   - English output only.
   - When introducing technical/proper nouns, always provide the original term/acronym in parentheses at first use. Subsequent mentions can use the normal English.
   - Example: Decentralized Physical Infrastructure Network (DePIN)

---

[Output 1: Detailed Analytical Report]
Using the JSON data, write a professional, well-structured, and highly readable full analysis report by following these rules:

Rules & Format:
- **Focus on readability (mandatory):** Use Markdown headings (###), subheadings (**), bullet points (-), and always divide content into clear paragraphs for maximal clarity. NEVER output uninterrupted massive walls of text.
- **Synthesize information:** For each section, synthesize all related info into a single, coherent explanation, and avoid repeat content across sections.
- **Objective style:** Do NOT use first-person phrasing (e.g., "I think..."). Maintain an objective, analytical voice at all times.
- **Balanced perspective:** Give both strengths and weaknesses as reflected in the data, but do NOT force 50:50 parity. Let the genuine pros/cons ratio reflect reality.
- **Flexible sectioning:** Organize the overall structure and section order in whatever way you judge to be most effective.

---

[Output 2: Telegram Summary Report]

Instructions:
- Use the following format as inspiration (do not treat it as mandatory). Modify, add, or remove sections to best suit the project.
- The summary MUST deliver a truly balanced view (both key strengths and weaknesses).

Example format:
[Project Name]
[Concise one-liner or tagline]
✨ Key Summary
Problem: Major market pain point solved.
Solution: Distinctive technical/architecture approach.
Investment Point: Why is this project interesting now?

💻 What is [Project Name]?
Plain English intro to project identity and purpose—with one or more beginner-friendly analogies/examples.

🔧 Core Technology—How does it work?
Clear, step-wise explanation for major technical innovations.
(E.g., Step 1: Data collection → Step 2: Data validation → Step 3: Reward)

🔗 Tokenomics: $TOKEN
Token's utility and distribution explained.

💸 User actions & airdrop outlook
Guide on how users can use apps, run nodes, participate, etc.
Airdrop assessment: Grade as High/Medium/Low with clear justification.

👥 Team & Investors
Highlight major team credentials and leading investors.

⚠️ Risks & opportunities
Fairly weigh strengths vs. weaknesses and call out key risks.

🤝 Glossary for Key Terms
DePIN: Decentralized Physical Infrastructure Network—operating physical infra on blockchain.
RTK: Real-time satellite correction for cm-level precision.

🧨 One-line verdict
Conclude the entire report in a single, powerful sentence.

Note: Sections and order can/should be adapted freely per project, and any detected weaknesses or missing points must always be included.

---

[Output 3: Promotional Tweets (Total: 10 — 5 Korean, 5 English)]

Instructions:
- Write five Korean and five English tweets promoting the project's main strengths and attractiveness.
- Rules:
    - Each tweet must focus on a unique appeal, avoid redundancy.
    - Do NOT use hashtags (#) or emojis.
    - Official project Twitter handle (e.g., @GTE_xyz) must appear in every tweet.
    - Write informative, readable content within Twitter's character limit.