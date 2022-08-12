from behave import *
from qa import *

@given ('a parser')
def step_impl(context):
    lista = get_values()
    args = get_args()
    context.parser = Parser(lista, args)
    context.parser.args.type = ['Daily newspaper']

@when ('input -n')
def step_impl(context):
    assert context.parser.args.type
    

@then ('the parser return a newspaper name and a title website')
def step_impl(context):
    test = context.parser.search()
    assert test == "El Mundo"
    
    
