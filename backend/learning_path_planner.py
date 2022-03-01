"""
Learning Path Planner
---------------------
This module generates a simple learning roadmap for users
based on their current skill set and a target career role.

The current logic is fully rule-based, mapping known missing
skills to static learning steps. Future iterations could be
integrated with personalized AI tutors or external course APIs.
"""

LEARNING_PATHS = {
    "Python": [
        "Complete a Python fundamentals course",
        "Work on 3 beginner Python projects",
        "Learn about data structures and functions",
        "Use Python to manipulate CSV/JSON files"
    ],
    "SQL": [
        "Learn SQL syntax (SELECT, WHERE, JOIN)",
        "Practice queries on free SQL sandbox sites",
        "Explore subqueries and window functions",
        "Understand database normalization"
    ],
    "Machine Learning": [
        "Study basic ML concepts (supervised/unsupervised)",
        "Build models using scikit-learn",
        "Understand overfitting and model evaluation",
        "Read real-world case studies"
    ],
    "Excel": [
        "Master basic formulas (SUM, IF, VLOOKUP)",
        "Explore pivot tables and charts",
        "Automate tasks with macros",
        "Recreate dashboards from sample data"
    ]
}


IDEAL_SKILLS = {
    "Data Analyst": ["Python", "SQL", "Excel"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "SQL"],
    "Project Manager": ["Excel"]
}


def plan_learning_path(current_skills, target_role):
    """
    Given current user skills and a target role,
    return a list of learning steps based on missing skills.

    Args:
        current_skills (list): skills user already has
        target_role (str): target job title (must be in IDEAL_SKILLS)

    Returns:
        dict: learning roadmap {skill: [steps]}
    """
    if target_role not in IDEAL_SKILLS:
        raise ValueError("Target role not supported")

    needed = set(IDEAL_SKILLS[target_role])
    owned = set(current_skills)
    missing = needed - owned

    roadmap = {}
    for skill in missing:
        if skill in LEARNING_PATHS:
            roadmap[skill] = LEARNING_PATHS[skill]

    return roadmap


def print_learning_path(roadmap):
    """
    Nicely prints the learning roadmap to console.
    """
    if not roadmap:
        print("No missing skills! You're ready for this role.")
        return

    print("\nRecommended Learning Plan:\n")
    for skill, steps in roadmap.items():
        print(f">> {skill}")
        for idx, step in enumerate(steps, 1):
            print(f"  {idx}. {step}")
        print()


# Manual test
if __name__ == "__main__":
    current = ["Python"]
    target = "Data Analyst"
    plan = plan_learning_path(current, target)
    print_learning_path(plan)
