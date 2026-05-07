from pyscript import display
import matplotlib.pyplot as plt
from js import document

days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
lates = [0, 0, 0, 0, 0, 0, 0]

# Create graph
fig, ax = plt.subplots(figsize=(8,5))

def update_attendance(event):

    # Get values from HTML
    day_input = document.getElementById("day").value
    lates_input = document.getElementById("lates").value

    # Check if valid
    if day_input in days and lates_input.isdigit():

        index = days.index(day_input)
        lates[index] = int(lates_input)

        # Clear old graph
        ax.cla()

        # Draft graph
        ax.plot(
            days,
            lates,
            marker="o",
            linestyle="-",
            color="blue",
            linewidth=2
        )

        ax.set_title("Late Attendance Per Day", fontsize=14, fontweight="bold")
        ax.set_xlabel("Day")
        ax.set_ylabel("Number of Lates")

        ax.grid(True, linestyle="--", alpha=0.6)

        ax.set_ylim(0, max(lates) + 2)

        # Clear old graph display
        document.getElementById("output").innerHTML = ""

        # Show new graph
        display(fig, target="output")