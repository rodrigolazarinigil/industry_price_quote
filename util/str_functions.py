def boolstr_to_int(val):
	if val in ("YES", "SIM", "Y", "S"):
		return 1
	elif val in ("NO", "NAO", "N"):
		return 0
	else:
		raise ValueError("Invalid parameter value")