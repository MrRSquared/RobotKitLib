import Led

led=Led.Led()

def Color(red, green, blue, white = 0):
        """COnvert the provided red, green, blue color to a 24 bit color value.
        Each color component should be a value 0-255 where 0 is the lowest intensity
        and 255 is the highest intensity.
        """
        return (white << 24) | (red << 16)|(green << 8)| blue

print ("Rainbow animation")
led.rainbow(led.strip)
led.rainbowCycle(led.strip)
led.colorWipe(led.strip, Color(0,0,0),10)