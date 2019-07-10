def defangIPaddr(address):
	"""
	:type address: str
	:rtype: str
	"""
	return address.replace(".", "[.]")