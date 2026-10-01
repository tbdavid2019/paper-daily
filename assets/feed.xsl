<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:atom="http://www.w3.org/2005/Atom"
  xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes" />
  <xsl:template match="/">
    <html lang="zh-Hant">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title><xsl:value-of select="/rss/channel/title"/> · RSS Feed</title>
        <style>
          :root {
            --ink: #17211b;
            --muted: #6d776f;
            --line: #dfe5dc;
            --paper: #f6f8f3;
            --card: #ffffff;
            --accent: #d96c3f;
            --accent-deep: #9f4124;
            --max-width: 860px;
          }
          * { box-sizing: border-box; margin: 0; padding: 0; }
          body {
            color: var(--ink);
            background: radial-gradient(circle at 12% 0%, rgba(217, 108, 63, 0.08), transparent 30rem), var(--paper);
            font-family: Georgia, "Times New Roman", "Noto Serif TC", serif;
            line-height: 1.75;
            padding: 40px 20px 80px;
          }
          .container {
            max-width: var(--max-width);
            margin: 0 auto;
          }
          .feed-notice {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 24px 28px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(23, 33, 27, 0.04);
          }
          .feed-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--accent-deep);
            font: 700 0.72rem/1.2 Arial, sans-serif;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 12px;
          }
          h1 {
            font-size: 2.2rem;
            font-weight: 400;
            line-height: 1.2;
            margin-bottom: 10px;
            letter-spacing: -0.03em;
          }
          .feed-desc {
            color: var(--muted);
            font-size: 1.05rem;
            margin-bottom: 20px;
          }
          .subscribe-box {
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
          }
          .feed-url {
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 0.9rem;
            color: var(--ink);
            word-break: break-all;
          }
          .actions {
            display: flex;
            gap: 10px;
            align-items: center;
          }
          .btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            border-radius: 9999px;
            font: 700 0.78rem/1 Arial, sans-serif;
            letter-spacing: 0.04em;
            text-decoration: none;
            cursor: pointer;
            transition: all 160ms ease;
            border: 1px solid transparent;
          }
          .btn-primary {
            background: var(--ink);
            color: #fff;
          }
          .btn-primary:hover {
            background: var(--accent-deep);
          }
          .btn-outline {
            background: transparent;
            border-color: var(--line);
            color: var(--ink);
          }
          .btn-outline:hover {
            border-color: var(--muted);
          }
          .section-title {
            font-size: 1.4rem;
            font-weight: 400;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--line);
          }
          .item-list {
            display: flex;
            flex-direction: column;
            gap: 18px;
          }
          .item-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: 24px;
            box-shadow: 0 4px 16px rgba(23, 33, 27, 0.02);
            transition: transform 140ms ease, box-shadow 140ms ease;
          }
          .item-card:hover {
            box-shadow: 0 10px 24px rgba(23, 33, 27, 0.05);
          }
          .item-meta {
            color: var(--accent-deep);
            font: 700 0.72rem/1.2 Arial, sans-serif;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 8px;
          }
          .item-title {
            font-size: 1.35rem;
            font-weight: 400;
            margin-bottom: 10px;
            line-height: 1.3;
          }
          .item-title a {
            color: var(--ink);
            text-decoration: none;
          }
          .item-title a:hover {
            color: var(--accent-deep);
          }
          .item-desc {
            color: var(--muted);
            font-size: 0.96rem;
            line-height: 1.65;
            margin-bottom: 14px;
          }
          .item-link {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            color: var(--accent-deep);
            font: 700 0.76rem/1.2 Arial, sans-serif;
            letter-spacing: 0.08em;
            text-decoration: none;
            text-transform: uppercase;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="feed-notice">
            <div class="feed-badge">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M4 11a9 9 0 0 1 9 9" />
                <path d="M4 4a16 16 0 0 1 16 16" />
                <circle cx="5" cy="19" r="1" fill="currentColor" />
              </svg>
              <span>RSS 摘要來源 (Feed)</span>
            </div>
            <h1><xsl:value-of select="/rss/channel/title"/></h1>
            <p class="feed-desc"><xsl:value-of select="/rss/channel/description"/></p>
            <div class="subscribe-box">
              <div class="feed-url"><xsl:value-of select="/rss/channel/atom:link/@href"/></div>
              <div class="actions">
                <button type="button" class="btn btn-primary" onclick="navigator.clipboard.writeText(window.location.href).then(()=>{{this.textContent='已複製！';setTimeout(()=>{{this.textContent='複製 Feed 網址'}},2000)}})">
                  複製 Feed 網址
                </button>
                <a class="btn btn-outline">
                  <xsl:attribute name="href">
                    <xsl:value-of select="/rss/channel/link"/>
                  </xsl:attribute>
                  返回網站首頁
                </a>
              </div>
            </div>
          </div>

          <h2 class="section-title">最新收錄報告</h2>

          <div class="item-list">
            <xsl:for-each select="/rss/channel/item">
              <article class="item-card">
                <div class="item-meta">
                  <xsl:value-of select="pubDate"/>
                  <xsl:if test="category">
                    · <xsl:value-of select="category"/>
                  </xsl:if>
                </div>
                <h3 class="item-title">
                  <a>
                    <xsl:attribute name="href">
                      <xsl:value-of select="link"/>
                    </xsl:attribute>
                    <xsl:value-of select="title"/>
                  </a>
                </h3>
                <p class="item-desc">
                  <xsl:value-of select="description"/>
                </p>
                <a class="item-link">
                  <xsl:attribute name="href">
                    <xsl:value-of select="link"/>
                  </xsl:attribute>
                  閱讀全文 ↗
                </a>
              </article>
            </xsl:for-each>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
