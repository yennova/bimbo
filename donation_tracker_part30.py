# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: DonationTracker
import json, os, random

class Profile:
    def __init__(self, name, role='donor'):
        self.name = name
        self.role = role
        self.balance = 0.0
        self.donations = []

profiles = {}

def get_profile(name):
    if name not in profiles:
        profiles[name] = Profile(name)
    return profiles[name]
