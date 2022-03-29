#Color map:
# - Blue = state
# - Red = error
# - Cyan = name
# - Green = default

from src import fct_file
from src import fct_loop
from src import fct_signal
from src import fct_device
from src import fct_terminal
from src import fct_config


print("---- Start program ----")
#-------------

#Argument
fct_terminal.clear()
fct_terminal.compute_argument()

# [OPT] Show parameters
fct_config.make_config()

# [SSD] Create directories
fct_file.check_directories()
fct_file.check_capture_ID()

# [DEV] LiDAR portforwarding
fct_loop.lidar_loop()

# [STA] Show final statistics
fct_display.show_stat()

#-------------
print("---- Stop program ----")
