class list_divider(list):
    def __truediv__(self, n):
        if n<=0:
            raise ValueError()
        if type(n) is not int:
            raise TypeError()
        k, m = divmod(len(self), n)
        return [self[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]