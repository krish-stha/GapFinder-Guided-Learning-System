# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - Principles of Accounting-II question bank.

Authored content (not content partner data - loaded with source='synthetic'
by scripts/load_question_bank.py). Course 210's "Principles of
Accounting-II" subject (subject_id=34294) has exactly one real chapter in
the source data - a genuinely thin shell, not something this session is
choosing to under-cover. Chapter name verified exactly via
chapters_under_subject() before writing this module: note the source
data's spelling "Debetnture" (not "Debenture") - matched exactly per the
exact-match-only rule, not corrected/normalised. Never presented as
content partner content or as evidence about real students.

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}.
"""

QUESTIONS = {
    "Accounting for Debetnture (Batch 2081)": [
        {"q": "A 'debenture' is best described as:", "options": [
            "A document acknowledging a company's long-term debt to the holder, carrying a fixed rate of interest", "A share representing part ownership of a company",
            "A short-term IOU with no interest attached", "A government tax receipt"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Unlike equity shareholders, debenture holders are:", "options": [
            "Creditors of the company, not owners", "Owners of the company with voting rights",
            "Entitled to a share of company profits only, with no fixed return", "Liable for the company's debts personally"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Interest paid on debentures is treated in the company's accounts as:", "options": [
            "A charge against profit (an expense), payable regardless of whether the company earns a profit", "An appropriation of profit, paid only if the company is profitable",
            "A form of dividend to shareholders", "Not recorded in the accounts at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Redeemable debentures' are debentures that:", "options": [
            "Will be repaid by the company at or before a specified maturity date", "Can never be repaid by the company under any circumstance",
            "Automatically convert into equity shares at issue", "Carry no obligation of repayment whatsoever"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Irredeemable (perpetual) debentures' are debentures that:", "options": [
            "Have no fixed maturity date and are repaid only on company winding up or at the company's discretion", "Must be repaid within one year of issue",
            "Are automatically converted to preference shares", "Carry no interest obligation at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Convertible debentures' give the holder the option to:", "options": [
            "Convert their debentures into equity shares of the company after a specified period", "Convert their debentures into government bonds only",
            "Receive a permanent exemption from tax", "Vote at the company's annual general meeting immediately upon issue"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When a company issues debentures 'at par', it means the debentures are issued:", "options": [
            "At their exact face (nominal) value", "At a price higher than their face value", "At a price lower than their face value",
            "Without any face value being specified"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "When a company issues debentures 'at a discount', it means the issue price is:", "options": [
            "Lower than the face value of the debenture", "Higher than the face value of the debenture",
            "Exactly equal to the face value", "Unrelated to the face value"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When a company issues debentures 'at a premium', it means the issue price is:", "options": [
            "Higher than the face value of the debenture", "Lower than the face value of the debenture",
            "Exactly equal to the face value", "Determined only after redemption"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The journal entry to record cash received on issue of debentures at par would debit Bank/Cash Account and credit:", "options": [
            "Debenture Account", "Share Capital Account", "General Reserve Account", "Profit and Loss Appropriation Account"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When debentures are issued at a discount, the 'Discount on Issue of Debentures' account is treated as:", "options": [
            "A capital loss, written off gradually over the life of the debentures", "Immediate taxable income for the company",
            "A liability owed to the debenture holders", "A form of dividend paid to shareholders"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Debenture Redemption Reserve' is created by a company primarily to:", "options": [
            "Set aside profits over time to ensure funds are available when debentures fall due for repayment", "Increase the company's short-term cash expenses",
            "Pay dividends to equity shareholders", "Reduce the face value of outstanding debentures"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Debentures may be secured by a 'charge' on company assets, meaning that if the company defaults, debenture holders:", "options": [
            "Have a legal claim on the specified assets before unsecured creditors", "Automatically become equity shareholders instead",
            "Lose all rights to recover their investment", "Must wait until all equity shareholders are paid first"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Debentures issued as collateral security' means the debentures are:", "options": [
            "Pledged to a lender as additional security for a loan, without being a primary source of cash raised", "Sold directly to the public for cash",
            "Automatically cancelled once issued", "Converted immediately into equity shares"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "On the redemption (repayment) of debentures at par, the company's cash/bank balance:", "options": [
            "Decreases by the amount paid to redeem the debentures", "Increases by the amount of the debentures redeemed",
            "Remains completely unaffected by redemption", "Is only affected if debentures were issued at a premium"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Sinking fund method' of debenture redemption involves the company:", "options": [
            "Setting aside a fixed amount annually, often invested outside the business, to accumulate funds for redemption", "Paying off the entire debenture amount in a single lump sum with no advance planning",
            "Converting all debentures into equity shares automatically", "Ignoring the redemption obligation entirely until the due date"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Compared to raising funds through equity shares, raising funds through debentures generally:", "options": [
            "Does not dilute company ownership/control, since debenture holders are not owners", "Automatically gives debenture holders voting rights over company decisions",
            "Removes the company's obligation to ever repay the amount raised", "Guarantees the company will always be profitable"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key financial risk of raising a large proportion of capital through debentures is that the company:", "options": [
            "Must pay fixed interest regardless of profit levels, increasing financial risk during low-profit periods", "Faces no obligation to pay interest under any circumstance",
            "Automatically becomes debt-free after the first year", "Is legally prohibited from ever issuing further debentures"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In the Statement of Financial Position (Balance Sheet), debentures are typically classified under:", "options": [
            "Non-current (long-term) liabilities", "Current assets", "Equity/Share capital", "Current liabilities only, regardless of maturity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why a company might choose to issue debentures rather than additional equity shares to raise capital?", "options": [
            "Debentures allow the company to raise funds without diluting existing shareholders' ownership and control", "Debentures always cost the company less than the total amount raised, with no repayment required",
            "Issuing debentures automatically increases the company's total number of shareholders", "Debenture holders are legally entitled to the same voting rights as equity shareholders"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
