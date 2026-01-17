import os
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memory_core.settings')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

def test_create_reviewer():
    print("Starting Reviewer Creation Test...")
    
    # Cleanup previous run
    email = "test_reviewer@memory.com"
    User.objects.filter(email=email).delete()
    
    client = APIClient()
    url = '/auth/reviewer/create'
    data = {
        "username": "test_reviewer",
        "email": email,
        "password": "testpassword123"
    }
    
    print(f"Sending POST request to {url} with data: {data}")
    response = client.post(url, data)
    
    print(f"Response Status: {response.status_code}")
    print(f"Response Data: {response.data}")
    
    if response.status_code == status.HTTP_201_CREATED:
        print("✅ SUCCESS: Responded with 201 Created.")
    else:
        print("❌ FAILED: Did not get 201 Created.")
        exit(1)

    if response.data.get('role') == 'reviewer':
        print("✅ SUCCESS: Role is 'reviewer'.")
    else:
        print(f"❌ FAILED: Role is {response.data.get('role')}, expected 'reviewer'.")
        exit(1)
        
    # Verify DB
    user = User.objects.get(email=email)
    if user.is_active and user.is_verified:
        print("✅ SUCCESS: User is active and verified.")
    else:
        print(f"❌ FAILED: User active={user.is_active}, verified={user.is_verified}")
        exit(1)

if __name__ == "__main__":
    test_create_reviewer()
