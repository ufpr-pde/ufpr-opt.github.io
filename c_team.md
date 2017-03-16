---
layout: page
title: Team
permalink: /team/
---

{% assign team = site.data.team | sort: 'fullname' %}
{% for p in team %}
<div class="card container-fluid">

  <div class="col-xs-4 col-md-2">
  <div class="pull-left">
    {% if p.site %}<a href="{{ p.site }}">{% endif %}
      <img class="photo img-thumbnail" src="{{ site.baseurl }}/images/{{ p.key }}.jpg" alt="{{ p.fullname }}">
    {% if p.site %}</a>{% endif %}
  </div>
  </div>
  <div class="col-xs-4 col-md-6">
  <h4> <a href="{{ site.baseurl }}/team/{{ p.key }}.html"> {{ p.fullname }} </a> </h4>
  <p> {{ p.rank }} Professor </p>
  </div>

  <div class="col-xs-4 text-right team-info-logo">
    <a href="{{ p.lattes }}">
      <img src="{{ site.baseurl }}/images/lattes.png" alt="Lattes" title="Lattes">
    </a>
    {% if p.github %}
    <a href="http://github.com/{{ p.github }}">
      <i class="fa fa-github fa-3x"></i>
    </a>
    {% endif %}
    {% if p.email %}
    <a href="mailto:{{ p.email }}">
      <i class="fa fa-envelope fa-3x"></i>
    </a>
    {% endif %}
    {% if p.rgate %}
    <a href="https://www.researchgate.net/profile/{{ p.rgate }}">
      <i class="ai ai-researchgate ai-3x"></i>
    </a>
    {% endif %}
    {% if p.scholar %}
    <a href="https://scholar.google.com.br/citations?user={{ p.scholar }}">
      <i class="ai ai-google-scholar ai-3x"></i>
    </a>
    {% endif %}
    {% if p.orcid %}
    <a href="https://orcid.org/{{ p.orcid }}">
      <i class="ai ai-orcid ai-3x"></i>
    </a>
    {% endif %}
  </div>
  <div style="clear: both;"></div>
</div>
{% endfor %}
