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

<div class="card container-fluid next-seminar">
<h2> Next events - See <a href="/events/">details</a> </h2>
{% assign events = site.data.events | sort: 'date' %}
<ul class="fa-ul">
  {% for event in events %}
  {% assign eventdate = event.date | date: "%Y-%m-%d" %}
  {% if eventdate < now %}
  {% continue %}
  {% endif %}

  <li><i class="fa-li fa fa-window-maximize"> </i>
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

</div>

<!--
<h3> Seminars - See [details](/seminars) </h3>

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
-->

<!--
<h3> Next events - See [details](/events) </h3>

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
-->

</div>
