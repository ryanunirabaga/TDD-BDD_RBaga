Feature: dividing two numbers


    Scenario: when dividing two integers
        Given two valid integers
        When dividing the integers
        Then it should result to another integer
    
    Scenario: when dividing non-zero-integer by 0
        Given non-zero-integer and 0
        When dividing non-zero-integer by 0
        Then it should result to undefined
    
    Scenario: when dividing 0 by 0
        Given 0 and 0
        When dividing 0 by 0
        Then it should result to indeterminate