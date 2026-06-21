# Import tkinter for GUI
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set title, size and background color
root.title("calendar")
root.geometry("420x360")
root.configure(bg="lightpink")


# Optional label for friend's name
"""
label = tk.Label(
    root,
    text="Gay",
    font=("Arial",50,"bold"),
    bg="lightpink",
    fg="hotpink"
)
label.place(relx=0.5,rely=0.5,anchor="center")
"""


# Import modules for calendar and current date
import calendar
from datetime import datetime

# Get today's date
today = datetime.now()

# Store current month and year
month = today.month
year = today.year


# Create a header frame for buttons and month label
header = tk.Frame(root, bg="pink")
header.pack(pady=10)


# Label that displays current month and year
month_label = tk.Label(
    header,
    text="",
    font=("Arial",18),
    bg="hot pink",
    fg="white"
)
month_label.grid(row=0, column=1, padx=20)


# Frame that will contain the calendar
calendar_frame = tk.Frame(root, bg="#ffd8f0")
calendar_frame.pack()


# Function that draws and refreshes the calendar
def draw_calendar():

    # Update month name at the top
    month_label.config(
        text=f"{calendar.month_name[month]} {year}"
    )

    # Remove old calendar widgets before redrawing
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    # Weekday names
    day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    # Create weekday labels
    for col, day in enumerate(day):
        tk.Label(
            calendar_frame,
            text=day,
            width=4,
            height=2,
            bg="hot pink",
            fg="white",
            font=("Arial",11)
        ).grid(row=0, column=col, padx=1, pady=1)

    # Generate calendar data for selected month
    month_days = calendar.monthcalendar(year, month)

    # Create labels for every date
    for row, week in enumerate(month_days, start=1):
        for col, day in enumerate(week):

            # Default date color
            bg_colour = "#fff0f5"

            # Highlight today's date
            if (
                day == today.day and
                month == today.month and
                year == today.year
            ):
                bg_colour = "deep pink"

            # Empty spaces stay blank
            text = "" if day == 0 else str(day)

            # Create date label
            tk.Label(
                calendar_frame,
                text=text,
                width=4,
                height=2,
                bg=bg_colour,
                font=("Arial",11)
            ).grid(
                row=row,
                column=col,
                padx=1,
                pady=1
            )


# Function to move to previous month
def previous_month():

    global month, year

    month -= 1

    # Move to previous year if needed
    if month < 1:
        month = 12
        year -= 1

    # Refresh calendar
    draw_calendar()


# Function to move to next month
def next_month():

    global month, year

    month += 1

    # Move to next year if needed
    if month > 12:
        month = 1
        year += 1

    # Refresh calendar
    draw_calendar()


# Left navigation button
left_btn = tk.Button(
    header,
    text="◀",
    command=previous_month,
    bg="hot pink",
    fg="white",
    font=("Arial",12),
    width=3
)
left_btn.grid(row=0, column=0)


# Right navigation button
right_btn = tk.Button(
    header,
    text="▶",
    command=next_month,
    bg="hot pink",
    fg="white",
    font=("Arial",12),
    width=3
)
right_btn.grid(row=0, column=2)


# Draw calendar when program starts
draw_calendar()


# Keep window running
root.mainloop()

# End