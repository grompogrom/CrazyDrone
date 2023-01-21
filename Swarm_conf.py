class SwarmConfing:
    def __init__(self, count, *uris):
        self._uris = uris
        self._params = dict()
        [self._params.update({uris[i]: [False, {'x': 0, 'y': 0, 'z': 0}]}) for i in range(count)]

    def get_uris(self):
        return set(self._uris)

    def get_params(self):
        return self._params

    def add_end_point(self, uri, x, y, z):
        self._params[uri] = [True, {'x': x, 'y': y, 'z': z}]


if __name__ == '__main__':
    conf = SwarmConfing(3, 'a', 'b', 'c')
    print(conf.get_params())
