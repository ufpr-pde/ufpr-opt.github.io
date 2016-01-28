---
layout: page
title: Home
permalink: /
---

### Next events - See [all events](/events)

<div class="card">
<div class="content hideContent">
{% assign events = site.data.calendar %}
<ul>
{% for event in events %}
 <li> {{ event.date | date: "%Y, %b %d" }} -
 <a href="{{ site.baseurl }}/events/#{{ event.key }}">
 {{ event.name }} </a> </li>
{% endfor %}
</ul>
</div>
<div class="show-more">
  <a href="#">more</a> 
</div>
</div>

### News

{% for post in site.posts %}
<div class="card">
<h4> <a href="{{ post.url }}">{{ post.title }}</a> </h4>
<p style="position: absolute; right: 1%; top: 0;">
{{ post.date | date: "%Y, %b %d" }}
</p>
<p class="excerpt"> {{ post.excerpt | strip_html | truncatewords: 50 }}
... <a href="{{ post.url }}">more</a>
</p>
</div>
{% endfor %}
