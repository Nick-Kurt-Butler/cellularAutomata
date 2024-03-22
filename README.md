# Introduction
One and Two Dimensional Cellular Automata

The code for the figures below is given in the Python Jupyter Notebook cellularAutomate.ipynb 

Many of the figures in the repository are inspired by those in Stephen Wolfram's _A New Kind of Science_

# Standard 1 Dimensional Cellular Automata
Starting with the most basic example, the rules are simple.  We call this one
dimensional because we update a 1D array with each call of the rule.  The update
process when we have a radius of one relies on the fact that the state of the
3 cells above determines the state of the cell below.  To know how to interpret
the 3 cells we have to define a rule.  In our simple case of radius 1 and a binary
base.  We will have a total of 256 rules.  This is derived from the fact that
any three cell can have 8 different states and each of the cells can either
be on or off.  An example of rule 150 is shown below.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/Nick-Kurt-Butler/cellularAutomata/master/media/RuleBlock150.jpg" />
</p>

As you can see above there are 8 differents type of 3 cell arrays.  The cell
below each of these is determined by the rule number, is this case 150.
In binary we have that 150 is equal to 0b10010110.  Looking at the ones as
black cells and the zeros as white cells we have that in the picture above
we started with the least significant bit where there are all whites cells and
ended with the most significant bit where there are all black cells. Below
shows two rows.  The first is a randomly genrated array and the second is the
updated array based on rule 150.

<p align="center">
  <img src="https://raw.githubusercontent.com/Nick-Kurt-Butler/cellularAutomata/master/media/Rule150Rows2rand.png">
</p>

Note that the updated array loses two extra cells on either side of the array.
This is due to the radius being equal to 1.  If the radius equals n then we lose
2n with each update of the array.  In the figure below we show rule 150 after
25 iterations. We start with one black cell and assume an infinite amount of 
white cells surrounding the black cell to bypass the information limit of assigning
random colors to an infinite number of cells.  Then we zoom in on a 25 by 50 slice
of our set of rows.

<p align="center">
  <img src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/Rule150Rows25.png" />
</p>

And here is rule 150 with random initial conditions.

<p align="center">
  <img align="center" src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/Rule150Rows25Rand.png" />
</p>
These are the most interesting rules of the 256

<p align="center">
  <img src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/4StandardRules.png" />
</p>

To see all 256 more click on the links below.

[Standard Cellular Automata 256 Rules](https://raw.githubusercontent.com/Nick-Kurt-Butler/cellularAutomata/master/media/1D_Cell_Auto.pdf)]

[Standard Cellular Automata Random Initial Conditions](https://raw.githubusercontent.com/Nick-Kurt-Butler/cellularAutomata/master/media/1D_Cell_Auto_Random_IC.pdf)]

## Higher Radii
I mentioned before that there is an opportunity to change the radius of a rule. 
In the examples until now the radii have all been one.  Below is an example of
a rule (rule 2624667310) with a radius of two, and notice that it grows much faster than the rules
of radius one.
<p align="center">
  <img src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/Radius2Standard.png" />
</p>
Here is an example of a rule of radius 2 and random initial conditions
<p align="center">
  <img src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/Rule4067213884.png" />
</p>
Higher order radii have massive amounts of rules and tend to not produce meaningful 
figures. This is because, given a radius r, the number of rules for a base 2 set is 2<sup>2<sup>2r+1</sup></sup>.

## Using Logical Statements

Going back to our standard rules where the 3 cells above determined the one below, we
can a variable to each of those 3 cells and make a logical statement.

For this lets assigned the letters p, q, r to the cells and make a table of all
possible permutations of the 3 cells.  The fourth column represents rule 192.

p|q|r|rule 192
-|-|-|:------:
1|1|1|   1
1|1|0|   1
1|0|1|   0
1|0|0|   0
0|1|1|   0
0|1|0|   0
0|0|1|   0
0|0|0|   0

By using the bitwise | (or), & (and), and ^ (xor) we can construct a statement
for rule 192.  In rule 192 the first two statements are true where both p and q
are true.  This gives the simple rule: p&q.

*Note that using the ~ in python will change zero to -1 instead of 1. So, I
instead use 1-p for ~p.

For rule 30 we have p^(q|r), and for rule 150 we have p^q^r.

In the cell_auto_library to call rule 150 by function we would first make a function
that takes in a list of the three cell values.
```python
def rule150(x):
	p,q,r = [int(i) for i in x]
	return p^q^r
```
Then the function call would look like
```python
cell_auto(rows=100,func=rule150)
```
## Using Functions

Using the same syntax to make logical statements for binary rules, we can make
continous functions that give each cell a value between 0 and 1.  White is still
0 and black is still 1, but in between is a grayscale, that gives the appearance
of continous functions.

<p align="center">
  <img align="center" src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/continuousCellAuto.png" />
</p>
These plots were generated by taking the average of the the cell cells above, namely (p+q+r)/3, and adding a constant.
The constants used from left to right and then down are 0.35, 0.475, 0.495, and 0.9.

## Ternary Rules
So far we have talked about the two extremes.  First we talked about if there was only two states a cell could have.
Then we talked about when a cell could have and infinite number of states showing continuity.  The first step up from
base 2 is base 3 which we call ternary.  Below shows totalistic ternary rules where a cell can have 3 different states.
Making a rule totalistic helps to reduce to number of rules a set may have.  Without making this set totalistic we would
have 7625597484987 or 3<sup>3<sup>2(1)+1</sup></sup> rules. Totalistic rules sum the three cells above to determine the
one below.  For ternary specifically we can have a minimum sum of 0 where all three cells are 0 and a maximum of 6
where all cells equal 2.  This means that there are 7 different 3 cell cell states and 3 diffent one cell cell states for
the cell below.  This makes the total number of rules equal to 2187 or 3<sup>7</sup> rules, a much more managable set.
<p align="center">
  <img align="center" src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/ternary.png" />
</p>
These plots show the totalistic ternary rules, 1599, 2049, 1635, and 1572, from left to right and then down.
The different color scheme is to show a better contrast between the 3 cell states.

Below shows some ternary rules under random initial conditions. The top row shows two figures or rule 1599 and the
bottom row show two figures of rule 357. The left column is 300 iterations and the right is 100.
<p align="center">
  <img align="center" src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/ternaryRandom.png" />
</p>

## Conway's Game of Life
<img src="https://github.com/Nick-Kurt-Butler/cellularAutomata/blob/master/media/conway.gif" width="1000" height="500" />

