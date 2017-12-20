---
layout: page
title: Seminars
permalink: /seminars/
semesters:
  - 2017s1
  - 2017s2
  - 2018s1

---

<h2> Analysis and PDE  </h2>

This semester the seminars will take place at Anf B, at 11h00 am,
Fridays.

Older seminars:
<ul class="list-inline">
{% for semester in page.semesters %}
<li><button class="btn btn-primary" onclick="seminarShow('{{semester}}')">
{{semester}}
</button></li>
{% endfor %}
</ul>

<hr>

{% for semester in page.semesters %}
<div class="container-fluid seminar-show" id="{{ semester }}">
<h3> {{ semester }} </h3>
{% assign events = site.data.seminars | where: 'semester', semester | sort: 'date' %}
{% assign lastdate = "" %}

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
  <span><em> 
  {% if pres.download %}
  <a href="{{site.baseurl}}/seminar-slides/{{pres.download}}">
  {{ pres.title }}
  </a>
  {% else %}
  {{ pres.title }}
  {% endif %}
  </em></span><br>
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
</div> <!-- end div id=semeter -->

{% endfor %}
