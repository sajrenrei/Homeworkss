class GroupOverflowError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів!"):
        self.message = message
        super().__init__(self.message)