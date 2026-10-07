import unittest
from unittest.mock import MagicMock, patch

from scripts import decision


class DecisionTest(unittest.TestCase):
    def test_topic_questions_defined_for_embodied_and_general(self):
        q_emb = decision.get_topic_questions("embodied_ai")
        self.assertIn("is_embodied_ai", q_emb)
        self.assertIn("primary_category", q_emb)
        self.assertIn("impact_and_novelty", q_emb)
        self.assertIn("recommendation", q_emb)

        q_gen = decision.get_topic_questions("general_ai")
        self.assertIn("is_relevant", q_gen)

    def test_format_paper_state(self):
        paper = {
            "title": "RoboTest",
            "authors": ["Alice", "Bob"],
            "abstract": "We do robotic manipulation.",
        }
        state = decision.format_paper_state(paper)
        self.assertIn("Title: RoboTest", state)
        self.assertIn("Authors: Alice, Bob", state)
        self.assertIn("Abstract: We do robotic manipulation.", state)

    def test_parse_decision_summary(self):
        answers = {
            "is_embodied_ai": {"type": "noul", "noul": 0.942},
            "primary_category": {"type": "choice", "choice": "robot_manipulation", "confidence": 0.88},
            "impact_and_novelty": {"type": "score", "score": 1.25},
            "recommendation": {"type": "choice", "choice": "must_read"},
        }
        summary = decision.parse_decision_summary(answers, provider="jev")
        self.assertEqual(summary["provider"], "jev")
        self.assertEqual(summary["relevance_prob"], 0.942)
        self.assertEqual(summary["primary_category"], "robot_manipulation")
        self.assertEqual(summary["novelty_score"], 1.25)
        self.assertEqual(summary["recommendation"], "must_read")

    def test_calculate_decision_score_and_reranking(self):
        p1 = {
            "id": "must_read_p",
            "priority": 10,
            "decision": {
                "relevance_prob": 0.95,
                "novelty_score": 1.8,
                "recommendation": "must_read",
                "primary_category": "robot_manipulation",
            },
        }
        p2 = {
            "id": "non_embodied_p",
            "priority": 90,  # high crawler priority due to accidental keywords
            "decision": {
                "relevance_prob": 0.1,
                "novelty_score": 0.2,
                "recommendation": "skip",
                "primary_category": "non_embodied",
            },
        }
        p1["decision_score"] = decision.calculate_decision_score(p1["decision"])
        p2["decision_score"] = decision.calculate_decision_score(p2["decision"])

        self.assertGreater(p1["decision_score"], 70.0)
        self.assertLess(p2["decision_score"], 10.0)

        reranked = decision.rerank_papers([p2, p1])
        self.assertEqual([p["id"] for p in reranked], ["must_read_p", "non_embodied_p"])

    @patch.object(decision.DecisionClient, "_call_systemone")
    def test_fallback_when_jev_fails(self, mock_call):
        # 第一次呼叫 (Jev) 拋出異常，第二次呼叫 (Clef) 成功回傳
        mock_call.side_effect = [
            RuntimeError("Jev 503 Service Unavailable"),
            {
                "model": "clef-flash",
                "answers": {
                    "is_embodied_ai": {"type": "noul", "noul": 0.91},
                    "primary_category": {"type": "choice", "choice": "robot_manipulation"},
                },
            },
        ]
        client = decision.DecisionClient(
            jev_api_key="mock_key",
            jev_url="https://api.typesafe.ai/v1/systemone",
            clef_url="https://clef.aiurl.tw/v1/systemone",
        )
        res = client.decide("state", {})
        self.assertEqual(res["provider"], "clef")
        self.assertEqual(res["model"], "clef-flash")
        self.assertEqual(mock_call.call_count, 2)


if __name__ == "__main__":
    unittest.main()
