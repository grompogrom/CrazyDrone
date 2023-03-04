class Reporter:
	def __init__(self):
		self.error_reported = False
		self._errors = []

	@property
	def errors(self):
		return self._errors

	def report_error(self, e):
		self.error_reported = True
		self._errors.append(e)

	def is_error_reported(self):
		return self.error_reported