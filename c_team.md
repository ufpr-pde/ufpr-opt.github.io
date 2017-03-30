---
layout: page
title: Team
permalink: /team/
---

<div class="row">

{% assign team = site.data.team | sort: 'fullname' %}
{% for p in team %}
<div class="col-md-6 col-xs-12">
<div class="card container-fluid">

  <div class="photo pull-left">
    {% if p.site %}<a href="{{ p.site }}">{% endif %}
      <img class="photo img-thumbnail" src="{{ site.baseurl }}/images/{{ p.key }}.jpg" alt="{{ p.fullname }}">
    {% if p.site %}</a>{% endif %}
  </div>
  <div class="text-left">
  <!--
  <div class="col-xs-4 text-right team-info-logo">
  -->
  <span class="card-team-name">
    <a href="{{ site.baseurl }}/team/{{ p.key }}.html"> {{ p.fullname }} </a>
  </span>
  <p class="hidden-xs"> {{ p.rank }} Professor </p>

  <div class="icons">
  <a href="{{ p.lattes }}">
    <img src="{{ site.baseurl }}/images/lattes.png" alt="Lattes" title="Lattes">
  </a>
  {% if p.github %}
  <a href="http://github.com/{{ p.github }}">
    <i class="fa fa-github"></i>
  </a>
  {% endif %}
  {% if p.email %}
  <a href="mailto:{{ p.email }}">
    <i class="fa fa-envelope"></i>
  </a>
  {% endif %}
  {% if p.rgate %}
  <a href="https://www.researchgate.net/profile/{{ p.rgate }}">
    <i class="ai ai-researchgate"></i>
  </a>
  {% endif %}
  {% if p.scholar %}
  <a href="https://scholar.google.com.br/citations?user={{ p.scholar }}">
    <i class="ai ai-google-scholar"></i>
  </a>
  {% endif %}
  {% if p.orcid %}
  <a href="https://orcid.org/{{ p.orcid }}">
    <i class="ai ai-orcid"></i>
  </a>
  {% endif %}
  </div>
  </div>
</div>
</div>
{% endfor %}

</div>
