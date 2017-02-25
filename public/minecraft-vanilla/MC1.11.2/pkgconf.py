#cripackage minecraft-vanilla MC1.11.2

urltemplate = "https://s3.amazonaws.com/Minecraft.Download/versions/{0}/minecraft_server.{0}.jar"
version = "1.11.2"
destination = "server.jar"

def __url():
	global urltemplate
	global version
	return urltemplate.format(version)

def install(ctx):
	global destination
	ctx.download_url(__url(), destination)

def configure(ctx):
	# TODO Request configuration options.
	pass

def start(ctx):
	# TODO Specify Jar path to executor.
	pass
