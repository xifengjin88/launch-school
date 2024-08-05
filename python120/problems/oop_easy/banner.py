class Banner:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {" " * len(self.message)} |"

    def _horizontal_rule(self):
        return f"+{"-" * (len(self.message) + 2)}+"

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def _message_line(self):
        return f"| {self.message} |"


if __name__ == "__main__":
    banner = Banner("To boldly go where no one has gone before.")
    print(banner)
