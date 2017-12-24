  '-----------------------------------------------------------------------------------------
'name                     : servo DIY Driver
'copyright                : Bartosz Scencelek Bartcam
'micro                    : attiny44
'commercial use           : no
'-----------------------------------------------------------------------------------------

$regfile = "attiny44.dat"                                   ' specify the used micro
$crystal = 8000000                                          ' used crystal frequency

'The following is just pinout information
'Port      Pin     Function Used
'PB0       2       Output     Motor 1 Fwd
'PB1       3       Output     Motor 1 Rev
'PB2       5       OC0A       PWM Motor 1
'PB3       4       Reset
'PA0       13      Output     Motor 2 Rev
'PA1       12      ADC1       Motor 1 Position
'PA2       11      ACD2       Motor 2 Position
'PA3       10      Output     Motor 2 Fwd
'PA4       9       SCL/Ref1   I2C Communications
'PA5       8       Input      Control Mode
'PA6       7       SDA/Ref2   I2C Communications
'PA7       6       OC0B       PWM Motor 2
'############################################
' Just a note on the Control Mode
'
' When set to VCC we will use the PA4 and PA6
' as I2C communications
'
' When set to Gnd    We will use the PA4 and PA6
' as PWM inputs for Ref1 and Ref2
'
' When set to 2.5V or ADC 512 we will use PA4 and PA6
' as Analog inputs for Ref1 and Ref2
'############################################
Dim Pot1 As Single                                          'Current Average position value Motor 1
Dim Pot2 As Single                                          'Current Average position value Motor 2
Dim Ref1 As Single                                          'Motor 1 Target Position
Dim Ref2 As Single                                          'Motor 2 Target Position
Dim Refcount1 As Word
Dim Refcount2 As Word
Dim Err1 As Single
Dim Err2 As Single
Dim Integral1 As Single
Dim Integral2 As Single
Dim Derivative1 As Single
Dim Derivative2 As Single
Dim Preverr1 As Single
Dim Preverr2 As Single
Dim Output1 As Single
Dim Output2 As Single
Dim Kp1 As Single
Dim Ki1 As Single
Dim Kd1 As Single
Dim Kp2 As Single
Dim Ki2 As Single
Dim Kd2 As Single
Dim Deadband1 As Single                                     'Motor 1 DeadBand
Dim Deadband2 As Single                                     'Motor 2 DeadBand
Dim Filter As Single                                        'Filtering Value
Dim Filter2 As Single
'Dim Temp As String * 10
Dim Temp2 As Single
Dim Temp3 As Word
Dim Dt As Single
Dim Controltype As Bit
Dim Pwm_control As Byte

On Pcint0 Chint Save
On Oc1a Pwmint Save

Config Portb.0 = Output                                     'Motor1 Fwd
Config Portb.1 = Output                                     'Motor1 Rev
Config Portb.2 = Output                                     'Motor1 PWM
Config Porta.0 = Output                                     'Motor2 Rev
Config Porta.3 = Output                                     'Motor2 Fwd
Config Porta.7 = Output                                     'Motor2 PWM
Config Porta.5 = Input                                      'input Mode "Cotrol"

Config Adc = Single , Prescaler = 2
Config Timer0 = Pwm , Compare_a_pwm = Clear_up , Compare_b_pwm = Clear_up , Prescale = 8
Config Timer1 = Timer , Compare_a = Disconnect , Compare_b = Disconnect , Prescale = 8

Enable Interrupts

Ocr0b = 0                                                   'Motor1 Power
Ocr0a = 0                                                   'Motor2 Power
' the OCR1A (Output Compare Register 1 A) is used to generate an interruput every
' 20 mS which is the pulse period of most PWM controlled servos.
' Since this controller will be working as a servo driver, we need to use
' the same timings.
' 20mS periods occure 50 times per second
' With a system clock of 8000000 cycles persecond, 160000 cycles will elapse each period.
' Timer/Counter 1 can coun up to 65535 before it over runs, so we need to use a prescaler
' of at least 2.441 times. This of course does not exist, so the next lowest available
' is 8 time. Soo if we take 8000000/8 gives us 1000000. we divide that by our 50 times
' per second, we get 20000, which is below the max of 65535, so we set the OCR1A to 20000
' if a PWM pulse exceeds the 20 mS, then we will set the ref to the current pos.
Ocr1a = 20000                                               'PWM input Timer

Reset Portb.0                                               'Motor1 Fwd
Reset Portb.1                                               'Motor1 Rev
Reset Porta.0                                               'Motor2 Rev
Reset Porta.3                                               'Motor2 Fwd
Controltype = Porta.5


Start Timer0                                                'PWM Output Timer

If Controltype = 1 Then                                     'This section for PWM Input
   Set Pcie0
   Enable Oc1a
   Start Timer1
   Tcnt1 = 0
   Pwm_control = 0
   Set Pcint4
End If

Ref1 = 512
Ref2 = 512
Integral1 = 0
Integral2 = 0
Kp1 = 0.1
Ki1 = 0.1
Kd1 = 0
Deadband1 = 5
Deadband2 = 5
Filter = 5                                                  ' Set the filter to 5 Cycles
Filter2 = Filter + 1
Dt = 0.00173
Waitms 200



Do

