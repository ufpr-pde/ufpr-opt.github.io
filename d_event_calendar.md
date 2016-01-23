---
layout: page
title: Event Calendar
permalink: /event-calendar/
---

{% assign events = site.data.calendar | sort: 'date' %}
{% for event in events %}
<div class="card">
<h4>
{% if event.acro %}
  <strong> {{ event.acro }} </strong> -
{% endif %}
{{ event.name }}
</h4>
at <strong> {{ event.local }} </strong>
<br>
{% if event.dateend != event.date %}
from <strong> {{ event.date | date_to_string }} </strong>
 to <strong> {{ event.dateend | date_to_string }}. </strong>
{% else %}
on <strong> {{ event.date | date_to_string }}. </strong>
{% endif %}
<br>
Submission ends
on <strong> {{ event.datesub | date_to_string }}. </strong>
<br>
More information on the
<a href="{{ event.url }}">site</a>.
</div>

{% endfor %}
