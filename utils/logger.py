from datetime import datetime

class Logger:
    """Static and unique class to handle logging operations"""

    logpath = "./logs"
    logfile: str = 'user_cmds.log'
    default_time_fmt: str = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def get_current_timestamp(cls) -> str:
        """Get the current timestamp formatted"""
        now = datetime.now()
        now_str_formatted = now.strftime(cls.default_time_fmt)
        return ("[" + now_str_formatted + "]:")

    @classmethod
    def log_add(cls, movie, user) -> None:
        """Opens logfile and log film addition data"""
        current_timestamp = cls.get_current_timestamp()        
        with open(cls.logfile, 'a') as f:
            f.write(f"{current_timestamp} Filme '{movie}' ADICIONADO por '{user}'\n")
    
    @classmethod
    def log_delete(cls, movie, user) -> None:
        """Opens logfile and log film deletion data"""
        current_timestamp = cls.get_current_timestamp()
        with open(cls.logfile, 'a') as f:
            f.write(f"{current_timestamp} Filme '{movie}' REMOVIDO por '{user}'\n")
    
