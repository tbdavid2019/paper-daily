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


if __name__ == "__main__":
    unittest.main()
