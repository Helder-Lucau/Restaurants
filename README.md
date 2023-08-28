# Wk2 Code Challenge

# Phase 3 (Restaurants- without SQLAlchemy)

We have three models:

* ```Restaurant```
* ```Customer```
* ```Review```

For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many `Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.

## Deliverables

* Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
* returns the customer's given name
* returns the customer's family name
* returns the full name of the customer, with the given name and the family
* returns the restaurant's name
* returns the rating for a restaurant
* returns all of the reviews
* returns a list of all reviews for that restaurant
* Returns a **unique** list of all customers who have reviewed a particular restaurant
* Returns a **unique** list of all restaurants a customer has reviewed
* Returns the total number of reviews that a customer has authored
* returns the average star rating for a restaurant based on its reviews

## Project Setup 

### Clone the repository

```python
https://github.com/Helder-Lucau/Restaurants
```

### Navigate to the cloned repository using the command: 

```python
cd folder_name
```

### Run on terminal


## Author
* This project code files is authored by [Helder Lucau](https://github.com/Helder-Lucau).

## License

Copyright (c) 2023 [Helder Lucau](https://github.com/Helder-Lucau).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
