from behave import *
from qa import *

@given ('User input a owner')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)

@when ('I put owner: {arg} in a parser and i expect a {response}')
def step_impl(context, arg, response):
    owner = list()
    owner = arg.split(",")
    context.parser.args.owner = owner
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.owner

@then ('the parser return the newspapers organized by owner')
def step_impl(context):
    assert context.parser.search() == context.response

@given ('User input a country')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)

@when ('I put country: {arg} in a parser and i expect a {response}')
def step_impl(context, arg, response):
    country = list()
    country = arg.split(",")
    context.parser.args.country = country
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.country

@then ('the parser return the newspapers organized by country')
def step_impl(context):
    assert context.parser.search() == context.response

@given ('User input a type of newspaper')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)

@when ('I put type: {arg} in a parser and i expect a {response}')
def step_impl(context, arg, response):
    typ = list()
    typ = arg.split(",")
    context.parser.args.type = typ
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.type

@then ('the parser return the newspapers organized by type')
def step_impl(context):
    assert context.parser.search() == context.response

@given ('User input a language')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)

@when ('I put language: {arg} in a parser and i expect a {response}')
def step_impl(context, arg, response):
    lang = list()
    lang = arg.split(",")
    context.parser.args.language = lang
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.language

@then ('the parser return the newspapers organized by language')
def step_impl(context):
    assert context.parser.search() == context.response

@given ('User input a Name')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)

@when ('I put name: {arg} in a parser and i expect a {response}')
def step_impl(context, arg, response):
    name = list()
    name = arg.split(",")
    context.parser.args.name = name
    test = list()
    test = response
    context.response = test
    print(test)
    assert context.parser.args.name

@then ('the parser return the newspaper info')
def step_impl(context):
    assert context.parser.search() == context.response

@given ('User input a website')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)
@when ('I put website: {arg} in a parser and i expect a {response}')
def step_impl(context, arg, response):
    web = list()
    web = arg.split(",")
    context.parser.args.website = web
    test = list()
    test = response.split(">")
    context.response = test
    assert context.parser.args.website

@then ('the parser return the website title')
def step_impl(context):
    assert context.parser.search() == context.response



    
    
