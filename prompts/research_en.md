## project name ##
GTE

## prompt1: In-Depth Analysis and Report ##
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
main request: Research and analyze the project described in **project info**.

Your Role: You are an elite crypto analyst whose goal is to help the reader make intelligent decisions, not just deliver information.

Instructions:
- **Web search is required:** You MUST use your web browsing capabilities to find the latest information from reliable sources (official website, technical docs, GitHub, major media, X/Twitter, etc.).
- **Language and term notation:**
  1. **Default:** All explanations should be written in English, unless specifically instructed otherwise.
  2. **English term notation:** If a technical term or proper noun appears for the first time, always include the original (acronym) in parentheses for clarity.
  3. **Example:** Decentralized Physical Infrastructure Network (DePIN).
  4. For repeated terms, you may write just the English term after the first full notation.
- **Detailed analysis:** For each of the following topics, answer the guiding questions in depth and in a report format.
  1. **Project Overview (The Big Picture)**
     - What is it? Define the project in a single sentence.
     - Why is it needed? What problem does it solve and why is that important? Include realistic examples understandable to beginners.
  2. **Technology & Mechanisms (How it Works)**
     - How does it work? Explain the core technical mechanism step by step.
     - Differentiation: Specifically, how is this project innovative compared to alternative approaches or competitors (e.g., speed, cost, security, decentralization, etc.)?
     - Explain jargon: Where terms are difficult for non-experts, always offer a plain analogy.
  3. **Tokenomics** (if applicable)
     - Token info: Name, ticker, and main utility.
     - Distribution: Initial allocation, total supply, inflation/deflation model, etc.
  4. **Team & Investors (The People)**
     - Key personnel: What are the team members’ backgrounds? (If missing, refer to Rootdata.)
     - Team vision: From X (Twitter) or interviews, analyze what they emphasize and their main vision.
     - Key investors: Who are the top funders, and why do you think they invested?
  5. **Users and Community (For Users)**
     - Participation: Are there apps/products users can participate in or use now? If yes, how?
     - Airdrop potential: Are there ongoing or upcoming airdrop activities? Provide reasoning/evidence.
  6. **Competition & Risks**
     - Competitive landscape: What are the most direct competitors? What are GTE’s strengths and weaknesses by comparison?
     - Potential risks: What technical, business, or market risks may GTE face?
     - **Note:** The above sections (1-6) are templates; you may restructure, merge, or add sections for a better logical flow.
- **Output format:** Write a detailed analytical report, matching the structure above, in English. Do NOT summarize.

## prompt2: Cross-Validation & Fact Sheet Generation ##
# reasoning
# other_ai_info
Your role: You are the lead researcher responsible for fact-checking and synthesizing all information.

Instructions:
1. Review all data: Carefully review your own findings and those provided by other AIs in the previous step.
2. Produce a Master Fact Sheet: Integrate all information into a single, comprehensive, fully fact-checked 'Master Fact Sheet'.
   - Correct errors: Where there are contradictions, verify with web search and use only the most accurate information.
   - Enrich content: Add valuable new data, insights, or arguments that other AI responses may have provided.
3. Before presenting the Master Fact Sheet, briefly bullet major changes you made. (e.g., "- Corrected total token supply based on official docs," "- Added details on consensus mechanism from AI B’s answer.")
4. Output: First, the list of changes; second, the completed Master Fact Sheet.

## prompt3: Red Team Critical Analysis ##
# reasoning
Your role: Now, act as a skeptical investor and provide a "Red Team" critical analysis. Omit the positives and focus only on weaknesses, risks, or suspicious elements.

Instructions:
1. Maintain a critical perspective. Based on the Master Fact Sheet, answer the following, being as critical as possible:
   - Hype?: Is this project truly innovative or just a minor variation of existing tech? What lies behind the buzzwords/marketing language?
   - Unsustainable Tokenomics?: Is token allocation overly favorable to the team or early investors? Is there a sound model for maintaining long-term value?
   - Is the team's competence proven?: Are team backgrounds truly relevant? Is there evidence they can deliver on the roadmap?
   - Red Flags: What must any investor know? Any hidden risks? (e.g., vague roadmap, inactive community, intense competition, etc.)
2. Output: Write a detailed, logically argued critical report answering these.
3. Actively validate your criticisms via credible web sources as evidence.

## prompt4: Red Team Synthesis & Final Critical Report ##
# reasoning
# other_ai_info
Your role: Synthesize all critical analyses (from you and other AIs), and produce the sharpest, most logically sound final conclusion as the chief Red Team analyst.

Instructions:
1. Review only critical perspectives: Carefully review all Red Team critiques (your own and others’) from the previous step. (Do NOT reference the positive Master Fact Sheet in this step.)
2. Produce the final critical report: Merge all critiques into a single, fact-checked 'Final Critical Report'.
    - Core risks: Identify key recurring risks, and highlight them.
    - Enrich the logic: Where another AI’s critique adds a valid point, integrate it to reinforce the argument.
    - Remove duplicates: Merge or eliminate overlapping points for conciseness.
3. Change Log: Before the final report, briefly summarize any significant changes you made by incorporating others’ input.
4. Output: First, the change summary; second, the completed Final Critical Report.

## prompt5: Structured Data (JSON) Extraction (with Strengths/Weaknesses) ##
# reasoning
Your role: You are a data specialist integrating the "positive facts" (prompt2) and "critical analysis" (prompt4) to compose a balanced dataset.

