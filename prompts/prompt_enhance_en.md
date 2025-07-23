## project name ##
prompt_enhance

## metadata ##
- version: 001
- description: Analyze and improve AI prompt (.md) files

## context ##
This is a meta-prompt for systematically analyzing and enhancing prompt files (.md) used for AI collaboration.

# Target prompt types
- Analytical: Prompts for data/text analysis
- Generative: For content creation
- Transformative: For format/style changes
- Evaluative: For quality/performance assessment
- Other: Classify as you see fit

# Evaluation criteria (0-10 each)
1. Clarity: Ease of understanding and clear instructions
2. Completeness: Logical, systematic structure
3. Feasibility: AI’s ability to execute as written
4. Efficiency: Achievability in minimal steps
5. Reusability: Applicability to similar tasks

# Recursion limit
No more than 10 iterative improvements per case

# Prompt file rules
- ## project name ## and line below
- ## system prompt ## and line below
- ## context ## (optional, delimited)
- ## prompt1, prompt2... in order per project needs (AI decides count/assigns role)
- Each prompt includes role, instructions, optional items
- No project exceeds 12 steps (prompt12)
- If external AI feedback is needed, enable # other_ai_info on that step (from prompt2)
- Use # other_ai_info efficiently (not unnecessarily)
- AI must make all assumptions and resolve ambiguity itself—never ask users
- All # other_ai_info usage must refer to results from previous step(s)—never current
- All prompts execute in sequence only (no skipping)

# Option usage
- # reasoning : logs CoT
- # other_ai_info : references other AI results from prior step (prompt2+)
- # doc : attach doc
- # code : attach code
- # img : attach image
- # pdf : attach PDF

## system prompt ##
You are a meta-prompt engineer and Chain-of-Thought (CoT) expert. You excel at designing and optimizing collaborative AI prompt sets.

## prompt1: Prompt analysis and draft plan ##
# reasoning
# doc ./prompts/code_prototype.md
Role: “Prompt Diagnosis Expert”—analyze attached prompt (.md) and suggest improvements.

Chain-of-Thought:
1. Redefine the prompt’s end goal in one clear sentence
2. SWOT analysis:
   * Strengths: Well-written sections, clarity, etc.
   * Weaknesses: Vague areas, missing info, inefficiency
   * Opportunities: Improvement via CoT, stronger role assignment, etc.
   * Threats: Risks for unintended or substandard outcome
3. Suggest 3-5 improvement actions (what + why + how)
4. Project post-improvement scores per evaluation criteria (e.g. clarity 7→9, etc.)
5. State how many prompts the file will contain and assign precise roles; flag where # other_ai_info is needed

Important: Never involve user in any resolution or clarification; all ambiguity must be internally assumed/finalized and (if multiple AIs) reached by consensus.

Output: Present points 1-5 in a structured, clear report

## prompt2: Finalize comprehensive improvement blueprint ##
# reasoning
# other_ai_info
Role: “Lead Architect”—synthesize peer diagnosis strategies and finalize overall improvement plan

Instructions:
1. Compare drafts: Set your prompt1 as base, identify superior elements from peers, evaluate strengths/weaknesses
2. Integrate via CoT steps (example: list common themes, unique ideas, synthesis plan, then finalize)
3. Integrate by removing redundancy, resolving conflicts (priority: clarity > efficiency), and maximizing synergies; keep consistent style/structure
4. Ensure all AI strengths are included and that the result is practical and systematic

Output:  
Under “## Final Improvement Blueprint ##”, list the blueprint items with adoption rationale.

## prompt3: Initial prompt design per blueprint ##
# reasoning
Role: “Prompt Engineer”—write the full, systematic new prompt file as defined in your blueprint  
Instructions:
1. Study the final blueprint in prompt2
2. Compose the .md prompt file precisely as described (add nothing)
3. Produce both Korean and English draft versions  
4. Format must conform to context rules

Output:  
Under headings “==Korean Version==” and “==English Version==”, present the full prompt file as markdown blocks

## prompt4: Final prompt via peer review ##
# reasoning
# other_ai_info
Role: “QA Expert”—peer-review all designs, merge best ideas, output final version  
Instructions:
1. Use your previous as baseline
2. Critically review peer drafts (use evaluation criteria)
3. Merge improvements where justified; if none, note “No further improvements”
4. Summarize improvements and their rationale (changelog style)
5. Briefly analyze expected performance difference over original

Output:  
Under headings “==Korean Version==” and “==English Version==”, output final prompt file as markdown blocks