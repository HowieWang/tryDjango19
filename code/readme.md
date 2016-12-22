# url

- add <id> later in url part
- in url, (?P<id>\d+)
- in view function, add id=None after request, pk or id shoule followed the pattern in url,
that is a named parameter, change it to see the result 


## add href in index

    <a href="/posts/{{ obj.id }}/">{{ obj.title }}</a>  <br>

##  dynamic url

- name 
- get_absolute_url
- namespace

## error

```
posts.models.DoesNotExist: Post matching query does not exist.
[21/Dec/2016 17:21:17] "GET /posts/detail/99/ HTTP/1.1" 500 79397
```
- using get_object_or_404 to fix it.



---
## 1222 update

## modelform

1. add forms.py and class form 
2. add forms.html add form tags in it
3. first test GET, then add method to POST, BUT be care of csrf
    In the template, there is a {% csrf_token %} template tag
     inside each POST form that targets an internal URL.
     ```
     Forbidden (CSRF token missing or incorrect.): /posts/create/
    [22/Dec/2016 14:46:17] "POST /posts/create/ HTTP/1.1" 403 2502
     ```
     after add token in html page, refresh to see the result.
4. action="" means to the current url
5. add date to models
```
    print(request.POST)
    <QueryDict: {'title': ['csrf'], 'content': ['post test'],
     'csrfmiddlewaretoken': ['A4FmxW1w4wetOBzfUU0TpeFb8qh5UEKGx4rBH9WxborMRFXdBnzBgHs8eXrJgC1R']}>
also in html, every time get a new one：
    <input type="hidden" name="csrfmiddlewaretoken"
     value="PUaaCONf63Wiou45KVGJa9K9Sxx4GmRoMUWpM1IgdV9Brys3rofr1Cx6Y4HI2k8z">
```
6. put request.POST just in form 
    This field is required.
    add or None to get rid of it.

7. if form.is_valid():

8. form.cleaned_data

9. update page, then redirect url
