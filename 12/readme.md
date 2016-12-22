# order and pagination

## order

- order_by in view
        obj_list = Post.objects.all().order_by("-updated")

- using Meta in model
        class Meta:
            ordering = ["-timestamp", "-updated"]

---
## paginator

https://docs.djangoproject.com/en/1.10/topics/pagination/

