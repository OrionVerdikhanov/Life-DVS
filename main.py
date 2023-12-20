from datetime import datetime, timedelta

class EngineLifespanSimulator:
    def __init__(self, total_lifespan_years=3):
        self.total_lifespan = total_lifespan_years * 365
        self.remaining_lifespan = self.total_lifespan

        # Настройки списания жизни
        self.daily_deduction_idle = 1       # Списание, когда двигатель не работает
        self.daily_deduction_running = 3    # Списание, когда двигатель работает
        self.maintenance_penalty = 5        # Штраф за пропуск обслуживания
        self.extreme_weather_penalty = 2    # Штраф за работу в экстремальных условиях

        # Статусы и тайминги
        self.last_maintenance = datetime.now()
        self.maintenance_interval = 30      # Интервал обслуживания в днях

    def run_day(self, is_running, extreme_weather=False):
        # Списание жизни в зависимости от работы двигателя
        if is_running:
            self.remaining_lifespan -= self.daily_deduction_running
        else:
            self.remaining_lifespan -= self.daily_deduction_idle

        # Списание за работу в экстремальных условиях
        if extreme_weather:
            self.remaining_lifespan -= self.extreme_weather_penalty

        # Проверка на пропуск обслуживания
        if (datetime.now() - self.last_maintenance).days > self.maintenance_interval:
            self.remaining_lifespan -= self.maintenance_penalty

    def perform_maintenance(self):
        self.last_maintenance = datetime.now()

    def get_remaining_lifespan(self):
        return max(self.remaining_lifespan, 0)  # Не допускаем отрицательное значение

# Создание экземпляра симулятора
simulator = EngineLifespanSimulator()

# Пример использования: имитация 60 дней работы двигателя
for day in range(60):
    # Допустим, двигатель работает каждый второй день
    is_running = day % 2 == 0
    # Каждые 15 дней - экстремальные погодные условия
    extreme_weather = day % 15 == 0
    simulator.run_day(is_running, extreme_weather)

    # Обслуживание на 30-й день
    if day == 30:
        simulator.perform_maintenance()

# Получение оставшейся продолжительности жизни двигателя
remaining_lifespan = simulator.get_remaining_lifespan()
remaining_lifespan
