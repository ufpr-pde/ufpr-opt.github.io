---
layout: page
title: Home
permalink: /
---

### News

{% for post in site.posts %}
<div class="card">
<h4> {{ post.title }} </h4>
<p style="position: absolute; right: 1%; top: 0;">
{{ post.date | date: "%Y, %b %d" }}
</p>
<p> {{ post.excerpt }} </p>
</div>
{% endfor %}

### Next events

{{ assign events = site.data.calendar }}
{% for event in events %}
<div class="card">
{{ event.name }} - {{ event.date }}
</div>
{% endfor %}
