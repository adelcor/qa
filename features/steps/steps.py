from behave import *
from qa import *
import logging

logging.basicConfig(filename="testlog.log",
        format='%(asctime)s %(message)s',
        filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def search_errors(context, logger, identifier):
    search = context.parser.search()
    if search == context.response:
        logger.info("\033[0;32m%s output OK: %s  :-)\033[0m", identifier, context.parser.arg)
    else:
        logger.error("\033[0;31m%s error : %s :-(\033[0m",identifier, context.parser.arg)
    assert search == context.response

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
    context.parser.arg = arg
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.owner

@then ('the parser return the newspapers organized by owner')
def step_impl(context):
    search_errors(context,logger, "Owner")
    
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
    context.parser.arg = arg
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.country

@then ('the parser return the newspapers organized by country')
def step_impl(context):
    search_errors(context, logger, "Country")

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
    context.parser.arg = arg
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.type

@then ('the parser return the newspapers organized by type')
def step_impl(context):
    search_errors(context, logger, "Type")

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
    context.parser.arg = arg
    test = list()
    test = response.split(",")
    context.response = test
    assert context.parser.args.language

@then ('the parser return the newspapers organized by language')
def step_impl(context):
    search_errors(context,logger, "Language")

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
    context.parser.arg = arg
    test = list()
    test = response
    context.response = test
    print(test)
    assert context.parser.args.name

@then ('the parser return the newspaper info')
def step_impl(context):
    search_errors(context, logger, "Name")

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
    context.parser.arg = arg
    test = list()
    test = response.split(">")
    context.response = test
    assert context.parser.args.website

@then ('the parser return the website title')
def step_impl(context):
    search_errors(context, logger, "Website")



    
    
