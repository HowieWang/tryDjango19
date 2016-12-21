# queryset

## shell

```
.all
.create
.filter
__contains
```


## for in templates

```
{% for obj in obj_list %}
{{ obj.abc }}
{% endfor %}
```

## queryset in views.py

- detail
- new page of detail

------
> later:

- add <id> later in url part
- in url, (?P<id>\d+)
- in view function, add id=None after request, pk or id shoule followed the pattern in url,
that is a named parameter