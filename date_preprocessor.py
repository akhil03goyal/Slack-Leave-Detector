from datetime import datetime, timedelta
import re

def resolve_date(date_text):
    today = datetime.today()
    date_text = date_text.lower().strip()

    # Handle "today" and "tomorrow"
    relative_days = {
        "today": today,
        "tomorrow": today + timedelta(days=1),
    }

    if date_text in relative_days:
        return relative_days[date_text].strftime("%Y-%m-%d")

    # Handle "next Wednesday"
    match = re.search(r"next (monday|tuesday|wednesday|thursday|friday|saturday|sunday)", date_text)
    if match:
        target_day = match.group(1)
        weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        target_index = weekdays.index(target_day)
        days_ahead = (target_index - today.weekday() + 7) % 7 + 7  # Ensure it's the *next* occurrence
        return (today + timedelta(days=days_ahead)).strftime("%Y-%m-%d")

    # Handle single weekday ("Monday", "Friday", etc.)
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if date_text in weekdays:
        target_index = weekdays.index(date_text)
        days_ahead = (target_index - today.weekday() + 7) % 7 or 7
        return (today + timedelta(days=days_ahead)).strftime("%Y-%m-%d")

    # Handle date formats like "12 April" or "April 5"
    date_patterns = [
        r"(\d{1,2})\s*(January|February|March|April|May|June|July|August|September|October|November|December)",  # "12 April"
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s*(\d{1,2})",  # "April 5"
    ]

    for pattern in date_patterns:
        match = re.search(pattern, date_text, re.IGNORECASE)
        if match:
            day, month = match.groups() if match.lastindex == 2 else match[::-1]
            formatted_date = f"{day} {month} {today.year}"
            parsed_date = datetime.strptime(formatted_date, "%d %B %Y")
            return parsed_date.strftime("%Y-%m-%d")

    return date_text  # If no match, return original text
