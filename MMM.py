nx = 0.0        # New coordinates point of contur the fire
ny = 0.0
wx = 2          # Vector of wind direction
wy = 5
speed_fire = 5

def calc_normal(a, b, c):
    if a[0] == c[0]:
        xo = a[0]
        yo = b[1]
    elif a[1] == c[1]:
        xo = b[1]
        yo = a[1]
    else:
        xo = (a[0] * ((c[1] - a[1]) ** 2) + b[0] * ((c[0]-a[0]) ** 2) + ((c[0] - a[0]) * (c[1]-a[1]) * (b[1]-a[1]))) / (((c[1] -a [1]) ** 2) + ((c[0] - a[0]) ** 2))
        yo = (c[1] - a[1]) * (xo - a[0]) / (b[0] - a[0]) + a[1]

    if xo != b[0]:      # not vertical
        lA = (yo - b[1]) / (xo - b[0])              # equation of line
        lB = (yo + b[1] - lA * (xo + b[0])) / 2
        uA = lA + 2                                 # square equation
        uB = 2 * lA * lB - 2 * b[0] - 2 * lA * b[1]
        uC = (b[0] ** 2) + (b[1] ** 2) - b[1] * lB - (speed_fire ** 2)

        if uA != 0:                                 # if uA = 0 then equation is not square
            D = (uB ** 2) - 4 * uA * uC
            if D<0:
                print 'error'
                return 0, 0
            nx1=(-uB+(D ** 0.5))/(2*uA)
            ny1=lA*nx1+lB

            nx2=(-uB-(D ** 0.5))/(2*uA)
            ny2=lA*nx1+lB
        else:
            nx1 = -uC / uB
            ny1 = lA * nx1 +lB

            return nx1, ny1
    else:
        nx1 = b[0]
        ny1 = b[1] + speed_fire

        nx2 = b[0]
        ny2 = b[1] - speed_fire

    if b[0]>=xo:
        if nx1>=nx2:
            return nx1,ny1
        else:
            return nx2,ny2
    else:
        if nx1<nx2:
            return nx1,ny1
        else:
            return nx2,ny2

def calc_wind(a):
    nwx=a[0]+wx
    nwy=a[1]+wy
    return nwx,nwy

def summ_vec(a,b):
    s = a[0]
    f = a[1] + b[1]
    return s,f


a = (2,2)
b = (7,1)
c = (8,4)
d = (6,6)
e = (1,5)
wind_point = (0,0)
var_coord = [a, b, c, d, e]

i = 0
new_var_coord = []
for point in var_coord:
    prev_point = var_coord[i-1]
    if i == len (new_var_coord):
        next_point = var_coord[0]
    else:
        next_point = var_coord[i+1]
    wind_point = calc_wind(point)       # calculate vector of the wind in point
    coord_without_wind = calc_normal(prev_point, point, next_point)
    new_var_coord += [summ_vec(coord_without_wind, wind_point)]
    print '%s -> %s' % (str(point), str(new_var_coord[i]))
    i += 1

