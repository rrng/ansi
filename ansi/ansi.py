class Ansi:
    ResetAll   = "\033[0m"

    Bold       = "\033[1m"
    Dim        = "\033[2m"
    Underlined = "\033[4m"
    Blink      = "\033[5m"
    Invert     = "\033[7m"
    Hidden     = "\033[8m"

    ResetBold       = "\033[21m"
    ResetDim        = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink      = "\033[25m"
    ResetInvert     = "\033[27m"
    ResetHidden     = "\033[28m"

    Default       = "\033[39m"
    Black         = "\033[30m"
    Red           = "\033[31m"
    Green         = "\033[32m"
    Yellow        = "\033[33m"
    Blue          = "\033[34m"
    Magenta       = "\033[35m"
    Cyan          = "\033[36m"
    BrightGray    = "\033[37m"
    DarkGray      = "\033[90m"
    BrightRed     = "\033[91m"
    BrightGreen   = "\033[92m"
    BrightYellow  = "\033[93m"
    BrightBlue    = "\033[94m"
    BrightMagenta = "\033[95m"
    BrightCyan    = "\033[96m"
    White         = "\033[97m"

    BackgroundDefault       = "\033[49m"
    BackgroundBlack         = "\033[40m"
    BackgroundRed           = "\033[41m"
    BackgroundGreen         = "\033[42m"
    BackgroundYellow        = "\033[43m"
    BackgroundBlue          = "\033[44m"
    BackgroundMagenta       = "\033[45m"
    BackgroundCyan          = "\033[46m"
    BackgroundBrightGray    = "\033[47m"
    BackgroundDarkGray      = "\033[100m"
    BackgroundBrightRed     = "\033[101m"
    BackgroundBrightGreen   = "\033[102m"
    BackgroundBrightYellow  = "\033[103m"
    BackgroundBrightBlue    = "\033[104m"
    BackgroundBrightMagenta = "\033[105m"
    BackgroundBrightCyan    = "\033[106m"
    BackgroundWhite         = "\033[107m"


rainbow = [
    Ansi.Red,
    Ansi.Yellow,
    Ansi.Green,
    Ansi.Cyan,
    Ansi.Blue,
    Ansi.Magenta
]
rainbow_bright = [
    Ansi.BrightRed,
    Ansi.BrightYellow,
    Ansi.BrightGreen,
    Ansi.BrightCyan,
    Ansi.BrightBlue,
    Ansi.BrightMagenta
]

if __name__ == "__main__":
    text = "Sphinx of black quartz, judge my vow!"
    color_schemes = [rainbow, rainbow_bright]
    for scheme in color_schemes:
        colored_letters = []
        for i in range(len(text)):
            colored_letters.append(scheme[i % len(scheme)] + text[i])
        colored_letters.append(Ansi.ResetAll)
        print("".join(colored_letters))
