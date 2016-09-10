---
layout: page
title: Team
permalink: /team/
---

{% assign team = site.data.team | sort: 'date' %}
{% for p in team %}
<div class="card container-fluid">

  <div class="info col-md-8">
  <h3> <a href="{{ site.baseurl }}/team/{{ p.key }}.html"> {{ p.fullname }} </a> </h3>
  <p> {{ p.bio }} </p>
  </div>

  <div class="col-md-4 text-right">
    <a href="{{ p.lattes }}"> <img class="logo" src="{{ site.baseurl }}/images/lattes.png" alt="Lattes"> </a>
    {% if p.github %}
    <a href="http://github.com/{{ p.github }}"><img class="logo" src="{{ site.baseurl }}/images/github.png" alt="GitHub"> </a>
    {% endif %}
    {% if p.email %}
    <a href="mailto:{{ p.email }}"><img class="logo" src="{{ site.baseurl }}/images/mail.png" alt="{{ p.email }}"> </a>
    {% endif %}

    <div class="pull-right">
      {% if p.site %}<a href="{{ p.site }}">{% endif %}
        {% if p.image %}
          {% assign img = p.image %}
        {% else %}
          {% assign img = "missing.png" %}
        {% endif %}
        <img class="photo img-responsive img-circle" src="{{ site.baseurl }}/images/{{ img }}" alt="{{ p.fullname }}">
      {% if p.site %}</a>{% endif %}
      </div>
    </div>
  <div style="clear: both;"></div>
</div>
{% endfor %}
