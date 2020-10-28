Feature: RTOSmoke


@Smoke
Scenario: 001_SigninPage-User able to Sign in as a Store
	Given I click on Wrinch Icon
	Then I click on 'Sign in as Store'
	And I enter in to 'Sign In As Store' Page.
	And I enter store number in Store field and click on the respective store
	When I click on Wrinch Icon
	Then I click on 'Sign out as Store'
	Then I Signout from RTO Application
