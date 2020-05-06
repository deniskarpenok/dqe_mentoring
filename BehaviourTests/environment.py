from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def open_browser(context):
    context.browser = webdriver.Chrome('/Users/dinas/Desktop/dqe_mentoring/BehaviourTests/chromedriver')
    yield context.browser
    context.browser.quit()

@fixture
def start_logging(context):
    import sys
    sys.path.append('/Users/dinas/Desktop/dqe_mentoring/DemoTestFramework/')
    from resulting import Result

    context.logger = Result()
    yield context.logger
    context.logger.finish_test()

def before_all(context):
    use_fixture(open_browser, context)
    use_fixture(start_logging, context)

def before_feature(context, feature):
    context.logger.start_test(feature.name)

def before_scenario(context, scenario):
    context.logger.start_case(scenario.name)

def before_step(context, step):
    context.step = step