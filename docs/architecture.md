# SkillChain AI – Architecture Overview

> This document outlines the modular architecture of SkillChain AI, as originally conceived in 2022. The platform is designed to simulate a personalized career guidance engine based on AI-driven skill mapping and recommendation.

---

## 🧠 System Components

### 1. **Skill Extractor**
- Input: Unstructured user text (e.g. resume, bio, free-form input)
- Method: Token-based keyword matching (future: LLM-powered)
- Output: Structured list of user skills

### 2. **Career Matcher**
- Input: Extracted skills
- Method: Rule-based mapping to career profiles
- Output: Ranked list of career matches with confidence scores

### 3. **Learning Path Planner**
- Input: Target career, current skills
- Method: Compares against ideal role requirements
- Output: Ordered roadmap of learning steps (text-based)

---

## 🔄 Data Flow

