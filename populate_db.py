# # import os
# # import django
# # from faker import Faker
# # import random
# # from app1.models import Category, Event, Participant

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
# # django.setup()

# # # Function to populate the database


# # def populate_db():
# #     # Initialize Faker
# #     fake = Faker()


# #     # Create Category
# #     category = [Category.objects.create(
# #         name=fake.name(),
# #         description=fake.paragraph()
# #     ) for _ in range(10)]
# #     print(f"Created {len(category)}.")

# #     # Create Participant
# #     participant = []
# #     for _ in range(20):
# #         task = Participant.objects.create(
# #             name=fake.name(),
# #             email=fake.email(),
# #             phone=fake.phone_number(),
# #             event=random.choice(events)  # Assign a random event to each participant
# #         )
# #     print(f"Created {len(participant)}.")

# #     # Create Event
# #     events = [Event.objects.create(
# #         name=fake.bs().capitalize(),
# #         description=fake.paragraph(),
# #         date=fake.date_this_year(),
# #         time=fake.time(),
# #         location=fake.city(),
# #         category=random.choice(category)  # Assign a random category to each event
# #     ) for _ in range(5)]
# #     print(f"Created {len(events)} projects.")
# #     print("Populated Event for all Participant.")
# #     print("Database populated successfully!")








# # import os
# # import django
# # from faker import Faker
# # import random
# # from app1.models import Category, Event, Participant

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
# # django.setup()

# # # Function to populate the database
# # def populate_db():
# #     fake = Faker()

# #     # Create Categories
# #     categories = [Category.objects.create(
# #         name=fake.word().capitalize(),
# #         description=fake.paragraph()
# #     ) for _ in range(10)]
# #     print(f"Created {len(categories)} categories.")

# #     # Create Events (MUST come before Participants)
# #     events = [Event.objects.create(
# #         name=fake.bs().capitalize(),
# #         description=fake.paragraph(),
# #         date=fake.date_this_year(),
# #         time=fake.time(),
# #         location=fake.city(),
# #         category=random.choice(categories)  # Assign a random category
# #     ) for _ in range(5)]
# #     print(f"Created {len(events)} events.")

# #     # Create Participants (AFTER Events exist)
# #     participants = [Participant.objects.create(
# #         name=fake.word().capitalize()[:100],
# #         email=fake.email(),
# #         phone=fake.phone_number()[:15],
# #         event=random.choice(events)  # Assign a random event
# #     ) for _ in range(20)]
# #     print(f"Created {len(participants)} participants.")

# #     print("Database populated successfully!")

# # # Run the function
# # if __name__ == "__main__":
# #     populate_db()








# # import os
# # import django
# # from faker import Faker
# # import random
# # from app1.models import Category, Event, Participant

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
# # django.setup()

# # # Function to populate the database
# # def populate_db():
# #     fake = Faker()

# #     # Create Categories (ensure uniqueness)
# #     category_names = set()
# #     categories = []

# #     while len(categories) < 10:
# #         name = fake.word().capitalize()
# #         if name not in category_names:
# #             category, created = Category.objects.get_or_create(
# #                 name=name,
# #                 defaults={'description': fake.paragraph()}
# #             )
# #             if created:  # Add only if it's newly created
# #                 categories.append(category)
# #                 category_names.add(name)

# #     print(f"Created {len(categories)} categories.")

# #     # Create Events
# #     events = [Event.objects.create(
# #         name=fake.bs().capitalize(),
# #         description=fake.paragraph(),
# #         date=fake.date_this_year(),
# #         time=fake.time(),
# #         location=fake.city(),
# #         category=random.choice(categories)  # Assign a random category
# #     ) for _ in range(10)]

# #     print(f"Created {len(events)} events.")

# #     # Create Participants
# #     participants = [Participant.objects.create(
# #         name=fake.name()[:100],  # Fix: Use full name instead of a single word
# #         email=fake.email(),
# #         phone=fake.phone_number()[:15],
# #         event=random.choice(events)  # Assign a random event
# #     ) for _ in range(20)]

# #     print(f"Created {len(participants)} participants.")

# #     print("Database populated successfully!")

# # # Run the function
# # if __name__ == "__main__":
# #     populate_db()







# # import os
# # import django
# # from faker import Faker
# # import random
# # from app1.models import Category, Event, Participant

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
# # django.setup()

# # # Function to populate the database
# # def populate_db():
# #     fake = Faker()

