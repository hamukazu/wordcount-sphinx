wordcount-sphinx
================
This Sphinx extension counts the number of the word in the current document and shows it.

This is made as a practice to develop a Sphinx extension at Pycon APAC 2013 Developper Sprints.

This is not packaged, so put the file ``count.py`` in the module path and add ``count`` to ``conf.py``. In a .rst file, write
```
.. wordcount::
```
Then you get the document like this:
```
1486 words
```
