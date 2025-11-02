from typing import Any, Dict, Iterable, List, Optional


def sort_dicts_by_key(
	items: Iterable[Dict[str, Any]],
	key: str,
	*,
	reverse: bool = False,
	missing: Optional[Any] = "last",
	case_insensitive: bool = False,
) -> List[Dict[str, Any]]:
	"""Return a new list of dicts sorted by the value at `key`.

	Parameters
	- items: iterable of dict-like objects to sort (each should be a dict)
	- key: the dictionary key to sort by
	- reverse: if True, sort descending
	- missing: controls where dicts missing `key` go:
		- "last" (default): place dicts without the key after those with the key
		- "first": place dicts without the key before those with the key
		- any other value: treat missing keys as if they had this value and sort accordingly
	- case_insensitive: when True and values are strings, compare using lowercased values

	The function is stable (uses Python's stable sort) and always returns a new list.
	"""

	MISSING = object()

	def _keyfunc(d: Dict[str, Any]):
		val = d.get(key, MISSING)

		# Missing-key handling
		if val is MISSING:
			if missing == "last":
				# Present items come first (is_missing=0), missing come after (is_missing=1)
				return (1, None)
			if missing == "first":
				# Missing come before present
				return (0, None)
			# Treat missing as the provided constant value
			v = missing
			is_missing = 0
		else:
			v = val
			# If the policy is 'first', then present items should sort after missing items
			is_missing = 1 if missing == "first" else 0

		if case_insensitive and isinstance(v, str):
			try:
				v = v.lower()
			except Exception:
				# Fallback: keep original value if lower() fails
				pass

		return (is_missing, v)

	return sorted(list(items), key=_keyfunc, reverse=reverse)


if __name__ == "__main__":
	# Quick demonstration
	sample = [
		{"name": "Bob", "age": 30},
		{"name": "alice", "age": 25},
		{"age": 40},
	]
	print("Sorted by name (case-insensitive, missing last):")
	for d in sort_dicts_by_key(sample, "name", case_insensitive=True):
		print(d)

