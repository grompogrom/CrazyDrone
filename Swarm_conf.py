class SwarmConfing:
    def __init__(self, count, *uris):
        self.uris = uris
        self.params = dict()
        [self.params.update({uris[i]: {'is_for_me': False, 'x': 0, 'y': 0, 'z': 0}}) for i in range(count)]

    def get_uris(self):
        return set(self.uris)

    def get_params(self):
        return self.params

    def add_end_point(self, uri, x, y, z):
        self.params[uri] = {'is_for_me': True, 'x': x, 'y': y, 'z': z}

if __name__ == '__main__':
    conf = SwarmConfing(3, 'a', 'b', 'c')
    print(conf.get_params())
