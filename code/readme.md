# url

- add <id> later in url part
- in url, (?P<id>\d+)
- in view function, add id=None after request, pk or id shoule followed the pattern in url,
that is a named parameter, change it to see the result 


## add href in index

    <a href="/posts/{{ obj.id }}/">{{ obj.title }}</a>  <br>



## error

```
posts.models.DoesNotExist: Post matching query does not exist.
[21/Dec/2016 17:21:17] "GET /posts/detail/99/ HTTP/1.1" 500 79397
```
- using get_object_or_404 to fix it.