# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import fire

#loading loan intialization fuctions.
from qualifier.utils.loan_initialization import load_bank_data
from qualifier.utils.loan_initialization import get_applicant_info
from qualifier.utils.loan_initialization import find_qualifying_loans

#loading output csv file save.
from qualifier.utils.fileio import save_qualifying_loans


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
