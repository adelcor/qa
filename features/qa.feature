Feature: Scan Json
	Scenario Outline: input owner
		Given User input a owner
		When I put owner: <arg> in a parser and i expect a <response>
		Then the parser return the newspapers organized by owner

		Examples: Owners
		| arg	                         | response               |
		| PRISA           		 | El Pais,AS             |
		| Unidad Editorial               | Marca                  |
		| Unidad Editorial S.A.          | El Mundo               |
		| News UK Independent            | The Sun                |
		| Telegraph Media Group          | The Daily Telegraph    |
		| The New York Times Company     | The New York Times     |
		| Warner Bros. Discovery         | CNN International      |
		| People's Daily                 | Global Times	          |

	Scenario Outline: input country
		Given User input a country
		When I put country: <arg> in a parser and i expect a <response>
		Then the parser return the newspapers organized by country

		Examples: Countries
		| arg		    | response                             |
		| China	            | Global Times                         |
		| Spain		    | El Mundo,El Pais,Marca,AS            |
		| United Kingdom    | The Sun,The Daily Telegraph          |
		| United States	    | The New York Times,CNN International |

	Scenario Outline: input type
		Given User input a type of newspaper
		When I put type: <arg> in a parser and i expect a <response>
		Then the parser return the newspapers organized by type

		Examples: Types
		| arg                     | response                                                                                       |
		| Daily newspaper         | El Mundo,El Pais,The Sun,The Daily Telegraph,The New York Times,CNN International,Global Times | 
		| Daily sports newspaper  | Marca,AS                                                                                       |

	Scenario Outline: input language
		Given User input a language
		When I put language: <arg> in a parser and i expect a <response>
		Then the parser return the newspapers organized by language

		Examples: Languages
		| arg        | response                                                                                    | 
		| Spanish    | El Mundo,El Pais,Marca,AS,The New York Times                                                |
		| Portuguese | El Pais                                                                                     |
		| Catalan    | El Pais                                                                                     |
		| English    | El Pais,Marca,The Sun,The Daily Telegraph,The New York Times,CNN International,Global Times |
		| Chinese    | The New York Times,Global Times                                                             |



		
		


