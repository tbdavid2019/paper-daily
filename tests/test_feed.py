import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


class FeedTest(unittest.TestCase):
    def test_config_has_url_and_baseurl(self):
        config_path = ROOT / "_config.yml"
        content = config_path.read_text(encoding="utf-8")
        self.assertIn('url: "https://tbdavid2019.github.io"', content)
        self.assertIn('baseurl: "/paper-daily"', content)

    def test_feed_xml_exists_and_has_null_layout(self):
        feed_path = ROOT / "feed.xml"
        self.assertTrue(feed_path.exists())
        content = feed_path.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\nlayout: null\n---"))
        self.assertIn('<rss version="2.0"', content)
        self.assertIn('xmlns:atom="http://www.w3.org/2005/Atom"', content)
        self.assertIn('xmlns:content="http://purl.org/rss/1.0/modules/content/"', content)

    def test_feed_xsl_is_valid_xml(self):
        xsl_path = ROOT / "assets/feed.xsl"
        self.assertTrue(xsl_path.exists())
        # Parsing with ET checks well-formed XML
        tree = ET.parse(xsl_path)
        root = tree.getroot()
        self.assertIn("stylesheet", root.tag)

    def test_default_html_has_rss_autodiscovery(self):
        layout_path = ROOT / "_layouts/default.html"
        content = layout_path.read_text(encoding="utf-8")
        self.assertIn('type="application/rss+xml"', content)
        self.assertIn('href="{{ \'/feed.xml\' | absolute_url }}"', content)
        self.assertIn('nav-rss', content)

    def test_simulated_rendered_feed_is_valid_xml(self):
        feed_path = ROOT / "feed.xml"
        content = feed_path.read_text(encoding="utf-8")
        # Strip front matter
        xml_content = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)
        # Mock jekyll liquid tags for standalone XML validation
        simulated = xml_content
        simulated = simulated.replace("{{ '/assets/feed.xsl' | relative_url }}", "/paper-daily/assets/feed.xsl")
        simulated = simulated.replace("{{ site.title | xml_escape }}", "888每日論文雷達")
        simulated = simulated.replace("{{ site.description | xml_escape }}", "繁體中文研究摘要")
        simulated = simulated.replace("{{ '/' | absolute_url }}", "https://tbdavid2019.github.io/paper-daily/")
        simulated = simulated.replace("{{ '/feed.xml' | absolute_url }}", "https://tbdavid2019.github.io/paper-daily/feed.xml")
        simulated = simulated.replace('{{ site.lang | default: "zh-Hant" }}', "zh-Hant")
        simulated = simulated.replace("{{ site.time | date_to_rfc822 }}", "Thu, 01 Oct 2026 12:00:00 +0000")
        simulated = simulated.replace("{{ site.time | date_to_rfc822 }}", "Thu, 01 Oct 2026 12:00:00 +0000")
        
        # Replace the for-loop with a sample item
        loop_pattern = re.compile(r"\{% for post in site\.posts limit:30 %\}.*?\{% endfor %\}", re.DOTALL)
        sample_item = """
        <item>
          <title>每日論文雷達｜2026-10-01</title>
          <link>https://tbdavid2019.github.io/paper-daily/posts/2026/10/01/daily-paper-scout/</link>
          <guid isPermaLink="true">https://tbdavid2019.github.io/paper-daily/posts/2026/10/01/daily-paper-scout/</guid>
          <pubDate>Thu, 01 Oct 2026 00:00:00 +0000</pubDate>
          <category>embodied_ai</category>
          <description>本日重點論文摘要...</description>
          <content:encoded><![CDATA[<p>論文詳細內容</p>]]></content:encoded>
        </item>
        """
        simulated = loop_pattern.sub(sample_item, simulated)

        # Parse with ET
        root = ET.fromstring(simulated)
        self.assertEqual(root.tag, "rss")
        channel = root.find("channel")
        self.assertIsNotNone(channel)
        self.assertEqual(channel.find("title").text, "888每日論文雷達")
        item = channel.find("item")
        self.assertIsNotNone(item)
        self.assertEqual(item.find("title").text, "每日論文雷達｜2026-10-01")


if __name__ == "__main__":
    unittest.main()
