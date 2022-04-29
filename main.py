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
from src import fct_lidar
from src import fct_display
from src import fct_http


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
fct_http.geo_connection()

# [DEV] LiDAR portforwarding
fct_lidar.lidar_start_motor()
fct_loop.lidar_loop()
fct_lidar.lidar_stop_motor()
fct_http.geo_disconnect()

# [STA] Show final statistics
fct_display.show_stat()

#-------------
print("---- Stop program ----")
