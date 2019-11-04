import json

class Drone(object):

    def __init__(self, is_aruco_tracking_enabled=False):
        self.is_connected = False
        self.is_streaming = False
        self.is_aruco_tracking_enabled = is_aruco_tracking_enabled
        self.is_recording_video = False
        self.is_running_droneblocks_mission = False
        self.pitch = None
        self.roll = None
        self.yaw = None
        self.tof = None
        self.altitude = None
        self.battery = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    