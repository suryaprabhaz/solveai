import { EditorContext } from '../types';

export function buildSolvePrompt(context: EditorContext): string {
  return `You are SolveAI, a programming practical assistant.

Your task is to solve the user's coding question.

Rules:
1. Give the simplest correct solution.
2. Return complete executable code when code is requested.
3. Preserve the requested programming language.
4. Do not unnecessarily change the user's requirements.
5. Prefer practical-exam-friendly code.
6. Avoid unnecessary libraries.
7. Do not add long explanations unless requested.
8. If the question asks for code, return the code first.
9. Do not wrap the answer in unnecessary conversational text.
10. Never claim that code was executed unless it actually was.

Programming language: ${context.language}

User question:
${context.text}

Return the best answer.`;
}

export function buildFixPrompt(context: EditorContext): string {
  return `Fix the following code.

Requirements:
- Preserve the intended functionality.
- Make the smallest necessary changes.
- Return corrected code only.
- Do not rewrite unnecessarily.
- If there is a bug, fix it without changing working parts.

Language: ${context.language}

Code:
${context.text}

Return only the fixed code.`;
}

export function buildExplainPrompt(context: EditorContext): string {
  return `Explain the following code clearly and concisely.

Language: ${context.language}

Code:
${context.text}

Provide a clear explanation of what this code does, how it works, and any important details.`;
}

export function stripCodeFences(text: string, shouldStrip: boolean): string {
  if (!shouldStrip) {
    return text;
  }

  // Remove opening fence with optional language tag
  const stripped = text
    .replace(/^```[\w]*\n?/m, '')
    .replace(/\n?```\s*$/m, '')
    .trim();

  // If the entire string is wrapped in a fence, return stripped version
  // Otherwise return original trimmed
  const originalTrimmed = text.trim();
  if (originalTrimmed.startsWith('```') && originalTrimmed.endsWith('```')) {
    return stripped;
  }

  // Handle case where response has multiple code blocks, take first
  const fenceMatch = originalTrimmed.match(/```[\w]*\n([\s\S]*?)```/);
  if (fenceMatch && fenceMatch[1]) {
    return fenceMatch[1].trim();
  }

  return originalTrimmed;
}
