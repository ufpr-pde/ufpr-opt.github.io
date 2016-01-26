---
layout: page
title: Home
permalink: /
---

### Next events - See [all events](/events)

<div class="card">
{% assign events = site.data.calendar %}
<ul>
{% for event in events limit: 5%}
 <li> {{ event.date | date: "%Y, %b %d" }} - {{ event.name }} </li>
{% endfor %}
</ul>
</div>

### News

{% for post in site.posts %}
<div class="card">
<h4> <a href="{{ post.url }}">{{ post.title }}</a> </h4>
<p style="position: absolute; right: 1%; top: 0;">
{{ post.date | date: "%Y, %b %d" }}
</p>
<p> {{ post.excerpt }} </p>
</div>
{% endfor %}

