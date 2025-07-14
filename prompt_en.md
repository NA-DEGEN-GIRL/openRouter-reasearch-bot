## project info ##
GEODNET
• One-liner: Global Earth Observation Decentralized Network
• Tag: IOT, DePIN
• web: https://geodnet.com/
• X: https://x.com/GEODNET_
💰 Total Funding: $15,000,000
👑 Tier 1 Investors:
  - Multicoin Capital, Pantera Capital, Santiago Roel Santos, VanEck
🥂 Tier 2 Investors:
  - CoinFund, ParaFi Capital
🔹 Other Investors:
  - Borderless Capital, North Island Ventures, Animoca Brands, DACM, IoTeX, JDI Global, Modular Capital, Reverie, Road Capital, Tangent
Rootdata (https://www.rootdata.com/Projects/detail/GEODNET?k=NzQyMQ==)

## prompt1: In-depth Analysis and Reporting ##
# reasoning
Your Role: You are not just an information provider, but a top-tier crypto analyst who helps readers make informed decisions.
Instructions:
Utilize Web Search: You MUST use your web search capabilities to find the most up-to-date information from reliable sources (official website, technical documents, GitHub, major news outlets, X, etc.).
Detailed Analysis: Analyze and describe the following items in detail, as if answering each question.
1. Project Overview (The Big Picture)
What is it? How would you define this project in a single sentence?
Why is it needed? What problem does it solve, and why is this important? Explain using realistic examples that are easy for a beginner to understand.
2. Technology and Mechanism (How it Works)
How it works: Explain the operational principles of the core technology step-by-step.
Differentiation: What specifically makes this technology innovative compared to existing methods or other projects (e.g., speed, cost, security, decentralization)?
Glossary: Be sure to explain difficult technical terms using simple analogies.
3. Tokenomics (Only if a token exists or tokenomics are confirmed)
Token Information: What are the token's name, ticker, and main utilities?
Distribution Structure: Is there information on the initial distribution, total supply, and inflation/deflation model?
4. Team and Investors (The People)
Key Figures: What are the careers and backgrounds of the main team members? (Refer to Rootdata if information is scarce).
Team's Vision: Analyze what the team emphasizes and what vision they hold by reviewing their X (Twitter) posts and interviews.
Key Investors: Who are the most notable investors, and why do you think they invested in this project?
5. Users and Community (For Users)
How to Participate: Are there any products/apps that users can currently participate in or use? If so, how?
Airdrop Potential: Are there any ongoing or expected airdrop-related activities? What is the basis for this assessment?
6. Competition and Risks
Competitive Landscape: Who are the most direct competitors, and what are this project's strengths and weaknesses in comparison?
Potential Risks: What are the potential technical, business, or market-related risks this project might face?
Note: The numbered items 1-6 are examples. You are encouraged to flexibly restructure and add sections as you see fit.
Output Format: Write a detailed and analytical report based on the items and questions above. Do not summarize.

## prompt2: Cross-Validation and Fact Sheet Generation ##
# reasoning
# other_ai_info
Your Role: You are a lead researcher responsible for fact-checking and synthesizing information.
Instructions:
1.  Review All Data: Carefully review your own initial research from the previous step and the research provided by other AIs.
2.  Create a Master Fact Sheet: Your goal is to consolidate all information into a single, comprehensive, and fact-checked 'Master Fact Sheet'.
    * Correct Discrepancies: If you find conflicting information, use your web search ability to verify the facts and adopt the most accurate information.
    * Enrich Content: Add new, valuable details from other AI responses that you may have missed.
3.  Report Changes: Before presenting the final 'Master Fact Sheet', provide a brief, bulleted list summarizing the key changes you made. (e.g., "- Corrected the total token supply based on the official docs.", "- Added details about the consensus mechanism from AI B's response.")
4.  Output: First, the summary of changes. Second, the complete Master Fact Sheet.

## prompt3: Structured Data (JSON) Extraction (Flexible Schema) ##
# reasoning
Your Role: You are a data specialist skilled in extracting and structuring key information from text.
Instructions:
1. Convert to JSON: Based on the 'Master Fact Sheet' from the previous step, extract information according to the JSON template below.
2. Flexible Schema Application: The schema below is a mandatory checklist. If the project has important information not covered by this schema (e.g., 'Partnerships', 'Patented Technology', etc.), you are encouraged to freely extend the JSON by adding new keys.
3. Value Handling: Fields with no available information should be handled as `null` or an empty value.
4. Output: Output only the JSON code block. No other explanations are needed.

JSON Template:
{
  "projectName": "",
  "oneLiner": "",
  "tags": [],
  "overview": {
    "summary": "",
    "details": "" // Include detailed explanations, examples, nuances
  },
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
      "type": "",      // e.g., VC, Angel, Corporate, etc. ("Other" is allowed)
      "tier": "",      // null if unknown, or note as "estimated"
      "description": "",// If known: funding amount, round (Seed/Series A), notability/description
      "details": ""    // Details (e.g., investment date, strategic/financial, related articles)
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


## prompt4: JSON Data Merging and Finalization ##

# reasoning

# other_ai_info

Your Role: You are a lead data architect responsible for integrating multiple data sources to build a Single Source of Truth.
Instructions:

1.  Merge JSON: Compare and merge the JSON object you created with those from other AIs to create a single, most complete and accurate final JSON object.
2.  Merging Rules:
      * Extend Structure: If other AIs have added useful keys, include them in the final JSON.
      * Integrate and Enrich Information: For the same item, merge and enrich the information from all AIs to create the most complete content. You should not simply choose one over the other or summarize it to be shorter. For example, if one AI explained aspect A of a technology and another explained aspect B, the final output must include explanations for both A and B.
      * Preserve Details: When combining information from multiple AIs, do not just list keywords. Synthesize or replace with the most complete and detailed explanation to maintain the depth of information.
3.  Output: Output only the final merged JSON code block. All other explanations are forbidden.

## prompt5: Final Output Generation (3 Styles) ##

# reasoning

Your Role: You are a versatile content creator who produces various styles of content based on the objective.

Instructions:

1.  Use Final JSON Only: Your sole source of information is the final JSON data confirmed in the previous step. Under no circumstances should you infer, guess, or add information from other knowledge. Every sentence must be based on the data in the JSON.
2.  Output in Three Styles: Generate three types of outputs in order, according to the instructions below.

-----

[Output 1: Detailed Analysis Report]

Instruction:

  - Write a report focused on detailed information delivery, similar to the 'Master Fact Sheet' from `prompt2`.
  - Elaborate on each item in depth, based on the JSON data.

-----

[Output 2: Telegram Summary Report]

Instruction:

  - Referring to the example format below, write a concise and highly readable summary report suitable for a Telegram channel.
  - The AI should use the structure below as 'inspiration' but must freely change, add, or delete section titles and configurations to best fit the researched project.

Example Format (For Structure and Style Reference):

[Project Name]

[A one-line summary or tagline capturing the project's essence]

✨ Key Summary

  * Problem: The existing market problem this project aims to solve.
  * Solution: The differentiated technical approach this project presents.
  * Investment Point: The main reason to pay attention to this project now.

💻 What is [Project Name]?

  * Explain the project's identity and goals in the most understandable way.
  * Include realistic analogies or examples that a beginner can relate to.

🔧 How does [Core Technology] work?

  * Explain the operational principle of the project's most important technology (e.g., decentralized storage, real-time verification) step-by-step.
  * Describe sequentially, e.g., Step 1: Data Collection → Step 2: Data Validation → Step 3: Reward.

🔗 Tokenomics: $TOKEN

  * Briefly describe the token's core utility and distribution structure.

💸 What Users Can Do & Airdrop Outlook

  * Provide concrete guidance on how users can currently participate, such as using an app or running a node.
  * Assess the airdrop potential as 'High/Medium/Low' based on evidence like token issuance status, investor tendencies, and similar project precedents, and explain the reasoning.

👥 Team and Investors: Who's Building and Who's Backing?

  * Highlight the careers and expertise of notable team members.
  * Key Investors:

⚠️ Risks and Opportunities

  * Objectively analyze strengths and weaknesses compared to similar projects.
  * Specify the technical, business, or market hurdles the project must overcome to succeed.

🤝 Key Terms Explained

  * DePIN: Decentralized Physical Infrastructure Networks. A way to operate physical infrastructure like Wi-Fi, computing power, etc., using blockchain.
  * RTK: Real-Time Kinematic. A positioning technique that corrects satellite signal errors in real-time to provide centimeter-level accuracy.

🧨 Final Take

  * Conclude by summarizing the entire project in a single sentence.

Note: Again, to emphasize, sections should be freely configured to fit the project's characteristics.

-----

[Output 3: Twitter Promotional Posts (10 total)]

Instruction:

  - Write promotional tweets that highlight the project's strengths and appeal.
  - Rules:
      - Quantity: Write 5 in Korean and 5 in English, for a total of 10 tweets.
      - Content: Ensure the theme of each tweet is diverse and not too repetitive.
      - Forbidden: Absolutely no hashtags (#) or emojis.
      - Required: Naturally include the project's official Twitter handle (e.g., @GEODNET_) in the body of the tweet.
      - Style: Write in a readable format, not too short, containing as much information as possible within Twitter's character limit.