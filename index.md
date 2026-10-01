---
layout: default
title: 文章總覽
---
<section class="hero">
  <p class="eyebrow">RESEARCH RADAR · EMBODIED AI</p>
  <h1>把每天的新論文，整理成可以閱讀的研究線索。</h1>
  <p class="hero-copy">每日讀取研究雷達資料，依研究興趣排序，再由 LLM 產生有來源、有連結的繁體中文摘要。</p>
  <div class="hero-actions">
    <a class="btn-primary" href="{{ '/feed.xml' | relative_url }}">
      <svg class="rss-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M4 11a9 9 0 0 1 9 9" />
        <path d="M4 4a16 16 0 0 1 16 16" />
        <circle cx="5" cy="19" r="1" fill="currentColor" />
      </svg>
      <span>訂閱 RSS</span>
    </a>
    <button type="button" class="btn-secondary" onclick="navigator.clipboard.writeText('https://tbdavid2019.github.io/paper-daily/feed.xml').then(()=>{const el=this.querySelector('.btn-label');el.textContent='已複製！';setTimeout(()=>{el.textContent='複製 Feed 網址'},2000)})" aria-label="複製 RSS Feed 網址">
      <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
      </svg>
      <span class="btn-label">複製 Feed 網址</span>
    </button>
  </div>
</section>

<section class="section-heading">
  <div>
    <p class="eyebrow">DAILY NOTES</p>
    <h2>最新報告</h2>
  </div>
  <span class="count">{{ site.posts.size }} 篇</span>
</section>

<section class="post-grid">
  {% for post in site.posts %}
    <article class="post-card">
      <p class="eyebrow">{{ post.date | date: "%Y.%m.%d" }} · {{ post.topic }}</p>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | strip_newlines | truncate: 180 }}</p>
      <a class="read-link" href="{{ post.url | relative_url }}">閱讀報告 <span>↗</span></a>
    </article>
  {% else %}
    <div class="empty-state">
      <h3>第一篇報告即將出現</h3>
      <p>每日 workflow 完成一次 LLM 摘要後，文章會自動發佈在這裡。</p>
    </div>
  {% endfor %}
</section>
