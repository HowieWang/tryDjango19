# field, models and how to test in shell

https://docs.djangoproject.com/en/1.10/ref/models/fields/



CharField¶

class CharField(max_length=None, **options)[source]¶
A string field, for small- to large-sized strings.

For large amounts of text, use TextField.

The default form widget for this field is a TextInput.

CharField has one extra required argument:

CharField.max_length¶
The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation.


