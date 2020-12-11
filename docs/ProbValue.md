# ProbValue

## About
This is an abstract class that allows for probabilistic selection with whole integers. Think of selecting colored
marbles out of a bag. If there are 5 blue marbles, 5 red marbles, and 10 yellow marbles, there is a 25% chance of 
selecting blue, a 25% chance of selecting red, and a 50% chance of selecting yellow. If we want to adjust or raise the 
likelihood of red being selected we can just raise the number of red marbles without having to recalculate the exact 
percentages of probability for each color of marble. This idea is the basis for ProbValue. You enter in a whole number 
amount to represent the likelihood something will be selected and you also pass a value (this can be anything). When
multiple ProbValues are created (e.g. ProbValue(1, "blue"), ProbValue(1, "red"), ProbValue(2, "yellow")), a generator is
created that can will return a random selection with the specified probabilities from the ProbValues. In the example 
case this generator will return "yellow" twice as many times as "red" or "blue" in the long run.

## Inputs

ProbValue( \<int>: Amount, \<any> Value)

## Usage

This is used to create a range of varying depths and breadths and demographics (each with their own set of ProbValues) 
in order to maximize the control over "randomness" during organization generation.  

e.g. depths that range from 3-5 equally (ProbValue(1, 3), ProbValue(1, 4), ProbValue(1, 5))  
e.g. depths that favor 3 and not 5 (ProbValue(10, 3), ProbValue(5, 4), ProbValue(1, 5))  
e.g. creating a uniform gender range (ProbValue(33, "MALE"), ProbValue(33, "FEMALE"))  <i>could include "OTHER" as at 33</i>  

From these ProbValues a generator can be pulled to fetch a value with the given likelihood as specified.