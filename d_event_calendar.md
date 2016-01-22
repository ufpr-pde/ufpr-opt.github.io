---
layout: page
title: Event Calendar
comments: yes
permalink: /event-calendar/
---

{% for event in site.data.calendar %}
#### {% if event.sigla %} **{{ event.sigla }}** - {% endif %} {{ event.name }}

{% endfor %}
