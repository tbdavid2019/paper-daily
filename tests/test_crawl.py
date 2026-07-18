import unittest
from datetime import date

from scripts import crawl


class CrawlHelpersTest(unittest.TestCase):
    def test_arxiv_window_is_inclusive(self):
        self.assertEqual(
            crawl.arxiv_submitted_range(date(2026, 7, 14), date(2026, 7, 18)),
            "submittedDate:[202607140000 TO 202607182359]",
        )

    def test_candidate_key_normalizes_arxiv_versions(self):
        self.assertEqual(
            crawl.candidate_key({"id": "https://arxiv.org/abs/2607.12345v2"}),
            "arxiv:2607.12345",
        )

    def test_same_day_rerun_is_repeatable_but_prior_day_is_filtered(self):
        papers = [{"id": "2607.00001", "title": "Robot"}]
        seen = {
            "arxiv:2607.00001": {
                "first_seen_on": "2026-07-18",
                "first_seen_at": "2026-07-18T02:00:00Z",
            }
        }
        self.assertEqual(len(crawl.filter_unseen(papers, seen, "2026-07-18")), 1)
        self.assertEqual(len(crawl.filter_unseen(papers, seen, "2026-07-21")), 0)

    def test_records_all_candidates_before_selection(self):
        seen = {}
        crawl.record_first_seen(
            [{"id": "2607.00002", "title": "World Model"}],
            seen,
            "2026-07-18",
            "2026-07-18T02:00:00Z",
        )
        self.assertEqual(seen["arxiv:2607.00002"]["first_seen_on"], "2026-07-18")


if __name__ == "__main__":
    unittest.main()
