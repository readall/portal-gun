from portal_gun.commands.base_command import BaseCommand


class GeneratePortalSpecCommand(BaseCommand):
	def __init__(self, args):
		BaseCommand.__init__(self, args)

	def run(self):
		print('Running init')

	@staticmethod
	def cmd():
		return 'init'
