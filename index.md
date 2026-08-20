---
layout: default
title: 文章總覽
---
<section class="hero">
  <p class="eyebrow">RESEARCH RADAR · EMBODIED AI</p>
  <h1>把每天的新論文，整理成可以閱讀的研究線索。</h1>
  <p class="hero-copy">每日讀取研究雷達資料，依研究興趣排序，再由 LLM 產生有來源、有連結的繁體中文摘要。</p>
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
