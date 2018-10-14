import platform
import os


def default_beep():
    """ Make a beep sound whatever your OS is. """
    print("\a")  # Equivalent to `print("\007")`


def default_beep_windows_positive():
    """ Make a default Windows positive beep sound. """
    import winsound

    winsound.MessageBeep(type=winsound.MB_OK)


def default_beep_windows_negative():
    """ Make a default Windows negative beep sound. """
    import winsound

    winsound.MessageBeep(type=winsound.MB_ICONHAND)


def custom_beep(duration: int, frequence: int):
    """ Make a beep sound with a custom duration and frequence.
    :param duration: The duration of the beep, in milliseconds.
    :param frequence: THe frequence of the beep, in Hertz.
    """
    current_os = platform.system()
    if current_os == "Windows":
        assert 37 <= frequence <= 32767

        import winsound

        winsound.Beep(frequence, duration)
    elif current_os == "Linux":
        duration /= 1000  # GNU/Linux command's duration is in seconds
        os.system("play --no-show-progress --null --channels 1 "
                  "synth %s sine %f" % (duration, frequence))
    else:
        raise NotImplemented("The following platform is currently not supporte"
                             "d: " + current_os)


if __name__ == '__main__':
    pass
