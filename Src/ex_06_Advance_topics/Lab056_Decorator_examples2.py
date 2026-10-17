def before_after_ui_test(func):
    def wrapper():
        print("Before Running Code")
        func()
        print("After Running Code")
    return wrapper



@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Test")

test_ui()

# without decorater also we can do this just we need to create multiple functions and call them like