# #     # Create Categories (ensure uniqueness)
# #     category_names = set()
# #     categories = []

# #     while len(categories) < 10:
# #         name = fake.word().capitalize()
# #         if name not in category_names:
# #             category, created = Category.objects.get_or_create(
# #                 name=name,
# #                 defaults={'description': fake.paragraph()}
# #             )
# #             if created:  # Add only if it's newly created
# #                 categories.append(category)
# #                 category_names.add(name)

# #     print(f"Created {len(categories)} categories.")

# #     # Create Events
# #     events = [Event.objects.create(
# #         name=fake.bs().capitalize(),
# #         description=fake.paragraph(),
# #         date=fake.date_this_year(),
# #         time=fake.time(),
# #         location=fake.city(),
# #         category=random.choice(categories)  # Assign a random category
# #     ) for _ in range(10)]

# #     print(f"Created {len(events)} events.")

# #     # Create Participants
# #     participants = [Participant.objects.create(
# #         name=fake.name()[:100],  # Fix: Use full name instead of a single word
# #         email=fake.email(),
# #         phone=fake.phone_number()[:15],
# #         event=random.choice(events)  # Assign a random event
# #     ) for _ in range(20)]

# #     print(f"Created {len(participants)} participants.")

# #     print("Database populated successfully!")

# # # Run the function
# # if __name__ == "__main__":
# #     populate_db()









# # import os
# # import django
# # from faker import Faker
# # import random
# # from app1.models import Category, Event, Participant
# # from django.utils import timezone
# # from datetime import time
# # from django.core.files.base import ContentFile
# # import requests  # Import requests to download images

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
# # django.setup()

# # # Function to populate the database
# # def populate_db():
# #     fake = Faker()

# #     # Create Categories (ensure uniqueness)
# #     category_names = set()
# #     categories = []

# #     while len(categories) < 10:
# #         name = fake.word().capitalize()
# #         if name not in category_names:
# #             category, created = Category.objects.get_or_create(
# #                 name=name,
# #                 defaults={'description': fake.paragraph()}
# #             )
# #             if created:
# #                 categories.append(category)
# #                 category_names.add(name)

# #     print(f"Created {len(categories)} categories.")

# #     # Create Events
# #     events = []
# #     for _ in range(10):
# #         event_date = fake.date_time_this_year(tzinfo=timezone.get_current_timezone())
# #         event_time = time(hour=random.randint(0, 23), minute=random.randint(0, 59))

# #         event = Event.objects.create(
# #             name=fake.bs().capitalize(),
# #             description=fake.paragraph(),
# #             date=event_date,
# #             time=event_time,
# #             location=fake.city(),
# #             category=random.choice(categories),
# #         )

# #         # Download a random image from a placeholder service or your own source
# #         image_url = f"https://source.unsplash.com/random/400x300/?event,{fake.word()}" #Example using unsplash, you can use lorempixel or your own source
# #         try:
# #             response = requests.get(image_url, stream=True)
# #             response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

# #             if response.status_code == 200:
# #                 event.image.save(f"random_event_image_{_}.jpg", ContentFile(response.content), save=True)
# #         except requests.exceptions.RequestException as e:
# #             print(f"Error downloading image: {e}")

# #         events.append(event)

# #     print(f"Created {len(events)} events.")

# #     # Create Participants
# #     participants = [Participant.objects.create(
# #         name=fake.name()[:100],
# #         email=fake.email(),
# #         phone=fake.phone_number()[:15],
# #         event=random.choice(events)
# #     ) for _ in range(20)]

# #     print(f"Created {len(participants)} participants.")

# #     print("Database populated successfully!")

# # # Run the function
# # if __name__ == "__main__":
# #     populate_db()
    
    
    
    
    
    
    
 
    
    
    
    
    
    
    
    
    
# import os
# import django
# from faker import Faker
# import random
# from app1.models import Category, Event, Participant
# from django.utils import timezone
# from datetime import time
# from django.core.files.base import ContentFile
# import requests
# import sys
# from io import BytesIO

# # UNSPLASH_URL = "https://source.unsplash.com/random/400x300/?event"
# UNSPLASH_URL = "https://placeimg.com/400/300/any"
# # UNSPLASH_IMAGES = [
# #     "https://source.unsplash.com/400x300/?concert",
# #     "https://source.unsplash.com/400x300/?conference",
# #     "https://source.unsplash.com/400x300/?workshop",
# # ]

