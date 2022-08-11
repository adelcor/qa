Feature: Scan Json
	Scenario: input a parameter
		Given a parser
		When input -w
		Then the parser return a newspaper name and a title website

