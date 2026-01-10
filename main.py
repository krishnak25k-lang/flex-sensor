import machine
import utime

# Initialize ADC pins
s1 = machine.ADC(26)
s2 = machine.ADC(27)
s3 = machine.ADC(28)

def get_smoothed_value(adc_pin, samples=10):
    total = 0
    for _ in range(samples):
        total += adc_pin.read_u16()
    return total // samples  # Return the average

while True:
    # Get averaged readings to stop the jumping
    val1 = get_smoothed_value(s1)
    val2 = get_smoothed_value(s2)
    val3 = get_smoothed_value(s3)
    
    # Print the clean values
    print(f"{val1},{val2},{val3}")
    
    utime.sleep(0.05)