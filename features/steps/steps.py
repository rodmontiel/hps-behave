from behave import *

use_step_matcher('re')

@given(r'I start the coffee machine "(.*)"')
@when(r'I start the coffee machine "(.*)"')
def impl(context, lang = "en"):
    context.actionwords.i_start_the_coffee_machine(lang)


@when(r'I shutdown the coffee machine')
def impl(context):
    context.actionwords.i_shutdown_the_coffee_machine()


@then(r'message "(.*)" should be displayed')
def impl(context, message):
    context.actionwords.message_message_should_be_displayed(message)


@then(r'coffee should be served')
def impl(context):
    context.actionwords.coffee_should_be_served()


@then(r'coffee should not be served')
def impl(context):
    context.actionwords.coffee_should_not_be_served()


@when(r'I take a coffee')
def impl(context):
    context.actionwords.i_take_a_coffee()


@given(r'I empty the coffee grounds')
def impl(context):
    context.actionwords.i_empty_the_coffee_grounds()


@when(r'I fill the beans tank')
def impl(context):
    context.actionwords.i_fill_the_beans_tank()


@when(r'I fill the water tank')
def impl(context):
    context.actionwords.i_fill_the_water_tank()


@when(r'I take "(.*)" coffees')
def impl(context, coffee_number):
    context.actionwords.i_take_coffee_number_coffees(coffee_number)


@given(r'the coffee machine is started')
def impl(context):
    context.actionwords.the_coffee_machine_is_started()


@when(r'fifty coffees have been taken without filling the tank')
def impl(context):
    context.actionwords.fifty_coffees_have_been_taken_without_filling_the_tank()


@when(r'thirty eight coffees are taken without filling beans')
def impl(context):
    context.actionwords.thirty_eight_coffees_are_taken_without_filling_beans()


