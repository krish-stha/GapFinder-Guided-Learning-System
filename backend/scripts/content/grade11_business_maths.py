# -*- coding: utf-8 -*-
"""
NEB Grade 11 Management - Business Mathematics question bank.

Authored content (not content partner data - loaded with source='synthetic'
by scripts/load_question_bank.py). Topically accurate, written to read
like genuine exam questions per explicit user instruction. Course 209
("NEB Grade 11 Management") had NO existing "Business Maths" subject at
all (unlike its sibling Science course, 91) - the 13 chapter names below
are reused from course 91's real Business Maths subject (id=35255) so
the new subject/chapters created by scripts/create_subject.py match
genuine NEB Grade 11 Management curriculum topics, not invented ones.
Never presented as content partner content or as evidence about real
students.

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}.
"""

QUESTIONS = {
    "Financial Mathematics": [
        {"q": "Simple interest is calculated using the formula I = PRT/100, where P, R and T represent:", "options": [
            "Principal, Rate of interest per annum, and Time in years", "Profit, Revenue, and Tax",
            "Price, Return, and Total cost", "Principal, Revenue, and Tax rate"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "If Rs. 10,000 is invested at 8% simple interest per annum for 3 years, the interest earned is:", "options": [
            "Rs. 2,400", "Rs. 800", "Rs. 24,000", "Rs. 2,000"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Under compound interest, interest is calculated on:", "options": [
            "The principal plus previously accumulated interest", "Only the original principal, every period",
            "Only the final amount at maturity", "A fixed amount decided in advance regardless of principal"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The compound amount formula is A = P(1 + R/100)^T, where T represents:", "options": [
            "The number of compounding periods (e.g. years)", "The total interest earned",
            "The principal amount only", "The rate of interest only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For the same principal, rate, and time (beyond one period), compound interest compared to simple interest is:", "options": [
            "Generally higher, since interest is earned on accumulated interest too", "Always exactly equal",
            "Always lower", "Impossible to compare"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'annuity' in financial mathematics refers to:", "options": [
            "A series of equal payments made at regular intervals", "A single lump-sum payment made once",
            "A type of tax refund", "A government subsidy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'ordinary annuity' is one in which payments are made:", "options": [
            "At the end of each period", "At the beginning of each period only",
            "Randomly throughout the year", "Only once every ten years"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Present value' of a future sum of money refers to:", "options": [
            "The current worth of a future amount, discounted at a given interest rate", "The exact same amount as its future value with no discounting",
            "The value after adding all future interest", "A value used only for insurance calculations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Future value' of a present sum of money refers to:", "options": [
            "The value that a current sum will grow to after earning interest over time", "The value of money one day in the past",
            "A value unrelated to interest rates", "The value after subtracting all interest"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Depreciation of an asset's value over time can be modelled mathematically using:", "options": [
            "A declining (compound-decrease) percentage formula, similar in structure to compound interest", "Simple addition of a fixed amount each year, with no formula needed",
            "Random numbers with no pattern", "Only government-fixed values with no calculation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The concept of 'discounting' in financial mathematics is used to:", "options": [
            "Convert a future cash flow into its equivalent present value", "Increase a present value into a larger future value",
            "Calculate the tax on a good", "Determine a company's total number of employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If interest is compounded semi-annually (twice a year) at an annual rate R%, the rate used per compounding period is:", "options": [
            "R/2 %", "R %", "2R %", "R/4 %"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Amortization' of a loan refers to:", "options": [
            "Gradually paying off a debt through regular instalments covering both principal and interest", "A one-time full repayment with no instalments",
            "Cancelling a loan without repayment", "Increasing a loan amount without repayment"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'sinking fund' is best described as:", "options": [
            "A fund built up through regular deposits to accumulate a target amount by a future date", "A fund that automatically loses all value over time",
            "A one-time tax payment", "A type of insurance premium only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, financial mathematics techniques like compound interest and present value are commonly used for:", "options": [
            "Investment appraisal, loan repayment planning, and valuation decisions", "Only calculating employee attendance",
            "Only designing product packaging", "Only setting advertising budgets with no financial basis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the compounding frequency increases (e.g. from annual to monthly) while the nominal annual rate stays the same, the effective annual return:", "options": [
            "Increases slightly", "Decreases", "Stays exactly the same regardless of frequency", "Becomes zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'time value of money' concept reflects the principle that:", "options": [
            "A given sum of money today is worth more than the same sum in the future, due to its earning potential", "Money never changes in value over time",
            "Future money is always worth more than present money", "Time has no relevance to financial decisions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A loan repayment schedule showing how each instalment splits between principal and interest is called an:", "options": [
            "Amortization schedule", "Income statement", "Balance sheet", "Trial balance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is generally true when comparing simple interest and compound interest over a period longer than one year (same P, R)?", "options": [
            "Compound interest yields a higher total amount than simple interest", "Simple interest always yields a higher amount",
            "Both always yield an identical amount for any duration", "Neither can be calculated without a computer"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business decision-making, calculating the present value of expected future cash flows from a project helps managers:", "options": [
            "Assess whether the investment is worthwhile in today's terms", "Determine the exact office address",
            "Set the company's dress code", "Choose the company's logo colour"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Linear function, equations, inequalities and its applications": [
        {"q": "A 'linear function' is one that can be expressed in the general form:", "options": [
            "y = mx + c, where m and c are constants", "y = x^2 + c", "y = 1/x", "y = log(x)"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In the equation y = mx + c, 'm' represents the:", "options": [
            "Slope (gradient) of the line", "y-intercept", "x-intercept", "The value of y when x is zero, always"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In the equation y = mx + c, 'c' represents the:", "options": [
            "y-intercept (the value of y when x = 0)", "The slope of the line", "The x-intercept always",
            "The maximum value of y"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A linear cost function is often written as C = a + bx, where 'a' typically represents:", "options": [
            "Fixed cost (cost incurred even at zero output)", "Variable cost per unit", "Total revenue",
            "Profit margin"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a linear cost function C = a + bx, 'b' typically represents:", "options": [
            "Variable cost per unit of output", "Fixed cost", "Total cost", "Total revenue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'break-even point' in business mathematics is the level of output where:", "options": [
            "Total revenue equals total cost (zero profit or loss)", "Total revenue is at its maximum",
            "Total cost is zero", "Profit is at its highest possible level"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If Total Revenue (TR) = px and Total Cost (TC) = a + bx, the break-even quantity is found by solving:", "options": [
            "px = a + bx for x", "p = a for x", "x = a + b", "px + bx = a only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'linear inequality' differs from a linear equation mainly in that it uses:", "options": [
            "Inequality symbols such as <, >, ≤ or ≥ instead of an equals sign", "Only the equals sign, exactly like an equation",
            "Exponents instead of coefficients", "Logarithms instead of variables"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The solution set of a linear inequality in one variable, such as x > 5, is typically represented graphically as:", "options": [
            "A ray/half-line on the number line starting from the boundary point", "A single fixed point only",
            "The entire number line with no restriction", "An empty set always"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Two lines with the same slope (m) but different y-intercepts (c) are:", "options": [
            "Parallel lines that never intersect", "The same line", "Perpendicular lines",
            "Lines that always intersect at the origin"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Solving a system of two linear equations graphically means finding:", "options": [
            "The point of intersection of the two lines", "The slope of only one of the lines",
            "The y-intercept of only one line", "The midpoint between the two y-intercepts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The demand function in economics/business is often modelled as a linear equation of the form:", "options": [
            "p = a - bx (price decreases as quantity demanded increases)", "p = a + bx (price always increases with quantity)",
            "p = x^2", "p = log(x)"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Given the linear equation 2x + 3y = 12, if x = 0, the value of y is:", "options": [
            "4", "6", "3", "12"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Given the linear equation 2x + 3y = 12, if y = 0, the value of x is:", "options": [
            "6", "4", "3", "12"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The slope of a line passing through points (2, 3) and (4, 7) is:", "options": [
            "2", "4", "1", "0.5"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A vertical line on a graph (e.g. x = 5) has a slope that is:", "options": [
            "Undefined", "Zero", "Equal to 5", "Equal to 1"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A horizontal line on a graph (e.g. y = 3) has a slope of:", "options": [
            "Zero", "Undefined", "Equal to 3", "Equal to 1"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business, linear equations are commonly applied to model relationships such as:", "options": [
            "Cost, revenue and profit as functions of quantity produced/sold", "Only the company's holiday calendar",
            "Only the company's office layout", "Only random, unrelated data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If total profit P = TR - TC, and both TR and TC are linear functions of quantity x, then P is generally:", "options": [
            "Also a linear function of x", "Always a quadratic function of x", "Always a constant regardless of x",
            "Impossible to express in terms of x"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Solving the inequality 3x - 6 > 0 gives the solution:", "options": [
            "x > 2", "x < 2", "x > -2", "x < -2"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "System of linear equations, and its applications": [
        {"q": "A 'system of linear equations' consists of:", "options": [
            "Two or more linear equations considered together, involving the same variables", "A single equation with one variable only",
            "An equation involving only exponents", "A single inequality with no equation"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A system of two linear equations in two unknowns has a UNIQUE solution when the two lines:", "options": [
            "Intersect at exactly one point (different slopes)", "Are parallel with different intercepts",
            "Are identical (the same line)", "Never touch at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A system of two linear equations has NO solution when the two lines are:", "options": [
            "Parallel with different y-intercepts (never intersect)", "Intersecting at one unique point",
            "Identical (infinite common points)", "Perpendicular to each other"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A system of two linear equations has INFINITELY MANY solutions when the two equations represent:", "options": [
            "The exact same line", "Two distinct, non-parallel lines", "Two parallel, distinct lines",
            "Two perpendicular lines"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'substitution method' for solving a system of linear equations involves:", "options": [
            "Solving one equation for one variable and substituting it into the other equation", "Graphing both equations only, with no algebra",
            "Adding both equations directly without any rearrangement", "Ignoring one of the two equations entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'elimination method' for solving a system of linear equations involves:", "options": [
            "Adding or subtracting the equations (after suitable scaling) to eliminate one variable", "Only graphing both lines",
            "Multiplying both equations by zero", "Ignoring the coefficients entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Solving the system x + y = 10 and x - y = 4 gives:", "options": [
            "x = 7, y = 3", "x = 3, y = 7", "x = 10, y = 4", "x = 5, y = 5"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, a system of linear equations can be used to find the equilibrium point where:", "options": [
            "The demand and supply functions (both linear) intersect", "Only the demand function is considered, with no supply",
            "Only fixed costs are calculated", "The company's total number of employees is determined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'consistent' system of linear equations is one that has:", "options": [
            "At least one solution", "No solution at all", "Exactly zero equations", "Only inequalities, no equations"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "An 'inconsistent' system of linear equations is one that has:", "options": [
            "No solution at all", "Exactly one solution", "Infinitely many solutions", "Exactly two solutions always"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "When solving a system of three linear equations in three unknowns, a unique solution corresponds to:", "options": [
            "A single point where all three planes intersect", "A single line shared by all three planes",
            "No possible geometric interpretation", "A single point on only one of the equations"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Matrix methods (e.g. using coefficient matrices) can be used to solve systems of linear equations mainly because they:", "options": [
            "Provide a systematic way to organise and solve multiple equations simultaneously", "Are only usable for a single equation",
            "Cannot handle more than one variable", "Are unrelated to systems of equations"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A company sells two products, and total revenue depends on the quantities of each. Setting up a system of linear equations from given revenue and quantity conditions helps to:", "options": [
            "Determine the individual quantities or prices that satisfy both conditions", "Determine the company's registered address",
            "Determine the color scheme of the products", "Eliminate the need for any pricing decision"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the graphical solution approach to a system of two linear equations?", "options": [
            "Plotting both lines and identifying their point(s) of intersection, if any", "Plotting only one line and ignoring the other",
            "Calculating only the y-intercepts with no plotting", "Adding the two equations' constants only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a system of equations models a mixture problem (e.g. blending two products to meet a target), the solution gives:", "options": [
            "The quantities of each component needed to satisfy all stated conditions", "Only the total cost with no quantity information",
            "The exact profit margin with no reference to quantities", "A value unrelated to either equation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a real business application of a system of linear equations?", "options": [
            "Determining the break-even point where two different cost/revenue plans yield the same profit", "Selecting the company's brand colour",
            "Scheduling employee holidays", "Choosing an office decoration theme"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the system 2x + y = 8 and x - y = 1, solving gives:", "options": [
            "x = 3, y = 2", "x = 2, y = 3", "x = 1, y = 6", "x = 4, y = 0"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why business analysts use systems of linear equations rather than a single equation for many real problems?", "options": [
            "Real business problems often involve multiple interdependent variables/conditions that must be satisfied simultaneously",
            "A single equation is always sufficient for any business problem", "Systems of equations are used only in pure mathematics with no real application",
            "Multiple equations always have no solution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If two supply-and-demand equations for a good are linear and their intersection lies outside the feasible (positive quantity/price) region, this suggests:", "options": [
            "The mathematical model may need review, since a negative price/quantity has no real economic meaning", "The market is in perfect equilibrium",
            "The equations are automatically correct with no issue", "Demand and supply can never be modelled linearly"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is generally the LAST step after finding a numerical solution to a system of equations in a business word problem?", "options": [
            "Interpreting the numerical result in the context of the original business question", "Ignoring the result entirely",
            "Deleting the original equations", "Recalculating using unrelated numbers"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Quadratic functions and equations and its applications": [
        {"q": "A 'quadratic function' is generally expressed in the form:", "options": [
            "y = ax^2 + bx + c, where a ≠ 0", "y = ax + b", "y = a/x", "y = log(ax)"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The graph of a quadratic function is a:", "options": [
            "Parabola", "Straight line", "Circle", "Hyperbola"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "If the coefficient 'a' in y = ax^2 + bx + c is positive, the parabola:", "options": [
            "Opens upward, with a minimum point", "Opens downward, with a maximum point",
            "Is a straight line instead", "Has no defined shape"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the coefficient 'a' in y = ax^2 + bx + c is negative, the parabola:", "options": [
            "Opens downward, with a maximum point", "Opens upward, with a minimum point",
            "Becomes a straight line", "Has no vertex at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'roots' (or zeros) of a quadratic equation ax^2 + bx + c = 0 are the values of x where:", "options": [
            "The function equals zero (where the graph crosses the x-axis)", "The function reaches its maximum value",
            "The function equals 'a'", "The function is undefined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The quadratic formula for solving ax^2 + bx + c = 0 is:", "options": [
            "x = [-b ± √(b^2 - 4ac)] / 2a", "x = -b/a", "x = b^2 - 4ac", "x = c/a"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'discriminant' of a quadratic equation, b^2 - 4ac, when positive, indicates that the equation has:", "options": [
            "Two distinct real roots", "No real roots", "Exactly one repeated real root", "Infinitely many roots"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "When the discriminant (b^2 - 4ac) of a quadratic equation equals zero, the equation has:", "options": [
            "Exactly one repeated real root", "Two distinct real roots", "No real roots at all", "Three real roots"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "When the discriminant (b^2 - 4ac) of a quadratic equation is negative, the equation has:", "options": [
            "No real roots (roots are complex/imaginary)", "Exactly one real root", "Two distinct real roots",
            "Infinitely many real roots"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, a quadratic profit function P(x) = -ax^2 + bx - c (a > 0) reaches its MAXIMUM profit at the:", "options": [
            "Vertex of the downward-opening parabola", "Point where P(x) = 0", "The value where x is smallest",
            "The value where x is largest, regardless of the function's shape"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The x-coordinate of the vertex of a parabola y = ax^2 + bx + c is given by:", "options": [
            "x = -b/2a", "x = b/2a", "x = -c/a", "x = a/b"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A quadratic revenue function is often derived when:", "options": [
            "A linear demand function p = a - bx is multiplied by quantity x to get TR = px = ax - bx^2", "Revenue is always a constant regardless of price or quantity",
            "Only fixed costs are considered", "Demand is assumed to be completely unrelated to price"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Solving x^2 - 5x + 6 = 0 gives the roots:", "options": [
            "x = 2 and x = 3", "x = 1 and x = 6", "x = -2 and x = -3", "x = 5 and x = 6"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Solving x^2 - 9 = 0 gives the roots:", "options": [
            "x = 3 and x = -3", "x = 9 and x = -9", "x = 3 only", "x = 0 and x = 9"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Factoring is one method to solve a quadratic equation; it works by expressing the equation as:", "options": [
            "A product of two linear factors set equal to zero", "A sum of two unrelated terms",
            "A single linear equation only", "An equation with no x-term at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In cost analysis, a quadratic cost function might be used to model situations where:", "options": [
            "Costs rise at an increasing or decreasing rate as output changes, not at a constant rate", "Costs are always exactly proportional to output with no curvature",
            "Costs never change regardless of output", "Costs only depend on fixed cost, never variable cost"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'axis of symmetry' of a parabola y = ax^2 + bx + c is the vertical line:", "options": [
            "x = -b/2a", "y = -b/2a", "x = c", "y = a"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is a real-world business application of quadratic functions?", "options": [
            "Finding the output level that maximises profit or minimises average cost", "Choosing an employee's job title",
            "Setting the company's founding date", "Deciding the office furniture colour"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The sum of the roots of a quadratic equation ax^2 + bx + c = 0 is given by:", "options": [
            "-b/a", "b/a", "c/a", "-c/a"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The product of the roots of a quadratic equation ax^2 + bx + c = 0 is given by:", "options": [
            "c/a", "-c/a", "b/a", "-b/a"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Exponential and logarithmic functions and its applications": [
        {"q": "An 'exponential function' is generally expressed in the form:", "options": [
            "y = a · b^x, where b > 0 and b ≠ 1", "y = ax + b", "y = ax^2 + bx + c", "y = a/x"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "If the base 'b' in an exponential function y = a · b^x is greater than 1, the function represents:", "options": [
            "Exponential growth", "Exponential decay", "A constant (unchanging) value", "A linear relationship"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the base 'b' in an exponential function y = a · b^x is between 0 and 1, the function represents:", "options": [
            "Exponential decay", "Exponential growth", "A quadratic relationship", "An undefined function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Compound interest growth, A = P(1 + r)^t, is a real-world example of:", "options": [
            "An exponential function", "A linear function", "A quadratic function", "A logarithmic function only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'logarithmic function' is the inverse of a(n):", "options": [
            "Exponential function", "Linear function", "Quadratic function", "Constant function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The logarithmic equation log_b(x) = y is equivalent to the exponential equation:", "options": [
            "b^y = x", "y^b = x", "x^y = b", "b^x = y"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The value of log_10(100) is:", "options": [
            "2", "10", "100", "1"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The value of log_2(8) is:", "options": [
            "3", "2", "8", "4"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to the product rule of logarithms, log(MN) equals:", "options": [
            "log(M) + log(N)", "log(M) - log(N)", "log(M) × log(N)", "log(M) / log(N)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "According to the quotient rule of logarithms, log(M/N) equals:", "options": [
            "log(M) - log(N)", "log(M) + log(N)", "log(M) × log(N)", "log(N) - log(M)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "According to the power rule of logarithms, log(M^n) equals:", "options": [
            "n · log(M)", "log(M)^n as a separate operation, unrelated to multiplication", "log(n) · M",
            "log(M) / n only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, exponential functions are commonly used to model:", "options": [
            "Compound growth situations, such as population growth, investment growth, or depreciation", "Only fixed, unchanging quantities",
            "Only straight-line relationships between two variables", "Situations with no time dimension at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The time required for an investment to double in value under compound interest can be estimated using:", "options": [
            "Logarithms, by solving 2P = P(1+r)^t for t", "Only simple interest formulas",
            "A quadratic equation only", "Basic addition with no exponential reasoning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'natural logarithm', denoted ln(x), uses which base?", "options": [
            "The mathematical constant e (approximately 2.718)", "Base 10", "Base 2", "Base 1"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes exponential decay in a business context?", "options": [
            "The declining value of an asset or quantity over time at a rate proportional to its current value", "A constant increase in value each period by a fixed amount",
            "A value that never changes over time", "A value that only increases, never decreases"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Solving the exponential equation 2^x = 8 gives:", "options": [
            "x = 3", "x = 4", "x = 2", "x = 8"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "log(1) in any valid base is always equal to:", "options": [
            "0", "1", "The base itself", "Undefined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "log_b(b) in any valid base b is always equal to:", "options": [
            "1", "0", "b", "Undefined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an application of logarithms in business/finance?", "options": [
            "Calculating the number of years needed for an investment to reach a target value under compound growth", "Determining a company's office address",
            "Setting the company's dress code policy", "Choosing a product's packaging material"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The graph of an exponential growth function y = a · b^x (b > 1, a > 0) as x increases will:", "options": [
            "Rise continuously, becoming steeper over time", "Fall continuously toward zero",
            "Remain a flat horizontal line", "Form a symmetric parabola"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Limits and Continuity": [
        {"q": "The 'limit' of a function f(x) as x approaches a value 'a' describes:", "options": [
            "The value that f(x) approaches as x gets arbitrarily close to 'a'", "The exact value of f(a) always, with no exception",
            "The maximum possible value of f(x) over all x", "The total area under the curve of f(x)"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The notation lim(x→a) f(x) = L means:", "options": [
            "As x approaches a, f(x) approaches the value L", "f(a) is always undefined", "L is always equal to zero",
            "f(x) equals L for all values of x"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A function f(x) is said to be 'continuous' at x = a if:", "options": [
            "f(a) is defined, the limit as x approaches a exists, and the limit equals f(a)", "f(a) is undefined at that point",
            "The function has a break or jump at that point", "The function is only defined for negative x values"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A function has a 'discontinuity' at a point if:", "options": [
            "The function is not continuous there - e.g. it has a break, jump, or is undefined", "It is perfectly smooth and unbroken at that point",
            "Its limit exists and equals its function value there", "It has no domain restrictions anywhere"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The limit of a constant function f(x) = c as x approaches any value 'a' is:", "options": [
            "c", "a", "0", "Undefined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to the sum rule for limits, lim(x→a)[f(x) + g(x)] equals:", "options": [
            "lim(x→a) f(x) + lim(x→a) g(x), provided both limits exist", "lim(x→a) f(x) × lim(x→a) g(x)",
            "Always zero", "Undefined in every case"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The limit of f(x) = x as x approaches 5 is:", "options": [
            "5", "0", "Undefined", "Infinity"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best describes why the concept of a limit is foundational to calculus?", "options": [
            "It provides the rigorous basis for defining derivatives and integrals", "It has no connection to derivatives or integrals",
            "It only applies to whole numbers", "It replaces the need for any function at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A function is continuous over an interval if it is continuous at:", "options": [
            "Every point within that interval", "Only the first point of the interval", "Only the last point of the interval",
            "No points within the interval"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business/economics, the concept of continuity is relevant because many models assume:", "options": [
            "Cost, revenue, and demand functions behave smoothly without abrupt breaks over the relevant range", "All business functions must have breaks at every point",
            "Prices are always fixed and never modelled as functions", "Continuity has no relevance to any business application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The limit lim(x→0) (sin x)/x is a classic example used to illustrate:", "options": [
            "A limit that exists (equal to 1) even though the function is undefined at x = 0", "A limit that never exists for any trigonometric function",
            "A discontinuous function with no defined limit at all", "A function unrelated to calculus"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'removable discontinuity' in a function's graph typically appears as:", "options": [
            "A single missing point (a 'hole') that could be 'fixed' by redefining the function at that point", "A vertical asymptote where the function goes to infinity",
            "A jump between two different function values", "A function with no domain at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'jump discontinuity' occurs when:", "options": [
            "The left-hand and right-hand limits at a point exist but are not equal to each other", "The function is perfectly continuous at that point",
            "The function has no limit defined anywhere", "The function is a straight line throughout"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following functions is typically continuous everywhere on the real number line?", "options": [
            "A polynomial function, such as f(x) = x^2 + 3x + 1", "1/x, which is undefined at x = 0",
            "A step function with deliberate jumps", "A function defined only for x > 0"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "As x approaches infinity, the limit of the function f(x) = 1/x approaches:", "options": [
            "0", "1", "Infinity", "Undefined with no pattern"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The left-hand limit of a function at a point refers to the value the function approaches as x approaches that point:", "options": [
            "From values smaller than the point (from the left side)", "From values larger than the point",
            "From both sides simultaneously with no distinction", "Only at x = 0"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "For a limit to exist at a point, the left-hand limit and right-hand limit must:", "options": [
            "Be equal to each other", "Always be different from each other", "Both be equal to zero",
            "Have no relationship to each other"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A cost function that has a sudden jump in value at a particular output level (e.g. due to a step in wholesale pricing) would be an example of a function that is:", "options": [
            "Discontinuous at that output level", "Continuous everywhere with no exception", "Always linear",
            "Always quadratic"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the practical importance of continuity in demand/supply modelling?", "options": [
            "It allows smooth analysis of how small changes in price lead to small changes in quantity", "It guarantees the price will never change",
            "It eliminates the need for any economic model", "It applies only to government-set prices"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Evaluating lim(x→2) (x^2 - 4)/(x - 2) by simplifying (factoring) first gives a limit of:", "options": [
            "4", "0", "2", "Undefined"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Differentiation": [
        {"q": "'Differentiation' in calculus refers to the process of finding a function's:", "options": [
            "Derivative, which measures the rate of change of the function", "Integral, which measures the area under its curve",
            "Limit at a single point only", "Domain and range"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The derivative of a function y = f(x) is commonly denoted as:", "options": [
            "dy/dx or f'(x)", "∫f(x)dx", "lim f(x)", "f(x)^2"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The derivative of a constant function f(x) = c is:", "options": [
            "0", "c", "1", "x"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Using the power rule, the derivative of f(x) = x^n is:", "options": [
            "n · x^(n-1)", "x^(n+1)/(n+1)", "n · x^n", "x^n / n"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The derivative of f(x) = x^3 is:", "options": [
            "3x^2", "x^2", "3x", "x^4/4"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The derivative of f(x) = 5x is:", "options": [
            "5", "5x", "x", "0"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "According to the sum rule for differentiation, the derivative of [f(x) + g(x)] is:", "options": [
            "f'(x) + g'(x)", "f'(x) × g'(x)", "f(x) + g'(x) only", "Always zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'product rule' for differentiation states that the derivative of f(x)·g(x) is:", "options": [
            "f'(x)g(x) + f(x)g'(x)", "f'(x) × g'(x)", "f'(x) + g'(x)", "f(x)/g(x)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'quotient rule' for differentiation is used to differentiate:", "options": [
            "A function expressed as one function divided by another, f(x)/g(x)", "A sum of two functions only",
            "A single constant only", "A product of two functions only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'chain rule' is used to differentiate:", "options": [
            "A composite function, i.e. a function of another function", "Only simple polynomial functions",
            "Only constant functions", "Only linear functions"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Geometrically, the derivative of a function at a point represents the:", "options": [
            "Slope of the tangent line to the curve at that point", "Area under the curve up to that point",
            "The y-intercept of the function", "The maximum value of the function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business/economics, 'marginal cost' is defined as:", "options": [
            "The derivative of the total cost function with respect to quantity", "The total cost divided by fixed cost",
            "The integral of the total cost function", "The average of all past costs"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business/economics, 'marginal revenue' is defined as:", "options": [
            "The derivative of the total revenue function with respect to quantity", "The total revenue divided by price",
            "The integral of the total revenue function", "A fixed constant unrelated to quantity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'second derivative' of a function represents:", "options": [
            "The rate of change of the first derivative (e.g. used to identify concavity, maxima/minima)", "The original function itself",
            "The integral of the function", "A value that is always exactly zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If the first derivative of a function is zero at a point, that point is likely a:", "options": [
            "Critical point, potentially a maximum, minimum, or inflection point", "Point where the function is undefined",
            "Point of discontinuity always", "Point where the function's value is always zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The derivative of f(x) = 4x^2 + 3x - 7 is:", "options": [
            "8x + 3", "4x + 3", "8x^2 + 3x", "8x - 7"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Differentiation is used in business primarily to:", "options": [
            "Analyse rates of change, such as marginal cost/revenue, and identify optimal points like maximum profit",
            "Calculate the total sum of all past sales with no reference to rates of change", "Determine a company's registered legal name",
            "Set the company's holiday schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A function is 'differentiable' at a point if:", "options": [
            "Its derivative exists (is well-defined) at that point", "It is undefined at every point",
            "It has a sharp corner or break at that point", "It is always a constant function"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following functions has a constant derivative (the same value everywhere)?", "options": [
            "A linear function, f(x) = mx + c", "A quadratic function, f(x) = x^2", "A cubic function, f(x) = x^3",
            "An exponential function, f(x) = 2^x"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If total revenue TR = 100x - 2x^2, the marginal revenue function (derivative with respect to x) is:", "options": [
            "100 - 4x", "100 - 2x", "100x - 4x", "-4x"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Application of Derivatives": [
        {"q": "To find the value of x that MAXIMISES or MINIMISES a function, the standard first step is to:", "options": [
            "Set the first derivative equal to zero and solve for x", "Set the original function equal to zero",
            "Integrate the function", "Multiply the function by -1"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'second derivative test' is used to determine whether a critical point is a maximum or minimum by checking:", "options": [
            "The sign (positive or negative) of the second derivative at that point", "The value of the original function only",
            "The value of x alone with no calculation", "The sum of all derivatives at every point"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If the second derivative at a critical point is POSITIVE, that point is a:", "options": [
            "Minimum point", "Maximum point", "Point of discontinuity", "Point with no meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If the second derivative at a critical point is NEGATIVE, that point is a:", "options": [
            "Maximum point", "Minimum point", "An undefined point", "A point unrelated to the function"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Profit is maximised at the output level where:", "options": [
            "Marginal Revenue equals Marginal Cost (MR = MC)", "Marginal Revenue is always zero",
            "Total Cost is at its minimum regardless of revenue", "Fixed Cost equals Variable Cost"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "To minimise the average cost of production, a firm typically looks for the output level where:", "options": [
            "The derivative of the average cost function equals zero (and the second derivative confirms a minimum)", "Total cost is at its absolute maximum",
            "Fixed cost is zero", "Marginal cost is always negative"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Elasticity of demand' can be expressed using calculus as related to:", "options": [
            "The derivative of quantity demanded with respect to price, scaled by price and quantity", "Only the total revenue with no reference to derivatives",
            "The second derivative of total cost", "A value unrelated to price or quantity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A firm's total cost function is minimised (in terms of average cost) typically where marginal cost:", "options": [
            "Equals average cost", "Equals zero always", "Is always negative", "Equals total revenue"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is a practical business use of derivative-based optimisation?", "options": [
            "Determining the production level that maximises profit or minimises cost", "Choosing a company's official slogan",
            "Selecting office furniture", "Deciding on a company holiday party theme"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The rate of change of demand with respect to price is found by taking the derivative of the:", "options": [
            "Demand function with respect to price", "Supply function with respect to time",
            "Cost function with respect to labour", "Profit function with respect to tax rate"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If total profit P(x) = -2x^2 + 40x - 50, the value of x that maximises profit is found by solving P'(x) = 0, giving:", "options": [
            "x = 10", "x = 20", "x = 5", "x = 40"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Marginal analysis' in business economics primarily uses derivatives to study:", "options": [
            "The effect of a small (one-unit) change in an input or output variable", "Only the total historical accumulated profit",
            "The company's total number of shareholders", "The company's brand logo design"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "At the point of maximum profit (where MR = MC), the second-order condition requires that:", "options": [
            "Marginal Cost is increasing faster than Marginal Revenue at that point (MC' > MR')", "Marginal Cost is always exactly zero",
            "Marginal Revenue is always negative", "Total Cost must be zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "An 'inflection point' on a curve is a point where:", "options": [
            "The curve changes concavity (from concave up to concave down, or vice versa)", "The function reaches its absolute highest value",
            "The function is completely undefined", "The derivative is always positive"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes 'rate of change' as applied via derivatives in a business context?", "options": [
            "How quickly a quantity such as cost, revenue or profit changes in response to a change in output", "A fixed number that never varies",
            "Only the initial value of a function", "The total accumulated value over all time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Finding the maximum revenue point on a total revenue curve TR(x) involves solving:", "options": [
            "TR'(x) = 0 for x, then confirming it is a maximum using the second derivative", "TR(x) = 0 for x directly",
            "Only checking where x = 0", "Integrating the revenue function"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of using derivatives for cost minimisation in production planning?", "options": [
            "Finding the output level where the average cost function's derivative equals zero", "Choosing a random output level with no calculation",
            "Ignoring cost entirely and focusing only on revenue", "Fixing output at exactly zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Businesses use the concept of 'marginal utility' (related to derivatives) mainly to understand:", "options": [
            "How consumer satisfaction changes with each additional unit consumed", "How government tax policy is decided",
            "How employee salaries are fixed by law", "How a company's logo should be designed"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why the first-order condition (derivative = 0) alone is not sufficient to confirm a maximum?", "options": [
            "It could also indicate a minimum or an inflection point - the second derivative test is needed to distinguish them",
            "The first-order condition always guarantees a maximum with no further check needed", "Derivatives are never used for optimisation in business",
            "The first derivative is irrelevant to optimisation problems"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In practice, applying derivative-based optimisation to real business problems requires that the cost/revenue/profit functions:", "options": [
            "Be reasonably modelled as differentiable functions of the relevant variable(s)", "Never be expressed mathematically at all",
            "Only ever be constant with no variation", "Only be applicable to non-business contexts"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Indefinite integral": [
        {"q": "'Integration' in calculus is best understood as the reverse process of:", "options": [
            "Differentiation", "Addition", "Multiplication", "Taking a limit"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'indefinite integral' of a function f(x) is written as:", "options": [
            "∫f(x)dx = F(x) + C, where C is the constant of integration", "f'(x)", "lim(x→a) f(x)",
            "A single numeric value with no variable"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'constant of integration', C, is added to an indefinite integral because:", "options": [
            "The derivative of any constant is zero, so infinitely many antiderivatives differ only by a constant", "It represents the exact value of the function at x = 0 in every case",
            "It is always equal to 1", "It has no mathematical justification"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Using the power rule for integration, ∫x^n dx (for n ≠ -1) equals:", "options": [
            "x^(n+1)/(n+1) + C", "n·x^(n-1) + C", "x^n/n + C", "n·x^n + C"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "∫5 dx equals:", "options": [
            "5x + C", "5 + C", "x/5 + C", "0 + C"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "∫x^2 dx equals:", "options": [
            "x^3/3 + C", "2x + C", "x^3 + C", "3x^2 + C"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to the sum rule for integration, ∫[f(x) + g(x)]dx equals:", "options": [
            "∫f(x)dx + ∫g(x)dx", "∫f(x)dx × ∫g(x)dx", "f(x) + g(x), with no integration performed",
            "Always a single constant"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business/economics, integrating a marginal cost function with respect to quantity gives back:", "options": [
            "The total cost function (up to a constant, often the fixed cost)", "The marginal revenue function directly",
            "A value unrelated to cost", "The demand function"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If marginal revenue MR(x) = 50 - 4x, then total revenue TR(x), found by integration, is:", "options": [
            "50x - 2x^2 + C", "50x - 4x^2 + C", "50 - 4x^2 + C", "50x^2 - 4x + C"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The constant of integration in a total cost function derived from marginal cost typically represents:", "options": [
            "The fixed cost of production", "The total variable cost only", "The marginal cost itself",
            "The break-even quantity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes the relationship between differentiation and integration?", "options": [
            "They are inverse operations of each other", "They always give the exact same result",
            "They are completely unrelated mathematical operations", "Integration is only used in geometry, never in algebra"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "∫(3x^2 + 2x) dx equals:", "options": [
            "x^3 + x^2 + C", "6x + 2 + C", "x^3 + 2x + C", "3x^3 + x^2 + C"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Integration is used in business mathematics primarily to:", "options": [
            "Recover total functions (such as total cost or total revenue) from their marginal (derivative) functions",
            "Only calculate simple interest", "Only determine a company's tax bracket", "Replace the need for algebra entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Verifying an indefinite integral is correct can be done by:", "options": [
            "Differentiating the result and checking it matches the original function", "Adding a random constant with no check",
            "Multiplying the result by zero", "Ignoring the original function entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "∫(1/x) dx equals (for x > 0):", "options": [
            "ln|x| + C", "1/x^2 + C", "x^2/2 + C", "0 + C"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If a firm's marginal cost function is MC(x) = 10, a constant, then the variable cost function (via integration) is:", "options": [
            "10x + C", "10 + C", "10/x + C", "x/10 + C"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of using integration in economic analysis?", "options": [
            "Calculating total cost by integrating a known marginal cost function over a range of output", "Setting a company's employee dress code",
            "Choosing the company's office location", "Determining the founder's personal daily schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The indefinite integral of a function always results in:", "options": [
            "A family of functions differing by a constant, not a single unique function", "A single unique numeric answer only",
            "The original function unchanged", "Zero, regardless of the function"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "∫(4x^3 - 6x) dx equals:", "options": [
            "x^4 - 3x^2 + C", "12x^2 - 6 + C", "x^4 - 6x^2 + C", "4x^4 - 3x^2 + C"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why the constant of integration is often ignored/dropped in certain business applications?", "options": [
            "Because a specific boundary condition (e.g. known fixed cost) is used to solve for its exact value", "Because it is always exactly zero by definition",
            "Because integration never produces a constant", "Because business applications never require total functions"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Linear Programming Problems": [
        {"q": "'Linear Programming' is a mathematical technique used to:", "options": [
            "Find the optimal (maximum or minimum) value of a linear objective function, subject to linear constraints",
            "Solve only quadratic equations", "Calculate compound interest only", "Determine a company's tax liability only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'objective function' in a linear programming problem represents:", "options": [
            "The quantity (e.g. profit or cost) to be maximised or minimised", "A restriction on the variables",
            "A fixed constant with no variables", "The company's mission statement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Constraints' in a linear programming problem represent:", "options": [
            "Limitations or restrictions on the decision variables, typically expressed as linear inequalities", "The final numerical answer to the problem",
            "Random, unrelated values", "The objective function itself"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'feasible region' in a linear programming problem refers to:", "options": [
            "The set of all points that satisfy every given constraint simultaneously", "A single fixed point with no area",
            "The region outside all constraints", "The objective function's value at the origin"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a two-variable linear programming problem, the optimal solution (if it exists) occurs at:", "options": [
            "A corner point (vertex) of the feasible region", "The exact centre of the feasible region",
            "A point outside the feasible region", "Any random point within the feasible region"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The graphical method of solving a linear programming problem involves:", "options": [
            "Plotting the constraints to find the feasible region, then evaluating the objective function at each corner point",
            "Only plotting the objective function with no constraints", "Ignoring all constraints entirely",
            "Randomly guessing a solution with no method"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Non-negativity constraints' (x ≥ 0, y ≥ 0) are included in most business linear programming problems because:", "options": [
            "Quantities such as units produced or resources used cannot logically be negative", "They are mathematically required for every possible equation",
            "They eliminate the need for any other constraint", "They guarantee the objective function is always maximised"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A typical business application of linear programming is:", "options": [
            "Determining the optimal product mix to maximise profit given limited resources (labour, materials, time)",
            "Choosing a company's brand name", "Setting an employee's personal holiday schedule", "Deciding the company's logo colour scheme"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a linear programming problem's feasible region is unbounded and the objective is to maximise profit, the solution:", "options": [
            "May not have a finite maximum, depending on the direction of the objective function", "Is always exactly zero",
            "Is always found at the origin", "Cannot be analysed at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In linear programming, if the feasible region is empty (no point satisfies all constraints), the problem is said to be:", "options": [
            "Infeasible", "Optimally solved", "Unbounded", "Perfectly balanced"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A furniture company makes chairs and tables, each requiring different amounts of wood and labour, with limited supplies of both. This scenario is a classic example suited to:", "options": [
            "Linear programming (product-mix optimisation)", "Simple interest calculation only",
            "Logarithmic analysis only", "A single linear equation with one variable"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes a 'decision variable' in a linear programming problem?", "options": [
            "An unknown quantity (e.g. units of product A to produce) that the solver is trying to determine", "A fixed constant given in the problem",
            "The final answer to the problem, given at the start", "An irrelevant number with no role in the model"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'corner point method' for solving linear programming problems relies on the mathematical fact that:", "options": [
            "The optimal value of a linear objective function over a convex feasible region occurs at a vertex", "The optimal value always occurs strictly inside the region, never at a vertex",
            "There is never more than one feasible corner point", "The feasible region is always a single straight line"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A resource constraint such as '2x + 3y ≤ 60' (e.g. labour hours) in a linear programming problem means:", "options": [
            "The combination of x and y chosen cannot use more than 60 units of that resource", "x and y must always equal exactly 60",
            "The resource has no upper limit at all", "x and y must both be zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a limitation of basic (two-variable) linear programming as taught at this level?", "options": [
            "It becomes difficult to solve graphically once there are more than two decision variables", "It can only be used for problems with a single constraint",
            "It cannot be applied to any real business problem", "It requires no mathematical assumptions at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Evaluating the objective function at each feasible corner point and comparing the results allows the solver to:", "options": [
            "Identify which corner point gives the maximum (or minimum) value of the objective function", "Guarantee the objective function is always zero",
            "Eliminate the need for any constraints", "Avoid using the objective function altogether"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why linear programming assumes 'linearity' of both the objective function and constraints?", "options": [
            "It keeps the problem mathematically tractable, especially for graphical/corner-point solution methods at this level", "Because no real business relationship can ever be linear",
            "Because non-linear relationships are always easier to solve", "Because linearity has no bearing on solvability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A minimisation linear programming problem (e.g. minimising cost) still requires finding the:", "options": [
            "Corner point of the feasible region that gives the lowest objective function value", "Corner point that gives the highest objective function value only",
            "Centre of the feasible region only", "A point outside the feasible region"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following industries commonly uses linear programming for resource allocation and planning?", "options": [
            "Manufacturing (e.g. optimising production schedules given limited materials and labour)", "None - linear programming has no industry application",
            "Only the entertainment industry", "Only government tax departments"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best describes the overall goal of formulating a business problem as a linear programming model?", "options": [
            "To systematically determine the best allocation of limited resources to achieve a specific business objective", "To eliminate the need for any business decision-making",
            "To guarantee the company earns unlimited profit with no constraints", "To avoid quantifying any business goal"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Measures of Central tendency": [
        {"q": "'Measures of central tendency' are statistical values that describe:", "options": [
            "The centre or typical value of a data set", "The spread or variability of a data set",
            "The total number of observations only", "The relationship between two unrelated data sets"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'arithmetic mean' of a data set is calculated as:", "options": [
            "The sum of all observations divided by the number of observations", "The middle value when data is arranged in order",
            "The most frequently occurring value", "The largest value minus the smallest value"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'median' of a data set is:", "options": [
            "The middle value when data is arranged in ascending or descending order", "The average of all values",
            "The most frequently occurring value", "Always equal to the mean"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "For a data set with an EVEN number of observations, the median is calculated as:", "options": [
            "The average of the two middle values", "The larger of the two middle values only", "The smaller of the two middle values only",
            "The sum of all values divided by two"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'mode' of a data set is:", "options": [
            "The value that occurs most frequently", "The middle value", "The average of all values",
            "The difference between the highest and lowest values"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A data set can have more than one mode; such a data set is called:", "options": [
            "Bimodal (two modes) or multimodal (more than two)", "Unimodal only, by definition",
            "Impossible under standard statistical rules", "Always normally distributed"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which measure of central tendency uses EVERY value in the data set in its calculation?", "options": [
            "The arithmetic mean", "The mode", "The median (for a data set with more than 3 values)", "None of them use every value"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which measure of central tendency is LEAST affected by extreme outlier values?", "options": [
            "The median", "The arithmetic mean", "Both are equally affected", "Neither can be calculated with outliers present"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "For grouped (class-interval) data, the mean is typically calculated using:", "options": [
            "The midpoint of each class multiplied by its frequency, summed and divided by total frequency", "Only the highest class boundary",
            "Only the lowest class boundary", "The number of classes alone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'weighted mean' differs from the simple arithmetic mean in that it:", "options": [
            "Assigns different weights/importance to different values before averaging", "Gives every value exactly equal importance, just like the simple mean",
            "Can only be used for exactly two values", "Ignores all but the largest value"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, the mean salary of employees is a useful measure primarily because it:", "options": [
            "Provides a single summary figure representing the typical salary level, useful for comparison and planning", "Has no practical value in business decisions",
            "Always represents every individual employee's exact salary", "Only applies to government employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a company's salary data contains one extremely high outlier (e.g. the CEO's salary), which measure of central tendency would best represent a 'typical' employee salary?", "options": [
            "The median", "The mean", "Both give an identical, unaffected picture", "Neither can be used at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The mode is particularly useful for which type of data?", "options": [
            "Categorical/qualitative data, such as the most popular product colour sold", "Only precise numerical data with no repeats",
            "Only data with exactly two values", "Data that cannot be counted"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For a perfectly symmetric (normal) distribution, the mean, median, and mode are:", "options": [
            "All equal to each other", "Always completely different from each other", "Impossible to calculate",
            "Only defined for the mean, not the median or mode"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Given the data set {2, 4, 4, 6, 9}, the mean is:", "options": [
            "5", "4", "6", "9"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Given the data set {2, 4, 4, 6, 9}, the mode is:", "options": [
            "4", "5", "6", "9"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Given the data set {3, 7, 9, 12, 15}, the median is:", "options": [
            "9", "7", "12", "10"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why businesses commonly report BOTH the mean and the median of a data set (e.g. household income)?", "options": [
            "Comparing them can reveal the presence and effect of outliers or skewness in the data", "The two values are always mathematically identical, so reporting both is redundant",
            "Only the mean is ever meaningful in business", "Only the median is legally permitted to be reported"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is a limitation of the arithmetic mean as a measure of central tendency?", "options": [
            "It can be heavily distorted by extreme values (outliers)", "It never uses any of the actual data values",
            "It cannot be calculated for numerical data", "It is always identical to the mode"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Central tendency' measures are useful for business decision-making mainly because they:", "options": [
            "Summarise large data sets into a single representative figure for easier comparison and analysis", "Eliminate the need to collect any data at all",
            "Always guarantee an increase in profit", "Apply only to government statistics, never business data"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Probability": [
        {"q": "'Probability' is best defined as a measure of:", "options": [
            "The likelihood that a particular event will occur", "The exact outcome of an event with certainty",
            "The total number of events that have already occurred", "A fixed value unrelated to chance"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The probability of any event always lies within the range:", "options": [
            "0 to 1 (inclusive)", "-1 to 1", "0 to 100 only", "1 to infinity"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A probability of 0 means an event is:", "options": [
            "Impossible", "Certain to occur", "Equally likely to occur or not occur", "Occurring exactly half the time"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A probability of 1 means an event is:", "options": [
            "Certain to occur", "Impossible", "Very unlikely", "Undefined"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The classical formula for probability of an event E is:", "options": [
            "Number of favourable outcomes / Total number of possible outcomes", "Total number of outcomes / Number of favourable outcomes",
            "Number of favourable outcomes × Total number of outcomes", "Always exactly 0.5"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When a fair coin is tossed once, the probability of getting heads is:", "options": [
            "0.5", "1", "0", "0.25"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "When a fair six-sided die is rolled once, the probability of getting a 4 is:", "options": [
            "1/6", "1/2", "1/4", "1/3"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Two events are 'mutually exclusive' if:", "options": [
            "They cannot occur at the same time", "They always occur together", "One event's probability is always zero",
            "They are completely unrelated to any sample space"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For two mutually exclusive events A and B, P(A or B) is calculated as:", "options": [
            "P(A) + P(B)", "P(A) × P(B)", "P(A) - P(B)", "P(A) / P(B)"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Two events are 'independent' if:", "options": [
            "The occurrence of one does not affect the probability of the other occurring", "They always occur at exactly the same time",
            "They can never both occur", "One always causes the other to occur"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For two independent events A and B, P(A and B) is calculated as:", "options": [
            "P(A) × P(B)", "P(A) + P(B)", "P(A) - P(B)", "Always equal to 1"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Conditional probability', P(A|B), refers to:", "options": [
            "The probability of event A occurring, given that event B has already occurred", "The probability of A and B occurring completely independently",
            "The probability that neither A nor B occurs", "A value that is always equal to P(A)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'complement' of an event A, denoted A', represents:", "options": [
            "The event that A does NOT occur", "The event that A definitely occurs", "An unrelated event",
            "An event with probability always equal to P(A)"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The probability of the complement of an event A is calculated as:", "options": [
            "1 - P(A)", "P(A)", "1 + P(A)", "P(A) / 2"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A business uses probability to estimate the likelihood of a new product's success primarily to:", "options": [
            "Support risk assessment and informed decision-making under uncertainty", "Guarantee the product will definitely succeed",
            "Eliminate all business risk completely", "Avoid the need for any market research"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In quality control, probability can be used to estimate:", "options": [
            "The likelihood that a randomly selected product is defective", "The exact number of employees in the factory",
            "The company's registered office address", "The founder's personal preferences"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a bag contains 4 red balls and 6 blue balls, the probability of randomly drawing a red ball is:", "options": [
            "0.4", "0.6", "0.4/0.6", "1"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When two fair coins are tossed together, the probability of getting two heads is:", "options": [
            "0.25", "0.5", "1", "0.75"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'sample space' in probability refers to:", "options": [
            "The set of all possible outcomes of a random experiment", "Only the single most likely outcome",
            "A fixed constant with no relation to outcomes", "The average of all outcomes"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why insurance companies rely heavily on probability theory?", "options": [
            "To estimate the likelihood of claims/events and set premiums accordingly to manage risk", "Because probability has no relevance to insurance pricing",
            "Because insurance companies never assess risk", "Because probability guarantees zero claims will ever occur"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Measures of Dispersion": [
        {"q": "'Measures of dispersion' describe:", "options": [
            "The extent to which data values are spread out or scattered around the central value", "The single most typical value in a data set",
            "The total number of observations only", "The relationship between two unrelated variables"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Range', as a measure of dispersion, is calculated as:", "options": [
            "The highest value minus the lowest value in a data set", "The average of all values",
            "The middle value of the data set", "The most frequent value"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A key limitation of the range as a measure of dispersion is that it:", "options": [
            "Only considers the two extreme values and ignores the distribution of all other data points", "Uses every single data value in its calculation",
            "Is always equal to the mean", "Cannot be calculated for any numerical data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Variance' is defined as:", "options": [
            "The average of the squared deviations of each value from the mean", "The simple average of all values",
            "The difference between the highest and lowest values", "The most frequently occurring value"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Standard deviation' is calculated as:", "options": [
            "The square root of the variance", "The square of the variance", "The variance divided by the mean",
            "The sum of all deviations without squaring"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A LARGER standard deviation indicates that the data values are:", "options": [
            "More spread out (more variable) around the mean", "More tightly clustered around the mean",
            "All exactly equal to each other", "Impossible to interpret"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A standard deviation of ZERO would indicate that:", "options": [
            "All values in the data set are identical (equal to the mean)", "The data set has extremely high variability",
            "The mean cannot be calculated", "The data set contains negative numbers only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Quartiles' divide an ordered data set into:", "options": [
            "Four equal parts", "Two equal parts", "Ten equal parts", "One hundred equal parts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Interquartile Range (IQR)' is calculated as:", "options": [
            "The third quartile (Q3) minus the first quartile (Q1)", "The maximum value minus the minimum value",
            "The mean minus the median", "The second quartile alone"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Mean deviation' (mean absolute deviation) is calculated as:", "options": [
            "The average of the absolute differences between each value and the mean", "The average of the squared differences from the mean",
            "The difference between the highest and lowest values", "The most frequently occurring deviation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'Coefficient of Variation (CV)' is useful primarily because it allows comparison of variability between:", "options": [
            "Two data sets with different units or different means", "Only data sets that are already identical",
            "Only two values within the exact same data set", "Data sets that contain no numerical values"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The Coefficient of Variation is typically calculated as:", "options": [
            "(Standard Deviation / Mean) × 100", "Standard Deviation × Mean", "Mean / Standard Deviation only, with no percentage",
            "Variance × 100"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, comparing the standard deviation of monthly sales for two branches helps managers understand:", "options": [
            "Which branch has more consistent (less variable) sales performance", "The exact total annual revenue of the company",
            "The founder's personal investment portfolio", "The company's registered legal address"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Given the data set {4, 4, 4, 4}, the standard deviation is:", "options": [
            "0", "4", "1", "Undefined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following measures of dispersion uses every data value in its calculation?", "options": [
            "Standard deviation", "Range", "Neither uses all data values", "Only the mode does"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A stock with a HIGH standard deviation in its daily returns is generally considered to have:", "options": [
            "Higher risk/volatility", "Lower risk/volatility", "No risk at all", "A guaranteed fixed return"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes why measures of dispersion are used ALONGSIDE measures of central tendency, not instead of them?", "options": [
            "Central tendency shows the typical value while dispersion shows how much individual values vary around it - together they give a fuller picture",
            "Dispersion measures always replace the need to know the mean", "Central tendency alone is always sufficient to fully describe any data set",
            "The two types of measures are mathematically identical"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Quartile Deviation' (Semi-Interquartile Range) is calculated as:", "options": [
            "(Q3 - Q1) / 2", "Q3 - Q1", "(Q3 + Q1) / 2", "Q3 × Q1"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Two data sets can have the SAME mean but DIFFERENT standard deviations. This illustrates that:", "options": [
            "Central tendency and dispersion capture different, complementary aspects of a data set", "The mean alone always fully describes the shape of a data set",
            "Standard deviation is always identical whenever the mean is identical", "Measures of dispersion are redundant and unnecessary"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In quality control, a manufacturing process with a smaller standard deviation in product dimensions is generally considered:", "options": [
            "More consistent/reliable, since output is closer to the target value", "Less reliable than a process with a larger standard deviation",
            "Completely unrelated to product quality", "Impossible to measure in practice"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
