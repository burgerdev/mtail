mtail
=====

Format given input in columns based on regular expression patterns.

Building
========

The build uses OCaml's Oasis.

```
oasis setup -setup-update dynamic
make
```

Usage
=====

```
cat log_mentioning_fruits.txt | ./mtail.native -w 20 'apple' 'banana' 'cherry'
```

License
=======

Licensed under GPLv3.
