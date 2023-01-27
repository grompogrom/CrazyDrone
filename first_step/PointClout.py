class PointCloud:
    def __init__(self,save_func):
        self._points_array = []
        self._save_func = save_func

    def add(self, elements):
        self._points_array.extend(elements)

    def get_points(self):
        return self._points_array

    def save(self):
        self._save_func(self._points_array)