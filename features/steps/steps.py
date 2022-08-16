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

    
    
