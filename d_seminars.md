---
layout: page
title: Seminars
permalink: /seminars/
---

<h2> Optimization and Numerical Analysis </h2>

This semester the seminars will take place on the Anfiteatro A, at 15h30,
Fridays.

<hr>

{% assign events = site.data.seminars | sort: 'date' %}
{% assign lastdate = "" %}

<div class="container-fluid">
{% for pres in events %}
<div class="row">
{% if pres.date != lastdate %}
  <div class="col-md-2">
  <em> {{ pres.date | date: "%b. %d, %Y" }}: </em> <br>
  </div>
  <div class="col-md-10">
{% else %}
  <div class="col-md-offset-2 col-md-10">
{% endif %}
{% if pres.author == "TBA" %}
  <span><strong> Free Spot </strong></span>
  <p> Contact us if you'd like to give a talk </p>
{% else %}
  <span><strong> {{ pres.author }} </strong></span> - 
  <span> {{ pres.affiliation }} </span><br>
{% if pres.title %}
  <p>
  <span><em> {{ pres.title }} </em></span><br>
    {% if pres.abstract %}
  <small>{{ pres.abstract }}</small><br>
    {% endif %}
  </p>
{% else %}
<br>
{% endif %}
    {% endif %}
  </div>
{% assign lastdate = pres.date %}
</div>
{% endfor %}
</div>
