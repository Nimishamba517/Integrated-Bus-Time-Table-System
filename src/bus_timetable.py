# Integrated Bus Time Table System
# Static bus timetable data for demonstration

bus_timetable = {
    "101": ["08:00 AM", "10:00 AM", "12:00 PM"],
    "202": ["09:00 AM", "11:00 AM", "01:00 PM"],
    "303": ["07:30 AM", "09:30 AM", "11:30 AM"],
}

def show_timetable(route_no):
    """
    Returns the timetable for a given route number.
    This is a simple placeholder function for demonstration.
    """
    return bus_timetable.get(route_no, "Route not found")

# Test output
if __name__ == "__main__":
    print("Bus Timetable for Route 101:", show_timetable("101"))
    print("Bus Timetable for Route 999:", show_timetable("999"))
