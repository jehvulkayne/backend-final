# demo_agent_flow.py

from pprint import pprint

# Simulated mock user data from website
mock_user_session = {
    "user_id": "u123",
    "age": 34,
    "gender": "male",
    "location": "San Francisco",
    "interactions": [
        {"page": "homepage", "timestamp": "2025-04-19T09:00:00"},
        {"page": "product_suv", "duration": 40, "clicked": True},
        {"page": "360_view_suv", "duration": 80},
        {"action": "booked_test_drive", "model": "SUV-X", "timestamp": "2025-04-19T09:04:00"}
    ]
}

# Simulated agent behaviors

def data_collector(session):
    print("[Data Collector] Collecting behavioral and demographic data...")
    return {
        "user_id": session["user_id"],
        "demographics": {
            "age": session["age"],
            "gender": session["gender"],
            "location": session["location"]
        },
        "behavior": session["interactions"]
    }

def persona_architect(collected_data):
    print("[Persona Architect] Synthesizing user persona...")
    return {
        "persona_id": collected_data["user_id"],
        "type": "SUV Explorer",
        "needs": ["family space", "modern tech"],
        "preferred_channel": "TikTok",
        "location": collected_data["demographics"]["location"],
        "anonymized_cluster": "Cluster A - West Coast Tech-Savvy"
    }

def meeting_dispatcher(persona, interactions):
    print("[Meeting Dispatcher] Checking for in-person bookings...")
    for entry in interactions:
        if entry.get("action") == "booked_test_drive":
            print("  > Booking found. Sending persona to sales team.")
            return True
    return False

def ad_placer(persona):
    print("[Ad Placer] Selecting TikTok ad for persona...")
    return {
        "ad_id": "tiktok_023",
        "product": "SUV-X",
        "creative_type": "high production",
        "cta": "Book your test drive now",
        "audience_segment": persona["anonymized_cluster"]
    }

def brand_guardian(ad):
    print("[Brand Guardian] Validating brand alignment...")
    if ad["creative_type"] == "high production":
        print("  > Ad passes brand criteria.")
        return True
    else:
        print("  > Ad rejected: inconsistent with brand tone.")
        return False

def fraud_watcher(ad):
    print("[Fraud Watcher] Analyzing traffic source...")
    if ad["ad_id"] == "tiktok_023":
        print("  > No suspicious patterns detected.")
        return "verified"
    return "flagged"

def crm_adapter(persona):
    print("[CRM Adapter] Adapting follow-up journey...")
    return f"Send follow-up email with SUV-X test drive benefits to {persona['persona_id']}"

# === Simulated agent sequence ===

collected = data_collector(mock_user_session)
persona = persona_architect(collected)
dispatched = meeting_dispatcher(persona, collected["behavior"])
ad = ad_placer(persona)
validated = brand_guardian(ad)
fraud_status = fraud_watcher(ad)
crm_followup = crm_adapter(persona)

# === Display final state ===

print("\n--- FINAL OUTPUT ---")
pprint({
    "persona": persona,
    "ad_selected": ad,
    "brand_check": validated,
    "fraud_check": fraud_status,
    "meeting_dispatched": dispatched,
    "crm_followup": crm_followup
})
