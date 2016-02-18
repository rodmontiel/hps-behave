# encoding: UTF-8
from behave import *
from src.coffee_machine import CoffeeMachine

class Actionwords:
    def __init__(self):
        self.sut = CoffeeMachine()

    def i_start_the_coffee_machine(self, lang = "en"):
        self.sut.start(lang)

    def i_shutdown_the_coffee_machine(self):
        self.sut.stop()

    def message_message_should_be_displayed(self, message):
        assert (self.sut.message == message) is True

    def coffee_should_be_served(self):
        assert self.sut.coffee_served is True

    def coffee_should_not_be_served(self):
        assert self.sut.coffee_served is False

    def i_take_a_coffee(self):
        self.sut.take_coffee()

    def i_empty_the_coffee_grounds(self):
        self.sut.empty_grounds()

    def i_fill_the_beans_tank(self):
        self.sut.fill_beans()

    def i_fill_the_water_tank(self):
        self.sut.fill_tank()

    def i_take_coffee_number_coffees(self, coffee_number = 10):
        coffee_number = int(coffee_number)

        while (coffee_number > 0):
            self.i_take_a_coffee()
            coffee_number = coffee_number - 1

    def the_coffee_machine_is_started(self):
        self.i_start_the_coffee_machine()

    def fifty_coffees_have_been_taken_without_filling_the_tank(self):
        self.i_take_coffee_number_coffees(coffee_number = 30)
        self.i_fill_the_beans_tank()
        self.i_empty_the_coffee_grounds()
        self.i_take_coffee_number_coffees(coffee_number = 20)
        self.i_fill_the_beans_tank()
        self.i_empty_the_coffee_grounds()

    def thirty_eight_coffees_are_taken_without_filling_beans(self):
        self.i_take_coffee_number_coffees(coffee_number = 37)
        self.i_empty_the_coffee_grounds()
        self.i_fill_the_water_tank()
        self.i_take_a_coffee()
