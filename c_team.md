---
layout: page
title: Team
permalink: /team/
---

<div class="row">

{% assign team = site.data.team | sort: 'fullname' %}
{% for member in team %}
<div class="col-md-6 col-xs-12">
<div class="card container-fluid">

  <div class="photo pull-left">
    {% if member.site %}<a href="{{ member.site }}">{% endif %}
      <img class="photo img-thumbnail" src="{{ site.baseurl }}/images/{{ member.key }}.jpg" alt="{{ member.fullname }}">
    {% if member.site %}</a>{% endif %}
  </div>
  <div class="text-left">
  <!--
  <div class="col-xs-4 text-right team-info-logo">
  -->
  <span class="card-team-name">
    <a href="{{ site.baseurl }}/team/{{ member.key }}.html"> {{ member.fullname }} </a>
  </span>
  <p class="hidden-xs"> {{ member.rank }} Professor </p>

  <div class="icons">
  <a href="{{ member.lattes }}">
    <img src="{{ site.baseurl }}/images/lattes.png" alt="Lattes" title="Lattes">
  </a>
  {% include team-info.html %}
  </div>
  </div>
</div>
</div>
{% endfor %}

</div>
