from behave import *
from time import sleep

@given('main page was opened')
def step_impl(context):
    context.browser.get('https://www.google.com/')
    try:
        google_image = context.browser.find_element_by_css_selector('img[alt="Google"]')
        context.logger.add_pass(context.step, 'page was opened')
    except:
        context.logger.add_fail(context.step, 'page was not opened')


@when('search for "{}"')
def step_impl(context, search_phrase):
    try:
        search_field = context.browser.find_element_by_css_selector('input[name="q"]')
        context.logger.add_pass(context.step, 'search field was found')
    except:
        context.logger.add_fail(context.step, 'search field was not found')

    search_field.send_keys('{}\n'.format(search_phrase))
    sleep(3)



@then('link "{}" on the result page')
def step_impl(context, link):
    try:
        result = context.browser.find_element_by_xpath('.//cite[text()="{}"]'.format(link))
        context.logger.add_pass(context.step, 'link {} was found'.format(link))
    except:
        context.logger.add_fail(context.step, 'link {} was not found'.format(link), link)