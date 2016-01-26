---
layout: post
title: Submitting New Events
---

Here is a quick guide to submitting new events.

We generate our events list automatically from a
[YAML](http://www.yaml.org/) file.
The file we use specifically is
[this](https://github.com/ufpr-opt/ufpr-opt.github.io/blob/master/_data/events.yml).
The easiest way you have to do to submit a new event is

 - Create a [GitHub](http://github.com) account;
 - On the [page of the
   file](https://github.com/ufpr-opt/ufpr-opt.github.io/blob/master/_data/events.yml),
   click the edit button (a pencil) close to the buttons `Raw`, `Blame` and
   `History`;
 - Create an entry following the pattern;
 - Create a pull request in the bottom (you'll see a green button).

The necessary entries for the event are

 - `name`: The name of the event;
 - `key`: Unique string used internally; (Lowercase alphanumeric preferred)
 - `venue`: The conference venue (Country required if not in Brazil);
 - `date`: First day of the event; (YYYY-MM-DD)
 - `dateend`: Last day of the event; (YYYY-MM-DD)
 - `datesub`: Last day for submitting abstracts or similar;
 - `url`: the event website.

Optional keys for the event

 - `acro`: Acronym of the event. Very helpful having one.
 - `keywords`: Comma-separated keywords for the event. We are not using this
   yet.

When your pull request is created, I'll download it and complete the steps
required.
However, keep reading if you want to know and do more.

A more complete way to submit a new event requires you to know some
[git](http://git-scm.com/), which is a great tool to know, and also
have [Python 3](https://www.python.org/) installed.
Then you

 - Clone the [repositoty](https://github.com/ufpr-opt/ufpr-opt.github.io);
 - Update the `_data/events.yml` file;
 - Run the python script `create-calendar.py` generating a file `calenday.yml`;
 - Commit your modifications and submit a PR or e-mail the patch to me on
   `abelsiqueira` at `ufpr.br`.

If done correctly, I can accept your event directly.
