---
layout: page
title: Team
comments: yes
permalink: /team/
---

{% assign team = site.data.team | sort: 'date' %}
{% for p in team %}
<div class="card">
  <div class="info">
  <h3> {% if p.site %}<a href="{{ p.site }}">{% endif %}
  {{ p.name }}
  {% if p.site %}</a>{% endif %}
  </h3>
  <p> {{ p.bio }} </p>
  <p class="logo">
    <a href="{{ p.lattes }}"> <img src="{{ site.baseurl }}/images/lattes.png"> </a>
    {% if p.github %}
    <a href="http://github.com/{{ p.github }}"><img src="{{ site.baseurl }}/images/github.png"> </a>
    {% endif %}
    {% if p.email %}
    <a href="mailto:{{ p.email }}"><img src="{{ site.baseurl }}/images/mail.png" alt="{{ p.email }}"> </a>
    {% endif %}
  </p>
  </div>

  <div class="photo">
    {% if p.site %}<a href="{{ p.site }}">{% endif %}
      {% if p.image %} <img src="{{ site.baseurl }}/images/{{ p.image }}">
      {% else %} <img src="{{ site.baseurl }}/images/missing.png">
      {% endif %}
    {% if p.site %}</a>{% endif %}
  </div>
  <div style="clear: both;"></div>
</div>
{% endfor %}
