from app.scheduler import schedule_post
from app.social_media import post_to_social_media, get_analytics, get_content_recommendations

def handle_message(message, sender):
    if message.startswith("schedule"):
        return handle_schedule(message, sender)
    elif message.startswith("analytics"):
        return handle_analytics(message, sender)
    elif message.startswith("recommend"):
        return handle_recommendations(message, sender)
    else:
        return "Command not recognized. Try 'schedule', 'analytics', or 'recommend'."

def handle_schedule(message, sender):
    # Extract details from message and schedule the post
    # Example: schedule <time> <content>
    details = message.split(maxsplit=2)
    time = details[1]
    content = details[2]

    schedule_post(time, content)
    return "Post scheduled successfully."

def handle_analytics(message, sender):
    # Fetch and return analytics data
    data = get_analytics()
    return f"Analytics: {data}"

def handle_recommendations(message, sender):
    # Fetch and return content recommendations
    recommendations = get_content_recommendations()
    return f"Recommendations: {recommendations}"
