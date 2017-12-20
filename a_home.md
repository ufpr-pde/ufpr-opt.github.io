---
layout: page
title: Home
permalink: /
---

<div class="row">

<div class="col-xs-12 col-lg-6">
<div class="card container-fluid">

  <h2> News </h2>

  <ul class="fa-ul">
  {% for post in site.posts %}
  <li><i class="fa-li fa fa-newspaper-o"> </i>
  <a href="{{ post.url }}">{{ post.title }}</a> &nbsp;
    <span class="secondary"> {{ post.date | date: "%Y, %b %d" }} </span>
  <p class="excerpt hidden-xs"> {{ post.excerpt | strip_html | truncatewords: 50 }}
    ... <a href="{{ post.url }}">more</a>
  </p>
  </li>
  {% endfor %}
  </ul>
</div>
</div> <!-- END OF NEWS -->



<div class="col-xs-12 col-lg-6">
{% assign now = site.time | date: "%Y-%m-%d" %}

{% assign seminars = site.data.seminars | sort: 'date' %}
<div class="card container-fluid next-seminar">
<h2> Next Seminar (see <a href="/seminars">all</a>) </h2>
{% for seminar in seminars %}
{% assign semdate = seminar.date | date: "%Y-%m-%d" %}
{% if semdate > now %}

<h3>{{ seminar.author }}
<small>{{ seminar.date | date: "%Y, %b %d" }}</small>
</h3>
<span><strong>{{ seminar.title }}</strong></span><br>
<p class="text-justify">{{ seminar.abstract }}</p>

{% break %}
{% endif %}
{% endfor %}
</div>
</div>
