from gpiozero import MCP3008
gas =MCP3008(0)

while True:
		print(gas.value)