---
layout: post
title: Submitting New Events
---

<strong>
If you know what to do already, [here is the
link](https://github.com/ufpr-opt/ufpr-opt.github.io/blob/master/_data/events.yml).
</strong>

<hr>

We generate our events list automatically from a
[YAML](http://www.yaml.org/) file.
The file we use specifically is
[this](https://github.com/ufpr-opt/ufpr-opt.github.io/blob/master/_data/events.yml).

To submit a new event, all you have to do it

 - Create a [GitHub](http://github.com) account;
 - On the [page of the
   file](https://github.com/ufpr-opt/ufpr-opt.github.io/blob/master/_data/events.yml),
   click the **edit button (a pencil)** close to the buttons `Raw`, `Blame` and
   `History`;
 - Create a new event following the **pattern** (see below);
 - Create a **pull request** in the bottom (you'll see a green button).
   A good message for the pull request would be be
   "Create event ACRONYM".

## Event entry pattern

The necessary entries for the event are

 - `name`: The name of the event;
 - `key`: Unique string used internally; (Lowercase alphanumeric preferred)
 - `venue`: The conference venue (Country required if not in Brazil);
 - `date`: First day of the event; (YYYY-MM-DD)
 - `dateend`: Last day of the event; (YYYY-MM-DD)

Optional keys for the event

 - `acro`: Acronym of the event. Very helpful having one;
 - `datesub`: Last day for submitting abstracts or similar;
 - `url`: the event's website;
 - `keywords`: Comma-separated keywords for the event. We are not using this
   yet.
