class MyContextManager:
    def __init__(self, timeout):
        self.timeout = timeout

    def __enter__(self):
        print("Setup complete")
        return "a simple value"

    def __exit__(self, *args):
        print(f"Teardown")

        # Commenting out since we replaced *args for explicit
        # exception_type, exception_value, traceback parameters
        
        for arg in args:
            print(arg)

        return False

with MyContextManager(timeout=30) as cm:
    print(cm)
    print("Inside the block")


