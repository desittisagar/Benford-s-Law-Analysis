# Benford-s-Law-Analysis

Write an application in Python that will apply Benford’s Law to
a given set of your own data.

Your Task
Develop a Python program which will load up a set of data, determine the frequencies of the
leading digits and compare them with the predicted distribution of Benford’s law. Display this in
a bar chart and a table of values. For example:
Digit 1: Observed = 0.321 Expected = 0.301
Digit 2: Observed = 0.153 Expected = 0.176
and so on up till digit 9.
We shall look at three cases.
An Excel spreadsheet has been taken from Office-Watch: Benford’s Law and Excel 5 to let you
quickly visualize the Python application that we need make.
Case 1 - Fibonacci series 6
This series begins with two numbers 1,1 – these two numbers are added to continue the
series giving rise to the following (only the first 8 terms of the series are shown here):
1,1,2,3,5,8,13,21,. . .
There are many examples of this pattern in Nature and the series is closely related to the
Golden 7 ratio.
Using the Excel spreadsheet generate a Fibonacci series up to the 24 th term and see if the first
digits obey Benford’s Law. Does it get better if you add more terms?
The Chi-test 8 measures how close an actual value is to the expected value – the closer it is to
100% the closer the actual value is to the expected value. In our case, we are testing how
close the frequency of each digit in our dataset is to Benford’s prediction for that digit.
What is the value of the ChiTest comparison for this Fibonacci series? Does it get better if we
add more terms to the series?
Case 2 – Fibonacci numbers & Benford’s law using Python
In this case you are to repeat the analysis in Case 1 but using you Python code.
5 https://office-watch.com/2012/benfords-law-and-excel/
6 https://en.wikipedia.org/wiki/Fibonacci_number
7 https://en.wikipedia.org/wiki/Golden_ratio
8 Also written as
 2 -test
CRICOS Provider No. 00103D
1400 Assig 2, 2020-07
4Case 3 – Length of Rivers 9 in the World
In this case, use your Python code to see whether the lengths of rivers in the world follow
Benford’s law.
Fraud detection using Benford’s Law
One use of Benford’s Law is to detect cases of Fraud. Consider the 1993 case of State of Arizona v Nelson.
The accused diverted nearly $2M to fake vendors in an attempt to defraud the State. The frequency of first
digits in the written cheques clearly violates Benford’s Law leading to a conviction.
Another case is that of Enron in its posting of revenue for the year 2000. Comparison of the
frequency of first digits versus the expected frequency shows large discrepancies. The
company went bankrupt the following year – one of the greatest financial failures in history.
