class ConfigurationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigurationManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Ensure initialization only happens once
            self.initialized = True
            self.settings = {}
            self.load_configuration()

    def load_configuration(self):
        # Simulate loading configuration from a file or database
        self.settings = {
            'database': 'postgres://user:password@localhost:5432/mydatabase',
            'debug': True,
            'secret_key': 'supersecretkey'
        }

    def get_setting(self, key):
        return self.settings.get(key)

# Usage
config1 = ConfigurationManager()
config2 = ConfigurationManager()

print(config1.get_setting('database'))  # Output: postgres://user:password@localhost:5432/mydatabase
print(config2.get_setting('database'))
print(config1 is config2)  # Output: True