Instructions:
1. Aggregate information: Combine the Master Fact Sheet (prompt2 result) and Final Critical Report (prompt4 result) to provide a comprehensive evaluation of strengths, weaknesses, opportunities, and threats. Fill in the JSON template below.
2. Data preservation: This JSON becomes the definitive single source for further reports. Never summarize, but preserve the original explanations, full sentences, and important nuances in each field.
3. Balanced judgment: Let your output reflect the *real* weighting of pros/cons. If positive points are 90%, reflect that; don't force artificial 50:50 parity. *Do not state explicit ratio.* 
4. Schema flexibility: The template below is a checklist; freely add new fields/keys as warranted by the project.
5. For any missing data, fields should be set to `null` or left empty.
6. Output: Only print the JSON code block. No additional text.

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
      "type": "",       // VC, Angel, Corporate, etc. ('Other' allowed)
      "tier": "",       // If unknown: null or 'estimated'
      "description": "",// E.g. known funding, seed/series, reputation/notes
      "details": ""     // When supported: investment date, strategic/pure, links
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

## prompt6: JSON Data Merging & Finalization ##
# reasoning
# other_ai_info
Your role: As the lead data architect, integrate all data sources into a final Single Source of Truth.

Instructions:
1. Merge all JSONs produced by you and other AIs into the single, most complete and accurate final JSON.
2. Rules:
   - Expand structure: If another AI added useful new keys, include them.
   - Merge and enrich: Combine all contents for the same key/field—don't just pick or summarize. E.g., if some AIs cover aspect A of the tech and others aspect B, both must be present.
   - Depth preservation: When merging, always synthesize into a detailed and complete final version.
3. Output: Output a single merged final JSON code block—do not add any other text.

## prompt7: Final Output Generation (3 Styles) ##
# reasoning
Your role: You are a master content creator, able to produce outputs in a range of styles for different scenarios.

Instructions:
1. You MUST USE ONLY the finalized JSON from the previous step as your source. DO NOT infer, speculate, or add any information that isn't in the JSON.
2. Produce all three outputs in order, according to the instructions below.
3. **Language and notation guidelines:**
   - All outputs must be written in English.
   - When technical/proper terms appear for the first time, include the original or acronym in parentheses. You may later refer to them with just the standard English term.
   - Use format: Explained term (Original Term, Acronym)
   - Ex: Decentralized Physical Infrastructure Network (DePIN)

---

[Output 1: Detailed Analytical Report]

Using the JSON data, write a professional, readable, and highly structured in-depth report according to the following rules:

Rules:
- **Structure for readability:** Use headings (###), subheadings (**), bullet points (-), and divide text into clear paragraphs. Do NOT write long unbroken text blocks.
- **Synthesize information:** For each section, merge related points into a unified narrative. Avoid repeating the same content in multiple places.
- **Objective voice:** Do NOT use first-person perspective (e.g., "I think..."). Maintain an objective analyst's tone.
- **Balanced perspective:** Cover both strengths and weaknesses as they truly exist (not forced 50:50). Let the actual weighting in the project data be reflected, not arbitrary symmetry.
- **Flexible structure:** Organize/report the structure and sections in the way you judge most effective for communication.

---

[Output 2: Telegram Summary Report]

Instructions:
- Use the following format only as inspiration/influence—adapt section titles and arrangement as best fits the project.
- Your summary MUST be a genuinely balanced analysis (strengths & weaknesses).

Example format:
[Project Name]
[One-liner or tagline about the project]
✨ Key Summary
Problem: The key market pain point this project targets.
Solution: The distinctive technical approach.
Investment point: Why should people pay close attention to this project now?

💻 What is [Project Name]?
Explain the project's core identity and goals accessibly. Use analogies/examples that even newcomers will understand.

🔧 How does the core technology work?
Explain the most important technology (e.g., decentralized storage, real-time validation) step by step.
E.g.: Step 1: Data collection → Step 2: Data validation → Step 3: Rewards.

🔗 Tokenomics: $TOKEN
Clearly specify token utility: governance, payments, staking, etc.
Outline distribution structure: team, investors, community, etc.

💸 User actions & airdrop outlook
Guide concretely on app participation, node operation, etc.
Assess airdrop potential (High/Medium/Low) and explain with evidence (token status, investor type, case studies, etc.)

👥 Team & investors: Who built and funded the project?
Highlight credentials of notable team members & key investors.

⚠️ Risks & opportunities
Objectively analyze strengths and weaknesses vs similar projects.
Call out key risk factors.

🤝 Key term explanations
DePIN: Decentralized Physical Infrastructure Network—a method of operating physical infrastructure with blockchain.
RTK: Real-Time Kinematic—satellite error correction for centimeter-level accuracy.

🧨 One-line verdict
Sum up the project in a single sentence.

Note: Structure can and should be adapted per the project, and when clear weaknesses or gaps are present, include them.

---

[Output 3: Promotional Tweets (10 total)]

Instructions:
- Write 5 Korean and 5 English tweets to promote the greatest strengths and appeal of the project.
- Rules:
    - Each tweet should be about a different point—avoid repetition.
    - Do NOT use hashtags (#) or emojis.
    - The project's official X (Twitter) handle (e.g., @GTE_xyz) must appear in each tweet.
    - Tweets should have as much information as possible within the character limit, and be clear/readable.