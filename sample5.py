class zero_error(Exception):
    def __init__(self, msg):
        self.msg = msg

        def msg(self):
            return self.msg

        try:
            a = int(input("Enter a number:"))
            if a >= 0:
                print(a)
            else:
                err = zero_error("entered value is less than zero")
        except zero_error as z:
            print("Exception is", z)
