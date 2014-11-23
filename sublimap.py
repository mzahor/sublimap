import sublime, sublime_plugin

class SubliMapCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit = edit
		self.view.window().show_input_panel('Map lambda t, i:', '', self.map_text, None, None)

	def map_text(self, inp):
		try:
			edit = self.view.begin_edit()
			replacer = eval('lambda t, i: str(' + inp + ')')
			for idx, region in enumerate(self.view.sel()):
				txt = self.view.substr(region)
				replacement = replacer(txt, idx)
				self.view.replace(self.edit, region, replacement)
		except Exception as e:
			print 'Error in SubliMap: ', e
		finally:
			self.view.end_edit(edit)

class SubliReduceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit = edit
		self.view.window().show_input_panel('Reduce lambda x, y:', '', self.reduce_text, None, None)

	def reduce_text(self, inp):
		try:
			edit = self.view.begin_edit()
			reducer = eval('lambda x, y: ' + inp)
			reduce(reducer, map(self.view.sel(), lambda x: self.view.substr(x))),
			self.view.replace(self.edit, region, replacement)
		except Exception as e:
			print 'Error in SubliReduce: ', e
		finally:
			self.view.end_edit(edit)