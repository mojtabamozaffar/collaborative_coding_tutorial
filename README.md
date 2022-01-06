# Collaborative Coding Repo

TASK: A is a set of points in 3D space. B is another set of points in 3D space. d1, d2, d3, d4, and d5 are five constant numeric values representing five distances for which applies d1 < d2 < d3 < d4 < d5. Write fast Python code that for each point in set A counts how many points from set B are at different ranges of distances from that point (see the pseudocode below). GOAL: Code execution time should be as short as possible.

```
INPUTS: A, B, d1, d2, d3, d4, d5

FOR each pointA in set A


count1 = 0
count2 = 0
count3 = 0
count4 = 0
FOR each pointB in set B

      dist = distanceBetweenTwoPoints(pointA, pointB)

      IF dist >= d1 AND dist < d2 THEN
         count1 = count1 + 1
      ENDIF
      IF dist >= d2 AND dist < d3 THEN
         count2 = count2 + 1
      ENDIF
      IF dist >= d3 AND dist < d4 THEN
         count3 = count3 + 1
      ENDIF
      IF dist >= d4 AND dist < d5 THEN
         count4 = count4 + 1
      ENDIF


ENDFOR
ENDFOR
```
