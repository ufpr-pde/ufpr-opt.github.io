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

<div class="container-fluid">
{% for pres in events %}
  <div class="col-md-2">
    <em> {{ pres.date | date: "%b. %d, %Y" }}: </em> <br>
  </div>
  <div class="col-md-10">
    <span><strong> {{ pres.title }} </strong></span><br>
    <span><em> {{ pres.author }} </em></span>
    <p> {{ pres.abstract }} <br>
    </p>
  </div>
{% endfor %}
</div>
