# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - Economics question bank.

Authored content (not content partner data - loaded with source='synthetic'
by scripts/load_question_bank.py). Topically accurate, written to read
like genuine exam questions per explicit user instruction. Chapter names
match, exactly, the Section rows already sitting under course 210 ("NEB
Grade 12 Management") Economics subject (subject_id=34293) - verified via
a direct DB query (not assumed) before writing this module, since an
earlier chapter name in this course had a real double-space typo that
required exact matching. Never presented as content partner content or as
evidence about real students.

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}.
"""

QUESTIONS = {
    "Basic Concept of Economics and Allocation of Resources": [
        {"q": "Economics, at Grade 12 level, continues to be defined fundamentally as the study of:", "options": [
            "How society allocates scarce resources among competing unlimited wants", "How governments print unlimited currency",
            "How companies design their advertisements", "How banks build new branches"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'central economic problem' of scarcity requires every economy to answer the questions:", "options": [
            "What to produce, how to produce, and for whom to produce", "Where to produce, when to advertise, and who owns the currency",
            "How to tax, how to vote, and how to migrate", "What colour to use, how loud to advertise, and when to close"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Allocative efficiency' in resource allocation refers to a situation where resources are used to:", "options": [
            "Produce the combination of goods and services that best satisfies society's wants", "Produce only a single good regardless of demand",
            "Produce nothing at all", "Maximise waste in production"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A command (planned) economy differs from a market economy mainly in that resource allocation is decided by:", "options": [
            "Central government planning rather than market forces", "Market forces of demand and supply alone",
            "Random chance with no decision-maker", "International organisations only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's economy is generally best classified as a:", "options": [
            "Mixed economy, combining market forces with government intervention", "A purely centrally planned economy with no market activity",
            "A purely free market economy with zero government role", "An economy with no resource allocation mechanism at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Production Possibility Curve (PPC) illustrates the concept of:", "options": [
            "Opportunity cost and the trade-off between producing two goods with limited resources", "The exact price of every good in the economy",
            "The government's total annual tax revenue", "A single fixed level of output with no alternatives"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An outward shift of a country's PPC represents:", "options": [
            "Economic growth due to increased resources or improved technology", "A decrease in the country's productive capacity",
            "No change in the economy's productive capacity", "A purely theoretical concept with no real-world relevance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Opportunity cost' is best defined as:", "options": [
            "The value of the next best alternative given up when a choice is made", "The total monetary price of a good",
            "A cost that never changes regardless of choice", "A cost incurred only by government agencies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the difference between microeconomics and macroeconomics, as studied by this stage?", "options": [
            "Microeconomics studies individual markets/units; macroeconomics studies the economy as a whole", "The two terms are entirely identical with no distinction",
            "Macroeconomics only studies a single firm", "Microeconomics only studies government policy"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A key factor of production unique in that its total supply is often considered relatively fixed in the short run is:", "options": [
            "Land", "Labour", "Capital", "Entrepreneurship"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a market economy, the 'price mechanism' allocates resources primarily by:", "options": [
            "Signalling relative scarcity and value through changing prices, guiding producers and consumers", "Fixing every price permanently by law",
            "Ignoring consumer preferences entirely", "Allocating resources randomly with no reference to price"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a 'positive economic statement'?", "options": [
            "\"Nepal's inflation rate was 7% last year\" (a verifiable fact)", "\"The government should reduce taxes\" (an opinion)",
            "\"It is unfair that some people are poor\" (a value judgment)", "\"Businesses ought to pay higher wages\" (a value judgment)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of a 'normative economic statement'?", "options": [
            "\"The government should increase the minimum wage\"", "\"GDP grew by 5% last year\"",
            "\"The unemployment rate is currently 4%\"", "\"The exchange rate is Rs. 133 per US dollar\""],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why resource allocation is a central concern of economics, even in resource-rich countries?", "options": [
            "Human wants are considered unlimited, so even abundant resources remain relatively scarce against total demand", "Resources are always exactly sufficient to meet every possible want",
            "Allocation only matters in resource-poor countries", "Wants are always fully satisfied regardless of resource availability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Economic growth' is most directly measured by an increase in a country's:", "options": [
            "Real Gross Domestic Product (GDP) over time", "Population size alone, regardless of output",
            "Number of government ministries", "Number of registered political parties"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best describes why economics is often called a 'social science'?", "options": [
            "It studies human behaviour and decision-making regarding the use of scarce resources within society", "It has no connection to human behaviour at all",
            "It is purely a natural/physical science with no social element", "It studies only non-human natural phenomena"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'mixed economy' seeks to combine the advantages of:", "options": [
            "Market efficiency with government intervention to address market failures and equity concerns", "Complete central planning with zero market activity",
            "Complete market freedom with zero government involvement of any kind", "Neither market forces nor government planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best illustrates the concept of opportunity cost for the Nepal government when allocating its budget?", "options": [
            "Spending more on road infrastructure means less budget is available for healthcare, given a fixed total budget", "The government's budget is always unlimited with no trade-offs",
            "All government programs can always be fully funded simultaneously with no constraint", "Budget allocation has no relationship to opportunity cost"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is generally considered a limitation of relying purely on free market forces to allocate all resources?", "options": [
            "Markets may fail to account for externalities or provide public goods adequately, requiring some government role", "Free markets always produce a perfectly equitable distribution of resources with no exception",
            "Free markets eliminate the need for any resource allocation decision", "Free markets have no limitations of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why studying resource allocation is particularly relevant for a developing economy like Nepal's?", "options": [
            "Limited resources must be carefully prioritised across competing development needs such as infrastructure, education and health",
            "Developing economies have unlimited resources with no need for prioritisation", "Resource allocation is only relevant to already-developed economies",
            "Nepal faces no resource constraints of any kind"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Market and Revenue Curves": [
        {"q": "A 'perfectly competitive market' is characterised by:", "options": [
            "Many buyers and sellers, homogeneous products, and free entry/exit", "A single seller controlling the entire market",
            "Only two firms competing", "Complete government control over all prices"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'monopoly' market structure is characterised by:", "options": [
            "A single seller with significant control over price, and high barriers to entry", "Many sellers offering identical products",
            "No barriers to entry at all", "A market where price is always set by the government only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Monopolistic competition' is characterised by:", "options": [
            "Many sellers offering differentiated (not identical) products, with relatively free entry", "A single seller with no competitors",
            "Exactly two firms with identical products", "Complete government ownership of all firms"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'oligopoly' market structure is characterised by:", "options": [
            "A few large firms dominating the market, often interdependent in pricing decisions", "An unlimited number of small firms with no market power",
            "A single government-owned firm only", "A market with no barriers to entry whatsoever"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a perfectly competitive market, an individual firm is a 'price taker', meaning it:", "options": [
            "Must accept the market price and cannot influence it individually", "Can set any price it wishes with no consequence",
            "Controls the entire market price", "Sets prices only in coordination with the government"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Total Revenue (TR)' is calculated as:", "options": [
            "Price per unit multiplied by quantity sold", "Total cost minus total profit",
            "Fixed cost plus variable cost", "Price per unit divided by quantity sold"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Average Revenue (AR)' is calculated as:", "options": [
            "Total Revenue divided by quantity sold", "Total Revenue multiplied by quantity sold",
            "Marginal Revenue divided by price", "Total Cost divided by quantity sold"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Marginal Revenue (MR)' is defined as:", "options": [
            "The additional revenue earned from selling one more unit of output", "The total revenue earned from all units sold",
            "The average price charged across all units", "The total cost of producing one more unit"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a perfectly competitive market, the firm's Average Revenue (AR) curve is:", "options": [
            "Horizontal, equal to the market price at every quantity", "Downward sloping, like a monopolist's demand curve",
            "Upward sloping throughout", "Always equal to zero"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In a perfectly competitive market, Marginal Revenue (MR) is:", "options": [
            "Equal to price (MR = AR = Price) at every output level", "Always greater than price",
            "Always less than average cost", "Unrelated to price"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In a monopoly, the demand curve facing the firm (which is also its AR curve) is:", "options": [
            "Downward sloping, since the firm must lower price to sell more", "Perfectly horizontal, identical to perfect competition",
            "Vertical, with no relationship to quantity", "Always upward sloping"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "For a monopolist facing a downward-sloping demand curve, the Marginal Revenue curve lies:", "options": [
            "Below the Average Revenue (demand) curve", "Above the Average Revenue curve",
            "Exactly on top of the Average Revenue curve", "Unrelated to the demand curve"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Product differentiation', a key feature of monopolistic competition, refers to firms:", "options": [
            "Making their products appear distinct through branding, quality, or features", "Selling completely identical, indistinguishable products",
            "Being legally required to sell the exact same product as competitors", "Ignoring consumer preferences entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Interdependence' among firms is a distinguishing feature of which market structure?", "options": [
            "Oligopoly", "Perfect competition", "Monopoly", "Monopolistic competition (to a lesser extent than oligopoly)"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A key barrier to entry that helps sustain a monopoly could be:", "options": [
            "Legal patents, licences, or control over an essential resource", "An unlimited number of competing sellers",
            "Perfect information available to all potential entrants", "Zero start-up costs for competitors"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a good produced under conditions closer to perfect competition?", "options": [
            "A standardised agricultural commodity like rice, sold by many farmers", "Electricity supply from a single national utility",
            "A patented pharmaceutical drug", "A unique piece of software with no substitutes"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Non-price competition, such as advertising and branding, is especially prominent under:", "options": [
            "Monopolistic competition and oligopoly", "Perfect competition only", "Pure monopoly only, with no branding needed",
            "None of the market structures use non-price competition"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why understanding market structure is important for a business's pricing strategy?", "options": [
            "The degree of competition and control over price varies significantly across market structures, shaping strategy",
            "Market structure has no bearing on how a firm sets its prices", "All market structures allow a firm to set any price with no consequence",
            "Pricing strategy is identical across every market structure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a firm's Total Revenue is Rs. 50,000 from selling 1,000 units, its Average Revenue is:", "options": [
            "Rs. 50", "Rs. 500", "Rs. 50,000,000", "Rs. 5"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following market structures is generally considered to have the LEAST control by an individual firm over the market price?", "options": [
            "Perfect competition", "Monopoly", "Oligopoly", "Monopolistic competition"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Cost Curves": [
        {"q": "'Total Fixed Cost (TFC)' refers to costs that:", "options": [
            "Do not change with the level of output in the short run", "Change directly and proportionally with output",
            "Are always exactly zero", "Only occur in the long run"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Total Variable Cost (TVC)' refers to costs that:", "options": [
            "Change directly with the level of output produced", "Remain exactly constant regardless of output",
            "Are incurred only once, at business start-up", "Never appear on a firm's cost curve"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Total Cost (TC)' is calculated as:", "options": [
            "Total Fixed Cost plus Total Variable Cost", "Total Revenue minus Total Profit",
            "Average Cost divided by quantity", "Marginal Cost multiplied by quantity"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Average Fixed Cost (AFC)' continuously falls as output increases because:", "options": [
            "A constant total fixed cost is spread over an increasing number of units", "Fixed cost increases with output",
            "Variable cost is ignored entirely", "AFC is unrelated to output level"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Marginal Cost (MC)' is defined as:", "options": [
            "The additional cost incurred in producing one more unit of output", "The total cost of all units produced",
            "The average price charged to consumers", "The fixed cost divided by total output"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The typical shape of the short-run Average Variable Cost (AVC) curve is:", "options": [
            "U-shaped, first falling then rising as output increases", "A straight horizontal line at all output levels",
            "Continuously falling with no minimum point", "Continuously rising from the very first unit with no initial fall"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Marginal Cost (MC) curve intersects the Average Variable Cost (AVC) and Average Total Cost (ATC) curves at:", "options": [
            "Their respective minimum points", "Their respective maximum points", "The output level of zero",
            "A point unrelated to either curve"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The law of diminishing marginal returns is a key reason why, in the short run, Marginal Cost eventually:", "options": [
            "Rises as more units of a variable input are added to a fixed input", "Falls continuously with no eventual rise",
            "Remains constant forever regardless of output", "Becomes negative at high output levels"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In the long run, ALL costs are considered:", "options": [
            "Variable, since all factors of production can be adjusted", "Fixed, since no factor can be changed",
            "Irrelevant to a firm's output decision", "Identical to short-run costs in every respect"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Economies of scale' refer to a situation where, as output increases, a firm's:", "options": [
            "Long-run average cost decreases", "Long-run average cost increases",
            "Total fixed cost increases proportionally with output", "Marginal cost is always zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Diseconomies of scale' occur when, beyond a certain output level, a firm's long-run average cost:", "options": [
            "Begins to rise as output continues to increase", "Continues to fall indefinitely with no limit",
            "Becomes exactly zero", "Has no relationship to output level"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of a fixed cost for a factory in the short run?", "options": [
            "Rent paid on the factory building", "Cost of raw materials used in production",
            "Wages of hourly production workers", "Cost of electricity used by machines during production"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Long-Run Average Cost (LRAC)' curve is often described as an 'envelope curve' because it is formed by:", "options": [
            "Tracing the lowest point achievable across a series of short-run average cost curves at each output level",
            "A single fixed short-run cost curve with no relationship to others", "Ignoring all short-run cost curves entirely",
            "A curve that only applies to a single specific output level"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Average Total Cost (ATC) is calculated as:", "options": [
            "Average Fixed Cost plus Average Variable Cost (or Total Cost divided by output)", "Total Fixed Cost divided by Total Variable Cost",
            "Marginal Cost multiplied by output", "Total Revenue minus Total Cost"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If Marginal Cost is below Average Total Cost, Average Total Cost is:", "options": [
            "Falling", "Rising", "Constant with no change", "Undefined"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If Marginal Cost is above Average Total Cost, Average Total Cost is:", "options": [
            "Rising", "Falling", "Always exactly equal to Marginal Cost", "Unrelated to Marginal Cost"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Understanding cost curves helps a business primarily in:", "options": [
            "Making informed decisions about the optimal level of output and pricing", "Determining the company's official holiday calendar",
            "Choosing the company's office paint colour", "Setting the founder's personal daily schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A firm experiencing economies of scale by expanding production might benefit from:", "options": [
            "Bulk purchasing discounts and more efficient use of specialised equipment", "Increased average cost with every additional unit produced",
            "A complete loss of any cost advantage from expanding", "No change in cost structure whatsoever"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best distinguishes short-run cost analysis from long-run cost analysis?", "options": [
            "The short run has at least one fixed factor, while in the long run all factors are variable", "Short-run and long-run cost analysis are always identical",
            "The long run has more fixed factors than the short run", "Cost analysis is irrelevant in the long run"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A firm's decision on whether to shut down production in the short run is often linked to whether price covers at least:", "options": [
            "Average Variable Cost", "Average Fixed Cost only, ignoring variable cost", "Zero cost, regardless of any expense",
            "Only the founder's personal salary"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Theory of Price and Output Determination": [
        {"q": "Under perfect competition, in the short run, a firm maximises profit at the output level where:", "options": [
            "Marginal Revenue equals Marginal Cost (MR = MC)", "Total Revenue is at its absolute highest regardless of cost",
            "Total Cost is exactly zero", "Average Fixed Cost equals Average Variable Cost"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In perfect competition, since MR = Price, the profit-maximising condition MR = MC becomes:", "options": [
            "Price = Marginal Cost", "Price = Average Fixed Cost only", "Price = Total Cost",
            "Price = Total Revenue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the long run, under perfect competition, firms tend to earn:", "options": [
            "Normal profit only, due to free entry and exit eliminating supernormal profit", "Permanently high supernormal profit with no competition",
            "Guaranteed losses in every case", "Profits set entirely by government decree"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A monopolist maximises profit at the output level where:", "options": [
            "Marginal Revenue equals Marginal Cost (MR = MC), then reads price off the demand curve at that quantity", "Price always equals Marginal Cost, exactly as in perfect competition",
            "Total Revenue is minimised", "Average Cost is at its highest possible level"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Because a monopolist's MR curve lies below its demand (AR) curve, the profit-maximising price is generally:", "options": [
            "Higher than marginal cost, unlike in perfect competition", "Always exactly equal to marginal cost",
            "Always below average variable cost", "Set entirely by consumers, not the firm"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Supernormal (economic) profit' refers to profit that is:", "options": [
            "Above the normal return needed to keep a firm in business", "Exactly equal to zero",
            "Always negative", "Identical to total revenue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Normal profit' is best understood as:", "options": [
            "The minimum return required to keep a firm's resources employed in their current use (an implicit cost)", "An extraordinarily large profit earned only by monopolies",
            "A profit that is always exactly zero for the entire economy", "A profit earned only by government-owned firms"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Under monopolistic competition, in the long run, firms tend to earn:", "options": [
            "Normal profit only, as free entry erodes any supernormal profit over time", "Permanent supernormal profit with no erosion",
            "Guaranteed losses at every output level", "Profits fixed by international agreement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Price rigidity ('sticky prices') is sometimes observed in oligopoly markets due to firms' fear of:", "options": [
            "Triggering a price war if they change prices unilaterally", "Losing all customers regardless of price changes",
            "Government intervention in every single pricing decision", "Complete elimination of any competitor"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'kinked demand curve' model is used to explain price rigidity in which market structure?", "options": [
            "Oligopoly", "Perfect competition", "Pure monopoly", "Monopolistic competition"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A firm operating at a loss in the short run will continue to produce (rather than shut down) as long as:", "options": [
            "Price covers at least its average variable cost", "Price is exactly zero",
            "Price covers only a fraction of its rent", "The firm has no variable cost at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In a perfectly competitive market, if firms are earning supernormal profits in the short run, in the long run we would expect:", "options": [
            "New firms to enter the market, increasing supply and driving price/profit down toward normal profit", "All existing firms to immediately shut down",
            "The government to permanently fix the price at the current level", "No change at all, regardless of profit levels"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Price discrimination by a monopolist refers to:", "options": [
            "Charging different prices to different customer groups for the same product, based on willingness to pay", "Charging every customer the exact identical price with no variation",
            "A practice that is legally required in every market", "Selling below cost to every customer at all times"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following conditions is generally necessary for successful price discrimination?", "options": [
            "The seller must have some market power and be able to separate customer groups/prevent resale", "The market must be perfectly competitive with zero market power",
            "All customers must have identical willingness to pay", "The good must be freely resold between customers with no restriction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Government price controls, such as a price ceiling, are sometimes imposed on monopoly output primarily to:", "options": [
            "Protect consumers from excessively high prices due to the monopolist's market power", "Increase the monopolist's profit further",
            "Eliminate the product from the market entirely", "Guarantee the monopolist a higher output at a higher price"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why output tends to be lower and price higher under monopoly compared to perfect competition, for a similar cost structure?", "options": [
            "A monopolist restricts output to maximise profit, since MR lies below the demand curve", "A monopolist always produces the maximum possible output regardless of profit",
            "Monopoly and perfect competition always produce an identical price and output", "Monopolists are legally required to minimise their own profit"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Allocative efficiency' is generally best achieved under which market structure, in simple theoretical models?", "options": [
            "Perfect competition, where price equals marginal cost", "Pure monopoly, where price exceeds marginal cost",
            "Oligopoly, due to price rigidity", "None of the market structures can achieve allocative efficiency"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes a monopolist's incentive regarding innovation, according to some economic arguments?", "options": [
            "Supernormal profits can provide funds and incentive for research and development", "Monopolists have no possible incentive to innovate under any circumstance",
            "Monopolists are legally banned from any research spending", "Innovation is only possible under perfect competition"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following market structures is most likely to result in advertising and non-price competition as a central strategy for output/price determination?", "options": [
            "Monopolistic competition", "Perfect competition, where products are identical", "Pure monopoly with a single seller and no competitors",
            "A market with only one buyer and one seller"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why studying price and output determination across market structures matters for economic policy?", "options": [
            "It helps policymakers understand efficiency, consumer welfare, and when intervention (e.g. regulation) may be warranted", "Market structure has no relevance to any government policy",
            "Price and output are always identical regardless of market structure", "Policy analysis never considers market structure"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Price Determination of Factors of Production": [
        {"q": "'Factor pricing' refers to the process of determining the:", "options": [
            "Price (return) paid to factors of production such as labour, land, capital and entrepreneurship", "Price of only final consumer goods",
            "Government's total tax rate", "Exchange rate between two currencies"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The price of labour is generally referred to as:", "options": [
            "Wage", "Rent", "Interest", "Profit"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The price/return to land is generally referred to as:", "options": [
            "Rent", "Wage", "Interest", "Profit"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The price/return to capital is generally referred to as:", "options": [
            "Interest", "Wage", "Rent", "Dividend only, with no other term"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The reward to entrepreneurship for organising production and bearing risk is generally referred to as:", "options": [
            "Profit", "Wage", "Rent", "Interest"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The demand for a factor of production (e.g. labour) is often described as a 'derived demand' because it:", "options": [
            "Arises from the demand for the final goods/services that factor helps produce", "Exists independently with no relation to any final good",
            "Is set entirely by government decree with no market basis", "Has no connection to consumer demand at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'Marginal Revenue Product (MRP)' of a factor refers to:", "options": [
            "The additional revenue generated by employing one more unit of that factor", "The total cost of employing all units of that factor",
            "The average wage paid across the entire economy", "A fixed government-set value unrelated to output"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A profit-maximising firm will hire additional units of a factor (e.g. labour) up to the point where:", "options": [
            "Marginal Revenue Product equals the factor's price (e.g. wage)", "Marginal Revenue Product is exactly zero regardless of wage",
            "The factor's price is entirely ignored", "Total Revenue Product equals Total Cost only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following would generally cause an increase in the market wage rate for a particular type of labour?", "options": [
            "An increase in demand for that labour, with supply unchanged", "A decrease in demand for that labour, with supply unchanged",
            "An increase in the supply of that labour, with demand unchanged", "No change in either demand or supply"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Trade unions can influence wage determination primarily by:", "options": [
            "Collectively bargaining with employers on behalf of workers", "Having no possible influence on wages at all",
            "Reducing worker representation entirely", "Setting the national currency exchange rate"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A legally mandated 'minimum wage' set above the market equilibrium wage may result in:", "options": [
            "A surplus of labour (unemployment), since quantity of labour supplied exceeds quantity demanded at that wage", "An automatic increase in the demand for labour to match supply",
            "No effect on the labour market whatsoever", "A decrease in the market wage rate"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Economic rent' in the context of land refers to:", "options": [
            "Payment for the use of land, whose supply is often considered relatively fixed", "A payment made only for capital equipment",
            "A type of government tax on income", "A payment made only to entrepreneurs"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The interest rate on capital/loans is influenced significantly by:", "options": [
            "The demand for and supply of loanable funds in the financial market", "Only the government's annual holiday calendar",
            "Only the exchange rate with a single foreign currency", "A value fixed permanently and never changing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Profit' as a factor reward differs from wage, rent, and interest mainly because it is:", "options": [
            "A residual, uncertain return remaining after all other costs are paid, reflecting risk-bearing", "A perfectly guaranteed, fixed payment regardless of business performance",
            "Paid before any other factor cost is settled", "Entirely unrelated to business risk"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Migration of workers, such as Nepali workers seeking employment abroad, can affect the DOMESTIC wage rate for certain skills by:", "options": [
            "Reducing domestic labour supply for those skills, potentially raising domestic wages for remaining workers", "Having absolutely no effect on domestic labour markets",
            "Automatically lowering wages for all remaining domestic workers in every case", "Eliminating the need for any wage determination at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why factor pricing is important for understanding income distribution in an economy?", "options": [
            "The prices paid to labour, land, capital and entrepreneurship largely determine how national income is distributed among these groups",
            "Factor pricing has no relationship to how income is distributed in society", "Income distribution is determined solely by government lottery",
            "Factor prices are always identical regardless of the amount of each factor supplied"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A skill shortage in a particular occupation (e.g. skilled IT professionals) would typically be expected to:", "options": [
            "Push wages upward for that occupation, other things equal", "Push wages downward for that occupation",
            "Have no effect on that occupation's wage", "Immediately eliminate the need for that occupation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'transfer earning' of a factor of production refers to:", "options": [
            "The minimum payment required to keep that factor in its current use, rather than moving to its next best alternative use", "The entire total payment received by the factor, with no reference to alternative use",
            "A payment made only to government employees", "A concept with no relevance to factor pricing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why entrepreneurs, unlike labourers on a fixed wage, may earn negative returns (losses)?", "options": [
            "Entrepreneurial profit is a residual reward tied directly to business risk and uncertain outcomes", "Entrepreneurs are legally guaranteed a fixed positive return regardless of business performance",
            "Entrepreneurs never bear any risk in a business venture", "Profit is fixed by government regulation at a guaranteed positive rate"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises how factor markets differ from product (goods) markets?", "options": [
            "Factor markets determine payments to the owners of productive resources, while product markets determine prices of final goods/services",
            "Factor markets and product markets are entirely identical with no distinction", "Factor markets only exist in developed economies",
            "Product markets determine wages, while factor markets determine consumer goods prices"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Banking System and Monetary Policy": [
        {"q": "A 'central bank' in a country's banking system primarily functions to:", "options": [
            "Regulate the money supply, oversee commercial banks, and implement monetary policy", "Only provide personal savings accounts to individual citizens",
            "Only issue business loans to small shopkeepers", "Only manage the government's foreign embassies"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Nepal's central bank is known as:", "options": [
            "Nepal Rastra Bank", "Nepal Commercial Bank", "Nepal Industrial Bank", "Nepal Cooperative Bank"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Monetary policy' refers to actions taken by a central bank to control:", "options": [
            "Money supply and interest rates in order to influence economic activity", "Only the level of government taxation",
            "Only international diplomatic relations", "Only the price of imported oil directly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Expansionary monetary policy' typically involves the central bank:", "options": [
            "Lowering interest rates and/or increasing money supply to stimulate economic activity", "Raising interest rates and reducing money supply to slow the economy",
            "Eliminating the currency altogether", "Fixing all prices in the economy by law"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Contractionary (tight) monetary policy' typically involves the central bank:", "options": [
            "Raising interest rates and/or reducing money supply to control inflation", "Lowering interest rates to boost spending",
            "Printing unlimited currency with no restriction", "Removing all banking regulation entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Cash Reserve Ratio (CRR)' refers to the:", "options": [
            "Minimum percentage of deposits commercial banks must hold as reserves with the central bank", "Maximum interest rate a bank can charge on any loan",
            "Total profit earned by a commercial bank", "Exchange rate between two currencies"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Increasing the Cash Reserve Ratio (CRR) tends to:", "options": [
            "Reduce the amount of money commercial banks can lend, tightening money supply", "Increase the amount banks can lend without limit",
            "Have no effect on the money supply", "Automatically lower interest rates"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'Bank Rate' (or policy rate) refers to the rate at which:", "options": [
            "The central bank lends to commercial banks", "Commercial banks lend to each other exclusively",
            "Customers deposit money in a savings account", "The government collects income tax"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Open Market Operations' as a monetary policy tool involve the central bank:", "options": [
            "Buying or selling government securities to influence money supply", "Only setting the national minimum wage",
            "Only regulating foreign embassies", "Only issuing personal identity documents"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The primary function of commercial banks in the banking system is to:", "options": [
            "Accept deposits from the public and provide loans/credit", "Only print new currency notes",
            "Only set national fiscal policy", "Only manage international diplomatic missions"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Credit creation' by commercial banks refers to the process by which banks:", "options": [
            "Expand the effective money supply by lending out a portion of deposits, which are redeposited and re-lent", "Physically print new banknotes themselves",
            "Reduce the total money supply to zero", "Only hold deposits with no lending activity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "One key objective of Nepal Rastra Bank's monetary policy is to maintain:", "options": [
            "Price stability and support sustainable economic growth", "Maximum possible inflation with no limit",
            "Zero banking activity in the country", "Complete elimination of the national currency"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Inflation targeting' as a monetary policy approach involves the central bank:", "options": [
            "Setting a specific inflation rate goal and adjusting policy tools to achieve it", "Ignoring inflation entirely with no target",
            "Targeting only the unemployment rate with no reference to prices", "Fixing all prices directly by government decree"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A rise in the policy interest rate set by the central bank generally makes borrowing:", "options": [
            "More expensive, which tends to reduce consumer and business spending", "Cheaper, boosting spending immediately",
            "Completely free with zero cost", "Entirely unrelated to spending decisions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'financial inclusion' as a modern policy goal of Nepal Rastra Bank?", "options": [
            "Expanding access to banking and financial services to underserved populations, including rural areas", "Restricting banking services only to the wealthiest citizens",
            "Eliminating rural banking access entirely", "A goal unrelated to the central bank's mandate"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a supervisory function of a central bank over commercial banks?", "options": [
            "Setting prudential regulations and monitoring banks' financial soundness", "Directly managing each commercial bank's daily customer service",
            "Setting the exact salary of every bank employee", "Choosing each bank's office decoration"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The money supply in an economy broadly includes:", "options": [
            "Currency in circulation plus deposits held in banks", "Only physical banknotes and coins, excluding all deposits",
            "Only gold reserves held by the government", "Only foreign currency held abroad"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why monetary policy and fiscal policy are often coordinated by governments?", "options": [
            "Together they influence overall aggregate demand, and uncoordinated policy could work against shared economic goals", "The two policies have no possible interaction with each other",
            "Only one of the two policies is ever used at any given time", "Coordination has no relevance to macroeconomic stability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Remittance inflows into Nepal's banking system are significant partly because they:", "options": [
            "Add to the country's foreign exchange reserves and support banking sector liquidity", "Have no relationship to the banking system at all",
            "Always decrease the total money supply", "Are illegal under Nepal Rastra Bank's regulations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of monetary policy in a modern economy like Nepal's?", "options": [
            "To manage money supply and interest rates in pursuit of price stability, growth and financial stability", "To eliminate the banking system entirely",
            "To fix all prices directly with no role for markets", "To have no influence on economic activity whatsoever"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Government Finance": [
        {"q": "'Government finance' (public finance) refers to the study of:", "options": [
            "How governments raise revenue and allocate expenditure", "How private individuals manage personal savings only",
            "How foreign companies set their prices", "How international sports events are funded exclusively"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The two main components of a government budget are:", "options": [
            "Government revenue and government expenditure", "Only foreign aid and foreign debt",
            "Only import duties and export duties", "Only private company profits"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Tax revenue' as a government income source includes:", "options": [
            "Income tax, VAT, customs duty, and other taxes collected from citizens/businesses", "Only foreign grants received by the government",
            "Only loans taken from international organisations", "Only lottery winnings collected by citizens"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Non-tax revenue' for a government includes sources such as:", "options": [
            "Fees, fines, royalties, and dividends from state-owned enterprises", "Only income tax collected from individuals",
            "Only VAT collected from businesses", "Only customs duty on imports"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Recurrent (current) expenditure' by government typically covers:", "options": [
            "Regular, ongoing costs such as salaries and administrative expenses", "Only one-time infrastructure projects like building a new road",
            "Only foreign investment abroad", "Only debt owed by other countries to Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Capital expenditure' by government typically covers:", "options": [
            "Spending on long-term infrastructure and development projects, such as roads and hydropower", "Only day-to-day salary payments",
            "Only routine office supply purchases", "Only interest payments on existing debt"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'balanced budget' occurs when:", "options": [
            "Government revenue equals government expenditure", "Government revenue is always exactly zero",
            "Government expenditure always exceeds revenue by a fixed amount", "The government collects no tax revenue whatsoever"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'budget deficit' occurs when:", "options": [
            "Government expenditure exceeds government revenue", "Government revenue exceeds government expenditure",
            "Revenue and expenditure are exactly equal", "The government has no expenditure of any kind"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'budget surplus' occurs when:", "options": [
            "Government revenue exceeds government expenditure", "Government expenditure exceeds government revenue",
            "The government collects zero revenue", "Revenue and expenditure are always exactly equal by law"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Fiscal policy' refers to the government's use of:", "options": [
            "Spending and taxation to influence the economy", "Only interest rate changes by the central bank",
            "Only foreign exchange rate management", "Only private company pricing decisions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Expansionary fiscal policy' typically involves:", "options": [
            "Increasing government spending and/or cutting taxes to stimulate economic activity", "Decreasing government spending and raising taxes to slow the economy",
            "Eliminating all government spending entirely", "Fixing all prices in the economy directly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Contractionary fiscal policy' typically involves:", "options": [
            "Decreasing government spending and/or raising taxes to reduce inflationary pressure", "Increasing government spending without limit",
            "Cutting all taxes to zero permanently", "Removing the government's role in the economy entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's federal budget is typically presented and approved through:", "options": [
            "The federal parliament, following constitutional budgetary procedures", "A private company board meeting",
            "An international organisation with no domestic role", "A random public vote with no formal parliamentary process"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Public debt' refers to:", "options": [
            "The total amount a government owes to domestic and/or foreign creditors", "The total savings held by private citizens",
            "A private company's outstanding loans only", "A measure of a country's population size"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Governments may borrow (incurring public debt) primarily to:", "options": [
            "Finance a budget deficit or fund long-term development projects", "Avoid ever collecting any tax revenue",
            "Eliminate the need for a national budget entirely", "Reduce their own annual expenditure to zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Progressive taxation', often used in income tax systems, means that the tax rate:", "options": [
            "Increases as income increases", "Decreases as income increases", "Remains exactly the same for every income level",
            "Applies only to government employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Since Nepal's transition to federalism, government finance responsibilities are shared across:", "options": [
            "Federal, provincial, and local levels of government, each with budgetary authority", "Only the federal government, with no provincial or local role",
            "Only local governments, with no federal or provincial involvement", "A single unelected central authority with no other tiers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Intergovernmental fiscal transfers in Nepal's federal system refer to:", "options": [
            "Funds transferred from the federal government to provincial and local governments", "Funds transferred only from private companies to the government",
            "Payments made only to foreign governments", "A concept irrelevant to Nepal's federal structure"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why governments use fiscal policy alongside monetary policy to manage the economy?", "options": [
            "Fiscal policy directly influences government spending/taxation, complementing monetary policy's control of money supply/interest rates",
            "Fiscal policy and monetary policy are entirely identical in every respect", "Fiscal policy has no possible impact on aggregate demand",
            "Only monetary policy is ever used to manage a modern economy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of government finance/public finance as a field of study?", "options": [
            "Understanding how governments efficiently raise and allocate resources to meet public needs and economic objectives", "Understanding only how private individuals invest their personal savings",
            "A field with no connection to national economic policy", "A field relevant only to foreign governments, not Nepal"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "International Trade": [
        {"q": "'International trade' refers to:", "options": [
            "The exchange of goods and services between countries", "Trade that occurs only within a single country's borders",
            "Trade conducted exclusively by government agencies", "A concept with no relevance to modern economies"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The theory of 'Absolute Advantage', proposed by Adam Smith, suggests a country should specialise in producing goods it can produce:", "options": [
            "More efficiently (using fewer resources) than other countries", "Less efficiently than any other country",
            "Only for its own domestic consumption, never for trade", "Using the exact same resources as every other country"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The theory of 'Comparative Advantage', proposed by David Ricardo, suggests that even if a country is less efficient at producing everything, it can still benefit from trade by specialising in goods where it has:", "options": [
            "The lowest opportunity cost of production relative to other goods", "No opportunity cost of production at all",
            "The highest possible opportunity cost", "Complete self-sufficiency with no need for trade"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Exports' refer to goods and services:", "options": [
            "Sold by a country to foreign buyers", "Purchased by a country from foreign sellers",
            "Produced and consumed entirely domestically", "Donated freely with no payment involved"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Imports' refer to goods and services:", "options": [
            "Purchased by a country from foreign sellers", "Sold by a country to foreign buyers",
            "Produced and consumed entirely domestically with no foreign involvement", "Always illegal under international law"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A country's 'balance of trade' refers to the difference between its:", "options": [
            "Total exports and total imports of goods", "Total government revenue and expenditure",
            "Total population and total land area", "Total interest rate and inflation rate"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'trade deficit' occurs when a country's:", "options": [
            "Imports exceed its exports", "Exports exceed its imports", "Imports and exports are exactly equal",
            "Government collects zero tax revenue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'trade surplus' occurs when a country's:", "options": [
            "Exports exceed its imports", "Imports exceed its exports", "The country engages in no trade at all",
            "The government has a balanced budget"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'tariff' is best described as:", "options": [
            "A tax imposed on imported (or sometimes exported) goods", "A subsidy given to domestic exporters only",
            "A type of foreign aid", "A private company's internal pricing policy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key purpose of imposing tariffs is often to:", "options": [
            "Protect domestic industries from foreign competition by raising the price of imports", "Make imported goods cheaper than domestic goods",
            "Eliminate all domestic industries entirely", "Guarantee zero government revenue from trade"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'quota' in international trade refers to:", "options": [
            "A limit on the quantity of a good that can be imported (or exported)", "A tax imposed on domestic production only",
            "A subsidy paid to foreign producers", "An agreement to eliminate all trade barriers immediately"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Free trade' refers to international trade conducted:", "options": [
            "With minimal government-imposed barriers such as tariffs and quotas", "Under complete government control with no market activity",
            "Only between two countries with identical economies", "Only when both countries have zero exports"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Protectionism' refers to government policies that:", "options": [
            "Restrict international trade to protect domestic industries", "Actively encourage completely unrestricted free trade with no barriers",
            "Have no relationship to trade policy at all", "Apply exclusively to domestic-only transactions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The World Trade Organization (WTO) primarily aims to:", "options": [
            "Facilitate and regulate international trade among member countries", "Set each country's domestic tax policy directly",
            "Control the internal politics of member nations", "Replace all national currencies with a single currency"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key argument in favour of free trade is that it allows countries to benefit from:", "options": [
            "Specialisation according to comparative advantage, increasing overall efficiency and consumer choice", "Complete self-sufficiency with no need for any other country",
            "Eliminating the need for any domestic production", "Guaranteed equal income for every citizen"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A common argument in favour of protectionism is to:", "options": [
            "Protect 'infant industries' that are not yet able to compete internationally", "Maximise foreign imports at the expense of domestic industry",
            "Eliminate all domestic industries as quickly as possible", "Guarantee that no country ever exports any good"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Exchange rate' refers to:", "options": [
            "The value of one currency expressed in terms of another currency", "The total interest rate charged by a bank",
            "The government's total annual tax rate", "A measure of a country's population growth"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'devaluation' of a country's currency generally makes its exports:", "options": [
            "Cheaper for foreign buyers, potentially boosting export volumes", "More expensive for foreign buyers",
            "Completely unaffected by the exchange rate change", "Illegal to sell internationally"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes a Free Trade Agreement (FTA) between two or more countries?", "options": [
            "An agreement to reduce or eliminate trade barriers such as tariffs among the participating countries", "An agreement to permanently ban all trade between the countries",
            "An agreement that applies only to a single company", "An agreement that has no effect on tariffs or trade barriers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall economic rationale for international trade?", "options": [
            "It allows countries to specialise based on comparative advantage, increasing total global output and welfare", "International trade always reduces total global output",
            "Countries never benefit from engaging in international trade under any theory", "Trade is only relevant to the world's largest economies"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Foreign Trade and Foreign Employment of Nepal": [
        {"q": "Nepal's foreign trade has historically been characterised by:", "options": [
            "A persistent trade deficit, with imports significantly exceeding exports", "A large and persistent trade surplus",
            "Perfectly balanced trade every single year", "Complete absence of any international trade"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's largest trading partner, both for imports and exports, has traditionally been:", "options": [
            "India, due to geographic proximity and historical trade relations", "A distant island nation with no land connection",
            "A country with no shared border or historical trade ties", "An entirely unspecified, unknown trading partner"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a commonly cited item in Nepal's export basket?", "options": [
            "Carpets, handicrafts, and agricultural products", "Commercial passenger aircraft", "Large-scale petroleum exports",
            "Advanced semiconductor manufacturing equipment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a commonly cited major import for Nepal?", "options": [
            "Petroleum products", "Handicrafts", "Carpets", "Herbal and medicinal plants for export"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Foreign employment' refers to Nepali citizens:", "options": [
            "Working abroad in foreign countries", "Working exclusively within Nepal's own borders",
            "Being employed only by the Nepal government", "Retiring without any employment history"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A major reason for the large scale of foreign employment among Nepali workers is:", "options": [
            "Limited domestic employment opportunities relative to the size of the labour force", "An excess of high-paying domestic jobs with no need to migrate",
            "A government ban on all domestic employment", "Complete absence of any unemployment in Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Remittance' refers to:", "options": [
            "Money sent home by migrant workers from abroad to their families in their home country", "A type of import tariff",
            "A government tax on foreign companies", "A type of domestic bank loan"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Remittance income is significant to Nepal's economy mainly because it:", "options": [
            "Forms a substantial share of GDP, supports household consumption, and boosts foreign exchange reserves", "Has no measurable impact on Nepal's economy",
            "Is used exclusively for government military spending", "Is smaller than Nepal's total goods export earnings"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following are common destination countries/regions for Nepali foreign labour migrants?", "options": [
            "Gulf countries (e.g. Qatar, Saudi Arabia) and Malaysia", "Only Antarctica", "Only uninhabited islands",
            "Nowhere - Nepali citizens are legally barred from working abroad"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A major challenge associated with Nepal's high reliance on foreign employment is:", "options": [
            "Loss of a significant working-age population domestically, affecting domestic labour supply and family structures", "A complete absence of any economic benefit from remittances",
            "Zero risk to migrant workers in any destination country", "Full replacement of the entire domestic economy by migration"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's trade deficit is partly financed/offset by:", "options": [
            "Remittance inflows from foreign employment", "A complete absence of any external financing",
            "Only foreign military aid", "Only revenue from stock market trading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's membership in regional/international trade frameworks, such as SAARC, aims to:", "options": [
            "Promote regional trade cooperation and reduce trade barriers among member countries", "Eliminate all international relationships entirely",
            "Ban Nepal from trading with any country", "Apply only to military cooperation, not trade"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Being a land-locked country affects Nepal's foreign trade mainly by:", "options": [
            "Increasing transportation costs and dependence on transit routes through neighbouring countries", "Having no effect on trade costs whatsoever",
            "Guaranteeing Nepal the lowest possible shipping costs in the world", "Eliminating the need for any import/export infrastructure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Government policy aimed at promoting Nepali exports might include:", "options": [
            "Export incentives, improved trade infrastructure, and trade facilitation agreements", "Banning all exports entirely",
            "Increasing tariffs on Nepal's own export goods", "Eliminating all trade-related government agencies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the relationship between foreign employment and Nepal's foreign exchange reserves?", "options": [
            "Remittances sent by migrant workers are a major source of foreign exchange inflow, supporting reserves", "Foreign employment has no connection to foreign exchange reserves",
            "Migrant remittances always deplete Nepal's foreign exchange reserves", "Foreign exchange reserves are determined solely by tourism revenue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following industries in Nepal benefits directly from foreign tourist arrivals as a form of 'invisible export'?", "options": [
            "Tourism and hospitality (hotels, trekking, travel services)", "Deep-sea fishing", "Heavy machinery export",
            "Domestic-only retail with no foreign customers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes a policy challenge related to managing Nepal's foreign employment sector?", "options": [
            "Ensuring migrant worker safety, fair recruitment practices, and protection against exploitation abroad", "Foreign employment requires no government oversight or policy attention",
            "Migrant workers face no risks of any kind while working abroad", "Recruitment agencies require no regulation whatsoever"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Diversifying Nepal's export base beyond traditional goods is often recommended by economists mainly to:", "options": [
            "Reduce reliance on a narrow range of products and markets, lowering economic vulnerability", "Increase Nepal's dependence on a single export product",
            "Eliminate the need for any international trade", "Guarantee an immediate trade surplus with no further effort"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why Nepal's trade deficit with India specifically has been historically large?", "options": [
            "Geographic proximity, open border trade relations, and Nepal's high demand for Indian consumer and industrial goods",
            "Nepal exports far more to India than it imports", "Nepal and India have no trade relationship of any kind", "India is entirely landlocked and unable to trade with Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall importance of studying foreign trade and foreign employment together in Nepal's economic context?", "options": [
            "Both are deeply interconnected forces shaping Nepal's balance of payments, foreign exchange earnings, and overall economic stability",
            "Foreign trade and foreign employment are completely unrelated economic phenomena", "Neither foreign trade nor foreign employment has any effect on Nepal's economy",
            "This topic is relevant only to countries other than Nepal"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Poverty, Inequality, Unemployment and Human Resources": [
        {"q": "'Absolute poverty' refers to a situation where a person's income/consumption is:", "options": [
            "Insufficient to meet basic subsistence needs such as food, shelter and clothing", "Higher than the national average income",
            "Determined purely by personal preference with no reference to basic needs", "Always exactly zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Relative poverty' is measured in comparison to:", "options": [
            "The general standard of living or income distribution within a society", "A single, universally fixed dollar amount with no reference to context",
            "A person's own past income only", "Zero income only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'poverty line' refers to:", "options": [
            "A minimum income/consumption threshold below which a person is considered poor", "The maximum income a person can legally earn",
            "A measure of a country's total population", "A type of government tax bracket for the wealthy only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Income inequality' refers to:", "options": [
            "The uneven distribution of income among individuals or households in a society", "A situation where every individual earns exactly the same income",
            "A measure of a country's total government spending", "A measure unrelated to income distribution"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The Gini coefficient is commonly used to measure:", "options": [
            "The degree of income inequality within a country", "The exchange rate between two currencies",
            "The literacy rate of a country", "The unemployment rate directly"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A Gini coefficient of 0 would represent:", "options": [
            "Perfect income equality (everyone has the exact same income)", "Perfect income inequality (one person has all the income)",
            "An undefined or impossible value", "A measure unrelated to income at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Unemployment' refers to a situation where individuals who are:", "options": [
            "Willing and able to work cannot find suitable employment", "Not part of the labour force at all, such as retirees",
            "Fully employed in their preferred job", "Working exactly the number of hours they wish"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Disguised (hidden) unemployment' refers to a situation, common in agriculture, where:", "options": [
            "More workers are employed than are actually needed, so removing some would not reduce output", "Every worker is fully and productively employed with no excess labour",
            "No workers are employed at all in the sector", "Unemployment is measured with perfect accuracy in every case"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Seasonal unemployment' refers to unemployment that occurs due to:", "options": [
            "Regular seasonal fluctuations in demand for labour, such as in agriculture or tourism", "A permanent, year-round mismatch of worker skills",
            "A one-time, non-repeating economic shock", "A worker's personal choice to never seek employment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Underemployment' refers to a situation where a person is:", "options": [
            "Employed but working fewer hours than desired, or in a job below their skill/qualification level", "Fully and appropriately employed with no mismatch",
            "Completely outside the labour force by personal choice", "Retired with a full pension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Human resources' in the context of national development refers to:", "options": [
            "The skills, knowledge, health, and productive capacity of a country's population", "Only the physical natural resources of a country",
            "Only the government's financial reserves", "Only imported machinery and equipment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Investment in education and healthcare is often described as investment in:", "options": [
            "Human capital, which raises long-term productivity and living standards", "Only physical infrastructure with no reference to people",
            "A concept unrelated to economic development", "A category with no effect on productivity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is often cited as a cause of poverty in developing economies like Nepal?", "options": [
            "Low levels of productive employment, limited access to capital, and low human capital investment", "Excessive government investment in education and health",
            "Universal access to high-quality employment for all citizens", "An oversupply of investment capital with no unmet need"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following government strategies is commonly used to address poverty and unemployment?", "options": [
            "Employment generation programs, skills training, and targeted social protection schemes", "Eliminating all government spending on social welfare",
            "Reducing access to education for low-income groups", "Banning any form of skills training"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Social protection' programs (e.g. social security allowances) primarily aim to:", "options": [
            "Provide a safety net for vulnerable groups such as the elderly, disabled, or poor", "Increase income inequality deliberately",
            "Eliminate the need for any employment in the economy", "Apply only to the wealthiest citizens"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why unemployment and underemployment are both important to measure, not just unemployment alone?", "options": [
            "Underemployment captures cases where people are working but not fully utilising their productive capacity, which unemployment figures alone would miss",
            "Underemployment and unemployment are identical concepts with no meaningful difference", "Measuring underemployment is legally prohibited in most countries",
            "Only unemployment has any relevance to human resource planning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Rural-urban migration in Nepal is often driven partly by:", "options": [
            "The search for better employment opportunities and living standards in urban areas", "A government requirement with no economic motive",
            "A decline in urban job opportunities relative to rural areas", "Higher agricultural wages relative to urban wages"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes how income inequality can affect long-term economic growth, according to some economic arguments?", "options": [
            "High inequality may limit access to education/opportunity for the poor, potentially reducing overall human capital development", "Income inequality has no possible connection to economic growth",
            "Higher inequality always guarantees faster economic growth with no downside", "Inequality is entirely irrelevant to human capital formation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the link between human resource development and reducing unemployment?", "options": [
            "Better-skilled and educated workers are more likely to find and create productive employment opportunities", "Human resource development always increases unemployment",
            "Skills and education have no bearing on employability", "Unemployment is entirely unrelated to workforce skill levels"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises why poverty, inequality, unemployment, and human resources are typically studied together in development economics?", "options": [
            "They are closely interrelated - addressing one often requires understanding and addressing the others as part of a broader development strategy",
            "These four topics have no relationship to one another whatsoever", "Only unemployment matters for development, the others are irrelevant", "These issues are relevant only to already-developed countries"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Development Planning in Nepal": [
        {"q": "'Development planning' refers to a government's systematic approach to:", "options": [
            "Setting goals and strategies to guide a country's economic and social development over a defined period", "Randomly allocating resources with no defined goals",
            "Only managing a single private company's operations", "Only regulating international sports events"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Nepal's national development plans have traditionally been coordinated by the:", "options": [
            "National Planning Commission", "World Trade Organization", "International Monetary Fund",
            "United Nations Security Council"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's development plans have historically been structured mainly as:", "options": [
            "Periodic (multi-year, e.g. five-year) national development plans", "A single, one-time plan created only once in the country's history",
            "Plans that are never reviewed or revised", "Plans developed and controlled entirely by a foreign government"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key objective commonly emphasised across Nepal's development plans has been:", "options": [
            "Poverty reduction and balanced regional development", "Eliminating all private economic activity",
            "Discouraging any form of foreign investment", "Halting agricultural production entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Balanced regional development' as a planning goal aims to:", "options": [
            "Reduce disparities in development between different regions of the country", "Concentrate all development exclusively in the capital city",
            "Ignore rural areas completely", "Focus development efforts on only one province"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Since 2015, Nepal's federal structure has affected development planning by:", "options": [
            "Distributing planning and budgetary responsibilities across federal, provincial, and local governments", "Centralising all planning decisions exclusively at the federal level with no other tier involved",
            "Eliminating the need for any national development plan", "Removing all local government involvement in planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key challenge often cited in implementing Nepal's development plans is:", "options": [
            "Limited institutional capacity and resource constraints for effective implementation", "An excess of financial resources with no allocation challenge",
            "Complete absence of any development goals", "Universal agreement with zero coordination challenges"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's periodic development plans typically set targets related to:", "options": [
            "Economic growth rate, poverty reduction, and social indicators such as literacy and health", "Only foreign diplomatic protocol",
            "Only military expenditure", "Only stock market regulations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Long-term vision' documents, sometimes prepared alongside periodic plans, aim to:", "options": [
            "Set a broader, multi-decade direction for national development beyond a single plan period", "Replace the need for any periodic planning",
            "Focus exclusively on a single year's budget", "Apply only to a single private company"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Foreign aid and development assistance have historically played a role in Nepal's development plans by:", "options": [
            "Supplementing domestic resources for infrastructure and development projects", "Completely replacing the need for any domestic revenue",
            "Being entirely prohibited under Nepal's constitution", "Having no relationship to development financing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sector has commonly been prioritised in Nepal's development plans given the country's economic structure?", "options": [
            "Agriculture, given its role in employment and rural livelihoods", "Deep-sea fishing, despite Nepal being landlocked",
            "Offshore oil drilling", "Large-scale desert irrigation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Public-Private Partnership (PPP)' models, increasingly used in Nepal's development planning, involve:", "options": [
            "Collaboration between government and private sector entities to finance and implement development projects", "Complete exclusion of the private sector from any development project",
            "Only foreign governments partnering with Nepal, excluding domestic private firms", "A model with no relevance to infrastructure development"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Monitoring and evaluation of development plans is important mainly because it helps to:", "options": [
            "Assess whether planned targets are being achieved and inform necessary adjustments", "Guarantee that no plan will ever require any revision",
            "Eliminate the need for any future planning cycle", "Replace the plan itself with no further action needed"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why development planning in Nepal places emphasis on infrastructure such as roads and hydropower?", "options": [
            "These are seen as foundational for supporting broader economic activity, trade, and industrial growth", "Infrastructure has no relationship to overall economic development",
            "These sectors are the only ones ever mentioned in national plans", "Infrastructure investment always reduces a country's growth rate"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'inclusive development' as a planning principle?", "options": [
            "Ensuring the benefits of development reach all sections of society, including marginalised and disadvantaged groups", "Focusing development benefits exclusively on the wealthiest citizens",
            "Excluding rural populations from any development benefit", "A principle with no relevance to modern development planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a source of financing commonly used for Nepal's development plans?", "options": [
            "A combination of domestic tax revenue, foreign aid/grants, and borrowing", "Exclusively foreign military assistance",
            "Exclusively private individual donations with no government revenue involved", "No financing source of any kind is required"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the importance of aligning provincial and local development plans with the national plan under Nepal's federal structure?", "options": [
            "It helps ensure coherent, coordinated development efforts across all levels of government rather than conflicting or duplicated efforts",
            "Provincial and local plans have no relationship to the national plan", "Alignment across government levels is legally irrelevant",
            "Only the federal plan has ever mattered under any structure"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Nepal's graduation from Least Developed Country (LDC) status is a goal often linked to its development planning because it reflects:", "options": [
            "Progress in key development indicators such as income, human assets, and economic vulnerability", "A goal entirely unrelated to development planning",
            "A status that has no international significance", "A purely symbolic label with no basis in actual indicators"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why development plans are typically reviewed and revised periodically rather than fixed permanently?", "options": [
            "Changing economic conditions, new challenges, and lessons learned require plans to adapt over time", "Development plans are legally required to remain unchanged forever",
            "Periodic review has no practical value for policymaking", "Economic conditions never change once a plan is set"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of national development planning for a country like Nepal?", "options": [
            "To provide a structured, strategic framework guiding the efficient use of resources toward economic growth and social wellbeing", "To eliminate the need for any government budget",
            "To have no defined economic or social objective", "To focus exclusively on foreign policy with no domestic relevance"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Sustainable Development Goals and Nepal": [
        {"q": "The Sustainable Development Goals (SDGs) were adopted by:", "options": [
            "United Nations member states, including Nepal, as a global development framework", "A single private corporation with no government involvement",
            "Only the government of one specific country with no international agreement", "An organisation unrelated to global development"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The SDGs consist of a total of:", "options": [
            "17 goals covering economic, social and environmental dimensions of development", "Only 3 goals focused solely on economic growth",
            "A single unified goal with no sub-targets", "50 goals with no thematic structure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The SDGs succeeded an earlier global development framework known as the:", "options": [
            "Millennium Development Goals (MDGs)", "World Trade Agreement", "International Monetary Fund Charter",
            "Kyoto Protocol on trade"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "SDG 1 ('No Poverty') aims to:", "options": [
            "End poverty in all its forms everywhere", "Increase global poverty rates", "Focus exclusively on wealthy nations with no relevance to developing countries",
            "Eliminate the need for any social protection programs"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "SDG 4 ('Quality Education') aims to:", "options": [
            "Ensure inclusive and equitable quality education for all", "Restrict education access to a small elite group",
            "Eliminate all public education systems", "Apply only to primary education with no reference to higher levels"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "SDG 13 ('Climate Action') addresses:", "options": [
            "Urgent action to combat climate change and its impacts", "Only issues unrelated to the environment",
            "Exclusively the aviation industry with no broader relevance", "A goal irrelevant to developing countries like Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's approach to implementing the SDGs typically involves:", "options": [
            "Integrating SDG targets into national and local development plans and budgets", "Ignoring the SDGs entirely with no domestic policy connection",
            "Implementing SDGs only at the international level with no domestic action", "Rejecting the SDG framework altogether"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key challenge Nepal faces in achieving the SDGs includes:", "options": [
            "Limited financial resources and institutional capacity for full implementation", "An excess of financial resources with no implementation gap",
            "Complete absence of any development challenge", "Universal achievement of all targets well ahead of schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "SDG 5 ('Gender Equality') emphasises:", "options": [
            "Achieving gender equality and empowering all women and girls", "Restricting opportunities based on gender",
            "A goal relevant only to men", "Eliminating any reference to gender in development policy"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Nepal's post-earthquake (2015) and post-pandemic recovery efforts are often discussed in relation to the SDGs because they:", "options": [
            "Highlight the importance of resilience and sustainable rebuilding aligned with SDG targets", "Have no connection to sustainable development goals",
            "Occurred in a country not covered by the SDG framework", "Are entirely unrelated to poverty or health-related SDGs"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "SDG 8 ('Decent Work and Economic Growth') emphasises promoting:", "options": [
            "Sustained, inclusive economic growth and full, productive employment", "Only economic growth with no reference to employment conditions",
            "A reduction in overall economic activity", "Employment only for a small select group of citizens"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Localising the SDGs in Nepal's federal structure means:", "options": [
            "Adapting and implementing SDG targets at the provincial and local government levels", "Applying SDGs only at the national federal level with no local role",
            "Ignoring the federal structure entirely when addressing the SDGs", "A concept with no practical application in Nepal"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Monitoring progress on the SDGs typically requires:", "options": [
            "Reliable data collection and reporting on relevant indicators", "No data collection of any kind",
            "Only qualitative opinions with no quantitative measurement", "A single one-time assessment with no ongoing tracking"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "SDG 6 ('Clean Water and Sanitation') is particularly relevant to Nepal given:", "options": [
            "Ongoing challenges in ensuring universal access to clean water and sanitation, especially in rural areas", "Nepal already having achieved 100% access with no remaining challenge",
            "The complete absence of any water resources in Nepal", "A goal irrelevant to landlocked, mountainous countries"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's National Planning Commission's role regarding the SDGs typically includes:", "options": [
            "Coordinating SDG integration into national plans and tracking progress", "Having no role or responsibility related to the SDGs",
            "Being responsible only for foreign affairs with no domestic SDG role", "Opposing the implementation of the SDG framework"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why the SDGs are described as addressing 'sustainable' development, not just economic growth?", "options": [
            "They integrate economic, social and environmental dimensions to ensure development doesn't compromise future generations' needs", "They focus exclusively on economic growth with no environmental or social consideration",
            "Sustainability has no relationship to the SDG framework", "The SDGs apply only to environmental issues with no economic dimension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the relevance of SDG 9 ('Industry, Innovation and Infrastructure') to Nepal's development?", "options": [
            "It supports Nepal's need for improved infrastructure and industrial development to boost economic growth", "It has no relevance to Nepal's infrastructure challenges",
            "It applies only to already highly industrialised countries", "It focuses exclusively on space exploration technology"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Private sector and civil society involvement in achieving the SDGs in Nepal is generally considered:", "options": [
            "Important, since government resources alone are often insufficient to meet all targets", "Irrelevant, since only the government can contribute to SDG achievement",
            "Illegal under Nepal's SDG implementation framework", "Unnecessary given the SDGs are a purely government matter"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why international cooperation and support (e.g. foreign aid, technology transfer) remain relevant to Nepal's SDG achievement?", "options": [
            "Nepal's domestic resources and capacity may be insufficient alone to meet the full scope of the SDG targets by the target year",
            "International cooperation has no bearing on SDG achievement", "Nepal has already achieved all SDG targets without any external support", "The SDGs explicitly prohibit any international cooperation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall significance of the SDGs for a country like Nepal?", "options": [
            "They provide a comprehensive, internationally aligned framework to guide Nepal's economic, social and environmental development priorities", "They have no practical significance for Nepal's national policy",
            "They apply exclusively to already-developed nations", "They replace the need for any national development plan entirely"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Review of Basic Subject Matter of Statistics": [
        {"q": "'Statistics', as reviewed at this stage, refers to the science of:", "options": [
            "Collecting, organising, analysing and interpreting numerical data", "Only writing descriptive essays with no numerical content",
            "Only forecasting weather patterns", "A field unrelated to economic analysis"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Descriptive statistics' primarily involves:", "options": [
            "Summarising and presenting the main features of a data set", "Making predictions about an entirely different, unrelated population",
            "Only qualitative, non-numerical description", "A field unrelated to data of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'variable' in statistics refers to:", "options": [
            "A characteristic or quantity that can take different values across observations", "A quantity that is always exactly fixed and unchanging",
            "A term used only in algebra, never in statistics", "A value that is always equal to zero"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'population' in statistical terms refers to:", "options": [
            "The entire group of individuals or items being studied", "Only a small, randomly chosen subset of a larger group",
            "A term relevant only to demography, never to economics", "A single individual observation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'sample' in statistical terms refers to:", "options": [
            "A subset of the population selected for study", "The entire population without exception",
            "A term unrelated to data collection", "A value that is always identical to the population mean"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Quantitative data' refers to data that is:", "options": [
            "Numerical in nature and can be measured or counted", "Purely descriptive with no numerical value",
            "Always exactly the same for every observation", "Irrelevant to statistical analysis"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Qualitative data' refers to data that describes:", "options": [
            "Categories or characteristics that are not inherently numerical, such as colour or gender", "Only numerical measurements",
            "A concept unrelated to any classification of data", "Data that can only be collected from a census"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'frequency distribution' organises data by showing:", "options": [
            "How often each value or range of values occurs in a data set", "Only the single highest value in a data set",
            "Only the government's budget allocation", "A company's product catalogue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'arithmetic mean' of a data set, as reviewed from earlier study, is:", "options": [
            "The sum of all observations divided by the number of observations", "The middle value when data is arranged in order",
            "The most frequently occurring value", "The largest value in the data set"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'median', as reviewed, refers to:", "options": [
            "The middle value of an ordered data set", "The average of all values",
            "The most frequently occurring value", "The range between the highest and lowest values"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'bar diagram' is typically used to represent:", "options": [
            "Categorical data using rectangular bars of varying heights/lengths", "Only continuous data with no distinct categories",
            "A single numerical value with no comparison", "Only qualitative descriptions with no visual representation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'pie chart' is typically used to represent:", "options": [
            "The proportion of different categories as slices of a whole circle", "Only a single data point with no comparison",
            "Continuous time-series trends exclusively", "A concept unrelated to data visualisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'histogram' differs from a bar diagram mainly in that a histogram is used for:", "options": [
            "Continuous, grouped numerical data displayed in adjoining bars with no gaps", "Only categorical data with gaps between bars",
            "Only qualitative, non-numerical data", "A concept with no relevance to statistics"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Statistics is important to economic analysis mainly because it allows economists to:", "options": [
            "Quantify, analyse, and draw evidence-based conclusions about economic phenomena", "Avoid the need for any data collection whatsoever",
            "Rely purely on personal opinion with no supporting evidence", "Eliminate the need for any economic theory"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Inferential statistics' involves using sample data to:", "options": [
            "Make generalisations or predictions about a larger population", "Only describe the sample itself with no broader application",
            "Replace the need for any sample data collection", "Apply only to a single individual observation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why a well-designed frequency distribution is useful before further statistical analysis?", "options": [
            "It organises raw data into a clear, summarised form that reveals patterns not obvious in the raw data",
            "It has no analytical benefit whatsoever", "Raw data is always clearer than any organised summary", "Frequency distributions are only used for qualitative data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'class interval' in a grouped frequency distribution refers to:", "options": [
            "A range of values into which data is grouped", "A single exact data value with no range",
            "A term unrelated to grouped data", "The total sum of all data values"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of quantitative economic data?", "options": [
            "Nepal's GDP growth rate for a given year", "A general description of a country's culture",
            "An individual's personal opinion about a policy", "A qualitative description of a product's colour"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best explains why reviewing basic statistics is useful before studying more advanced economic topics like index numbers or dispersion?", "options": [
            "These advanced topics build directly on foundational statistical concepts such as data types, central tendency, and data presentation",
            "Basic statistics has no connection to advanced economic analysis", "Advanced topics require no statistical foundation whatsoever", "Index numbers and dispersion are unrelated to statistics"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall role of statistics within the study of economics?", "options": [
            "It provides the tools to collect, organise, and analyse the data needed to test economic theories and inform policy", "Statistics has no practical application within economics",
            "Economic theory never requires any supporting empirical data", "Statistics is relevant only to natural sciences, not economics"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Data Collection": [
        {"q": "'Primary data' refers to data that is:", "options": [
            "Collected firsthand by the researcher for a specific purpose", "Already published and collected by someone else previously",
            "Data that does not actually exist", "Collected only by international organisations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Secondary data' refers to data that:", "options": [
            "Was collected by someone else previously and is reused by the current researcher", "Is always collected firsthand by the current researcher",
            "Is always more accurate than primary data in every case", "Cannot be used in any economic study"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a common method of primary data collection?", "options": [
            "Conducting a survey or questionnaire", "Reading a previously published government report",
            "Reviewing an old newspaper article", "Consulting a textbook published years earlier"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'questionnaire' used in data collection is best described as:", "options": [
            "A structured set of questions designed to gather information from respondents", "A summary of already-published secondary data",
            "A type of financial statement", "A government tax form only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'interview' as a data collection method involves:", "options": [
            "Direct, often verbal, interaction between the researcher and respondent to gather information", "Only collecting data from previously published sources",
            "A method that cannot capture any qualitative information", "A method used exclusively for numerical data with no verbal component"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Observation' as a data collection method involves:", "options": [
            "Directly watching and recording behaviour or events as they occur", "Only reading data from a previously published book",
            "A method that requires no direct contact with the subject of study", "A method unrelated to primary data collection"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key advantage of secondary data is that it is often:", "options": [
            "Quicker and cheaper to obtain compared to collecting new primary data", "Always more relevant and up-to-date than primary data",
            "Impossible to access under any circumstance", "Available only for a single specific research purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A limitation of secondary data is that it may:", "options": [
            "Not perfectly match the specific needs or timeframe of the current research", "Always be perfectly suited to every research question",
            "Never require any evaluation of its reliability", "Guarantee complete accuracy in every case"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'census' refers to data collection that covers:", "options": [
            "The entire population being studied, not just a sample", "Only a small, randomly selected subset of the population",
            "A single individual only", "A method used exclusively for qualitative data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'sample survey', in contrast to a census, collects data from:", "options": [
            "A representative subset of the population", "The entire population without exception",
            "No individuals at all", "Only government employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Random sampling' aims to ensure that:", "options": [
            "Every member of the population has an equal chance of being selected", "Only the researcher's friends are selected",
            "Only the wealthiest individuals are included", "The sample is chosen based entirely on convenience with no randomisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's national population census is an example of:", "options": [
            "A large-scale primary data collection exercise covering the entire population", "A form of secondary data with no original collection involved",
            "A method used only by private companies", "A concept unrelated to statistics"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Government agencies such as the National Statistics Office in Nepal are important sources of:", "options": [
            "Secondary data for researchers, such as national economic indicators", "Only primary data collected exclusively by private individuals",
            "Data with no relevance to economic research", "Data that cannot legally be used by any researcher"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a source of secondary economic data for Nepal?", "options": [
            "Nepal Rastra Bank's published economic reports", "A survey the researcher personally conducts for the first time",
            "A direct interview conducted by the researcher", "Personal observation of a single individual's daily habits"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an important consideration when designing a questionnaire for primary data collection?", "options": [
            "Ensuring questions are clear, unbiased, and relevant to the research objective", "Making questions as confusing and ambiguous as possible",
            "Including questions entirely unrelated to the research topic", "Avoiding any consideration of respondent understanding"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Sampling error' refers to:", "options": [
            "The difference between a sample statistic and the true population parameter, due to using a sample rather than the full population", "An error that can never occur when using a sample",
            "An error that occurs only when using a full census", "A term unrelated to data collection methods"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why researchers often prefer sampling over a full census for many studies?", "options": [
            "Sampling is generally faster, cheaper, and more practical while still providing reasonably reliable estimates", "A census is always faster and cheaper than sampling in every case",
            "Sampling is always illegal for economic research", "A census provides no more accuracy than a very small sample"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Online surveys, as a modern method of primary data collection, offer the advantage of:", "options": [
            "Reaching a wide geographic audience relatively quickly and at lower cost", "Being completely unable to reach any respondent",
            "Requiring extensive physical travel for every response", "Being usable only for qualitative case studies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes why evaluating the reliability of a secondary data source (e.g. checking its original methodology) is important before using it?", "options": [
            "Poor-quality or biased original data collection can lead to inaccurate conclusions if reused without scrutiny", "Secondary data sources never require any evaluation of reliability",
            "All secondary data is automatically 100% reliable regardless of its source", "Reliability only matters for primary data, never secondary data"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall importance of proper data collection methods in economic research?", "options": [
            "Accurate, well-collected data forms the foundation for valid economic analysis and sound policy decisions", "Data collection methods have no bearing on the quality of economic analysis",
            "Any data, regardless of how it is collected, is equally useful for policy analysis", "Data collection is relevant only to non-economic fields of study"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Measures of Dispersion": [
        {"q": "'Measures of dispersion' describe:", "options": [
            "The extent to which data values are spread out around the central value", "The single most typical value in a data set",
            "The total number of observations only", "The relationship between two entirely unrelated variables"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Range' is calculated as:", "options": [
            "The highest value minus the lowest value in a data set", "The average of all values",
            "The middle value of the data set", "The most frequently occurring value"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Standard deviation' is calculated as:", "options": [
            "The square root of the variance", "The square of the variance", "The variance divided by the mean",
            "The sum of all values divided by their count"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Variance' is defined as:", "options": [
            "The average of the squared deviations of each value from the mean", "The simple average of all values",
            "The difference between the highest and lowest values", "The most frequently occurring value"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A LARGER standard deviation indicates that data values are:", "options": [
            "More spread out (more variable) around the mean", "More tightly clustered around the mean",
            "All exactly identical to each other", "Impossible to interpret meaningfully"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Coefficient of Variation (CV)' is particularly useful for:", "options": [
            "Comparing the relative variability of two data sets with different units or means", "Comparing values only within a single, identical data set",
            "Replacing the need for calculating the mean entirely", "A purpose unrelated to comparing variability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The Coefficient of Variation is calculated as:", "options": [
            "(Standard Deviation / Mean) × 100", "Standard Deviation × Mean", "Mean / Standard Deviation only, with no percentage",
            "Variance × 100"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Quartile Deviation' (Semi-Interquartile Range) is calculated as:", "options": [
            "(Q3 - Q1) / 2", "Q3 - Q1", "(Q3 + Q1) / 2", "Q3 × Q1"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Mean Deviation' is calculated as:", "options": [
            "The average of the absolute differences between each value and the mean", "The average of the squared differences from the mean",
            "The difference between the highest and lowest values", "The most frequently occurring deviation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Comparing the standard deviation of incomes in two different regions of Nepal would help economists assess:", "options": [
            "Which region has more variability (inequality) in income distribution", "The exact total government budget for each region",
            "The population size of each region only", "The exchange rate applicable to each region"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A standard deviation of ZERO would indicate that:", "options": [
            "All values in the data set are identical", "The data set has extremely high variability",
            "The mean cannot be calculated", "The data set is undefined"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following measures of dispersion uses every value in the data set in its calculation?", "options": [
            "Standard deviation", "Range", "Neither range nor standard deviation uses every value", "Only the mode does"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key limitation of the range as a measure of dispersion is that it:", "options": [
            "Only considers the two extreme values, ignoring the distribution of all other data points", "Uses every single data value in its calculation",
            "Is always identical to the standard deviation", "Cannot be calculated for any numerical data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Comparing the price volatility of two agricultural commodities using standard deviation of their prices over time helps assess:", "options": [
            "Which commodity's price has been more stable or more volatile", "The exact production cost of each commodity",
            "The commodities' total export value only", "The government's tax rate on each commodity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why measures of dispersion are used alongside measures of central tendency in economic analysis?", "options": [
            "Central tendency shows a typical value, while dispersion reveals how much individual values vary - together giving a fuller picture",
            "Dispersion measures always replace the need to calculate a mean or median", "Central tendency alone is always fully sufficient for any economic analysis", "The two types of measures are mathematically identical"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Two regions with the SAME average income but DIFFERENT standard deviations illustrate that:", "options": [
            "Average income alone does not fully describe how income is distributed within each region", "Standard deviation is always identical whenever average income is identical",
            "Average income alone always fully describes income distribution", "Measures of dispersion provide no additional insight beyond the average"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In quality control or price stability analysis, a smaller standard deviation is generally interpreted as indicating:", "options": [
            "Greater consistency/stability", "Greater instability and unpredictability",
            "No meaningful interpretation is possible", "An error in calculation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Given the data set {5, 5, 5, 5}, the standard deviation is:", "options": [
            "0", "5", "1", "Undefined"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the value of using the Coefficient of Variation rather than standard deviation alone, when comparing income variability between two countries with very different average income levels?", "options": [
            "It expresses variability relative to the mean, allowing fairer comparison across data sets with different scales", "It ignores the mean entirely, making comparisons meaningless",
            "It can only be used when both data sets have an identical mean", "It is always numerically identical to the standard deviation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises why measures of dispersion are relevant to economic policymaking?", "options": [
            "They help quantify inequality, price volatility, and variability, informing more targeted economic policy", "Measures of dispersion have no relevance to economic policy",
            "Only the mean is ever relevant to economic policymaking", "Dispersion measures apply only to non-economic data"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Index Number": [
        {"q": "An 'index number' is a statistical measure used to show:", "options": [
            "The relative change in a variable (e.g. price or quantity) over time compared to a base period", "The absolute population count of a country",
            "A fixed number that never changes over time", "A measure unrelated to any change over time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'base year' in constructing an index number serves as:", "options": [
            "The reference period against which later values are compared, usually set at 100", "The most recent year of data collection, by definition",
            "A year with the highest recorded values only", "An arbitrary year excluded from the index entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Consumer Price Index (CPI) is used primarily to measure changes in:", "options": [
            "The general price level of a fixed basket of consumer goods and services over time", "A country's total population",
            "A single company's stock price", "The exchange rate between two currencies"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The CPI is commonly used by economists and policymakers to measure:", "options": [
            "The rate of inflation experienced by typical consumers", "A country's total land area",
            "The number of registered companies in a country", "The exact wage of every individual worker"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Wholesale Price Index (WPI)' measures price changes at the:", "options": [
            "Wholesale/producer level, before goods reach final retail consumers", "Final retail level only, exclusively",
            "Household savings level only", "Government tax collection level only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the CPI in a given year is 120 (base year = 100), this indicates that prices have, on average:", "options": [
            "Increased by 20% compared to the base year", "Decreased by 20% compared to the base year",
            "Remained exactly unchanged from the base year", "Increased by 120% compared to the base year"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'quantity index' measures the relative change in:", "options": [
            "The physical quantity of goods produced or consumed over time", "Only the price of goods, with no reference to quantity",
            "A country's total government revenue", "The exchange rate between two currencies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Laspeyres price index formula uses quantity weights from the:", "options": [
            "Base year", "Current year only", "An average of all years combined", "A randomly selected year with no defined method"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The Paasche price index formula uses quantity weights from the:", "options": [
            "Current year", "Base year only", "A randomly chosen historical year", "No quantity weights are used at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Constructing a price index requires selecting a representative 'basket of goods', which refers to:", "options": [
            "A fixed set of goods and services chosen to reflect typical consumption patterns", "A single randomly chosen product with no broader relevance",
            "Every single good produced in the economy with no selection process", "A concept unrelated to index number construction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Index numbers are useful to economists mainly because they allow:", "options": [
            "Comparison of economic variables across different time periods in a standardised way", "Comparison only within a single, fixed point in time",
            "Replacement of the need for any actual price or quantity data", "A purpose unrelated to economic measurement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Inflation rate', as commonly reported by Nepal Rastra Bank and other agencies, is typically derived from changes in the:", "options": [
            "Consumer Price Index (CPI) over a given period", "Total population count", "A single company's annual sales",
            "The government's total number of employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key limitation of a fixed-basket price index (like a simple Laspeyres index) is that it may not fully capture:", "options": [
            "Changes in consumer buying patterns in response to relative price changes over time", "Any change in price whatsoever",
            "The base year price level", "A concept irrelevant to constructing any index"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Index numbers can also be used to measure changes in variables other than price, such as:", "options": [
            "Industrial production, stock market performance, or human development", "Only price, with no other possible application",
            "Only population size, with no other application", "A concept limited exclusively to agricultural output"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Updating the 'base year' of a price index periodically is important mainly because it helps to:", "options": [
            "Keep the basket of goods and weights relevant to current consumption patterns", "Guarantee the index never needs any future revision",
            "Eliminate the need for any base year at all", "Make the index intentionally less accurate over time"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If a country's real wages are calculated by adjusting nominal wages using a price index, this is done primarily to:", "options": [
            "Account for the effect of inflation on workers' actual purchasing power", "Ignore the effect of inflation entirely",
            "Increase nominal wages automatically with no calculation", "Replace the need for measuring nominal wages"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes why the government and central bank pay close attention to the CPI index in setting policy?", "options": [
            "It serves as a key indicator of inflation, informing monetary and fiscal policy decisions", "The CPI has no relevance to government or central bank policy",
            "Policy decisions are made without any reference to price levels", "The CPI only measures unrelated demographic data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains a practical challenge in constructing an accurate CPI for a country like Nepal?", "options": [
            "Diverse consumption patterns across regions and income groups make selecting a single representative basket challenging", "Nepal has no diversity in consumption patterns across its population",
            "Constructing a CPI requires no data collection whatsoever", "Every household in Nepal consumes an identical basket of goods"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes an index number from a simple raw data value (like a single price)?", "options": [
            "An index number expresses relative change compared to a reference base period, not just an absolute value",
            "An index number and a raw data value are always identical", "Index numbers never involve any base period comparison", "Raw data values always incorporate a base year automatically"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of index numbers in economic analysis?", "options": [
            "To provide a standardised way to track and compare changes in economic variables such as prices or quantities over time", "To eliminate the need for tracking any economic variable over time",
            "To replace all other forms of economic data collection", "To measure only non-economic phenomena with no relevance to prices or output"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
