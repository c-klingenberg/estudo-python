﻿''' From: https://edube.org/learn/pe-1/lab-essentials-of-the-if-else-statement-3
Objectives
Familiarize the student with:

using the if-else instruction to branch the control path;
building a complete program that solves simple real-life problems.

Scenario
Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.'''

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = 0.18*income - 556.02
if income > 85528:
    tax = 14839.02 + 0.32*(income-85528)

if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

'''Test Data
Sample input: 10000
Expected output: The tax is: 1244.0 thalers

Sample input: 100000
Expected output: The tax is: 19470.0 thalers

Sample input: 1000
Expected output: The tax is: 0.0 thalers

Sample input: -100
Expected output: The tax is: 0.0 thalers'''