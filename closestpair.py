import math

def dist(p3, p4):
    return math.sqrt((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2) # Update min_dist and points

def closest_pair(ax, ay):
    # It's quicker to assign variable
    ln_ax = len(ax)  
    
    if ln_ax <= 3:
        # A call to bruteforce comparison
        return brute(ax)  
    
    # Division without remainder, need int

    mid = ln_ax // 2  
    
    # Two-part split
    Qx = ax[:mid]  
    Rx = ax[mid:]
    
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]  
    Qy = list()
    Ry = list()
    
	# split ay into 2 arrays using midpoint
    for x in ay:  
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)

    # Call recursively both arrays after split  # Presorting y-wise
    (p3, q1, mi1) = closest_pair(Qx, Qy)
    (p4, q2, mi2) = closest_pair(Rx, Ry)

    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p3, q1)
    else:
        d = mi2
        mn = (p4, q2)

    # Call function to account for points on the boundary
    (p5, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p5, q3, mi3

def closest_split_pair(p_x, p_y, delta, best_pair):
    # store length - quicker
    ln_x = len(p_x)
    
    # select midpoint on x-sorted array
    mx_x = p_x[ln_x // 2][0]  
    
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    # assign best value to delta
    best = delta  
    # store length of subarray for quickness
    ln_y = len(s_y)  
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):# Presorting x-wise
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

def solution(a):
    ax = sorted(a, key=lambda x: x[0]) 
    ay = sorted(a, key=lambda x: x[1])  
    p3, p4, mi = closest_pair(ax, ay)  # Recursive D&C function
    return (p3, p4, mi)

def brute(ax):
    mi = dist(ax[0], ax[1])
    p3 = ax[0]
    p4 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p3, p4, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:  
                    mi = d
                    p3, p4 = ax[i], ax[j]
    return p3, p4, mi

solution_tuple = solution([(0,0),(5,4),(2,10),(12,15),(6,16),(5,18),(19,7),(14,32),(8,10),(7,29),(10,16),(1,23)])
print "Point 1",solution_tuple[0]
print "Point 2",solution_tuple[1]
print "Minimum distance =>",solution_tuple[2]


