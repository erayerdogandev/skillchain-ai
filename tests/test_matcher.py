"""
Test Script – Career Matcher
-----------------------------

This script manually tests the `match_career` function from
the SkillChain AI's `career_matcher` module.

Note:
- We intentionally avoid using pytest or unittest
  to keep the setup minimal for this early-stage prototype.
- Tests are written as standalone assert blocks.

Author: SkillChain AI Team
Date: 2022-11-05
"""

from backend.career_matcher import match_career


def test_basic_case():
    """
    A user with Python and SQL should match Data Analyst role.
    """
    user_skills = ["Python", "SQL"]
    matches = match_career(user_skills)

    # Expected match at the top
    assert matches[0][0] == "Data Analyst"
    assert matches[0][1] >= 2


def test_partial_overlap():
    """
    A user with only Excel should still receive Project Manager as a match.
    """
    user_skills = ["Excel"]
    matches = match_career(user_skills)

    roles = [role for role, _ in matches]
    assert "Project Manager" in roles


def test_empty_input():
    """
    An empty skill list should return no matches.
    """
    user_skills = []
    matches = match_career(user_skills)

    assert matches == []


# Run tests manually
if __name__ == "__main__":
    test_basic_case()
    test_partial_overlap()
    test_empty_input()
    print("✅ All tests passed.")

