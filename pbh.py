"""Creates a hash from a string.

Function: pbh(x)"""

__author__ = 'pbn.'


class PbhHash:
    def __init__(self, x, big_string=False, dash=False):
        self.value = x
        self.dash = dash
        self.big_string = big_string

    def seed(self, a=None):
        """
        :param a: String to convert to seed
        :return: Seed that is a Integer
        """
        if a and isinstance(a, str):
            x = ord(a[0]) << 16
            for c in map(ord, a):  # [ord(x) for x in a]
                x = ((10000000 * x) ^ c) & 0x71dc9900ef8a83590
            x = (x**48 if len(a) == 1 else x**32) >> 16 if self.big_string else x
            x ^= len(a)
            a = x
        return a

    @property
    def pbh(self):
        seed = str(self.seed(self.value))
        cut = 4 if len(self.value) == 1 else 5
        result = ''
        for i in range(len(seed)):
            result += hex(int(seed[i])).lstrip('0x')
        return ('-' if self.dash else '').join(
            [hex(int(result[i:i + cut])).lstrip('0x') for i in range(0, len(result), cut)])


def pbh(x, big_string=False, dash=False):
    """
    :type x: string
    :type big_string: bool
    :type dash: bool
    """
    return PbhHash(x, big_string, dash).pbh


if __name__ == '__main__':
    def _test_generator(string):
        print(
            "Running Normal Hash on '{0}':\n{1}\nRunning Big Hash on '{2}':\n{3}".format(
                string, pbh(string), string, pbh(string, True)
            )
        )
    _test_generator(input("Text: "))
    del _test_generator
