import RadeonMaster
from time import sleep
gpus = RadeonMaster.GPU()
print(gpus.get_output(0))
gpus.stop_logging()