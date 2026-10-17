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
print("\n\n")

# without decorater also we can do this just we need to create multiple functions and call them like
def start_ui():
    print("Before Running Code")
def end_ui():
    print("After Running Code")
def test_ui():
    print("Hi, I am testing a UI Test")
start_ui()
test_ui()
end_ui()
