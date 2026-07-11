---
layout: default
title: Journal
permalink: /journal/
---

# Journal

{% assign entries = site.journal | sort: "date" | reverse %}
{% if entries.size > 0 %}
<ol class="journal-list">
  {% for entry in entries %}
  <li>
    <a href="{{ entry.url | relative_url }}">{{ entry.title }}</a>
    <time datetime="{{ entry.date | date_to_xmlschema }}">{{ entry.date | date: "%B %-d, %Y" }}</time>
    {% if entry.tags %}
    <span class="journal-tags">{% for tag in entry.tags %}<span>{{ tag }}</span>{% endfor %}</span>
    {% endif %}
  </li>
  {% endfor %}
</ol>
{% else %}
The journal is still empty.
{% endif %}
