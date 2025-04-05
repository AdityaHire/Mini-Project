from django.shortcuts import render
from .models import Medicine, ContactMessage


# Home Page View
def home_page(request):
    return render(request, 'recommend/home.html')

from .models import Medicine



def recommend_medicine(request):
    if request.method == "POST":  # Handle only POST requests
        symptoms = request.POST.get("symptoms", "").lower().split()  # Convert input to lowercase and split words
        recommended_medicines = set()

        # Search for medicines that match any symptom in the "usage" field
        for symptom in symptoms:
            medicines = Medicine.objects.filter(usage__icontains=symptom)
            recommended_medicines.update(medicines)  # Add full objects

        return render(request, "recommend/result.html", {
            "symptoms": ", ".join(symptoms),
            "medicines": recommended_medicines  # Pass full objects
        })

    return render(request, "recommend/recommend.html")


# About Page View
def about_page(request):
    return render(request, 'recommend/about.html')

def contact_page(request):
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to the database
        ContactMessage.objects.create(name=name, email=email, message=message)
        success = True

    return render(request, "recommend/contact.html", {"success": success})
