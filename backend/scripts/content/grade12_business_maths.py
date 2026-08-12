# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - Business Maths question bank.

Authored content (not content partner data - loaded with source='synthetic'
by scripts/load_question_bank.py). This subject does NOT exist as a shell
under course 210 at all - course 38's real "Business Maths" subject has
28 chapters, but ~20 of them are near-duplicate variants across different
curriculum "batches"/revisions with a stray "syllabus" entry, not a clean
canonical list worth reproducing wholesale. Since this is a brand-new
subject being created from scratch (unlike matching against pre-existing
real content, where no such latitude exists), a clean, curated ~8-chapter
canonical NEB Grade 12 Business Maths syllabus is used instead - the
standard topics taught under this subject. Created via
scripts/create_subject.py (its QUESTIONS dict keys become the new chapter
names), then loaded via scripts/load_question_bank.py. Never presented as
content partner content or as evidence about real students.

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}.
"""

QUESTIONS = {
    "Matrices and Determinants": [
        {"q": "A 'matrix' is best defined as:", "options": [
            "A rectangular array of numbers arranged in rows and columns", "A single number with no arrangement",
            "A type of graph used only for statistics", "A function with no numerical values"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A matrix with the same number of rows and columns is called a:", "options": [
            "Square matrix", "Row matrix", "Column matrix", "Rectangular matrix"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'order' of a matrix with 3 rows and 4 columns is written as:", "options": [
            "3 x 4", "4 x 3", "3 + 4", "12 x 1"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Two matrices can be added together only if they:", "options": [
            "Have the same order (same number of rows and columns)", "Have the same number of rows only, regardless of columns",
            "Are both square matrices", "Have determinants equal to zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For matrix multiplication AB to be defined, the number of columns in A must equal:", "options": [
            "The number of rows in B", "The number of columns in B", "The number of rows in A", "Zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'identity matrix' is a square matrix with:", "options": [
            "1s on the main diagonal and 0s elsewhere", "All entries equal to 1", "All entries equal to 0",
            "Entries equal to the row number only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'determinant' of a matrix is defined only for:", "options": [
            "A square matrix", "Any matrix regardless of shape", "A row matrix only", "A column matrix only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For a 2x2 matrix [[a, b], [c, d]], the determinant is calculated as:", "options": [
            "ad - bc", "ac - bd", "ab - cd", "ad + bc"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A matrix is called 'singular' if its determinant is:", "options": [
            "Equal to zero", "Equal to one", "A negative number", "Always positive"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'inverse' of a matrix A (denoted A^-1) exists only if:", "options": [
            "A is a square matrix with a non-zero determinant", "A has a determinant equal to zero",
            "A is a row matrix", "A has more rows than columns"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'transpose' of a matrix is obtained by:", "options": [
            "Interchanging its rows and columns", "Multiplying every entry by -1", "Adding 1 to every entry",
            "Deleting the last row"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business applications, matrices are commonly used to represent:", "options": [
            "Systems of data such as sales figures across multiple products and regions", "Only single isolated numbers with no structure",
            "Only qualitative, non-numerical business descriptions", "A concept with no real business application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Cramer's Rule uses determinants to solve:", "options": [
            "A system of linear equations", "A single quadratic equation", "A probability distribution",
            "A matrix's transpose only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'zero (null) matrix' is a matrix in which:", "options": [
            "Every entry is equal to zero", "Every entry is equal to one", "The determinant is always undefined",
            "Only the diagonal entries are zero"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Matrix multiplication is, in general:", "options": [
            "Not commutative (AB is not necessarily equal to BA)", "Always commutative for every pair of matrices",
            "Undefined for all square matrices", "Identical to ordinary number multiplication in every property"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A business using matrices to track cost and revenue across several products over several months would primarily benefit from matrices':", "options": [
            "Ability to organise and process large, structured, multi-dimensional data efficiently", "Complete inability to represent more than one number at a time",
            "Restriction to only qualitative, non-numerical data", "Requirement that only one product ever be tracked at a time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If matrix A has order 2x3 and matrix B has order 3x2, the product AB will have order:", "options": [
            "2x2", "3x3", "2x3", "Undefined, since the orders don't match"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Scalar multiplication of a matrix involves:", "options": [
            "Multiplying every entry of the matrix by a single constant number", "Multiplying the matrix by another matrix of the same order",
            "Adding a constant to only the diagonal entries", "A process that is undefined for matrices"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Solving a system of linear equations using the 'inverse matrix method' requires that the coefficient matrix be:", "options": [
            "Square and non-singular (invertible)", "Rectangular with unequal rows and columns", "Singular, with determinant zero",
            "A row matrix only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why matrices are a useful tool in business and economic analysis?", "options": [
            "They provide a compact, systematic way to organise and manipulate large sets of interrelated numerical data", "Matrices can only represent a single number and have no organisational benefit",
            "Matrices are relevant only to pure mathematics with no business application", "Matrices eliminate the need for any other form of data analysis"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Definite Integral and its Application": [
        {"q": "A 'definite integral' of a function over an interval [a, b] represents:", "options": [
            "The net signed area under the curve of the function between x = a and x = b", "The slope of the function at a single point",
            "The value of the function at x = a only", "A value that is always exactly zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Fundamental Theorem of Calculus connects definite integrals to:", "options": [
            "Antiderivatives (indefinite integrals) of a function", "Matrix determinants",
            "Probability distributions only", "Linear programming constraints"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The definite integral of f(x) = 2x from x = 0 to x = 3 equals:", "options": [
            "9", "6", "3", "0"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the limits of a definite integral are equal (a = b), the value of the integral is:", "options": [
            "0", "1", "Undefined", "Always negative"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Reversing the limits of a definite integral (from [a,b] to [b,a]) has the effect of:", "options": [
            "Changing the sign of the integral's value", "Doubling the value of the integral", "Having no effect on the value",
            "Making the integral undefined"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business economics, the definite integral of a marginal cost function over a range of output gives:", "options": [
            "The total (additional) cost of producing that range of output", "The average price of the product",
            "The total number of units sold", "The company's total tax liability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The definite integral of a marginal revenue function from 0 to Q gives:", "options": [
            "Total revenue from producing/selling Q units", "The marginal cost at exactly Q units",
            "The fixed cost of the firm", "The break-even quantity only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Consumer surplus' in economics can be represented using a definite integral as the area:", "options": [
            "Between the demand curve and the market price, up to the equilibrium quantity", "Between the supply curve and the vertical axis only",
            "Under the marginal cost curve exclusively", "Equal to total government tax revenue"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Producer surplus' can similarly be represented as the definite integral of the area:", "options": [
            "Between the market price and the supply curve, up to the equilibrium quantity", "Between the demand curve and the horizontal axis only",
            "Equal to total consumer spending", "Under the average cost curve exclusively"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A definite integral is evaluated by:", "options": [
            "Finding the antiderivative and evaluating it at the upper and lower limits, then subtracting", "Only differentiating the function once",
            "Multiplying the function by the interval length with no further calculation", "Setting the function equal to zero and solving"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a function lies entirely below the x-axis over an interval, its definite integral over that interval is:", "options": [
            "Negative", "Always positive regardless of the function's sign", "Always exactly zero", "Undefined"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The definite integral is useful in business for calculating 'total change' because it:", "options": [
            "Accumulates a rate of change (like a marginal function) over an interval to find total change", "Only measures instantaneous rate of change at a single point",
            "Has no relationship to marginal functions", "Can only be applied to constant functions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The area between two curves over an interval [a, b] is found by:", "options": [
            "Taking the definite integral of the difference between the two functions over that interval", "Multiplying the two functions together directly",
            "Adding the two functions' values at a single point only", "A calculation impossible using integration"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The definite integral of a constant function f(x) = k from a to b equals:", "options": [
            "k(b - a)", "k + (b - a)", "k / (b - a)", "Always zero regardless of k"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following notations correctly represents the definite integral of f(x) from a to b?", "options": [
            "The integral sign with limits a (lower) and b (upper), applied to f(x) dx", "f'(x) evaluated only at x = a",
            "The determinant of f(x) at point b", "The matrix product of f(a) and f(b)"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Given total cost is the integral of marginal cost, if marginal cost MC(x) = 3, the total cost of producing from x=0 to x=10 (ignoring fixed cost) is:", "options": [
            "30", "13", "3", "10"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key distinction between a definite and an indefinite integral is that a definite integral:", "options": [
            "Produces a specific numerical value, while an indefinite integral produces a general antiderivative function plus a constant", "Always includes an arbitrary constant of integration, unlike an indefinite integral",
            "Has no relationship to antiderivatives at all", "Can never be evaluated numerically"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Definite integrals are applied in business to calculate cumulative quantities such as:", "options": [
            "Total profit over a production range, given a marginal profit function", "Only the price of a single unit of a good",
            "Only qualitative business descriptions", "A company's total number of employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If f(x) >= g(x) on [a, b], the area between the two curves is given by the definite integral of:", "options": [
            "f(x) - g(x), from a to b", "g(x) - f(x), from a to b", "f(x) + g(x), from a to b", "f(x) multiplied by g(x)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why definite integrals are valuable in business decision-making involving marginal functions?", "options": [
            "They convert a known rate of change (marginal cost, marginal revenue) into a total, cumulative value useful for decisions", "They only provide instantaneous values with no cumulative interpretation",
            "They eliminate the need to know any marginal function at all", "They apply only to matrices, not to business cost/revenue functions"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Applications of Derivatives": [
        {"q": "In business, the 'marginal cost' function is obtained by taking the:", "options": [
            "First derivative of the total cost function with respect to quantity", "Second derivative of the total cost function",
            "Integral of the total cost function", "Reciprocal of the average cost function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'marginal revenue' function is obtained by taking the:", "options": [
            "First derivative of the total revenue function with respect to quantity", "Integral of the total revenue function",
            "Second derivative of the price function", "Product of price and the quantity's square root"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A profit-maximising output level, using derivatives, is found where:", "options": [
            "The derivative of the profit function equals zero, and the second derivative is negative", "The derivative of the profit function is always positive",
            "Total cost is at its absolute minimum only", "Price is set to zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A function has a 'local maximum' at a point where its first derivative is zero and its second derivative is:", "options": [
            "Negative", "Positive", "Undefined at that point", "Always exactly zero as well"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A function has a 'local minimum' at a point where its first derivative is zero and its second derivative is:", "options": [
            "Positive", "Negative", "Always zero", "Never defined"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In finding 'critical points' of a function, we set the:", "options": [
            "First derivative equal to zero and solve for x", "Function itself equal to one", "Second derivative equal to the function's value",
            "Function's domain equal to zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The point where marginal cost equals marginal revenue (MC = MR) is significant in business because it:", "options": [
            "Identifies the output level at which profit is maximised (given standard second-order conditions)", "Identifies the output level at which the firm always makes a loss",
            "Has no economic significance in production decisions", "Only applies when the firm has zero fixed costs"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The derivative of a demand function with respect to price is used to compute:", "options": [
            "Price elasticity of demand", "Total tax revenue directly", "The firm's fixed cost", "The exact number of competitors in the market"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If total revenue TR = 100Q - 2Q^2, the marginal revenue function MR is:", "options": [
            "100 - 4Q", "100 - 2Q", "100Q - 4Q", "50 - Q"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A function is said to be 'increasing' on an interval where its first derivative is:", "options": [
            "Positive", "Negative", "Exactly zero throughout", "Undefined throughout"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A function is said to be 'decreasing' on an interval where its first derivative is:", "options": [
            "Negative", "Positive", "Always exactly one", "Equal to the function's own value"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In optimisation problems (e.g. minimising average cost), the 'second derivative test' is used to determine whether a critical point is a:", "options": [
            "Maximum or a minimum", "Root of the original function only", "Point where the function is undefined", "Point of discontinuity only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The rate of change of average cost with respect to output can be found by differentiating the:", "options": [
            "Average cost function with respect to quantity", "Total revenue function with respect to price", "Demand function with respect to income",
            "Supply function with respect to time only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Elasticity of demand', calculated using derivatives, measures the:", "options": [
            "Responsiveness of quantity demanded to a change in price", "Absolute level of total revenue only",
            "Total cost of production at a single price point", "Government's tax rate on the good"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A business wanting to find the output level that minimises average cost would use derivatives to locate the point where the average cost function's:", "options": [
            "First derivative equals zero (with a positive second derivative confirming a minimum)", "Value is always exactly zero, regardless of derivatives",
            "Second derivative is undefined at every point", "First derivative is always positive throughout"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes an 'inflection point' of a function?", "options": [
            "A point where the curve changes concavity, often where the second derivative equals zero and changes sign", "A point where the function's value is always exactly zero",
            "A point unrelated to the second derivative", "A point where the function is guaranteed to be at its global maximum"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If a firm's profit function is P(Q) = -Q^2 + 40Q - 100, the derivative P'(Q) equals:", "options": [
            "-2Q + 40", "-Q + 40", "-2Q - 100", "40Q - 100"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Using the profit function P(Q) = -Q^2 + 40Q - 100, the profit-maximising quantity Q (where P'(Q) = 0) is:", "options": [
            "20", "40", "10", "100"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Derivatives are useful in business decision-making primarily because they measure:", "options": [
            "The instantaneous rate of change of one variable (like cost or revenue) with respect to another (like quantity)", "Only the total accumulated value of a variable over a range",
            "A concept unrelated to cost, revenue, or profit functions", "Only fixed values with no relationship to change"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why both first and second derivative conditions are typically checked when solving a business optimisation problem (e.g. profit maximisation)?", "options": [
            "The first derivative locates candidate critical points, while the second derivative confirms whether each is a maximum, minimum, or neither", "Only the first derivative is ever needed to confirm a maximum with full certainty",
            "The second derivative alone, without the first, is sufficient to solve any optimisation problem", "Neither derivative has any bearing on identifying a maximum or minimum"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Differential Equations and Applications": [
        {"q": "A 'differential equation' is an equation that involves:", "options": [
            "An unknown function and one or more of its derivatives", "Only constants with no variables at all",
            "A matrix and its determinant only", "A probability distribution with no calculus involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'order' of a differential equation refers to:", "options": [
            "The highest derivative appearing in the equation", "The total number of terms in the equation", "The degree of the independent variable only",
            "The number of solutions the equation has"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A first-order differential equation involves derivatives up to:", "options": [
            "The first derivative only", "The second derivative", "The third derivative", "No derivatives at all"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Solving a differential equation of the form dy/dx = ky (exponential growth/decay) gives a general solution of the form:", "options": [
            "y = Ce^(kx), where C is a constant", "y = kx + C", "y = Cx^k", "y = k/x"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business/economics, a differential equation of the form dP/dt = kP is commonly used to model:", "options": [
            "The continuous growth (or decline, if k is negative) of a quantity such as population or investment value over time", "A fixed, unchanging quantity with no time dependence",
            "A single, one-time transaction with no ongoing change", "A discrete matrix operation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'general solution' to a differential equation includes:", "options": [
            "An arbitrary constant, representing a family of possible solutions", "A single unique numerical answer with no constant",
            "No reference to any constant of integration", "Only matrix values"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'particular solution' to a differential equation is obtained by:", "options": [
            "Using given initial conditions to solve for the value of the arbitrary constant", "Ignoring all initial conditions entirely",
            "Always setting the constant equal to zero regardless of context", "Multiplying the general solution by an unrelated factor"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Continuous compound interest, where the amount A grows according to dA/dt = rA, models growth using:", "options": [
            "A first-order differential equation with exponential solution A = A0 * e^(rt)", "A quadratic equation with no time variable",
            "A matrix equation with no continuous variable", "A static formula with no rate of change involved"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Separable differential equations' can be solved by:", "options": [
            "Rearranging the equation so all terms involving one variable are on one side, then integrating both sides", "Multiplying both sides by zero",
            "Ignoring one of the two variables entirely", "Converting the equation into a matrix and finding its determinant"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Differential equations are used in business demand/supply modelling to represent situations where:", "options": [
            "The rate of change of price or quantity over time depends on the current price or quantity itself", "Price and quantity never change over time under any model",
            "Only a single static equilibrium value exists with no dynamics", "The model requires no calculus of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'initial condition' in a differential equation problem specifies:", "options": [
            "A known value of the function at a specific starting point, used to find the particular solution", "The final answer to the differential equation with no further work required",
            "The highest derivative order in the equation", "A condition that makes the equation unsolvable"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a company's revenue grows according to dR/dt = 0.05R with R(0) = 10,000, this models:", "options": [
            "Continuous growth of revenue at a constant proportional rate of 5% per unit time", "A one-time fixed revenue amount that never changes",
            "A declining revenue trend with no growth", "A revenue figure entirely unrelated to time"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A linear first-order differential equation has the general form dy/dx + P(x)y = Q(x), which is typically solved using:", "options": [
            "An integrating factor", "Matrix inversion only", "A probability distribution table", "Simple algebraic factoring with no calculus"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Differential equations differ from ordinary algebraic equations mainly because they involve:", "options": [
            "Rates of change (derivatives) of an unknown function, not just the function's static value", "Only constant values with no functions at all",
            "No unknowns of any kind", "Exclusively matrix operations rather than functions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In modelling market price adjustment over time, a differential equation might represent price change as proportional to the:", "options": [
            "Excess demand (demand minus supply) at that price", "Government's total tax revenue only",
            "Number of registered companies in the market", "The determinant of a demand matrix"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Solving a differential equation modelling population/investment decay (dy/dx = -ky, k > 0) results in a solution that:", "options": [
            "Decreases exponentially over time", "Increases exponentially over time", "Remains exactly constant over time", "Oscillates with no defined pattern"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is a practical business application of differential equations?", "options": [
            "Modelling continuous compound growth of an investment or loan balance over time", "Calculating a single company's total number of employees at one point in time",
            "Listing a company's product catalogue", "Determining a fixed, unchanging tax rate with no time dependence"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'first-order linear' differential equation is distinguished by the fact that the unknown function and its first derivative appear:", "options": [
            "To the first power only, with no products of the function and its derivative", "Raised to the second power or higher",
            "Multiplied together as a single combined term", "Not at all - only constants appear in the equation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why differential equations are relevant to modelling dynamic business/economic processes, unlike simple algebraic equations?", "options": [
            "They explicitly capture how a quantity changes over time or in response to another variable, rather than just its value at one point", "They can only represent quantities that never change over time",
            "They eliminate the need to consider time or rate of change in any economic model", "They apply only to physics problems, never to business or economics"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of studying differential equations within a Business Maths course?", "options": [
            "To provide tools for modelling and analysing how business and economic quantities change continuously over time", "To replace the need for studying algebra or basic arithmetic",
            "Differential equations have no practical relevance to any business scenario", "To focus exclusively on static, unchanging business data"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Financial Mathematics": [
        {"q": "'Simple interest' is calculated based on:", "options": [
            "The original principal amount only, for the entire duration", "The principal plus all previously accumulated interest",
            "A randomly changing base amount each period", "The borrower's total annual income"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Compound interest' is calculated based on:", "options": [
            "The principal plus previously accumulated interest, so interest is earned on interest", "Only the original principal, with no reference to prior interest",
            "A fixed amount unrelated to the principal", "The lender's personal expenses"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The simple interest formula is given by I = P x R x T, where R and T represent:", "options": [
            "Rate of interest and Time period respectively", "Total repayment and Tax rate respectively", "Risk factor and Transaction fee respectively",
            "Revenue and Turnover respectively"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "For a given principal, rate, and time period (greater than one period), compound interest will generally be:", "options": [
            "Greater than simple interest", "Less than simple interest", "Always exactly equal to simple interest", "Unrelated to simple interest"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Annuity' refers to:", "options": [
            "A series of equal payments made at regular intervals over a period of time", "A single, one-time lump sum payment only",
            "A type of tax levied only on businesses", "A fixed asset with no cash flow attached"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'present value' of a future sum of money reflects the idea that:", "options": [
            "Money available today is worth more than the same amount received in the future, due to its earning potential", "Money today and money in the future always have identical value",
            "Future money is always worth more than present money under any circumstance", "Present value has no relationship to interest rates"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'future value' of an investment refers to:", "options": [
            "The value the investment will grow to at a specified future date, given a rate of return", "The original amount invested, unchanged over time",
            "A value that is always identical to the present value", "The rate of interest itself, with no time dimension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Depreciation' in financial mathematics refers to the:", "options": [
            "Gradual decrease in the value of an asset over time", "Gradual increase in the value of an asset over time",
            "Sudden, one-time increase in cash flow", "Fixed interest paid on a savings account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'straight-line method' of depreciation allocates:", "options": [
            "An equal amount of depreciation expense each year over the asset's useful life", "A different, randomly varying amount of depreciation every year",
            "All depreciation in the asset's very first year only", "No depreciation until the asset is sold"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Amortization' refers to the process of:", "options": [
            "Gradually paying off a debt (like a loan) through regular scheduled payments over time", "Instantly repaying an entire loan in a single payment",
            "Increasing a loan balance without any repayment", "A method used only for calculating simple interest"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'effective annual rate' differs from the 'nominal annual rate' mainly because the effective rate accounts for:", "options": [
            "The effect of compounding within the year (e.g. monthly or quarterly compounding)", "Only simple interest, ignoring compounding entirely",
            "A completely different principal amount", "A rate set arbitrarily with no mathematical basis"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'sinking fund' is a fund created by making regular deposits in order to:", "options": [
            "Accumulate a specific sum of money by a future date, e.g. to repay a debt or replace an asset", "Immediately spend all funds with no future savings goal",
            "Avoid ever needing to calculate any interest", "Replace the need for any future financial planning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The formula for compound amount is A = P(1 + r/n)^(nt), where n represents:", "options": [
            "The number of times interest is compounded per year", "The total number of years only", "The principal amount", "The final compound amount itself"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Comparing loan offers using their effective annual rates rather than nominal rates helps a borrower to:", "options": [
            "Make a fair, accurate comparison that accounts for differences in compounding frequency", "Ignore compounding frequency entirely when comparing loans",
            "Guarantee the lowest possible repayment regardless of terms", "Avoid the need to compare interest rates altogether"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "An 'ordinary annuity' involves payments made:", "options": [
            "At the end of each period", "At the beginning of each period only", "At a single random point with no regular schedule",
            "Only once, at the very start of the investment"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In business, financial mathematics is commonly applied to decisions such as:", "options": [
            "Evaluating loan repayment schedules, investment returns, and asset depreciation", "Choosing the company's office location with no financial calculation",
            "Setting employee dress codes", "Designing a company's marketing slogan"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If Rs. 10,000 is invested at 10% simple interest per year, the interest earned after 2 years is:", "options": [
            "Rs. 2,000", "Rs. 1,000", "Rs. 2,100", "Rs. 200"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'declining balance method' of depreciation, unlike the straight-line method, results in:", "options": [
            "Higher depreciation expense in earlier years, decreasing over the asset's life", "An identical depreciation expense every single year",
            "Zero depreciation expense in every year", "Depreciation expense that increases every year without limit"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Understanding present value calculations is particularly important for businesses when evaluating:", "options": [
            "Long-term investment projects, by comparing the value of future cash flows in today's terms", "The company's daily petty cash balance only",
            "A single employee's daily attendance record", "The colour scheme of a marketing brochure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why compound interest grows faster than simple interest over time?", "options": [
            "Compound interest is calculated on a continually growing base (principal plus accumulated interest), while simple interest is always calculated on the original principal alone", "Compound interest uses a lower interest rate than simple interest by definition",
            "Simple interest and compound interest always produce identical growth over any time period", "Compound interest ignores the principal amount entirely"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Linear Programming Problem": [
        {"q": "'Linear Programming (LP)' is a mathematical technique used to:", "options": [
            "Find the optimal (maximum or minimum) value of a linear objective function, subject to linear constraints", "Solve differential equations exclusively",
            "Calculate matrix determinants only", "Model non-linear relationships exclusively"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'objective function' in a linear programming problem represents:", "options": [
            "The quantity (e.g. profit or cost) that is to be maximised or minimised", "A fixed constraint that cannot be changed",
            "The feasible region of the problem", "A constant with no variables involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Constraints' in a linear programming problem represent:", "options": [
            "Limitations or restrictions (e.g. on resources) expressed as linear inequalities/equations", "The final optimal answer to the problem",
            "A term unrelated to resource limitations", "Only the objective function itself"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'feasible region' in a linear programming problem is the set of all points that:", "options": [
            "Satisfy all the given constraints simultaneously", "Violate at least one constraint", "Lie outside every constraint boundary",
            "Represent only the objective function's coefficients"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a two-variable linear programming problem solved graphically, the optimal solution occurs at:", "options": [
            "A corner point (vertex) of the feasible region", "The exact centre of the feasible region", "Any random point within the feasible region",
            "A point always outside the feasible region"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Non-negativity constraints' in a linear programming problem typically require that decision variables be:", "options": [
            "Greater than or equal to zero", "Always exactly equal to zero", "Always negative", "Unrestricted, including negative values"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A business might use linear programming to determine:", "options": [
            "The optimal product mix that maximises profit given limited resources like labour and raw materials", "The company's official holiday calendar",
            "The founder's personal daily schedule", "The exact colour of the company's logo"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a linear programming problem's feasible region is unbounded and the objective is to maximise profit, it is possible that:", "options": [
            "The objective function has no finite maximum (an unbounded solution)", "The problem always has exactly one unique optimal solution",
            "The feasible region has no corner points at all", "The problem becomes impossible to define"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If a linear programming problem has no feasible region satisfying all constraints simultaneously, the problem is said to be:", "options": [
            "Infeasible", "Unbounded", "Always solvable with a unique answer", "Identical to every other linear programming problem"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The graphical method of solving a linear programming problem is generally limited to problems with:", "options": [
            "Two decision variables (for a 2D graph)", "Any number of decision variables with no limit", "Exactly one decision variable only",
            "No decision variables at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a linear programming problem, an 'isoprofit line' represents:", "options": [
            "A line along which every point yields the same total profit", "A single fixed point of maximum profit only",
            "A constraint boundary, not related to profit", "A line representing zero profit at every point on the graph"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A company producing two products, each requiring labour and raw material, with the goal of maximising total profit subject to labour and material limits, is a classic example of a:", "options": [
            "Linear programming (product-mix) problem", "Differential equation problem", "Matrix determinant problem", "Simple interest calculation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Linear programming assumes that the relationships between variables (e.g. cost per unit) are:", "options": [
            "Linear (proportional), not curved or exponential", "Always exponential in nature", "Entirely random with no defined pattern",
            "Irrelevant to the objective function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'corner point method' for solving a linear programming problem involves:", "options": [
            "Evaluating the objective function at each vertex of the feasible region and selecting the best value", "Evaluating the objective function only at the origin",
            "Ignoring the feasible region entirely", "Randomly guessing values until one works"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In a minimisation linear programming problem (e.g. minimising cost), the optimal solution is the corner point with the:", "options": [
            "Lowest value of the objective function among all feasible corner points", "Highest value of the objective function",
            "Exact midpoint value between the highest and lowest", "A value chosen without reference to the objective function"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A key business benefit of using linear programming for resource allocation is that it:", "options": [
            "Provides a systematic, mathematically optimal solution rather than relying purely on guesswork", "Guarantees unlimited resources regardless of actual constraints",
            "Eliminates the need to consider any constraint on resources", "Applies only to non-business, purely theoretical problems"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a constraint that might appear in a manufacturing linear programming problem?", "options": [
            "Total labour hours used must not exceed the available labour hours per week", "The company's marketing slogan must contain exactly five words",
            "The office must be painted a specific colour", "The CEO's preferred meeting time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If two different corner points of the feasible region yield the same optimal objective function value, the linear programming problem is said to have:", "options": [
            "Multiple (alternate) optimal solutions", "No feasible solution at all", "An unbounded solution only", "An error in the constraint formulation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Linear programming is widely used in industries such as manufacturing, logistics, and finance mainly because it helps organisations:", "options": [
            "Make optimal decisions about allocating limited resources among competing needs", "Avoid the need for any resource planning altogether",
            "Guarantee unlimited profit regardless of resource limits", "Apply only to problems with zero constraints"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises why linear programming is a valuable tool within Business Maths for management decision-making?", "options": [
            "It provides a structured, quantitative method for optimising outcomes like profit or cost under real-world resource constraints", "It has no practical relevance to real business resource allocation decisions",
            "It can only be used for problems entirely unrelated to business", "It removes the need for management to make any decisions at all"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Statistics": [
        {"q": "In this Business Maths context, 'statistics' involves applying:", "options": [
            "Quantitative techniques to collect, analyse and interpret business-relevant data", "Only qualitative descriptions with no numerical analysis",
            "Techniques relevant exclusively to natural sciences, not business", "A field with no application to business decision-making"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'arithmetic mean' of a data set is calculated as:", "options": [
            "The sum of all values divided by the number of values", "The middle value when data is arranged in order",
            "The most frequently occurring value", "The difference between the highest and lowest values"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'median' of an ordered data set with an odd number of values is:", "options": [
            "The single middle value", "The average of the two middle values", "Always equal to the mean", "The smallest value in the set"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'mode' of a data set refers to:", "options": [
            "The value that occurs most frequently", "The average of all values", "The middle value when ordered",
            "The range between the highest and lowest values"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Standard deviation' measures:", "options": [
            "The spread/variability of data values around the mean", "Only the single highest value in a data set",
            "The total count of observations", "A measure unrelated to variability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Correlation' between two business variables (e.g. advertising spend and sales) measures:", "options": [
            "The strength and direction of the linear relationship between them", "Only the total value of one variable, ignoring the other",
            "A concept unrelated to any relationship between variables", "The exact cause-and-effect relationship with full certainty"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A correlation coefficient close to +1 indicates:", "options": [
            "A strong positive linear relationship between the two variables", "A strong negative linear relationship", "No relationship whatsoever between the variables",
            "An undefined relationship"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A correlation coefficient close to -1 indicates:", "options": [
            "A strong negative linear relationship between the two variables", "A strong positive linear relationship", "No relationship at all between the variables",
            "A relationship that cannot be measured"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A correlation coefficient close to 0 suggests:", "options": [
            "Little to no linear relationship between the two variables", "A perfect positive linear relationship", "A perfect negative linear relationship",
            "An error in the data collection process"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Regression analysis' is used in business primarily to:", "options": [
            "Model and predict the value of one variable based on one or more other variables", "Only calculate the mean of a single variable",
            "Replace the need for any data collection", "Measure a company's total number of employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In simple linear regression (y = a + bx), the coefficient 'b' represents:", "options": [
            "The slope, i.e. the estimated change in y for a one-unit change in x", "The y-intercept only", "A constant unrelated to x or y",
            "The correlation coefficient itself"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Index numbers', as a statistical tool, are used in business to measure:", "options": [
            "Relative changes in a variable such as price or sales over time compared to a base period", "The absolute total number of employees in a company",
            "A single, unchanging fixed value with no time comparison", "A concept with no application to business trends"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Time series analysis' in business statistics involves studying data that is:", "options": [
            "Collected sequentially over successive time periods, to identify trends and patterns", "Collected only once, at a single point in time",
            "Entirely unrelated to any chronological order", "Limited exclusively to financial statements"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'trend' in time series analysis refers to:", "options": [
            "The long-term general direction (upward, downward, or stable) in the data over time", "A single random fluctuation with no long-term pattern",
            "The data value at only the very first time period", "A concept unrelated to time series data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Businesses use statistical measures like the mean and standard deviation of monthly sales to:", "options": [
            "Understand typical sales performance and how much it varies from month to month", "Avoid the need for any sales data collection",
            "Set the company's official logo colour", "Determine an employee's personal daily schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which measure of central tendency is most affected by extreme outlier values in a data set?", "options": [
            "The arithmetic mean", "The median", "The mode", "None of the measures are affected by outliers"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A company analysing the relationship between its advertising expenditure and monthly sales using regression would primarily be trying to:", "options": [
            "Quantify how sales tend to change as advertising expenditure changes, to inform future budgeting", "Determine the exact colour scheme for its advertisements",
            "Avoid making any future advertising decisions", "Calculate the company's total tax liability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why both a measure of central tendency (like the mean) and a measure of dispersion (like standard deviation) are typically reported together in business statistics?", "options": [
            "The mean alone doesn't reveal how consistent or variable the underlying data is, which the dispersion measure captures", "Reporting both measures together always produces contradictory conclusions",
            "The mean and standard deviation always convey exactly the same information", "Dispersion measures are only relevant to non-business statistics"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes correlation from causation in business statistical analysis?", "options": [
            "Correlation shows two variables move together, but doesn't by itself prove that one variable causes the change in the other", "Correlation and causation always mean exactly the same thing",
            "A high correlation coefficient always proves a direct causal relationship", "Causation can be established without ever examining correlation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall value of statistics within a Business Maths curriculum?", "options": [
            "It equips learners with tools to analyse business data, identify patterns/relationships, and support evidence-based decisions", "Statistics has no practical connection to real business decision-making",
            "It is relevant only to government agencies, not private businesses", "It replaces the need for any other mathematical tool in business"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Probability": [
        {"q": "'Probability' is a numerical measure, between 0 and 1, of:", "options": [
            "The likelihood that a particular event will occur", "The exact total number of possible outcomes only",
            "A company's total revenue", "A fixed value unrelated to chance or uncertainty"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A probability value of 0 indicates that an event is:", "options": [
            "Impossible - it will certainly not occur", "Certain to occur", "Equally likely to occur or not occur",
            "Undefined"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A probability value of 1 indicates that an event is:", "options": [
            "Certain to occur", "Impossible to occur", "Equally likely to occur or not occur", "Always exactly 50% likely"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'sample space' of a random experiment refers to:", "options": [
            "The set of all possible outcomes of that experiment", "Only the single most likely outcome", "A single randomly chosen outcome only",
            "A concept unrelated to random experiments"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Two events are said to be 'mutually exclusive' if:", "options": [
            "They cannot both occur at the same time", "They always occur together", "One event's probability is always exactly double the other's",
            "They are entirely unrelated to the concept of probability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For two mutually exclusive events A and B, the probability of either A or B occurring is calculated as:", "options": [
            "P(A) + P(B)", "P(A) x P(B)", "P(A) - P(B)", "P(A) / P(B)"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Two events are 'independent' if:", "options": [
            "The occurrence of one event does not affect the probability of the other occurring", "They always occur together with certainty",
            "They can never both occur under any circumstance", "One event's occurrence guarantees the other's occurrence"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "For two independent events A and B, the probability of both A and B occurring is calculated as:", "options": [
            "P(A) x P(B)", "P(A) + P(B)", "P(A) - P(B)", "P(A) divided by 2"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Conditional probability', written P(A|B), refers to the probability of:", "options": [
            "Event A occurring, given that event B has already occurred", "Event A and event B never occurring together",
            "Event B occurring with no reference to event A at all", "A concept that cannot be defined mathematically"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If a fair coin is tossed once, the probability of getting 'heads' is:", "options": [
            "0.5", "1", "0", "0.25"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "If a fair six-sided die is rolled once, the probability of rolling a number greater than 4 is:", "options": [
            "2/6 (1/3)", "4/6 (2/3)", "1/6", "5/6"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In business, probability is commonly used in risk analysis to:", "options": [
            "Estimate the likelihood of uncertain future events, such as a project's success or failure", "Guarantee a certain, fixed business outcome with no uncertainty",
            "Eliminate the need to consider any risk at all", "Set a company's fixed tax obligation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Expected value' of a probability distribution represents:", "options": [
            "The weighted average of all possible outcomes, weighted by their probabilities", "Only the single highest possible outcome",
            "A value unrelated to probability", "The total count of all possible outcomes"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A business evaluating two investment options with different probable returns would use 'expected value' to:", "options": [
            "Compare the average anticipated outcome of each option, accounting for the likelihood of each possible result", "Guarantee the exact actual return with complete certainty",
            "Ignore the probability of different outcomes entirely", "Determine the company's total number of employees"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Addition rule' for two events A and B that are NOT mutually exclusive is given by:", "options": [
            "P(A or B) = P(A) + P(B) - P(A and B)", "P(A or B) = P(A) + P(B)", "P(A or B) = P(A) x P(B)", "P(A or B) = P(A) - P(B)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The sum of probabilities of all possible outcomes in a sample space must equal:", "options": [
            "1", "0", "100", "An undefined value depending on the experiment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'random variable' in probability refers to:", "options": [
            "A variable whose value is determined by the outcome of a random experiment", "A variable that is always fixed and unchanging",
            "A term unrelated to probability theory", "A value that can never be measured numerically"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In quality control, a business might use probability to estimate:", "options": [
            "The likelihood that a randomly selected product from a batch is defective", "The exact colour of the product packaging",
            "The founder's personal preferences", "The company's registered office address"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best distinguishes 'independent events' from 'mutually exclusive events' in probability?", "options": [
            "Independent events don't affect each other's probability and CAN occur together, while mutually exclusive events cannot occur together at all", "Independent and mutually exclusive events are always exactly the same thing",
            "Mutually exclusive events always occur together with certainty", "Independent events can never occur together under any circumstance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises why probability theory is valuable for business decision-making under uncertainty?", "options": [
            "It provides a systematic way to quantify and reason about uncertain outcomes, supporting more informed risk-based decisions", "It guarantees a certain, risk-free outcome for every business decision",
            "Probability has no relevance to real-world business decisions involving risk", "It applies only to games of chance, never to business scenarios"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
