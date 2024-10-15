What would a navigation puzzle look like?

A simple version is: Travel one way, then find your way back. 
--
What does this puzzle look like visually? 

You can imagine that the screen at any given point in time shows you either
an intersection or a street segment. 

For simplicity, the initial version of the puzzle can be run on a grid. 

what do the landmarks look like? 

one option is to have landmark "strips" that stack.

a strip can have whatever content we want,
but typically would have content aligned to one end or the other,
OR have full content.
Because it's annoying to merge strips with different orientations,
we can keep the strips as rows with controlled contents.
(Down the road, we'll have non-grid layouts. But
at that point, I imagine we can have more complex landmark blobs
that contain the same types of stuff but at a distance.)

----

One way to do this is to actually draw the entire map,
and just pan around on it. 

so you have this network of blocks. 

you can absolutely position each block and road,
and then adjust the overall position of the frame.