Feature: The Perth Mint - Product search

    Scenario: Search from the search bar
        Given a Google Chrome browser is at The Perth Mint home page : 'https://www.perthmint.com/'
        When the user enters 'James' into the search bar
        Then product cards related to 'James' are shown on the search results page