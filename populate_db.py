import os
import django
import random
import requests
from faker import Faker
from django.utils import timezone
from django.core.files.base import ContentFile
from datetime import time
from app1.models import Category, Event, Participant

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
django.setup()

# Initialize Faker
fake = Faker()

# Placeholder image source
IMAGE_SOURCE = "https://placeimg.com/400/300/any"

def fetch_image():
    """Fetch a random image from a placeholder source."""
    try:
        response = requests.get(IMAGE_SOURCE, timeout=5)
        response.raise_for_status()
        return response.content
    except requests.RequestException:
        print("Error downloading image, skipping...")
        return None

def populate_db():
    """Function to populate the database with sample data."""

    # Create Categories (Ensuring Uniqueness)
    categories = []
    for _ in range(10):
        name = fake.unique.word().capitalize()
        category = Category.objects.create(
            name=name,
            description=fake.paragraph()
        )
        categories.append(category)
    print(f"Created {len(categories)} categories.")

    # Create Events
    events = []
    for _ in range(50):
        event_date = fake.date_this_year()
        event_time = time(hour=random.randint(0, 23), minute=random.randint(0, 59))

        event = Event.objects.create(
            name=fake.sentence(nb_words=3),
            description=fake.paragraph(),
            date=event_date,
            time=event_time,
            location=fake.city(),
            category=random.choice(categories),
            status=random.choice(['ongoing', 'completed', 'upcoming'])
        )

        # Assign an image (optional)
        image_content = fetch_image()
        if image_content:
            event.image.save(f"event_{event.id}.jpg", ContentFile(image_content), save=True)

        events.append(event)
    print(f"Created {len(events)} events.")

    # Create Participants
    participants = []
    for _ in range(100):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number()[:15],
            event=random.choice(events)
        )
        participants.append(participant)
    print(f"Created {len(participants)} participants.")

    print("Database populated successfully!")

# Run the script
if __name__ == "__main__":
    populate_db()

    
    
  
  
  