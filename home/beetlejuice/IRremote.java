package org.myrobotlab.service;

import java.io.IOException;

import org.myrobotlab.framework.Peers;
import org.myrobotlab.framework.Service;
import org.myrobotlab.logging.Level;
import org.myrobotlab.logging.LoggerFactory;
import org.myrobotlab.logging.Logging;
import org.myrobotlab.logging.LoggingFactory;
import org.slf4j.Logger;

import java.util.concurrent.TimeUnit;

public class IRremote extends Service {

	private static final long serialVersionUID = 1L;

	public final static Logger log = LoggerFactory.getLogger(IRremote.class);
	
	transient public Arduino arduino;
	private int irOutPin = -1; // Must be a PWM pin
	private int irInPin = -1;
	private int ledPin = -1;
	private boolean ledIsConnected = false; // if true, the led blink when irIn receive datas
	private boolean irOutIsConnected = false;
	private boolean irInIsConnected = false;
	private int frequency = 38;
	
	
	public static Peers getPeers(String name) {
		Peers peers = new Peers(name);

		// put peer definitions in
		peers.put("arduino", "Arduino", "arduino");
		return peers;
	}


	@Override
	public void startService() {
		super.startService();

		arduino = (Arduino) startPeer("arduino");
		sleep(200); // Need to wait the service is started ...
		
	}

	/**
	 * Connect the arduino to a COM port and set pins . IrOut pin must be PWM. -1 mean no present
	 * Exemple : connect("COM8", 2, -1)
	 */
	public void attach(String port, int irIn, int irOut) throws IOException {
		if ( irOut > -1) {
			irOutPin = irOut;
			irOutIsConnected = true;
			}
		if ( irIn > -1) {
			irInPin = irIn;
			irInIsConnected = true;
			}
		arduino.connect(port);
		pinsSetup();
	}
	
	
	public void setLed(int led){
		ledPin = led;
		ledIsConnected = true;
		arduino.pinMode(ledPin, "OUTPUT");
	}
	
	public void setFrequency(int hz){
		frequency = hz;
	}
	
	private void pinsSetup(){
		if (irInIsConnected)	{
			arduino.pinMode(irInPin, "INPUT");
			}
		if (irOutIsConnected)	{
			arduino.pinMode(irOutPin, "OUTPUT");
			}
	}
	
	public int getIrInPin(){
		return irInPin;
	}
	
	public int getIrOutPin(){
		return irOutPin;
	}
	
	public int getLedPin(){
		return ledPin;
	}
	
	
	private String hexaToBin(String code){
		int toInt = Integer.valueOf(code ,16);
		return intToBin(toInt);
	}
			
	private String intToBin(int code){
		 String bin = Integer.toBinaryString(code);
		return bin;
	}
	
	private void mark(int period){
		if (irOutIsConnected){
			int time = (int)((1.0 / frequency) * 1000 / 2);
			int currentPeriod = 0;
			while (currentPeriod < period){ 
				try {
					arduino.digitalWrite(irOutPin, 1);
					TimeUnit.MICROSECONDS.sleep(time);
				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				try {
					arduino.digitalWrite(irOutPin, 0);
					TimeUnit.MICROSECONDS.sleep(time);
				} 	catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				currentPeriod += (2 * time);
				System.out.println("currentPeriod" + currentPeriod); // To be sure the loop work . Will be removed when all work well :D
			}
		}
		else{
			System.out.println("ERROR : IR Out Pin isn't connected !");
		}
	}
	
	private void space(int period){
		if (irOutIsConnected){
			try {
				arduino.digitalWrite(irOutPin, 0);
				TimeUnit.MICROSECONDS.sleep(period);
				} 
			catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
				}
		}
		else{
			System.out.println("ERROR : IR Out Pin isn't connected !");
		}
		
	}
	
	// datas for some signal protocol
	
	// TODO Add other datas

	
	// Robosapien V1 Remote
	int RS_HDR_MARK = 6500;
	int RS_BIT_MARK = 800;
	int RS_ONE_SPACE = 3550;
	int RS_ZERO_SPACE = 950;
	
	// End of section
	
	
	
	// Datas send functions
	
	// TODO Add other protocols
	
	public void RSsend(int code){RSsendBin(intToBin(code));}
	public void RSsend(String code){RSsendbin(hexaToBin(code));}
	public void RSsendBin(String code){ // For robosapien and most other Woowee robot
		char bit ;
		code = hexaToBin(code);
		mark(RS_HDR_MARK);
		for (int i = 0; i < code.length(); i++){ 
			bit = code.charAt(i);
			if (bit == '1'){
				mark(RS_ONE_SPACE);
			}
			else if (bit == '0'){
				space(RS_ZERO_SPACE);
			}
		}
	}
	
	
	// end of section
	
	
	
	public static void main(String[] args) {
		LoggingFactory.getInstance().configure();
		LoggingFactory.getInstance().setLevel(Level.INFO);

		try {

			IRremote IRtest = (IRremote) Runtime.start("IRremote", "IRremote");
			IRtest.test();

			Runtime.start("gui", "GUIService");

		} catch (Exception e) {
			Logging.logError(e);
		}
	}

	public IRremote(String n) {
		super(n);
	}

	@Override
	public String[] getCategories() {
		return new String[] { "sensor" };
	}

	@Override
	public String getDescription() {
		return "This service is used for send or receive IR codes";
	}
}
