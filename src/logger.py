class Logger:
    @staticmethod
    def info(message):
        print(f"{message}")

    @staticmethod
    def error(message):
        print(f"\033[1;31;40m❌ {message}\033[m")

    @staticmethod
    def warning(message):
        print(f"\033[1;33;40m⚠️ {message}\033[m")

    @staticmethod
    def debug(message):
        print(f"\033[1;34;40m{message}\033[m")

    @staticmethod
    def success(message):
        print(f"\033[1;32;40m✅ {message}\033[m")
