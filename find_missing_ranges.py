from typing import Dict, List

def find_missing_ranges(frames: List[int]) -> Dict[str, object]:
    """Return missing ranges, the longest gap, and total missing count.

    - Input is an UNORDERED list of positive integers (starting at 1).
    - The highest number in the list is the expected total frames.
    - No .sort() / sorted(). No third-party libs.

    Returns:
      {
        "gaps": list[[start, end]],
        "longest_gap": [start, end] | None,
        "missing_count": int
      }

    Complexity:
      Time  : O(n + T), where n = len(frames), T = max(frames)
      Space : O(n) for the set of present frames
    """
    if not isinstance(frames, list):
        raise TypeError("frames must be a list of positive integers")

    for x in frames:
        if not isinstance(x, int) or x < 1:
            raise ValueError("all frames must be positive integers starting from 1")

    if not frames:
        return {"gaps": [], "longest_gap": None, "missing_count": 0}

    present = set(frames)
    expected_total = max(present)

    gaps: List[List[int]] = []
    missing_count = 0

    i = 1
    while i <= expected_total:
        if i not in present:
            start = i
            while i <= expected_total and i not in present:
                i += 1
            end = i - 1
            gaps.append([start, end])
            missing_count += end - start + 1
        else:
            i += 1

    # Longest gap by length; tie-breaker = earliest start
    longest_gap = max(gaps, key=lambda g: (g[1] - g[0] + 1, -g[0])) if gaps else None

    return {"gaps": gaps, "longest_gap": longest_gap, "missing_count": missing_count}

if __name__ == "__main__":
    # Optional CLI for quick checks:
    #   python find_missing_ranges.py 1 2 3 5 6 10 11 16
    import argparse, json
    parser = argparse.ArgumentParser(description="Detect missing video frame ranges")
    parser.add_argument("frames", nargs="*", type=int, help="Unordered positive frame numbers")
    args = parser.parse_args()
    result = find_missing_ranges(args.frames)

    def _pretty_print_result(obj):
        import json
        lines = ["{"]
        items = list(obj.items())
        for idx, (k, v) in enumerate(items):
            # dump values compactly (keeps inner lists on one line)
            v_str = json.dumps(v, separators=(", ", ": "))
            comma = "," if idx < len(items) - 1 else ""
            lines.append(f"  {json.dumps(k)}: {v_str}{comma}")
        lines.append("}")
        print("\n".join(lines))

    _pretty_print_result(result)
