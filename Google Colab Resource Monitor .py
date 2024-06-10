#  This code sets up a live monitoring system for resource usage in a Colab cell.
#  It continuously tracks CPU, GPU, and RAM usage and displays the information in a text area widget.
#  The monitoring is done in a separate background thread to avoid blocking the main execution.
#  Exception handling is included to provide informative messages in case of errors.

#  To execute this code, simply copy and paste it into a Colab cell and run it.
#  If you prefer to shorten the Cell, you can remove the code.
#  But if you accidently delete the cell then just run last two line.

import psutil
import GPUtil
import ipywidgets as widgets
from IPython.display import display
import threading
import time
import queue

class SystemMonitor:
    def __init__(self):
        self.usage_widget = widgets.Textarea()
        self.usage_widget.layout.width = '500px'
        display(self.usage_widget)
        self.queue = queue.Queue()

    def update_usage(self):
        while True:
            try:
                cpu_usage = psutil.cpu_percent()
                gpus = GPUtil.getGPUs()
                gpu_usage = [gpu.load * 100 for gpu in gpus]
                ram_usage = psutil.virtual_memory().percent
                self.queue.put(f"CPU: {cpu_usage}%\nGPU: {gpu_usage}%\nRAM: {ram_usage}%")
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(1)

    def update_widget(self):
        while True:
            try:
                usage_text = self.queue.get()
                self.usage_widget.value = usage_text
            except Exception as e:
                print(f"Error: {e}")

    def start_monitoring(self):
        monitor_thread = threading.Thread(target=self.update_usage)
        monitor_thread.daemon = True
        monitor_thread.start()
        widget_thread = threading.Thread(target=self.update_widget)
        widget_thread.daemon = True
        widget_thread.start()

monitor = SystemMonitor()
monitor.start_monitoring()
