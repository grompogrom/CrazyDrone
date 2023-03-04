from beautiful_flie.trajectory import uris, takeoff_land


def at_local_coords(func):
    def wrapper_at_local_coords(scf, params):
        x = params['x']
        y = params['y']
        z = params['z']
        t = params['t']
        x, y, z = converter.cast_coords(x,y,z)
        func(scf, x, y, z, t)
    return wrapper_do_twice

@at_local_coords({'x':1, 'y':1, 'z':1, 't':7})
def flie(x,)
