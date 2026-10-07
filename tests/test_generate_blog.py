import unittest

from scripts import generate_blog


class GenerateBlogTest(unittest.TestCase):
    def test_select_papers_uses_deterministic_priority_order(self):
        papers = [
            {"id": "low", "priority": 10, "keyword_hits": 4, "sources": ["a", "b"]},
            {"id": "high", "priority": 80, "keyword_hits": 1, "sources": ["a"]},
            {"id": "middle", "priority": 40, "keyword_hits": 9, "sources": ["a", "b", "c"]},
        ]
        selected = generate_blog.select_papers(papers, 2)
        self.assertEqual([paper["id"] for paper in selected], ["high", "middle"])

    def test_select_papers_prioritizes_decision_score(self):
        papers = [
            {"id": "high_prio_no_dec", "priority": 99, "decision_score": 0.0},
            {"id": "lower_prio_high_dec", "priority": 10, "decision_score": 85.5},
        ]
        selected = generate_blog.select_papers(papers, 2)
        self.assertEqual([paper["id"] for paper in selected], ["lower_prio_high_dec", "high_prio_no_dec"])

    def test_compact_paper_includes_decision_metadata(self):
        paper = {
            "id": "2609.12345",
            "title": "Robot Policy",
            "decision": {"relevance_prob": 0.95, "primary_category": "robot_manipulation"},
            "decision_score": 88.0,
        }
        compact = generate_blog.compact_paper(paper)
        self.assertIn("decision", compact)
        self.assertEqual(compact["decision_score"], 88.0)

    def test_extracts_openai_message_content(self):
        response = {
            "choices": [{"message": {"content": "## 今日概況\nOK"}}]
        }
        self.assertEqual(generate_blog.extract_text(response), "## 今日概況\nOK")

    def test_extracts_gemini_candidate_parts(self):
        response = {
            "candidates": [{"content": {"parts": [{"text": "OK"}]}}]
        }
        self.assertEqual(generate_blog.extract_text(response), "OK")

    def test_cleans_markdown_wrappers_and_front_matter(self):
        body = "```markdown\n---\ntitle: Wrong\n---\n## 今日概況\n內容\n```"
        self.assertEqual(generate_blog.clean_markdown(body), "## 今日概況\n內容")

    def test_render_post_contains_safe_front_matter(self):
        post = generate_blog.render_post("2026-08-20", "embodied_ai", "## 今日概況\n內容")
        self.assertIn('layout: post', post)
        self.assertIn('title: "每日論文雷達｜2026-08-20"', post)
        self.assertIn("topic: \"embodied_ai\"", post)
        self.assertTrue(post.endswith("\n"))

    def test_missing_sections_are_detected_and_filled_honestly(self):
        body = "## 今日概況\n內容\n\n## Must-Read\n內容"
        missing = generate_blog.missing_sections(body)
        self.assertIn("Idea Sparks", missing)
        completed = generate_blog.ensure_required_sections(body)
        self.assertIn("## Idea Sparks", completed)
        self.assertIn("資料未提供", completed)


if __name__ == "__main__":
    unittest.main()
