import random
import json

# Sample data for tags and types
genre = ["action", "adventure", "romance", "fantasy", "comedy", "sci-fi"]
novel_types = ["manga", "manhwa", "comic"]
status_list = ["ongoing", "completed", "dropped"]

# Function to generate a random JSON object for a novel
def generate_novel(title_no):
    return {
        "title": "Title " + str(title_no),
        "description": "Description of the novel.",
        "image_url": "https://example.com/image_" + str(random.randint(1, 100)) + ".jpg",
        "rating": round(random.uniform(0, 5), 2),
        "author": "Author " + str(random.randint(1, 10)),
        "translator": "Translator " + str(random.randint(1, 5)),
        "genre": random.sample(genre, random.randint(1, 3)),
        "status": random.choice(status_list),
        "type": random.choice(novel_types)
    }

# Create an array of 30 novel records
novel_records = [generate_novel(i) for i in range(1, 31)]

print(json.dumps({"batch": novel_records}))
