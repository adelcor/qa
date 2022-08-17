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

	Scenario Outline: input name
		Given User input a Name
		When I put name: <arg> in a parser and i expect a <response>
		Then the parser return the newspaper info

		Examples: Names
		| arg                    | response                                                                                    |
		| El Pais                | Name: El Pais, Type: Daily newspaper, Language: ['Spanish', 'Portuguese', 'Catalan', 'English'], Owner: PRISA, Website: http://www.elpais.com, Country: Spain       |
		| El Mundo               | Name: El Mundo, Type: Daily newspaper, Language: ['Spanish'], Owner: Unidad Editorial S.A., Website: http://www.elmundo.es, Country: Spain                          |         
		| Marca                  | Name: Marca, Type: Daily sports newspaper, Language: ['Spanish', 'English'], Owner: Unidad Editorial, Website: http://www.marca.com, Country: Spain                 |
		| AS                     | Name: AS, Type: Daily sports newspaper, Language: ['Spanish'], Owner: PRISA, Website: http://as.com, Country: Spain |
		| The Sun                | Name: The Sun, Type: Daily newspaper, Language: ['English'], Owner: News UK Independent, Website: https://www.thesun.co.uk, Country: United Kingdom |
		| The Daily Telegraph    | Name: The Daily Telegraph, Type: Daily newspaper, Language: ['English'], Owner: Telegraph Media Group, Website: https://www.telegraph.co.uk, Country: United Kingdom |
		| The New York Times     | Name: The New York Times, Type: Daily newspaper, Language: ['English', 'Spanish', 'Chinese'], Owner: The New York Times Company, Website: https://www.nytimes.com, Country: United States |
		| CNN International      | Name: CNN International, Type: Daily newspaper, Language: ['English'], Owner: Warner Bros. Discovery, Website: https://edition.cnn.com, Country: United States |
		| Global Times           | Name: Global Times, Type: Daily newspaper, Language: ['English', 'Chinese'], Owner: People's Daily, Website: https://www.huanqiu.com, Country: China |

	Scenario Outline: input website
		Given User input a website
		When I put website: <arg> in a parser and i expect a <response>
		Then the parser return the website title

		Examples: Websites
		| arg                         | response                                                                                               |
		| https://www.nytimes.com     | The New York Times>The New York Times - Breaking News, US News, World News and Videos                  |
		| http://www.elmundo.es       | El Mundo>EL MUNDO - Diario online líder de información en español                                      |
		| http://www.elpais.com       | El Pais>EL PAÍS: el periódico global                                                                   |
                | http://www.marca.com        | Marca>MARCA - Diario online líder en información deportiva                                             |
		| http://as.com               | AS>AS.com - Diario online deportivo. Fútbol, motor y mucho más                                         |
		| https://www.thesun.co.uk    | The Sun>News, sport, celebrities and gossip  The Sun                                                   |
		| https://www.telegraph.co.uk | The Daily Telegraph>The Telegraph - Telegraph Online, Daily Telegraph, Sunday Telegraph - Telegraph    |
		| https://edition.cnn.com     | CNN International>CNN International - Breaking News, US News, World News and Video                     |
		| https://www.huanqiu.com     | Global Times>环球网_全球生活新门户_环球时报旗下网站                                                    |

		
		


