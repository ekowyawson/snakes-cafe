# Lab: Class 1

## Project: Intro to Python

### Author: Ekow Yawson

This is a command line utility which will mimic the functionality of a point of sale restaurant system using basic Python tools.

### Feature Tasks and Requirements

* When run, the program should print an intro message and the menu for the restaurant
* The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
* The program should prompt the user for an order
* When a user enters an item, the program should print an acknowledgment of their input
* The program should tell the user how to exit
* The program’s content should match included sample exactly
  * The > character represents user input line and should be printed out with a trailing space.

```bash
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**************************************
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
```

#### Entering an order

```bash
***********************************
** What would you like to order? **
***********************************
> Cake

** 1 order of Cake has been added to your meal **

> Cake

** 2 orders of Cake have been added to your meal **
```

#### Exiting

```bash
> quit
```
