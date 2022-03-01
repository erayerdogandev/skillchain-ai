"""
Career Matcher Module
---------------------
This module takes in a list of extracted skills and maps them to potential
career paths based on predefined logic.

The mapping is currently based on simple rule-based checks against known
career profiles. In a real-world version, this would be replaced by a
machine learning or embedding-based similarity engine.
"""

# Sample mapping of careers to required skills
CAREER_SKILL_MAP = {
    "Data Analyst": ["Python", "SQL", "Excel", "Data Analysis"],
    "Frontend Developer": ["JavaScript", "React", "HTML", "CSS"],
    "Project Manager": ["Communication", "Leadership", "Excel", "Project Management"],
    "Machine Learning Engineer": ["Python", "TensorFlow", "Machine Learning", "Data Analysis"],
    "Business Analyst": ["Excel", "SQL", "Communication", "Data Analysis"]
}

def match_skills_to_careers(user_skills):
    """
    Matches a given list of skills to possible career paths based on the number
    of overlapping skills with predefined career profiles.

    Args:
        user_skills (list): List of strings representing user skills.

    Returns:
        list: Sorted list of matched career paths with match scores.
    """
    results = []

    for career, required_skills in CAREER_SKILL_MAP.items():
        score = len(set(user_skills) & set(required_skills))
        if score > 0:
            results.append((career, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def pretty_print_matches(matches):
    """
    Prints matched careers with visual score.

    Args:
        matches (list): List of tuples (career, score)
    """
    print("Possible career matches:")
    for career, score in matches:
        print(f"- {career} (match score: {score})")
    user_input_skills = ["Python", "Excel", "Project Management", "Communication"]
    matched = match_skills_to_careers(user_input_skills)
    pretty_print_matches(matched)

# For manual test
if __name__ == "__main__":

