class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Method to set default values
        """
        self.__status = False
        self.__mute = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to set default values
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Method to set default values
        """
        if self.__mute:
            self.__mute = False
        else:
            self.__mute = True

    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase volume
        """
        if self.__status:
            self.__mute = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease volume
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self):
        """
        Method to display values
        """
        if self.__mute:
            return f" Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
