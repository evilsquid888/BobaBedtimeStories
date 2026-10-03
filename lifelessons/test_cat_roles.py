"""Regression tests for Cat's active roles after story 07."""
import unittest

from check_collection import cat_role_issues


class CatRoleTests(unittest.TestCase):
    def test_early_stories_keep_original_cat(self):
        self.assertEqual(cat_role_issues("`CAT the little blue penguin napping on books`", 7), [])

    def test_missing_role_is_reported(self):
        self.assertIn("active Cat role is not declared", cat_role_issues("", 8))

    def test_helper_and_bedtime_are_allowed(self):
        md = "**Cat’s role:** helper\n`CAT the little blue penguin holds a bag`\n"
        md += "`CAT the little blue penguin asleep on her bedroom pillow`"
        self.assertEqual(cat_role_issues(md, 8), [])

    def test_evening_outing_does_not_allow_sleeping_cat(self):
        md = "**Cat’s role:** dancer\n`At the night market: CAT the little blue penguin asleep on prizes`"
        self.assertTrue(cat_role_issues(md, 15))

    def test_stale_motion_action_is_reported(self):
        md = "**Cat’s role:** helper\n`Action: CAT snuggles into a nap, while flags sway. Character: penguin.`"
        self.assertTrue(cat_role_issues(md, 9))

    def test_napkin_helper_is_not_a_nap(self):
        md = "**Cat’s role:** helper\n`CAT the little blue penguin offers a napkin`"
        self.assertEqual(cat_role_issues(md, 24), [])


if __name__ == "__main__":
    unittest.main()
