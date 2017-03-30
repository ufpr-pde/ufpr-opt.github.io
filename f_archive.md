---
layout: page
title: Archive
permalink: /archive/
years:
  - "2017"
  - "2016"
---

<div class="archive">
{% for year in page.years %}
<h2> {{ year }} </h2>

<ul class="fa-ul">
{% for post in site.posts %}
{% assign pyear = post.date | date: "%Y" %}
{% if year == pyear %}
<li><i class="fa-li fa fa-newspaper-o"></i>{{ post.date | date: "%Y, %b %d"}} -
<a href="{{ post.url }}">{{ post.title }}</a>
</li>
{% endif %}
{% endfor %}
</ul>

{% endfor %}
</div>
