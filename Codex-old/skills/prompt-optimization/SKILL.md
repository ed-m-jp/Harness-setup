---
name: prompt-optimization
description: Rewrite and optimize user prompts using LLM best practices to improve clarity, reduce ambiguity, and maximize output quality while preserving the user's original intent.
---

# Prompt Optimization Skill

## Objective

Transform a user’s prompt into a high-quality, unambiguous, LLM-optimized prompt that follows modern prompt-engineering best practices and produces better results from Codex or other LLMs.

---

## When to Use

Use this skill when the user asks to:
- Optimize, refine, clarify, or rewrite a prompt
- Improve output quality from an LLM
- Apply best practices to a prompt
- Reduce ambiguity or improve instruction-following

---

## Workflow

1. **Understand Intent**
   - Carefully read the original prompt.
   - Identify the user’s true goal and expected outcome.
   - NEVER introduce new intent or assumptions.

2. **Identify Issues**
   - Ambiguity or missing context
   - Vague instructions or goals
   - Missing constraints (format, tone, length, audience)
   - Conflicting or overloaded instructions

3. **Apply LLM Best Practices**
   - Use clear, explicit instructions
   - Define role, task, and goal where helpful
   - Specify output format and structure
   - Add constraints only when they improve results
   - Prefer concrete instructions over abstract ones
   - Keep the prompt concise but complete

4. **Rewrite the Prompt**
   - Preserve the user’s intent
   - Improve clarity, specificity, and structure
   - Make the prompt robust to misinterpretation

5. **Validate**
   - Ensure the rewritten prompt is self-contained
   - Ensure it can be executed without additional clarification

---

## Output Format

Always return **both**:

### 1. Optimized Prompt
A clean, ready-to-use prompt that follows best practices.

### 2. Explanation of Improvements
A brief bullet list explaining:
- What was unclear or weak before
- What was added or changed
- How the changes improve LLM output quality

---

## Constraints

- Do NOT add domain knowledge not present in the original prompt
- Do NOT change the user’s intent
- Do NOT hallucinate requirements
- Prefer minimal improvements over over-engineering

---

## Quality Checklist (Internal)

Before finalizing, ensure the optimized prompt:
- Has a clear task and goal
- Is unambiguous
- Specifies output expectations
- Minimizes room for misinterpretation
- Would work well across multiple LLMs

---

## Example Triggers

- “Improve this prompt”
- “Rewrite this for better results”
- “Optimize this for Codex”
- “Make this prompt clearer”
- “Apply LLM best practices to this”