select rank() over (
        PARTITION BY a.x,
        a.y
        ORDER BY b.x asc,
            b.y asc
    ) rnk,
    a.x x1,
    a.y y1,
    b.x x2,
    b.y y2,
    b.x - a.x x_dist,
    b.y - a.y y_dist,
    abs(a.x - b.x) + abs(a.y - b.y) hamming_dist
from map_intersections a,
    map_intersections b
where (
        a.y - b.y = 0
        or a.x - b.x = 0
    )
    and (
        b.x >= a.x
        and b.y >= a.y
    )
    and not (
        a.x = b.x
        and a.y = b.y
    )
order by x1 asc,
    y1 asc,
    rnk asc,
    hamming_dist asc;