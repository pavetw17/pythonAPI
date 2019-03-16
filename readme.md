# Python API
## restful.py is a simple Python API

## app.py is a simple web for routing (login.html, bootstrap.min.css)

## script1.py ( includes main.css, about.html, home.html, and layout.html)

## Pythonic way to combine FOR loop and IF statement
### Case 1:
```
>>> a = [2,3,4,5,6,7,8,9,0]
... xyz = [0,12,4,6,242,7,9]
... for x in xyz:
...     if x in a:
...         print(x)
0,4,6,7,9

print([x for x in xyz if x in a])
```

### Case 2:
```
gen = (x for x in xyz if x not in a)
```

