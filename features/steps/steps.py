from behave import *

# This should be added to environment.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords()

use_step_matcher('re')


@when(r'I start the coffee machine using language "(.*)"')
def impl(context, lang = "en"):
    context.actionwords.i_start_the_coffee_machine_using_language_lang(lang)


@when(r'I shutdown the coffee machine')
def impl(context):
    context.actionwords.i_shutdown_the_coffee_machine()


@then(r'message "(.*)" should be displayed')
def impl(context, message = ""):
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


@when(r'I empty the coffee grounds')
def impl(context):
    context.actionwords.i_empty_the_coffee_grounds()


@when(r'I fill the beans tank')
def impl(context):
    context.actionwords.i_fill_the_beans_tank()


@when(r'I fill the water tank')
def impl(context):
    context.actionwords.i_fill_the_water_tank()


@when(r'I take "(.*)" coffees')
def impl(context, coffee_number = 10):
    context.actionwords.i_take_coffee_number_coffees(coffee_number)


@given(r'the coffee machine is started')
def impl(context):
    context.actionwords.the_coffee_machine_is_started()


@given(r'I handle everything except the water tank')
def impl(context):
    context.actionwords.i_handle_everything_except_the_water_tank()


@given(r'I handle water tank')
def impl(context):
    context.actionwords.i_handle_water_tank()


@given(r'I handle beans')
def impl(context):
    context.actionwords.i_handle_beans()


@given(r'I handle coffee grounds')
def impl(context):
    context.actionwords.i_handle_coffee_grounds()


@given(r'I handle everything except the beans')
def impl(context):
    context.actionwords.i_handle_everything_except_the_beans()


@given(r'I handle everything except the grounds')
def impl(context):
    context.actionwords.i_handle_everything_except_the_grounds()


@then(r'displayed message is')
def impl(context, free_text = ""):
    context.actionwords.displayed_message_is(context.text)


@when(r'I switch to settings mode')
def impl(context):
    context.actionwords.i_switch_to_settings_mode()


@then(r'settings should be')
def impl(context, datatable = "||"):
    context.actionwords.settings_should_be(context.table)
