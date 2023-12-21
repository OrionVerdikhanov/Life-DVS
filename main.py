import time
import random
from datetime import datetime, timedelta

class EngineLifespanSimulator:
    def __init__(self, total_lifespan_years=3):
        self.total_lifespan = total_lifespan_years * 365
        self.remaining_lifespan = self.total_lifespan

        self.daily_deduction_idle = 1
        self.daily_deduction_running = 3
        self.maintenance_penalty = 5
        self.extreme_weather_penalty = 2

        self.last_maintenance = datetime.now()
        self.maintenance_interval = 30

    def run_day(self, is_running, extreme_weather=False):
        if is_running:
            self.remaining_lifespan -= self.daily_deduction_running
        else:
            self.remaining_lifespan -= self.daily_deduction_idle

        if extreme_weather:
            self.remaining_lifespan -= self.extreme_weather_penalty

        if (datetime.now() - self.last_maintenance).days > self.maintenance_interval:
            self.remaining_lifespan -= self.maintenance_penalty

    def perform_maintenance(self):
        self.last_maintenance = datetime.now()

    def get_remaining_lifespan(self):
        return max(self.remaining_lifespan, 0)

class EngineLifespanSimulatorEnhanced(EngineLifespanSimulator):
    def simulate_days(self, number_of_days):
        for day in range(1, number_of_days + 1):
            is_running = random.choice([True, False])
            extreme_weather = random.choice([True, False])
            temperature = random.randint(-30, 40)

            self.run_day(is_running, extreme_weather)

            print(f"День {day} - температура: {temperature}°C")
            print("ДВС " + ("работает" if is_running else "не работает"))
            maintenance_needed = (datetime.now() - self.last_maintenance).days > self.maintenance_interval
            print("Необходимость в ТО " + ("имеется" if maintenance_needed else "не имеется"))
            print(f"Оставшаяся продолжительность жизни ДВС: {self.get_remaining_lifespan()} дней\n")

            time.sleep(random.uniform(3, 5))

# Создание экземпляра симулятора и запуск симуляции
simulator_enhanced = EngineLifespanSimulatorEnhanced()
simulator_enhanced.simulate_days(10)  # Имитация 10 дней работы
