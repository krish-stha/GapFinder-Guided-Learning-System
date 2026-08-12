# -*- coding: utf-8 -*-
"""
NEB Grade 11 Management - Principle of Accounting-I question bank.

Authored content (not content partner data - loaded with source='synthetic'
by scripts/load_question_bank.py). Topically accurate, written to read
like genuine exam questions per explicit user instruction. Chapter names
match, exactly, the Section rows already sitting under course 209 ("NEB
Grade 11 Management") Principle of Accounting-I subject (subject_id=34290)
- see scripts/reports/phase1_verify.json for the source list. Never
presented as content partner content or as evidence about real students.

NOTE: "Book of Original Entry- Journal, Ledgers Account and Trial
Balance" is a genuine duplicate chapter NAME in the source data - two
distinct Chapter rows (ids 34353, 34626) both carry this exact name.
This module supplies 40 questions for that key; load_question_bank.py
splits them into two 20-question batches (first half -> lower chapter
id, second half -> higher chapter id, ordered by id). The two halves are
deliberately written on different sub-topics (Journal/Ledger basics vs.
Trial Balance/error correction) so the split reads as two coherent,
non-repetitive chapters rather than an arbitrary cut.

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}.
"""

QUESTIONS = {
    "Book of Original Entry- Journal, Ledgers Account and Trial Balance": [
        # --- Batch 1 (20) - Journal and Ledger fundamentals ---
        {"q": "The 'Journal' in accounting is best described as:", "options": [
            "The book of original/prime entry where transactions are first recorded in chronological order",
            "A summary of only cash transactions", "The final financial statement of a business",
            "A register of employee attendance"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Under the double-entry system of bookkeeping, every transaction affects:", "options": [
            "At least two accounts, with equal debit and credit amounts", "Only one account",
            "Only the cash account", "Only the owner's personal account"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In a journal entry, the account that receives value is:", "options": [
            "Debited", "Credited", "Neither debited nor credited", "Recorded only in the ledger, not the journal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a journal entry, the account that gives value is:", "options": [
            "Credited", "Debited", "Ignored entirely", "Recorded twice"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A brief explanation written below a journal entry describing the transaction is called:", "options": [
            "Narration", "Posting", "Balancing", "Casting"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The accounting equation is expressed as:", "options": [
            "Assets = Liabilities + Capital (Owner's Equity)", "Assets = Liabilities - Capital",
            "Assets + Liabilities = Capital", "Capital = Assets x Liabilities"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'Ledger' in accounting is best described as:", "options": [
            "The principal book that contains all accounts in classified/summarised form, posted from the journal",
            "A book used only for recording cash sales", "A tax return document",
            "A list of a company's employees"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The process of transferring entries from the journal to the appropriate ledger accounts is called:", "options": [
            "Posting", "Casting", "Balancing", "Narration"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A ledger account in 'T-format' has which two sides?", "options": [
            "Debit (left) side and Credit (right) side", "Income side and Expense side only",
            "Asset side and Liability side only", "Opening side and Closing side only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "According to the rule for Real Accounts (assets), when an asset comes into the business, it is:", "options": [
            "Debited ('Debit what comes in')", "Credited", "Neither debited nor credited",
            "Recorded as an expense only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to the rule for Personal Accounts, the account of the person who receives something (the 'receiver') is:", "options": [
            "Debited ('Debit the receiver')", "Credited", "Ignored", "Always shown as a liability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to the rule for Nominal Accounts, all expenses and losses are:", "options": [
            "Debited", "Credited", "Neither debited nor credited", "Recorded only at year-end"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to the rule for Nominal Accounts, all incomes and gains are:", "options": [
            "Credited", "Debited", "Ignored in the journal", "Recorded as an asset"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When a business owner introduces additional capital in cash, the correct journal entry is:", "options": [
            "Debit Cash Account, Credit Capital Account", "Debit Capital Account, Credit Cash Account",
            "Debit Cash Account, Credit Purchases Account", "Debit Sales Account, Credit Capital Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When goods are purchased for cash, the correct journal entry is:", "options": [
            "Debit Purchases Account, Credit Cash Account", "Debit Cash Account, Credit Purchases Account",
            "Debit Sales Account, Credit Cash Account", "Debit Cash Account, Credit Capital Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When goods are sold for cash, the correct journal entry is:", "options": [
            "Debit Cash Account, Credit Sales Account", "Debit Sales Account, Credit Cash Account",
            "Debit Purchases Account, Credit Cash Account", "Debit Cash Account, Credit Purchases Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'compound journal entry' refers to an entry that:", "options": [
            "Involves more than two accounts in a single journal entry", "Can never be posted to the ledger",
            "Only records cash transactions", "Is used exclusively for closing the books"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The process of totalling the two sides of a ledger account is called:", "options": [
            "Casting", "Narration", "Journalising", "Vouching"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the debit side of a ledger account exceeds its credit side, the account is said to have a:", "options": [
            "Debit balance", "Credit balance", "Zero balance", "Negative balance always"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'balancing' a ledger account?", "options": [
            "Finding the difference between the total debit and total credit sides to determine the closing balance",
            "Recording a transaction for the very first time", "Preparing the final profit and loss account",
            "Writing a narration below a journal entry"],
         "correct": 0, "difficulty": "Medium"},
        # --- Batch 2 (20) - Trial Balance and error correction ---
        {"q": "A 'Trial Balance' is best described as:", "options": [
            "A statement listing all ledger account balances to check the arithmetical accuracy of the books",
            "A final statement showing the business's net profit", "A legal contract between buyer and seller",
            "A list of unpaid customer invoices only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A Trial Balance is normally prepared:", "options": [
            "At the end of an accounting period, after posting all ledger accounts", "Before any transaction is recorded",
            "Only once in the entire life of a business", "Only when the business is being sold"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "If a Trial Balance's debit and credit totals are equal, this confirms:", "options": [
            "The arithmetical accuracy of the ledger postings, but not necessarily the absence of all errors",
            "That absolutely no error of any kind exists in the books", "That the business has made a profit",
            "That all transactions were recorded in cash"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "An 'error of omission' occurs when:", "options": [
            "A transaction is completely omitted from being recorded in the books", "A transaction is recorded in the wrong account of the correct type",
            "Debit and credit entries are reversed", "Two errors cancel each other out by chance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'error of commission' occurs when:", "options": [
            "A transaction is recorded in the wrong account, but of the same class/type", "A transaction is completely left out of the books",
            "A wrong total is carried forward only", "A transaction is entered as a fictitious asset"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'error of principle' occurs when:", "options": [
            "A transaction is recorded in violation of accounting principles, such as treating a capital expenditure as revenue expenditure",
            "A transaction is recorded twice by mistake", "An amount is transposed, e.g. 45 written as 54",
            "A subsidiary book total is correct but posted incorrectly"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'compensating error' refers to a situation where:", "options": [
            "Two or more errors cancel out each other's effect on the Trial Balance totals", "An error is fully corrected before posting",
            "An error causes the Trial Balance to never agree", "Only credit entries are affected by an error"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following errors will typically cause the Trial Balance to NOT agree (disagree)?", "options": [
            "Posting an amount to only one side of an account (a one-sided error)", "Recording a transaction in the wrong account of the correct type",
            "Complete omission of a transaction from both journal and ledger", "A compensating error"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "When a Trial Balance does not agree, the difference is temporarily transferred to a:", "options": [
            "Suspense Account", "Capital Account", "Drawings Account", "Sales Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A Suspense Account is eventually closed once:", "options": [
            "All errors causing the Trial Balance disagreement have been located and corrected", "The business closes down permanently",
            "The owner withdraws all capital", "The next financial year begins, regardless of errors"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Transposition error' refers to:", "options": [
            "Writing the digits of a figure in the wrong order, e.g. Rs. churn 291 written as Rs. 219", "Omitting a transaction entirely",
            "Posting to the wrong side of the correct account", "Recording an asset as an expense"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a sale of goods on credit is completely omitted from the books, the effect on the Trial Balance is:", "options": [
            "No effect - the Trial Balance will still agree, since both sides are equally understated (in this case, unaffected)",
            "The Trial Balance will definitely disagree", "Only the debit side will be affected", "Only the credit side will be affected"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The Trial Balance serves as the basis for preparing:", "options": [
            "The final accounts (Trading Account, Profit and Loss Account, and Balance Sheet)", "Only the cash book",
            "Only the purchase order", "Only employee payslips"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following accounts would normally appear on the DEBIT side of a Trial Balance?", "options": [
            "Purchases Account", "Sales Account", "Capital Account", "Creditors Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following accounts would normally appear on the CREDIT side of a Trial Balance?", "options": [
            "Sales Account", "Purchases Account", "Cash Account", "Debtors Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If the Trial Balance shows unequal totals, the FIRST step an accountant typically takes is to:", "options": [
            "Recheck the totals (casting) of individual ledger accounts and the Trial Balance itself", "Immediately close the business",
            "Ignore the difference completely", "Prepare the final accounts regardless"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A Trial Balance that agrees (tallies) despite hidden errors demonstrates that agreement is:", "options": [
            "Necessary but not sufficient proof of complete accuracy", "Absolute and complete proof that no error exists",
            "Irrelevant to the accuracy of the books", "Only possible in computerised accounting"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Rectification of an error located AFTER the Trial Balance has been prepared, but before final accounts, is usually done through the:", "options": [
            "Suspense Account", "Capital Account directly, bypassing all other accounts", "Petty Cash Book",
            "Bank Reconciliation Statement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of a two-sided error that would NOT be revealed by the Trial Balance?", "options": [
            "Recording a purchase of furniture as 'Purchases' instead of 'Furniture' (an error of principle)", "Posting only the debit side of an entry",
            "Posting only the credit side of an entry", "Casting a ledger account total incorrectly"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the overall purpose of preparing a Trial Balance before final accounts?", "options": [
            "To verify that total debits equal total credits before proceeding to summarise the accounts into financial statements",
            "To directly calculate the exact amount of tax owed", "To replace the need for a Balance Sheet entirely",
            "To record transactions for the very first time"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Subsidiary Book": [
        {"q": "'Subsidiary Books' (books of original entry, other than the general journal) are used to:", "options": [
            "Record specific types of recurring transactions separately for convenience and control", "Replace the need for a ledger entirely",
            "Record only the owner's personal expenses", "Record only annual tax payments"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'Purchases Book' (Purchases Day Book) is used to record:", "options": [
            "Credit purchases of goods meant for resale", "Cash purchases of goods only", "Purchases of fixed assets on credit",
            "Sales of goods on credit"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Sales Book' (Sales Day Book) is used to record:", "options": [
            "Credit sales of goods in the normal course of business", "Cash sales of goods only", "Purchases of goods on credit",
            "Sale of a fixed asset such as old furniture"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Purchases Return Book' (Returns Outward Book) records:", "options": [
            "Goods purchased on credit that are returned to suppliers", "Goods sold on credit that are returned by customers",
            "Cash refunds paid to customers", "New purchases of fixed assets"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Sales Return Book' (Returns Inward Book) records:", "options": [
            "Goods sold on credit that are returned by customers", "Goods purchased on credit that are returned to suppliers",
            "Cash sales made during the day", "Purchases of office stationery"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The source document typically used to record entries in the Purchases Book is the:", "options": [
            "Purchase invoice (bill) received from the supplier", "Sales invoice issued to a customer",
            "Bank statement", "Petty cash voucher"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The source document typically used to record entries in the Sales Book is the:", "options": [
            "Sales invoice issued to the customer", "Purchase invoice received from a supplier",
            "Debit note issued to a supplier", "Bank pay-in slip"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Credit Note' is issued by a seller to a customer primarily when:", "options": [
            "Goods are returned by the customer, reducing the amount the customer owes", "Goods are purchased on credit",
            "A cash sale is made", "An employee's salary is paid"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Debit Note' is issued by a buyer to a supplier primarily when:", "options": [
            "Goods purchased are returned to the supplier, reducing the amount owed to them", "Goods are sold on credit",
            "A cash purchase is made", "An asset is revalued upward"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Using subsidiary books instead of recording every transaction directly in the general journal mainly helps by:", "options": [
            "Reducing the size of the journal and enabling division of clerical work and better control", "Making the accounting records less accurate",
            "Eliminating the need for a ledger", "Making it impossible to trace any transaction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Journal Proper' (or General Journal) is used to record transactions that:", "options": [
            "Do not fit into any of the specific subsidiary books, such as opening entries and adjustments", "Only involve cash receipts",
            "Only involve cash payments", "Only involve credit sales of trading goods"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Periodic totals of the Purchases Book are posted to the:", "options": [
            "Debit side of the Purchases Account in the ledger", "Credit side of the Purchases Account",
            "Debit side of the Sales Account", "Credit side of the Cash Account only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Periodic totals of the Sales Book are posted to the:", "options": [
            "Credit side of the Sales Account in the ledger", "Debit side of the Sales Account",
            "Credit side of the Purchases Account", "Debit side of the Cash Account only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Individual entries within the Purchases Book (each supplier's amount) are posted to:", "options": [
            "The credit side of each individual supplier's (creditor's) personal account", "The debit side of the Sales Account",
            "The Cash Account only", "The Capital Account only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Individual entries within the Sales Book (each customer's amount) are posted to:", "options": [
            "The debit side of each individual customer's (debtor's) personal account", "The credit side of the Purchases Account",
            "The Cash Account only", "The Drawings Account"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following transactions would NOT normally be recorded in the Purchases Book?", "options": [
            "A cash purchase of goods for resale", "A credit purchase of goods for resale from Supplier A",
            "A credit purchase of goods for resale from Supplier B", "A credit purchase of trading stock"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Trade discount, when shown on a purchase invoice, is generally:", "options": [
            "Deducted before recording the net amount in the Purchases Book", "Added to the invoice amount before recording",
            "Recorded as a separate expense account", "Ignored and recorded as income"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes a Purchases Book entry from a Cash Book entry?", "options": [
            "The Purchases Book records credit purchases only, while cash purchases go through the Cash Book",
            "The Purchases Book records only cash transactions", "Both books record identical types of transactions",
            "The Cash Book records only credit transactions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The use of multiple subsidiary books is most beneficial for a business that has:", "options": [
            "A large volume of repetitive transactions of a similar type", "Only one single transaction per year",
            "No credit transactions of any kind", "Only cash transactions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why the Purchases Return Book is kept separate from the Purchases Book?", "options": [
            "It allows purchases and purchase returns to be tracked and analysed separately for better control", "Because returns can never be recorded in accounting",
            "Because there is no difference between a purchase and a purchase return", "Because it eliminates the need for supplier accounts"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Cash Book": [
        {"q": "A 'Cash Book' serves the dual function of being:", "options": [
            "Both a book of original entry and a ledger account for cash (and bank) transactions", "Only a book of original entry, never a ledger",
            "Only a summary of credit transactions", "Only used for recording fixed asset purchases"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'Single Column Cash Book' records only:", "options": [
            "Cash receipts and cash payments", "Bank transactions only", "Discount allowed and received only",
            "Credit purchases and credit sales"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'Double Column Cash Book' typically has columns for:", "options": [
            "Cash and Bank", "Cash and Discount only, with no bank column", "Purchases and Sales",
            "Assets and Liabilities"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Triple Column Cash Book' typically includes columns for:", "options": [
            "Cash, Bank, and Discount", "Cash, Sales, and Purchases", "Assets, Liabilities, and Capital",
            "Debtors, Creditors, and Capital"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the Cash Book, cash/cheques received are recorded on the:", "options": [
            "Debit (receipts) side", "Credit (payments) side", "Neither side", "A separate ledger only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In the Cash Book, cash/cheque payments made are recorded on the:", "options": [
            "Credit (payments) side", "Debit (receipts) side", "Neither side", "Only in the Purchases Book"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Contra entry' in a Double/Triple Column Cash Book refers to a transaction where:", "options": [
            "Both the cash and bank columns are affected by the same transaction, e.g. cash deposited into the bank",
            "Only the cash column is affected", "Only the bank column is affected", "Neither cash nor bank is affected"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A contra entry is typically denoted in the Cash Book by writing which letter in the ledger folio column?", "options": [
            "'C'", "'B'", "'D'", "'X'"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Discount allowed' to a customer is recorded on which side of a Triple Column Cash Book?", "options": [
            "Debit side (alongside the cash/bank receipt)", "Credit side", "It is never recorded in the Cash Book",
            "Only in the Purchases Book"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Discount received' from a supplier is recorded on which side of a Triple Column Cash Book?", "options": [
            "Credit side (alongside the cash/bank payment)", "Debit side", "It is never recorded in the Cash Book",
            "Only in the Sales Book"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Petty Cash Book' is maintained primarily to record:", "options": [
            "Small, day-to-day cash expenses such as postage and office supplies", "Large capital expenditures only",
            "All credit sales of the business", "All bank loan transactions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Imprest System' of petty cash management involves:", "options": [
            "Reimbursing the petty cashier periodically for exact amount spent, to restore a fixed float", "Giving the petty cashier unlimited cash with no tracking",
            "Never reimbursing the petty cashier at all", "Recording petty cash only once a year"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The Cash Book, unlike other subsidiary books, does not require a separate:", "options": [
            "Cash Account in the ledger, since the Cash Book itself serves that role", "Journal entry for large purchases",
            "Debtors account for customers", "Creditors account for suppliers"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "If a cheque received from a customer is later dishonoured (bounced), the correct treatment in the Cash Book is to:", "options": [
            "Record it on the credit (payments) side, reversing the earlier receipt", "Ignore it completely",
            "Record it as a fresh cash sale", "Record it as discount allowed"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A cash sale of goods is recorded in the:", "options": [
            "Cash Book (debit/receipts side) and NOT in the Sales Book", "Sales Book only", "Purchases Book only",
            "Journal Proper only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is typically NOT recorded in the Cash Book?", "options": [
            "A credit sale of goods where no cash or cheque is yet received", "A cash payment for rent",
            "A cheque received from a debtor", "Cash withdrawn from the bank for office use"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cash Book balance' at the end of a period represents:", "options": [
            "The amount of cash (and/or bank balance) available with the business at that date", "The total profit earned during the period",
            "The total credit purchases made during the period", "The value of fixed assets owned"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best explains why many businesses prefer a Triple Column Cash Book over a Single Column one?", "options": [
            "It captures cash, bank, and discount information together, reducing the need for separate records", "It is legally mandatory in all cases",
            "It eliminates the need for any ledger posting whatsoever", "It only works for businesses with no bank account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When cash is withdrawn from the bank for office use, the correct treatment in a Double/Triple Column Cash Book is:", "options": [
            "Debit the Cash column and Credit the Bank column (a contra entry)", "Debit the Bank column and Credit the Cash column",
            "Debit the Sales column only", "No entry is required in the Cash Book"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The closing balance of the Cash Book is carried forward to the:", "options": [
            "Trial Balance and subsequently the Balance Sheet as the cash/bank balance", "Sales Account only",
            "Purchases Account only", "Capital Account permanently with no further use"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Modern Banking System and Bank Reconciliation System": [
        {"q": "A 'Bank Reconciliation Statement' is prepared to:", "options": [
            "Explain and reconcile the difference between the cash book bank balance and the bank statement (passbook) balance",
            "Calculate the business's total annual profit", "Record all cash sales of the business",
            "Replace the need for a cash book entirely"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A difference between the Cash Book and Bank Statement balances commonly arises due to:", "options": [
            "Cheques issued but not yet presented for payment, or cheques deposited but not yet cleared", "The business having two separate bank accounts",
            "An error that can never be identified", "A change in the business's ownership"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cheques issued but not yet presented' for payment cause the:", "options": [
            "Bank statement balance to be higher than the cash book balance (before reconciliation)", "Cash book balance to be higher than the bank statement balance",
            "Both balances to always be identical", "Bank statement balance to become negative permanently"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Cheques deposited but not yet collected/cleared' cause the:", "options": [
            "Cash book balance to be higher than the bank statement balance (before reconciliation)", "Bank statement balance to be higher than the cash book balance",
            "Both balances to always match exactly", "Bank to refuse the deposit entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Bank charges deducted directly by the bank, but not yet recorded in the business's cash book, will cause:", "options": [
            "The cash book balance to be overstated relative to the bank statement, until adjusted", "No difference between the two balances",
            "The bank statement to be automatically corrected by the business", "The business to receive a refund automatically"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Interest credited by the bank directly to the business's account, but not yet recorded in the cash book, will cause:", "options": [
            "The cash book balance to be understated relative to the bank statement, until adjusted", "No effect on either balance",
            "The bank statement balance to decrease", "An automatic correction with no further action needed"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'Passbook' (or bank statement) is a record maintained by the:", "options": [
            "Bank, showing all transactions in the customer's account from the bank's point of view", "Business itself, showing only cash transactions",
            "Government tax office", "Business's suppliers only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The starting point of a Bank Reconciliation Statement is typically:", "options": [
            "The balance as per the Cash Book (or the Bank Statement) on a given date", "The business's total annual sales",
            "The value of fixed assets", "The owner's personal net worth"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "If a cheque deposited by the business is later dishonoured by the bank, the correct treatment when reconciling is to:", "options": [
            "Deduct the amount from the cash book balance, since the expected deposit did not materialise", "Add the amount to the cash book balance",
            "Ignore the dishonoured cheque entirely", "Record it as a new sale"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Direct deposits made by customers straight into the business's bank account, not yet recorded in the cash book, require:", "options": [
            "Adding the amount to the cash book balance during reconciliation", "Deducting the amount from the cash book balance",
            "No adjustment of any kind", "Recording it as a bank charge"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is a common reason banks provide account holders with a periodic bank statement?", "options": [
            "To allow account holders to verify their recorded transactions and account balance", "To replace the need for any cash book",
            "To calculate the account holder's personal income tax", "To set the account holder's loan interest rate"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'overdraft' in modern banking refers to a situation where:", "options": [
            "A bank allows an account holder to withdraw more money than their account balance, up to an agreed limit", "The account holder can never withdraw any money",
            "The bank refuses to provide any credit facility", "The account is permanently closed"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Standing instructions/orders given to a bank allow the bank to:", "options": [
            "Automatically make regular payments (e.g. utility bills) on the account holder's behalf", "Close the account automatically after one year",
            "Refuse all future deposits", "Cancel all previous transactions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'electronic/digital banking' in the modern banking system?", "options": [
            "Conducting banking transactions via computers, mobile apps, or ATMs rather than only in person", "Banking that can only be done by visiting a branch physically",
            "A system with no security measures at all", "A system used exclusively by businesses, never individuals"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A bank reconciliation statement is typically prepared:", "options": [
            "Periodically (e.g. monthly), to promptly identify and correct discrepancies", "Only once when a business is first established",
            "Only when the business is closing down", "Every single day without exception"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following would NOT typically cause a difference between the cash book and bank statement balances?", "options": [
            "A cash sale that has been correctly recorded and banked on the same day with no delay", "An unpresented cheque",
            "A bank charge not yet recorded by the business", "Interest credited by the bank but not yet recorded"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Reconciling the cash book with the bank statement is an important internal control because it helps:", "options": [
            "Detect errors or fraud in either the business's own records or the bank's records promptly", "Guarantee that the business will always earn a profit",
            "Eliminate the need to record any bank transaction", "Automatically increase the account balance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A cheque that has become stale/expired (not presented within the valid period) should be treated, upon reconciliation, by:", "options": [
            "Adding it back to the cash book balance, since it will not be paid by the bank", "Deducting it again from the cash book balance",
            "Ignoring it, since it has no effect on the balance", "Treating it as a new bank charge"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes the relationship between the Cash Book (bank column) and the bank's Passbook, from the business's point of view?", "options": [
            "They should show mirror-image (opposite) balances that, once timing differences and errors are adjusted, reconcile to the same true balance",
            "They must always show numerically identical balances at every moment with no exceptions", "They record entirely unrelated sets of transactions",
            "The Passbook is prepared by the business, not the bank"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of a service typically offered under a 'modern banking system'?", "options": [
            "Online fund transfer and mobile banking", "Manual-only ledger keeping with no computer systems",
            "A complete ban on any electronic transaction", "Cash-only transactions with no account records kept"],
         "correct": 0, "difficulty": "Easy"},
    ],
    "Accounting for Fixed Assets": [
        {"q": "A 'Fixed Asset' is best described as:", "options": [
            "A long-term tangible or intangible asset used in business operations, not meant for resale", "An asset meant to be sold within a few days",
            "Cash held in the business's till", "A short-term amount owed by a customer"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Depreciation' in accounting refers to:", "options": [
            "The systematic allocation of a fixed asset's cost over its useful life", "An increase in the market value of an asset over time",
            "A one-time cash payment to a supplier", "The total sales revenue of a business"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Under the 'Straight Line Method' of depreciation, the depreciation amount charged each year is:", "options": [
            "The same fixed amount every year over the asset's useful life", "A different, decreasing amount each year",
            "Calculated only in the final year of the asset's life", "Based on the asset's resale price each year"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Under the 'Diminishing (Reducing) Balance Method' of depreciation, depreciation is calculated on:", "options": [
            "The asset's book value (original cost less accumulated depreciation) at the start of each year", "The asset's original cost only, every year",
            "The asset's resale/market value only", "A random amount decided annually"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The formula for annual depreciation under the Straight Line Method is generally:", "options": [
            "(Cost of asset - Estimated residual/scrap value) / Estimated useful life", "Cost of asset x Current market interest rate",
            "Cost of asset / Number of employees", "Estimated residual value / Cost of asset"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Residual value' (or scrap value) of a fixed asset refers to:", "options": [
            "The estimated value of the asset at the end of its useful life", "The original purchase price of the asset",
            "The market value of the asset one year after purchase only", "The insurance premium paid on the asset"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Depreciation is charged on fixed assets mainly because:", "options": [
            "Assets lose value over time due to wear and tear, obsolescence, or usage, and this cost must be matched against revenue",
            "Assets always increase in value and this must be recorded", "It is a purely optional bookkeeping exercise with no accounting basis",
            "It is only relevant for assets that are never used"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the ledger, the journal entry to record annual depreciation is typically:", "options": [
            "Debit Depreciation Account, Credit Asset Account (or Accumulated Depreciation Account)", "Debit Asset Account, Credit Depreciation Account",
            "Debit Cash Account, Credit Asset Account", "Debit Capital Account, Credit Depreciation Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Depreciation Account is ultimately closed by transferring its balance to the:", "options": [
            "Profit and Loss Account, as an expense", "Balance Sheet, as an asset directly, without going through Profit and Loss",
            "Capital Account directly", "Sales Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Accumulated Depreciation' refers to:", "options": [
            "The total depreciation charged on an asset from the date of purchase up to the current date", "The depreciation charged in only the current year",
            "The original cost of the asset", "The resale value expected in the future"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Net Book Value' (Written Down Value) of a fixed asset is calculated as:", "options": [
            "Original cost minus accumulated depreciation to date", "Original cost plus accumulated depreciation",
            "Market value minus original cost", "Residual value minus original cost"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a fixed (tangible) asset?", "options": [
            "Machinery used in production", "Cash in hand", "Trade debtors (accounts receivable)",
            "Closing stock of goods for sale"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is an example of an intangible fixed asset?", "options": [
            "Goodwill or a patent", "A delivery van", "Factory building", "Office furniture"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Capital expenditure' on a fixed asset refers to spending that:", "options": [
            "Increases the value or extends the useful life of the asset", "Is incurred purely for day-to-day running costs with no lasting benefit",
            "Must always be charged fully to this year's Profit and Loss Account", "Relates only to paying employee wages"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Revenue expenditure' on a fixed asset (e.g. routine repairs) refers to spending that:", "options": [
            "Maintains the asset in its normal working condition without increasing its value significantly", "Permanently increases the asset's capacity or useful life",
            "Is always recorded as an addition to the asset's cost", "Is never recorded in the books at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When a fixed asset is sold, a 'profit on sale of asset' arises when:", "options": [
            "The sale price exceeds the asset's net book value at the time of sale", "The sale price is less than the net book value",
            "The sale price exactly equals the original cost", "The asset is scrapped with zero sale proceeds"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "When a fixed asset is sold, a 'loss on sale of asset' arises when:", "options": [
            "The sale price is less than the asset's net book value at the time of sale", "The sale price exceeds the net book value",
            "The asset was never depreciated", "The asset is retained rather than sold"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Compared to the Straight Line Method, the Diminishing Balance Method generally charges:", "options": [
            "Higher depreciation in the earlier years and lower depreciation in later years", "The exact same depreciation amount every year",
            "Zero depreciation until the final year", "Higher depreciation only in the last year of the asset's life"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why choosing an appropriate depreciation method matters for a business?", "options": [
            "It affects the reported profit and the asset's book value shown in the financial statements each year", "It has no effect on the financial statements at all",
            "It only affects the business's marketing strategy", "It determines the exact market price of the asset"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is typically recorded as an addition to a fixed asset's cost (capitalised) rather than expensed immediately?", "options": [
            "The cost of installing new machinery to make it operational", "The cost of routine annual servicing/repair of machinery",
            "The cost of cleaning the office", "The cost of fuel used to run a delivery van"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Final Account (Traditional Structure/Approach)": [
        {"q": "'Final Accounts' of a business typically consist of:", "options": [
            "The Trading Account, Profit and Loss Account, and Balance Sheet", "Only the Cash Book",
            "Only the Trial Balance", "Only the Purchases Book"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'Trading Account' is prepared primarily to determine:", "options": [
            "The Gross Profit or Gross Loss of the business for the period", "The Net Profit or Net Loss of the business",
            "The total value of fixed assets", "The owner's total personal wealth"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Gross Profit' is calculated as:", "options": [
            "Net Sales minus Cost of Goods Sold", "Net Sales minus all operating and administrative expenses",
            "Total Assets minus Total Liabilities", "Capital plus Net Profit"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cost of Goods Sold' is generally calculated as:", "options": [
            "Opening Stock + Purchases (net) - Closing Stock", "Sales - Gross Profit only, with no reference to stock",
            "Closing Stock - Opening Stock", "Purchases + Closing Stock"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'Profit and Loss Account' is prepared to determine:", "options": [
            "The Net Profit or Net Loss of the business after accounting for indirect expenses and incomes", "The Gross Profit only",
            "The value of fixed assets only", "The amount of cash in hand only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The starting point of the Profit and Loss Account is normally:", "options": [
            "The Gross Profit (or Gross Loss) brought down from the Trading Account", "The Trial Balance total",
            "The Capital Account balance", "The value of closing stock only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a 'direct expense', typically shown in the Trading Account?", "options": [
            "Carriage inward (freight on purchases)", "Office rent", "Salaries of office staff",
            "Advertising expenses"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of an 'indirect expense', typically shown in the Profit and Loss Account?", "options": [
            "Office salaries and rent", "Carriage inward on purchases", "Wages directly related to production",
            "Purchase of raw materials"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Balance Sheet' is prepared to show:", "options": [
            "The financial position of a business - its assets, liabilities and capital - at a specific date", "The profit earned over an accounting period",
            "Only the cash transactions of the year", "Only the sales made during the year"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In a traditional Balance Sheet format, assets are typically shown on which side?", "options": [
            "The right-hand side (in the traditional 'T' format used in many textbooks)", "The left-hand side always, with no exception",
            "There is no fixed side - it depends only on the business's revenue", "Assets are never shown in a Balance Sheet"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Closing Stock' appearing in the Trading Account is also shown in the Balance Sheet as:", "options": [
            "A current asset", "A current liability", "A fixed asset", "Part of capital"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Outstanding expenses' (expenses incurred but not yet paid) at the year-end are shown in the Balance Sheet as:", "options": [
            "A current liability", "A current asset", "A fixed asset", "A deduction from capital only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Prepaid expenses' (expenses paid in advance) at the year-end are shown in the Balance Sheet as:", "options": [
            "A current asset", "A current liability", "A fixed asset", "Part of Gross Profit"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Accrued income' (income earned but not yet received) at year-end is shown in the Balance Sheet as:", "options": [
            "A current asset", "A current liability", "A fixed liability", "Not shown at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Net Profit calculated in the Profit and Loss Account is transferred to the:", "options": [
            "Capital Account, increasing the owner's capital", "Sales Account", "Purchases Account",
            "Depreciation Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Drawings' made by the owner during the year are shown in the Balance Sheet as a deduction from:", "options": [
            "Capital", "Fixed assets", "Current liabilities", "Gross Profit directly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the traditional format Balance Sheet, liabilities and capital are typically shown on which side?", "options": [
            "The left-hand side (in the traditional format)", "The right-hand side always",
            "They are never shown together with assets", "Only capital is shown, never liabilities"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The accounting principle that requires a Balance Sheet's two sides to always be equal reflects the:", "options": [
            "Accounting equation (Assets = Liabilities + Capital)", "Law of diminishing returns",
            "Law of supply and demand", "Principle of taxation only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is generally classified as a 'current liability' in the Balance Sheet?", "options": [
            "Trade creditors (accounts payable) due within a year", "Land and buildings owned by the business",
            "Long-term bank loan due in 10 years", "Goodwill"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why final accounts are prepared at the end of each accounting period?", "options": [
            "To determine the business's profit/loss and financial position for stakeholders and decision-making", "Because it is only done once when a business is first formed",
            "To replace the need for keeping a Trial Balance", "Because tax authorities forbid preparing them more than once"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