# # def fetch_image():
# #     try:
# #         url = random.choice(UNSPLASH_IMAGES)
# #         response = requests.get(url, timeout=5)
# #         response.raise_for_status()
# #         return response.content
# #     except requests.RequestException:
# #         return None


# # Set up Django environment
# sys.path.append('E:/Web Development/Django_2/Event Management System') #Add the root directory to the python path
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMSproject.settings')
# django.setup()

# # Function to populate the database
    


# # def fetch_image():
# #     try:
# #         response = requests.get(UNSPLASH_URL, timeout=5)
# #         response.raise_for_status()  # Raise error for 404/500
# #         return response.content
# #     except requests.RequestException:
# #         print("Error downloading image, using default.")
# #         return None  # Use default image

# # def populate_db():
# #     # Creating categories
# #     categories = ["Tech", "Music", "Education", "Health"]
# #     for name in categories:
# #         Category.objects.get_or_create(name=name, description=f"{name} events")

# #     # Creating events
# #     for i in range(10):  # Adjust count as needed
# #         category = Category.objects.order_by("?").first()
# #         event = Event.objects.create(
# #             name=f"Event {i}",
# #             description="This is a sample event.",
# #             date="2025-12-01",
# #             time="18:00",
# #             location="City Hall",
# #             category=category
# #         )

# #         # Fetch and save image
# #         image_content = fetch_image()
# #         if image_content:
# #             event.image.save(f"event_{i}.jpg", ContentFile(image_content), save=True)

# #     print("Database populated successfully!")
# def populate_db():
#     fake = Faker()

#     # Create Categories (ensure uniqueness)
#     categories = [
#         Category.objects.create(
#             name=fake.word().capitalize(),
#             description=fake.paragraph()
#             # image=fetch_image()
#         ) for _ in range(10)
#     ]
#     print(f"Created {len(categories)} categories.")
    
    
    
    
#     # category_names = set()
#     # categories = []
#     # while len(categories) < 10:
#     #     name = fake.word().capitalize()
#     #     if name not in category_names:
#     #         category, created = Category.objects.get_or_create(
#     #             name=name,
#     #             defaults={'description': fake.paragraph()}
#     #         )
#     #         if created:
#     #             categories.append(category)
#     #             category_names.add(name)
#     # print(f"Created {len(categories)} categories.")

#     # Create Events
#     events = [
#         Event.objects.create(
#             name=fake.bs().capitalize(),
#             description=fake.paragraph(),
#             date=fake.date_this_year(),
#             time=fake.time(),
#             location=fake.city(),
#             category=random.choice(categories),
#             status=random.choice(['ongoing', 'completed', 'upcoming']) 
#         ) for _ in range(50)
#     ]
#     print(f"Created {len(events)} events.")
    
#     # for _ in range(50):
#     #     event_date = fake.date_time_this_year(tzinfo=timezone.get_current_timezone())
#     #     event_time = time(hour=random.randint(0, 23), minute=random.randint(0, 59))
#     #     event = Event.objects.create(
#     #         name=fake.bs().capitalize(),
#     #         description=fake.paragraph(),
#     #         date=event_date,
#     #         time=event_time,
#     #         location=fake.city(),
#     #         category=random.choice(categories),
#     #         status=random.choice([choice[0] for choice in Event.EVENT_STATUS_CHOICES]) # add status field
#     #     )
#         # Download a random image from a placeholder service or your own source
#         # image_url = f"https://source.unsplash.com/random/400x300/?event,{fake.word()}"
#     #     image_url = f"https://placeimg.com/400/300/any,{fake.word()}"
#     #     try:
#     #         response = requests.get(image_url, stream=True)
#     #         response.raise_for_status()
#     #         if response.status_code == 200:
#     #             event.image.save(f"random_event_image_{_}.jpg", ContentFile(response.content), save=True)
#     #     except requests.exceptions.RequestException as e:
#     #         print(f"Error downloading image: {e}")
#     #     events.append(event)
#     # print(f"Created {len(events)} events.")

#     # Create Participants
#     participants = []
#     for _ in range(100):
#         participant = Participant.objects.create(
#             name=fake.name()[:100],
#             email=fake.email(),
#             phone=fake.phone_number()[:15],
#             event=random.choice(events)
#         )
#         participants.append(participant)
#     print(f"Created {len(participants)} participants.")
#     print("Database populated successfully!")

# # # Run the function
# # if __name__ == "__main__":
# #     populate_db()
    
    




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

    
    
  
  
  