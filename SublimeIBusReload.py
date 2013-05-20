import os
import sublime, sublime_plugin

class SublimeIbusReloadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pkgDir = sublime.packagesPath()
		target = "sublimeibusplugin.py"
		cmd = "touch"
		os.system(cmd + " " + pkgDir + "/" + target)
