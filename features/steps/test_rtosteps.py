import configparser
import time

from behave import given, when, then
from configparser import ConfigParser
from selenium import webdriver
from Pages.Dashboardbordpage import DashboardPage
from base_page import BasePage



@given('I click on Wrinch Icon')
def click_on_wrenchiconondashboard(context):
    dashboardpage = DashboardPage(context.driver)
    dashboardpage.click_on_wrenchicon()


@then('I click on \'Sign in as Store\'')
def click_on_signinasstore(context):
    dashboardpage = DashboardPage(context.driver)
    dashboardpage.click_on_signinasstore()


@then('I enter in to \'Sign In As Store\' Page.')
def step_impl(context):
    print()


@then('I enter store number in Store field and click on the respective store')
def step_impl(context):
    print()


@when(u'I click on Wrinch Icon')
def step_impl(context):
    print()


@then('I click on \'Sign out as Store\'')
def step_impl(context):
    print()


@then('I Signout from RTO Application')
def step_impl(context):
    print()
