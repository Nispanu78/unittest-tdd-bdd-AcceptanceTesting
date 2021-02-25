Example of Gherkin syntax:
Feature: Retrieve customer balance
    As a customer of the bank
    I wish to be able to view my current balance

Scenario: Customer retrieves balance successfully
    Given account number 0001 is a valid account
    When I try to retrieve the balance for account number 0001
    Then the balance of the account is "50"
