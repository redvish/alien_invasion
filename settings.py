class Settings:
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализирует статические настройки игры'''
        # Настройки экрана
        self.screen_width = 800
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Настройки снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся в ходе игры'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        '''Увеличивает настройки скорости и стоимость пришельцев'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
