# Programming tasks for interview.

## Task 1 - FizzBuzz
Located in ardigen_1.py
### Requirements
Write a program that prints the integers from n to m (inclusive), but
* for multiples of three, print Fizz (instead of the number)
* for multiples of five, print Buzz (instead of the numbe
* for multiples of both three and five, print FizzBuzz (instead of the numbe
Input numbers need to satisfy condition 1 <= n < m <= 10000.
#### Input
Two numbers in two lines (n, m).
#### Output
One result per line as described in requirements.
Sample input:
```
3
16
```
Sample output:
```
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```

## Task 2 - Valuation service
Run via ardigen_2_main.py
Unit tests are located in unit_tests.py.
### Requirements
You are building a valuation service.
Read the input data. From products with particular matching_id take those with the highest total
price (price * quantity), limit data set by top_priced_count and aggregate prices.
Unit tests are required.
Input
In the input there are three files containin
* data.csv - product representation with price,currency,quantity,matching_id
* currencies.csv - currency code and ratio to PLN, ie. GBP,2.4 can be converted to PLN as
follows 1 PLN * 2.4
* matchings.csv - matching data matching_id,top_priced_count
Output
Save the results as top_products.csv. Output file shall have five columns: 
```
matching_id, total_pr, avg_price, currency, ignored_products_count
```
