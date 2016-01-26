---
layout: page
title: Events
permalink: /events/
---

Here is a list of events of interest for the optimization community.
To submit an event to this list see our
[guide]({{ site.baseurl }}/2016/01/26/new-events.html).

{% assign events = site.data.events | sort: 'date' %}
{% for event in events %}
<div class="card">
<h4 id="{{event.key}}">
<a href="#{{ event.key }}">
{% if event.acro %}
  <strong> {{ event.acro }} </strong> -
{% endif %}
{{ event.name }}
</a>
</h4>
at <strong> {{ event.venue }} </strong>
<br>
{% if event.dateend != event.date %}
from <strong> {{ event.date | date: "%b, %d %Y" }} </strong>
 to <strong> {{ event.dateend | date: "%b, %d %Y" }}. </strong>
{% else %}
on <strong> {{ event.date | date: "%b, %d %Y" }}. </strong>
{% endif %}
<br>
Submission ends
on <strong> {{ event.datesub | date: "%b, %d %Y" }}. </strong>
<br>
More information on the
<a href="{{ event.url }}">site</a>.
</div>

{% endfor %}
