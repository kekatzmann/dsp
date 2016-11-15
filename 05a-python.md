# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they convey a sequence of information. However, tuples have semantic value at each position, and they cannot easily be changed (immutable). Lists on the other hand contian information of the same type, and are mutable.
>> Tuples will work as keys in dictonaries becasue they can be used to direct you to a specific location in a dataset, using their multiple levels of semantic value they (usually) have.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they both contain a sequence of information. They are different in that lists can contain duplicate entries, while sets filter out duplicates.
>> Example: The size of families that live on my street: LIST: [2, 4, 3, 2, 6, 4]; SET: [2, 6, 3, 4]
>> For finding an element, it is much quicker to use a set since your function would not need to inspect every element, including duplicates. This would be redundant and time-inefficient.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is a tool (function) used to create other functions, and is many times clearer and easier to employ than the 'def' tool.
>> Example 1: g = lambda x: x**2
>> Example 2: sorted(students, key=lambda x: x[0]) #this expression sorts the 'students' dataset by the first column of data

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are used to concisely and logically create a list. There are many different flavors of list comprehensions, but all of them follow some parameters to produce a new list. 
>> Example 1: squares = [i**2 for i in range(13)] #list of squares up to 12
>> Example 2: squares = list(map((lambda x: x**2), (arange(0,13)))) #list of squares up to 12 using map
>> Example 3: squares = list(filter((lambda x: sqrt(x) % 1 == 0), arange(0,12**2))) #list of squares up to 12 using filter
>> map and filter are similar in that they both modify lists, but map 'maps' a function to the entire list, modifying each item individually, while filter 'filters out' certain items that dont meet a specified criteria.
>> Set comprehensions are carried out similarly to lists.
>> Example (set): s = {i for i in range(10)}


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





