import random
import pandas as pd

# Define sample data options with realistic probabilities
genres = ["Rock", "Jazz", "Pop", "EDM", "Classical", "Blues", "Hip-Hop", "Folk", "Reggae", "Metal"]
instruments = ["Guitar", "Drums", "Piano", "Bass", "Violin", "Trumpet", "Saxophone", "Synthesizer", "Flute", "Cello"]
roles = ["Singer", "Composer", "Producer", "Sound Engineer", "Lyricist", "Multi-Instrumentalist"]
skill_levels = ["Beginner", "Intermediate", "Advanced", "Professional"]
collab_types = ["Live Performance", "Studio Recording", "Remote Collaboration", "Virtual Jam Session"]
languages = ["English", "Spanish", "French", "German", "Italian", "Japanese", "Portuguese"]

# Realistic probability distributions
genre_prob = [0.25, 0.15, 0.18, 0.12, 0.1, 0.08, 0.07, 0.04, 0.03, 0.03]
instrument_prob = [0.3, 0.2, 0.15, 0.1, 0.08, 0.07, 0.05, 0.03, 0.02, 0.02]
role_prob = [0.35, 0.2, 0.15, 0.15, 0.1, 0.05]
skill_prob = [0.1, 0.35, 0.4, 0.15]
collab_prob = [0.5, 0.3, 0.15, 0.05]

# Realistic names for musicians
first_names = ["James", "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "Benjamin", "Isabella"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Realistic city names
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco", "Seattle", "Boston", "Austin", "Denver"]

# Generate musician data
num_musicians = 500
musicians = []
used_ids = set()

for i in range(num_musicians):
    while True:
        user_id = f"MUS{random.randint(1000, 9999)}"
        if user_id not in used_ids:
            used_ids.add(user_id)
            break

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    musician = {
        "user_id": user_id,
        "name": name,
        "location": random.choice(cities),
        "genre_preferences": random.choices(genres, genre_prob, k=random.randint(1, 3)),
        "instruments": random.choices(instruments, instrument_prob, k=random.randint(1, 2)),
        "primary_role": random.choices(roles, role_prob, k=1)[0],
        "skill_level": random.choices(skill_levels, skill_prob, k=1)[0],
        "years_of_experience": random.randint(1, 30),
        "languages": random.sample(languages, k=random.randint(1, 3)),
        "activity": {
            "last_login": f"2025-02-{random.randint(1, 28)}",
            "total_projects_created": random.randint(1, 50),
            "songs_uploaded": random.randint(1, 100),
            "profile_views": random.randint(10, 5000)
        },
        "ratings_feedback": {
            "average_collaboration_rating": round(random.uniform(3.0, 5.0), 1),
            "reviews": [f"Review {random.randint(1, 100)}" for _ in range(random.randint(1, 3))]
        },
        "privacy_settings": {
            "data_consent": random.choice([True, False]),
            "profile_visibility": random.choice(["Public", "Private"])
        }
    }
    musicians.append(musician)

# Generate collaboration history
collaborations = []
for _ in range(num_musicians * 2):
    musician_a = random.choice(musicians)
    musician_b = random.choice(musicians)
    
    if musician_a["user_id"] != musician_b["user_id"]:
        collab = {
            "musician_id_a": musician_a["user_id"],
            "musician_id_b": musician_b["user_id"],
            "collaboration_type": random.choices(collab_types, collab_prob, k=1)[0],
            "project_genre": random.choice(musician_a["genre_preferences"]),
            "collaboration_rating": round(random.uniform(3.0, 5.0), 1)
        }
        collaborations.append(collab)

# Convert to DataFrame
musician_df = pd.DataFrame(musicians)
collaboration_df = pd.DataFrame(collaborations)

# Save as CSV
musician_df.to_csv("musicians_data.csv", index=False)
collaboration_df.to_csv("collaborations_data.csv", index=False)

print("🎵 Musician Dataset Generated! Files saved as CSV.")
