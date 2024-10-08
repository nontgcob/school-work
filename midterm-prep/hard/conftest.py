def pytest_sessionfinish(session, exitstatus):
    """
    Called after the whole test run finishes, right before returning the exit status to the system.
    """
    if exitstatus == 0:
        # All tests passed
        print("\n\033[1;36m" + "*" * 50)
        print("\033[1;32m  All tests passed successfully! Great job!  ")
        print("\033[1;36m" + "*" * 50 + "\033[0m")
    elif exitstatus == 1:
        # Tests failed
        print("\n\033[1;31m" + "Some tests failed. Please check the errors above." + "\033[0m")
    else:
        # Other exit statuses (e.g., interruption)
        print("\n\033[1;33m" + "Tests were interrupted or encountered an error." + "\033[0m")