'*************** Motor Feed Back with Filtering *************
' By taking the existing pot value and multiplying it by Filter
' then adding the raw pot value and deviding the total by Filter + 1
' We end up with a sudo average taken over filter cycles through the program
' The best part of this method of averaging is it is fast and doen't
' used much memory, the down side is it can take a long time for the average
' to match the raw when the raw is not moving.
    Temp3 = Getadc(1)
    Temp2 = Temp3
    Pot1 = Pot1 * Filter
    Pot1 = Pot1 + Temp2
    Pot1 = Pot1 / Filter2

    Temp3 = Getadc(2)
    Temp2 = Temp3
    Pot2 = Pot2 * Filter
    Pot2 = Pot2 + Temp2
    Pot2 = Pot2 / Filter2

'############################################################
' Control Method 2 Analog input control.
'############################################################
    If Controltype = 0 Then                                 ' Analog Input Control
         Temp3 = Getadc(4)
         Temp2 = Temp3
         Ref1 = Ref1 * Filter
         Ref1 = Ref1 + Temp2
         Ref1 = Ref1 / Filter2

         Temp3 = Getadc(6)
         Temp2 = Temp3
         Ref2 = Ref2 * Filter
         Ref2 = Ref2 + Temp2
         Ref2 = Ref2 / Filter2
    Else                                                    ' PWM input Control
         If Refcount1 < 1000 Or Refcount1 > 2000 Then       ' if the Refcount is not in range
            Ref1 = Pot1                                     'set the Ref to be equal to the current position
         Else
            Temp3 = Refcount1 - 988
            Ref1 = Temp3
         End If
         If Refcount2 < 1000 Or Refcount2 > 2000 Then
            Ref2 = Pot2
         Else
            Temp3 = Refcount2 - 988
            Ref2 = Temp3
         End If
    End If

'############################################################
' PID Loop to calculate the output value from the Input Error
'############################################################

    Err1 = Ref1 - Pot1
    Temp2 = Err1 * Dt
    Integral1 = Integral1 + Temp2
    Temp2 = Err1 - Preverr1
    Derivative1 = Temp2 / Dt
    Derivative1 = Derivative1 * Kd1
    Temp2 = Integral1 * Ki1
    Output1 = Kp1 * Err1
    Output1 = Output1 + Temp2
    Output1 = Output1 + Derivative1
    Preverr1 = Err1
    If Output1 > 255 Then
         Output1 = 255
    Elseif Output1 < -255 Then
         Output1 = -255
    End If

    Err2 = Ref2 - Pot2
    Temp2 = Err2 * Dt
    Integral2 = Integral2 + Temp2
    Temp2 = Err2 - Preverr2
    Derivative2 = Temp2 / Dt
    Derivative2 = Derivative2 * Kd2
    Temp2 = Integral2 * Ki2
    Output2 = Kp2 * Err2
    Output2 = Output2 + Temp2
    Output2 = Output2 + Derivative2
    Preverr2 = Err2

'############################################################
' Drive the Motor Output and PWM signal.
'############################################################
    If Output1 > Deadband1 Then                             ' Is the motor to far along
         Set Portb.0                                        ' Turn on the Fwd output
         Reset Portb.1                                      ' Turn off the Rev output
         Ocr0a = Output1                                    ' Set the PWM to Output
    Else
      Output1 = Output1 * -1
      If Output1 > Deadband1 Then                           ' Is the motor not far enough along
         Reset Portb.0                                      ' Turn off the Fwd output
         Set Portb.1                                        ' Turn on the Rev output
         Ocr0a = Output1                                    ' Set the PWM to Output
      Else
         Reset Portb.0                                      ' Turn off the Fwd output
         Reset Portb.1                                      ' Turn off the Rev output
         Ocr0a = 0                                          ' Turn Off the PWM
      End If
    End If

    If Output2 > Deadband2 Then                             ' Is the motor to far along
         Set Porta.3                                        ' Turn on the Fwd output
         Reset Porta.0                                      ' Turn off the Rev output
         Ocr0b = Output2                                    ' Set the PWM to Output
    Else
      Output2 = Output2 * -1
      If Output2 > Deadband2 Then                           ' Is the motor not far enough along
         Reset Porta.3                                      ' Turn off the Fwd output
         Set Porta.0                                        ' Turn on the Rev output
         Ocr0b = Output2                                    ' Set the PWM to Output
      Else
         Reset Porta.3                                      ' Turn off the Fwd output
         Reset Porta.0                                      ' Turn off the Rev output
         Ocr0b = 0                                          ' Turn Off the PWM
      End If
    End If


Loop

Chint:
   If Pwm_control = 0 Then
      If Porta.4 = 0 Then
         Tcnt1 = 0
         Pwm_control = 1
      End If
   Elseif Pwm_control = 1 Then
      If Porta.4 = 1 Then
         Refcount1 = Tcnt1
         Tcnt1 = 0
         Reset Pcmsk0.4
         Set Pcint6
         Pwm_control = 2
      End If
   Elseif Pwm_control = 2 Then
      If Porta.6 = 0 Then
         Tcnt1 = 0
         Pwm_control = 3
      End If
   Elseif Pwm_control = 3 Then
      If Porta.4 = 1 Then
         Refcount2 = Tcnt1
         Tcnt1 = 0
         Reset Pcmsk0.6
         Set Pcint4
         Pwm_control = 0
      End If
   End If
Return


Pwmint:
   If Pwm_control = 0 Or Pwm_control = 1 Then
      Reset Pcmsk0.4
      Set Pcint6
      Pwm_control = 2
      Refcount1 = 0
      Tcnt1 = 0
   Elseif Pwm_control = 2 Or Pwm_control = 3 Then
      Reset Pcmsk0.6
      Set Pcint4
      Pwm_control = 0
      Refcount2 = 0
      Tcnt1 = 0
   End If
Return
