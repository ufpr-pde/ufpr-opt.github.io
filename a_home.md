---
layout: page
title: Home
permalink: /
---

### News

<div class="card container-fluid">
  {% for post in site.posts %}
  <div class="row">
    <div class="visible-xs-block col-xs-12">
      <h4> <a href="{{ post.url }}">{{ post.title }}</a>
      <small> {{ post.date | date: "%Y, %b %d" }} </small>
      </h4>
    </div>
    <div class="hidden-xs">
      <h4> <a href="{{ post.url }}">{{ post.title }}</a>
      <small> {{ post.date | date: "%Y, %b %d" }} </small>
      </h4>
      <p class="excerpt"> {{ post.excerpt | strip_html | truncatewords: 50 }}
      ... <a href="{{ post.url }}">more</a>
      </p>
    </div>
  </div>
  {% endfor %}
</div>

### Seminars - See [details](/seminars)

<div class="card container-fluid">
  {% assign events = site.data.seminars | sort: 'date' %}
  {% assign lastdate = "" %}
  {% for event in events %}
  <div class="row">
    {% if event.date != lastdate %}
  <div class="col-xs-2 text-right">
    {{ event.date | date: "%Y, %b %d" }}
  </div>
  <div class="col-xs-10">
    {% else %}
  <div class="col-xs-offset-2 col-xs-10">
    {% endif %}
    {% if event.author == "TBA" %}
  <em>Free Spot</em>
    {% else %}
  <strong>{{ event.author }}</strong>{% if event.title %} {{ event.title }}{% endif %}
    {% endif %}
  </div>
    {% assign lastdate = event.date %}
  </div>
  {% endfor %}
</div>

### Next events - See [details](/events)

<div class="card container-fluid">
  {% assign events = site.data.events | sort: 'date' %}
  <ul class="fa-ul">
    {% for event in events %}

    <li><i class="fa-li fa fa-angle-double-right"> </i>
    <a href="{{ site.baseurl }}/events/#{{ event.key }}">
    {% if event.acro %}
      <strong>{{ event.acro }}</strong> -
    {% endif %}
    <small> {{ event.name }} </small> </a>
    <br>

    {% if event.date == event.dateend %}
      {{ event.date | date: "%b %d, %Y" }}
    {% else %}
      {% assign SD = event.date | date: "%d" %}
      {% assign SM = event.date | date: "%b" %}
      {% assign ED = event.dateend | date: "%d" %}
      {% assign EM = event.dateend | date: "%b" %}
      {% assign Y = event.date | date: "%Y" %}
      {% if SM == EM %}
      {{ SM }} {{ SD }}-{{ ED }}, {{ Y }}
      {% else %}
      {{ SM }} {{ SD }} to {{ EM }} {{ ED }}, {{ Y }}
      {% endif %}
    {% endif %}
    {% if event.datesub %}
    <small> <em> (Submit by {{ event.datesub | date: "%b %d, %Y" }}) </em> </small>
    {% endif %}
    </li>
    {% endfor %}
  </ul>
</div>

