#Files
from src import fct_file
from src import fct_loop
from src import fct_signal
from src import fct_device
from src import fct_display
from src import fct_terminal


print("---- Start program ----")
#-------------

#Argument
fct_terminal.clear()
fct_terminal.compute_argument()

# [OPT] Show parameters
fct_display.show_parameter()

# [SSD] Create directories
fct_file.check_directories()
fct_file.check_capture_ID()

# [DEV] LiDAr portforwarding
fct_device.select_lidar_devices()
fct_loop.lidar_loop()

# [STA] Show final statistics
fct_display.show_stat()

#-------------
print("---- Stop program ----")
