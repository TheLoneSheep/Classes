# from person import Person


class AttrDisplay:
    """
    Предоставляет наследуемый метод перегрузки отображения...
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'[{self.__class__.__name__}: {self.gatherAttrs()}]'


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

        def __gatherAttrs(self):
            return 'Spam'

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

    bob = Person('Bob Smith')

    print(list(bob.__dict__.keys()))
    print(dir(bob))
    print(len(dir(bob)))

    print(list(name for name in dir(bob) if not name.startswith('__')))
