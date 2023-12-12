Feature: Login and perform actions on the website

Background: Initialize driver
     Given initial details

Scenario: fill cash deposit voucher
    Then user name
    When password
    And Click on login
    Then select institute
    And select center
    Then go to Voucher entries in Accounts
    Then select cash deposit
    Then check mandatory option for Cash Deposited
    When enter Currency Denomination Details
#    And Compare the actual and expected results for currency notes
#    Then Check Cash Deposited Result
    Then check mandatory option for Voucher date
    Then check previous year date
    And  add current year date
    Then check mandatory option for bank name
    And  add bank details
    Then check mandatory option for purpose
    And  add purpose details
    Then save form
