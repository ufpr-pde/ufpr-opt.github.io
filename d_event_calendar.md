---
layout: page
title: Events
permalink: /events/
---

Here is a list of events of interest for the optimization community.
To submit an event to this list see our
[guide]({{ site.baseurl }}/2016/01/26/new-events.html).

Usual places to look for next events:
- [SIAM calendar](http://siam.org/meetings/calendar.php)
- [EURO calendar](https://www.euro-online.org/web/pages/460/calendar)

{% assign events = site.data.events | sort: 'date' %}
{% for event in events %}
<div class="card container-fluid">
<h4 id="{{event.key}}">
<a href="#{{ event.key }}"></a>
<a href="{{ event.url }}">
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
{% if event.datesub %}
Submissions end
on <strong> {{ event.datesub | date: "%b, %d %Y" }}. </strong>
<br>
{% endif %}
{% if event.url %}
More information on the
<a href="{{ event.url }}">site</a>.
{% else %}
We don't have a site for this event.
If you know the site, please submit to us.
{% endif %}
</div>

{% endfor %}
