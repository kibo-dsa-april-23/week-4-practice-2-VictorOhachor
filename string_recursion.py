class String:
    @staticmethod
    def print_dashed(s):
        if not s:
            return

        if len(s) > 1:
            print(s[0] + '-', end='')
        else:
            print(s[0])

        # recursive over the string
        String.print_dashed(s[1:])

    def remove_char(s, c):
        if not s:
            return s

        if s[0] == c:
            return String.remove_char(s[1:], c)
        return s[0] + String.remove_char(s[1:], c)

    def to_upper_case(s):
        if not s:
            return s

        return s[0].upper() + String.to_upper_case(s[1:])

    def get_index(s, c):
        # base cases
        if not s or not c:
            return -1

        if s[0] == c:
            return 0

        # recursive case
        index = String.get_index(s[1:], c)
        if index == -1:
            return -1
        return index + 1

    def prune(s):
        if not s:
            return s
        
        if s[0] == ' ':
            return String.prune(s[1:])
        if s[-1] == ' ':
            return String.prune(s[:-1])

        return s


if __name__ == "__main__":
    String.print_dashed("hello")
    print(String.remove_char("hello", 'l'))
    print(String.to_upper_case('hello'))
    print(String.get_index('hello', 'z'))
