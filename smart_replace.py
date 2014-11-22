import sublime, sublime_plugin

class SmartReplaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit = edit
		self.view.window().show_input_panel('Replace lambda t, i:', '', self.replace_text, None, None)

	def replace_text(self, inp):
		replacer = eval('lambda t, i: str(' + inp + ')')
		edit = self.view.begin_edit()
		for idx, region in enumerate(self.view.sel()):
			txt = self.view.substr(region)
			replacement = replacer(txt, idx)
			self.view.replace(self.edit, region, replacement)
		self.view.end_edit(edit)
