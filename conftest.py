import os

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver_path = 'D:/PycharmProjects/msedgedriver.exe'
# Provide the path to the EdgeDriver executable
edge_service = Service(executable_path=driver_path)


## This is the standard function to register options and get the browser here.
## Browser name is depend on our input what we are giving

def pytest_addoption(parser):
    parser.addoption("--browser_name", action = "store", default = "edge",
                     help = "Browser selection:")



@pytest.fixture(scope="function")
def BrowserInstance(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(6)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=edge_service)
        driver.implicitly_wait(6)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close() ## it will execute after your test function

@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome( service=service_obj )
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )

    driver.implicitly_wait( 5 )
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution
    driver.close()  #post your test function execution


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


import os, sys, pytest, contextlib

@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, "w") as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr

@pytest.fixture(autouse=True, scope="session")
def silence_tflite_logs():
    with suppress_stderr():
        yield