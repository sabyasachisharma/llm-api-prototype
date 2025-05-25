from faker import Faker
from datetime import datetime, timedelta
from typing import List
from .models import MockDataSchema

fake = Faker()

SUBJECTS = [
    "Consumer Behavior",
    "Digital Markets",
    "E-Commerce",
    "Social Media",
    "Mobile Usage",
    "Retail",
    "Healthcare",
    "Financial Services",
    "Technology",
    "Entertainment"
]

def generate_mock_data(count: int = 100) -> List[MockDataSchema]:
    data = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    for i in range(count):
        subject = fake.random_element(SUBJECTS)
        title = f"{subject} Statistics: {fake.catch_phrase()}"
        
        data.append(
            MockDataSchema(
                id=i + 1,
                title=title,
                subject=subject,
                description=fake.paragraph(nb_sentences=3),
                link=f"https://www.statista.com/statistics/{fake.uuid4()}/",
                date=fake.date_time_between(start_date=start_date, end_date=end_date)
            )
        )
    
    return data

# Generate and store mock data
mock_database = generate_mock_data() 