# queryset

## debug in vscode

- add python path, env is ok, windows using \\
- --reload is default for debug, so keep it

```
            "name": "Django",
            "type": "python",
            "request": "launch",
            "stopOnEntry": true,
            "pythonPath": "${config.python.pythonPath}",
            "program": "${workspaceRoot}/code/manage.py",
            "cwd": "${workspaceRoot}",
            "args": [
                "runserver",
                "--noreload"
            ],
```

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

## errors

> IntegrityError: NOT NULL constraint failed: posts_post.timestamp
- null=True

```
IntegrityError: NOT NULL constraint failed: posts_post.timestamp

In [3]: Post.objects.create(title='haha', content='lalalllaa')
Out[3]: <Post: haha>

In [4]: Post.objects.create(title='haha', content='lalalllaa')
Out[4]: <Post: haha>

In [5]: Post.objects.create(title='haha', content='lalalllaa')
Out[5]: <Post: haha>

In [6]: Post.objects.create(title='haha', content='lalalllaa')
Out[6]: <Post: haha>

In [7]: Post.objects.create(title='haha', content='lalalllaa')
Out[7]: <Post: haha>

In [8]: Post.objects.all()
Out[8]: <QuerySet [<Post: title>, <Post: haha>, <Post: haha>, <Post: haha>, <Post: haha>, <Post: haha>]>
```

------
> later:

- add <id> later in url part
- in url, (?P<id>\d+)
- in view function, add id=None after request, pk or id shoule followed the pattern in url,
that is a named parameter