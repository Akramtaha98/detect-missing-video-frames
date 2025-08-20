# Detecting Missing Video Frames

A compact Python solution for detecting missing frame ranges from an unordered list of frame numbers.  
It complies with the rules from the quiz: no built-in sorting and no third-party libraries.

## Function
```python
def find_missing_ranges(frames: list[int]) -> dict
```
Returns:
```json
{
  "gaps": [[start, end], ...],
  "longest_gap": [start, end] | null,
  "missing_count": int
}
```

## Example
```python
from find_missing_ranges import find_missing_ranges

frames = [1, 2, 3, 5, 6, 10, 11, 16]
print(find_missing_ranges(frames))
# {
#   "gaps": [[4, 4], [7, 9], [12, 15]],
#   "longest_gap": [12, 15],
#   "missing_count": 8
# }
```

## Why no sort?
To respect the constraint, the implementation walks from 1..max(frames) using a set for O(1) membership checks, so no `.sort()` or `sorted()` is used.

## Complexity
- **Time:** `O(n + T)` where `n = len(frames)` and `T = max(frames)`
- **Space:** `O(n)`

## Test
```bash
python find_missing_ranges.py 1 2 3 5 6 10 11 15
```

## Notes
- Assumes positive integers starting at 1.
- No duplicate frames (as per quiz statement).
