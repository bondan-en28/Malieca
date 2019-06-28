import base

while True:
	text = input('Malieca > ')
	result, error = base.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(repr(result))
