# static

[https://www.youtube.com/watch?v=YH-ipgxlJzs&index=25&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy](https://www.youtube.com/watch?v=YH-ipgxlJzs&index=25&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
Your project will probably also have static assets that aren’t tied to a particular app. In addition to 
using a static/ directory inside your apps, you can define a list of directories (STATICFILES_DIRS)
 in your settings file where Django will also look for static files. For example:

 ```
 STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
```

---
STATICFILES_DIRS in settings

---
add debug in urls.py

---

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')

---
change <link rel="stylesheet" href="/static/css/my.css">
to
<link rel="stylesheet" href="{% static '/css/my.css' %}">


---


---
## error

```
{% load staticfiles %}
{% extends 'base.html' %}
```
TemplateSyntaxError at /posts/create/
<ExtendsNode: extends 'base.html'> must be the first tag in the template.
