unsigned char valuereCieved;
void main()
{
    // F= 16 MHz
    // UCSR0A= 0; //flags
    ddrb = 255;
    UCSR0B = 0b00011000; //
    UCSR0C = 0b00000110; //
    UBRR0H = 0;
    UBRR0L = 103; // Buad Rate 9600 BPS
    while (1)
    {
        if (UCSR0A.B7 == 1)
        {
            valuereCieved = UDR0;
            if (valuereCieved == 'f')
            {
                portb.b2 = 1;
                portb.b0 = 0;
                portb.b1 = 1;
                portb.b3 = 0;
                delay_ms(1000);
            }
            else if (valuereCieved == 'b')
            {
                portb.b2 = 0;
                portb.b0 = 1;
                portb.b1 = 0;
                portb.b3 = 1;
                delay_ms(1000);
            }
            else if (valuereCieved == 'l')
            {
                portb.b2 = 1;
                portb.b0 = 0;
                portb.b1 = 0;
                portb.b3 = 1;
                delay_ms(1000);
            }

            else if (valuereCieved == 'r')
            {
                portb.b2 = 0;
                portb.b0 = 1;
                portb.b1 = 1;
                portb.b3 = 0;
                delay_ms(1000);
            }
            else if (valuereCieved == 's')
            {
                portb.b2 = 0;
                portb.b0 = 0;
                portb.b1 = 0;
                portb.b3 = 0;
                delay_ms(1000);
            }
        }
    }
}