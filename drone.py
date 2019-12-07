from dronekit import connect

# Connect to UDP endpoint.
vehicle = connect('127.0.0.1:14551', wait_ready=True)
# Use returned Vehicle object to query device state - e.g. to get the mode:
print("Mode: %s" % vehicle.mode.name)


vehicle.mode = VehicleMode("GUIDED")
vehicle.commands.goto(Location(-34.36, 149.16, 30))
vehicle.flush()