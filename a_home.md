---
layout: page
title: Home
permalink: /
---

### Seminars - See [details](/seminars)

<div class="card container-fluid">
  {% assign events = site.data.seminars %}
  <ul class="fa-ul">
    {% for event in events %}
    <li><i class="fa-li fa fa-angle-double-right"> </i>{{ event.date | date: "%Y, %b %d" }} -
    <em>{{ event.author }}</em>: {{ event.title }}
    </li>
    {% endfor %}
  </ul>
</div>

### Next events - See [details](/events)

<div class="card container-fluid">
  {% assign events = site.data.calendar %}
  <ul class="fa-ul">
    {% for event in events %}
    <li><i class="fa-li fa fa-angle-double-right"> </i>{{ event.date | date: "%Y, %b %d" }} -
    <a href="{{ site.baseurl }}/events/#{{ event.key }}"> {{ event.name }} </a> </li>
    {% endfor %}
  </ul>
</div>

### News

{% for post in site.posts %}
<div class="card container-fluid">
<h4> <a href="{{ post.url }}">{{ post.title }}</a> </h4>
<p style="position: absolute; right: 1%; top: 0;">
{{ post.date | date: "%Y, %b %d" }}
</p>
<p class="excerpt"> {{ post.excerpt | strip_html | truncatewords: 50 }}
... <a href="{{ post.url }}">more</a>
</p>
</div>
{% endfor %}
