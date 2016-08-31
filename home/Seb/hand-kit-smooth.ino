/*
 *  Pilotage de la main InMoov Campus
 *  05/2016 seb
 * // Idée : créer un mouvement ou tous les doigt atteigne la position finale en même temps...
 * 1 - DEMO mouvement  lent et de plus en plus rapide
 * 2 - Enchainement de mouvements
 * 
 *  Les + pour la gestion du mouvement :
 *  - Gestion des bornes
 *  - Gestion du pas entre chaque déplacement
 *  - Gestion de la durée entre chaque déplacement
 *  - Gestion de la durée entre 2 mouvements (une fois le 1er Terminé attente de X millisecondes)
 *  - Gestion automatique de la déconnexion des servos moteurs X millisecondes après la fin d'un mouvement
 *  - Ajout du Flex sensor + seuil pour le rendre inactif afin de ne pas interférer avec les mouvements programmés
 *  - Intégration des mouvements de Gaël main Palais de Tokyo (20.05.2016)
 *  - Gestion des accéllérations/ Déccélération des servos (de plus en plus lent à l'approche de l'objectif)
 *  - Ajout de la gestion des boutons pour lancer la demo / l'arrêter et avancer les mvts en mémoire un à un.
 *  - 25.05.16 - capteur de pression dans la paume pour déclencher la fermeture de la main.
 *  
 *  - TO DO : 
 *  - auto détection de l'absence des sensors pour ne pas rester sur la boucle de calibration
 *  - Intégration des mouvements de Gaël main Palais de Tokyo (20.05.2016)
 */

#include <Servo.h>;

// Varibales pour la gestion des accelerations/décélération du servo moteur
const float pi = 3.14;
int deplacement, angleIndex, angleprog;

// Execute la demo des mouvements par défaut
boolean demoMode=false;

boolean mvtencours = false;
boolean fermerturesurpression=false;

// Varibales pour la gestion du flex sensor
int angleFinger =0;
int powerFinger =0;

// Seuil de détection capteur inductif du poignet
// ces valeures s'auto-calibrent...

uint16_t THRESHOLD_GAUCHE ;
uint16_t THRESHOLD_DROIT;
uint8_t nbcycle=0;

uint16_t FINGER_FLEXSENSOR;

unsigned long oldtouchTimeStamp;

// Indice dans le tableau de description des servos
const uint8_t POUCE = 0;
const uint8_t INDEX = 1;
const uint8_t MAJEUR = 2;
const uint8_t ANNULAIRE = 3;
const uint8_t AURICULAIRE = 4;
const uint8_t POIGNET = 5;

const uint8_t nbServos = 6;

// Position main en degré pour les servos moteurs
const uint8_t OUVERT = 0;
const uint8_t FERME = 180;

// en MICROSECONDES secondes (10-6 s) , la valeur par defaut d'un déplacement valeur mini pour bouger d'un degré 
// (20 MS ( 1 cycle du signal PWM = 20 milli-secondes)
// sinon prend la valeur codé dans la table des mouvements
const int stdDelay = 5000; 
int G_servospeed=stdDelay;

// Pas de déplacement par defaut 1 degré
int pasendegre = 1;

// Déclaration des SERVOS
Servo servos[10];

// Pin Arduino pour les leds Droite et Gauche
int LEDG=13;
int LEDD=12;

// Attention sur arduino uniquement  D2 et D3 pouvant être attaché à une interuption
int POUSSG=2;
int POUSSD=3;

// Pouss ON / OFF volatile permet l'acces à la variable à partir de la fonction déclanché par une interuption
volatile byte state = LOW;
volatile byte stateg = HIGH;

unsigned long lastinterupt_millid=millis();
unsigned long lastinterupt_millig=millis();
unsigned long lastmeasurea0=millis();

// Arduino Pin auquelles sont rattaches les servos
const uint8_t  pouce = 4;
const uint8_t  index = 5;
const uint8_t  majeur = 6;
const uint8_t  annulaire = 7;
const uint8_t  auriculaire = 8;
const uint8_t  poignet = 9;

const uint8_t SENSOR_GAUCHE = 10;
const uint8_t SENSOR_DROIT = 11;

// Structure pour definit les proprietes d'un servo moteur
// Pin, point repot en degré / position mini en degré / position maxi en degré
// Position courante (theorique : derniere ordre exécuté en degré) / position de destination
// Position de départ nécessaire pour définir la courbe du mouvement.
// 
typedef struct{
  byte pin; 
  byte neutre;
  byte minPos;
  byte maxPos;
  byte startPos;
  byte curPos;
  byte destination;
  unsigned long timetag;
} ServoPos;


// Initialisation des servos moteurs / Main Fermé
// Par defaut à la position neutre avec comme position courrante le neutre et objectif idem...
// Exécution au de cette position au démarrage de l'arduino.
// => pas de gestion au pas pour l'initialisation car
// on ne connait pas la position actuelle...
//   { majeur, 140, 50, 175, 0, 0, 50},
ServoPos servosPos[] = {
  { pouce, 110, 30, 126, 0, 0, 50},
  { index, 150, 45, 161, 0, 0, 50},
  { majeur, 140, 50, 175, 0, 0, 50},
  { annulaire, 160, 60, 170, 0, 0, 50},
  { auriculaire, 150, 26, 158, 0, 0, 50},
  { poignet, 90, 25, 130, 0, 0, 90},
};


// Liste des mouvements
// Codage des angles des 6 moteurs dans un tableau
// Vitesse defini en micro seconde le délais entre 2 mouvement prend le pas sur la valeur par défaut
// si 0
typedef struct{
  byte pouce; 
  byte index;
  byte majeur;
  byte annulaire;
  byte auriculaire;
  byte poignet;
  unsigned long pause;
  byte vitesse;
} Mouvement;

Mouvement mvts[] = {
  {FERME, FERME, FERME, FERME, FERME, 90,500,5000},
  {50, FERME, FERME, FERME, FERME, 90,500,0},
  {50, 84, FERME, FERME, FERME, 90,500,0},
  {88, 84, FERME, FERME, FERME, 90,500,0},
  {88, 98, FERME, FERME, FERME, 90,3000,10000},
  
  {FERME, 90, FERME, FERME, FERME, 30,500,5000},
  {FERME, OUVERT, FERME, FERME, FERME, 40,500,5000},
  {FERME, 90, FERME, FERME, FERME, 50,500,5000},
  {FERME, OUVERT, FERME, FERME, FERME, 60,500,5000},
  {FERME, 90, FERME, FERME, FERME, 70,500,5000},
  
  {FERME, FERME, FERME, FERME, FERME, 30,2000,0},
  {OUVERT, FERME, FERME, FERME, FERME, 90,2000,0},
  {FERME, OUVERT, FERME, FERME, FERME, 100,2000,0},
  {FERME, FERME, OUVERT, FERME, FERME, 110,2000,0},
  {FERME, FERME, FERME, OUVERT, FERME, 120,2000,0},
  {FERME, FERME, FERME, FERME, OUVERT, 130,2000,0},
  {FERME, FERME, FERME, FERME, FERME, 130,4000,0},  
  {OUVERT, FERME, FERME, FERME, FERME, 130,2000,0},    
  {OUVERT, OUVERT, FERME, FERME, FERME, 130,2000,0},      
  {OUVERT, OUVERT, OUVERT, FERME, FERME, 130,2000,0},      
  {OUVERT, OUVERT, OUVERT, OUVERT, FERME, 130,2000,0},      
  {OUVERT, OUVERT, OUVERT, OUVERT, OUVERT, 130,2000,0},
  {FERME, OUVERT, FERME, FERME, OUVERT, 130,2000,0},     
  {FERME, FERME, FERME, FERME, FERME, 90,4000,0}, 
  {OUVERT, FERME, FERME, FERME, FERME, 90,2000,0}, 
  {0, 70, 70, 70, 70, 90,1000,0}, 
  {0, 120, 120, 120, 120, 95,1000,0}, 
  {0, 70, 70, 70, 70, 100,1000,0},
  {0, 120, 120, 120, 120, 105,1000,0}, 
  {0, 70, 70, 70, 70, 110,1000,0}, 
};

int nbMvts = 28;
int idxMvts = 0;

char commande;

void setup() {
   Serial.begin(115200);
   Serial.println("INMOOV HAND KIT - tapez help pour obtenir de l'aide sur le fonctionnement");
   
  pinMode(LEDG, OUTPUT);
  pinMode(LEDD, OUTPUT);

 // Eteind les led par défaut
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDD, HIGH);
  
  // Délcaration des boutons poussoirs
  // INPUT_PULLUP remplace la mise à l'état haut après la mise en entrée de la broche...
  // Active la résistance interne pour état haut (Pull UP)
  // digitalWrite(POUSSD,HIGH);
  pinMode(POUSSG, INPUT_PULLUP);
  pinMode(POUSSD, INPUT_PULLUP);

  oldtouchTimeStamp = millis();
   
   // Positionne les doigts à leur emplacement Médian
   initPosition(); 
   
   // Ferme la main
   mainOuverte();

    
    // IMPORTANT  : 
    // Auto calibration des "touchs sensors"
    // Pendant 5 secondes prend des mesures pour faire la moyenne.
    // ------------------------------------------------------------
    Serial.println("Auto calibration des 2 detecteurs du poignets : patientez 7 secondes");
    int cpt=0;
    uint32_t  nbcycletotal=0;
    
    while (millis()<2500) {
      nbcycletotal=nbcycletotal+touch_measure(SENSOR_GAUCHE);
      cpt++;       
      delay(20);
    }
    // Calcul la moyenne et ajoute 3 pour le seuil de déclenchement
    THRESHOLD_GAUCHE=uint16_t(nbcycletotal/cpt)+3;
    Serial.print("THRESHOLD_GAUCHE = ");Serial.println(THRESHOLD_GAUCHE);
    
    cpt=0;nbcycletotal=0;
    
    while (millis()<5000) {
      nbcycletotal=nbcycletotal+touch_measure(SENSOR_DROIT);
      cpt++;
      delay(20);
      // Serial.println(nbcycletotal);
    }
    // Calcul la moyenne et ajoute 3 pour le seuil de déclenchement
    THRESHOLD_DROIT=uint16_t(nbcycletotal/cpt)+3;
    Serial.print("THRESHOLD_DROIT = "); Serial.println(THRESHOLD_DROIT);

    // Idem pour le Flex Sensor calcul d'un seuil de prise en compte
    // le capteur doit être en position allongé
    cpt=0;nbcycletotal=0;
    while (millis()<7000) {
      nbcycletotal= nbcycletotal+analogRead(A0);
      cpt++;
      delay(20);
    }
    FINGER_FLEXSENSOR = uint16_t(nbcycletotal/cpt);
    Serial.print("FINGER_FLEXSENSOR = "); Serial.println(FINGER_FLEXSENSOR);

    // Connecte les 2 poussoir aux pin
    // Attention les interuptions externe ne concernent que le PIN 2 et 3 sur Arduino !
    attachInterrupt(digitalPinToInterrupt(POUSSG), changeLed, CHANGE );
    attachInterrupt(digitalPinToInterrupt(POUSSD), changeState, FALLING );
}

// ------------------------------------------------
// Deplace un servo sur la base de pas progressif
// de la config de sa structure...
// ----------------------------------------------
void bougeServos(int degrePas) {
 int sensRotation = 0; 
 int mvtfini=0;
 
 // Parcours tous les servos pour calculer les nouvelles positions
 for (int j=0; j<nbServos; j++) {
 
   // si la position de destination <> de la position courrante
   // déplace le servo vers son objectif au rytme défini...
   if (servosPos[j].curPos != servosPos[j].destination) {
      mvtencours=true;
      
      // regarde le sens de déplacement.
      if (servosPos[j].destination > servosPos[j].curPos) 
        sensRotation=+1;
      else sensRotation=-1;
  
      // Modifie la position courrante.
      servosPos[j].curPos =servosPos[j].curPos + sensRotation*degrePas;
  
      // Vérifie que l'on n'a pas dépassé la destination... et réaffecte la postion à la destination sinon
      if (sensRotation<0) servosPos[j].curPos=max(servosPos[j].curPos, servosPos[j].destination);
      if (sensRotation>0) servosPos[j].curPos=min(servosPos[j].curPos, servosPos[j].destination);
  
      // deplace le servo vers la nouvelle position courrante 
      // Mode avec pente sinusoidale...
      // 22.05.2016
      if (servosPos[j].destination>servosPos[j].startPos) {
        deplacement=(servosPos[j].destination-servosPos[j].startPos);
        angleIndex=servosPos[j].curPos-servosPos[j].startPos;
        angleprog =(servosPos[j].destination-deplacement)+int((deplacement/pi)*(((pi*angleIndex)/deplacement)-(cos(((pi*angleIndex)/deplacement))*sin(((pi*angleIndex)/deplacement))))+0.5);
      
      } else {
        deplacement=-(servosPos[j].destination-servosPos[j].startPos);
        angleIndex=servosPos[j].curPos-servosPos[j].startPos;
        angleIndex=abs(angleIndex);
        
        angleprog =(servosPos[j].startPos)-int((deplacement/pi)*(((pi*angleIndex)/deplacement)-(cos(((pi*angleIndex)/deplacement))*sin(((pi*angleIndex)/deplacement))))+0.5);

      }

      if (!servos[j].attached()) servos[j].attach(servosPos[j].pin);
      servos[j].write(angleprog);
     //  Serial.println(angleprog);
      
       // Mode deplacement linéaire (remplacé par mode pente)
       // servos[j].write(servosPos[j].curPos);

      servosPos[j].timetag = millis();
     } else {
        mvtfini++;
       // Eviter la surchauffe, detach le servo une fois position de destination atteinte
       // laisse 2 secondes entre le dernier ordre et le detach
        if (servos[j].attached() && (millis()-servosPos[j].timetag)>500)  servos[j].detach();
        // Serial.println("detach");
    } 
  }


  // Laisser un peut de temps entre chaque mvt
  if (mvtencours==true) delayMicroseconds(G_servospeed);
        
  // Si tous les servos sont en position alors plus de mouvements,
  // enchainement d'un autre mvt possible.
  if (mvtfini==nbServos && mvtencours==true) { mvtencours=false; }
}


void loop() {
  // put your main code here, to run repeatedly:
    commande=' ';
      
   while (Serial.available()) {
    commande = Serial.read();  //gets one byte from serial buffer
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  
  // Regarde si les capteurs sensitifs du poignets sont touchés
  // on fait les test des senseurs que si aucun mouvement en cours
  if (mvtencours==false) {sensor_touch(); }

  // Execute pour chaque servo la commande de déplacement
  bougeServos(1);
 
  // Serial.println(angleFinger);

  // Delay entre 2 mouvements de la main
  if (mvtencours==false && demoMode==true) {
     // Paramètre un nouveau mouvement 
     if (idxMvts<=nbMvts) {
        // fait la pause prévue avant enchainement mvt suivant
        if (idxMvts>=1) delay(mvts[idxMvts-1].pause);
         
         moveAllFingers(mvts[idxMvts].pouce,mvts[idxMvts].index,mvts[idxMvts].majeur,mvts[idxMvts].annulaire,mvts[idxMvts].auriculaire,mvts[idxMvts].poignet,mvts[idxMvts].vitesse );
         idxMvts++;
     } else {
        // On repard au debut
        idxMvts=0;
     }
  } 
  
    // **** Power Finger Glove / ou capteur de pression *********
   if (demoMode==false &&  FINGER_FLEXSENSOR>800 && (millis()-lastmeasurea0>100)) {
    powerFinger=analogRead(A0);
    // Seuil de déclenchement tmvt compris entre 449 = pas de flex sensor connecté 
    //  870 = connecté mais pas sous pression
    //  
    // (ouvert) et 180 (fermé)
     lastmeasurea0=millis();
     // Serial.println(powerFinger);

     // Sur une pression de 720 delcenche la fermeture de la main
     if(powerFinger < 840) {
       commande='f';
       fermerturesurpression=true;
     }

     if(powerFinger > 860 && fermerturesurpression==true) {
       commande='o';
       fermerturesurpression=false;
     }
     
    // Pour la fermeture d'un doit progressivement
    /*
    if(powerFinger < FINGER_FLEXSENSOR) {
      angleFinger=map(powerFinger,180,FINGER_FLEXSENSOR,FERME,OUVERT);
      moveAllFingers(-1,-1,angleFinger,-1,-1,-1,0); 
    }
    */
   }

  // ---------- Commandes  -----------
  if (commande=='s') { 
    // Stop l'animation automatique
    demoMode=false;
    commande='f';
  }
  if (commande=='d') { 
    // lance la demo : animation automatique
    demoMode=true;
    idxMvts=0;
  }
  
  if (commande=='o') mainOuverte();
  if (commande=='f') mainFermee();
  if (commande=='v') victoire();
  if (commande=='a') attrappe();

  // Deplacement du poignet 
  if (commande=='r') moveAllFingers(-1,-1,-1,-1,-1,180,0); ;
  if (commande=='l') moveAllFingers(-1,-1,-1,-1,-1,0,0); ;

  // Execute le mouvement suivant du tableau
  if (commande=='+') {
      Serial.print("Mouvement no ");Serial.println(idxMvts);
      moveAllFingers(mvts[idxMvts].pouce,mvts[idxMvts].index,mvts[idxMvts].majeur,mvts[idxMvts].annulaire,mvts[idxMvts].auriculaire,mvts[idxMvts].poignet,mvts[idxMvts].vitesse );
      idxMvts++;
      // On Va reboucler la demo en fin de cycle
      if (idxMvts>=nbMvts) idxMvts=0;
   }

  if (commande=='-') {
      Serial.print("Mouvement no ");Serial.println(idxMvts);
      moveAllFingers(mvts[idxMvts].pouce,mvts[idxMvts].index,mvts[idxMvts].majeur,mvts[idxMvts].annulaire,mvts[idxMvts].auriculaire,mvts[idxMvts].poignet,mvts[idxMvts].vitesse );
      idxMvts--;
      idxMvts=max(idxMvts,0 ); 
   }
  
  if (commande=='r') relax();  

  if (commande=='0') pouced(true); 
  if (commande=='5') pouced(false); 

  if (commande=='1') indexd(true); 
  if (commande=='6') indexd(false);   
  
  if (commande=='2') majeurd(true); 
  if (commande=='7') majeurd(false);   

  if (commande=='3') annulaired(true); 
  if (commande=='8') annulaired(false);   

  if (commande=='4') auriculaired(true); 
  if (commande=='9') auriculaired(false);   
  
}


void pouced(boolean sens) {
  if (sens==true)  moveAllFingers(OUVERT,-1,-1,-1,-1,-1,0); 
  if (sens==false) moveAllFingers(FERME,-1,-1,-1,-1,-1,0); 
}

void indexd(boolean sens) {
  if (sens==true) moveAllFingers(-1,OUVERT,-1,-1,-1,-1,0); 
  if (sens==false) moveAllFingers(-1,FERME,-1,-1,-1,-1,0); 
}

void majeurd(boolean sens) {
  if (sens==true) moveAllFingers(-1,-1,OUVERT,-1,-1,-1,0); 
  if (sens==false) moveAllFingers(-1,-1,FERME,-1,-1,-1,0);   
}

void annulaired(boolean sens) {
  if (sens==true) moveAllFingers(-1,-1,-1,OUVERT,-1,-1,0); 
  if (sens==false) moveAllFingers(-1,-1,-1,FERME,-1,-1,0);  
}

void auriculaired(boolean sens) {
  if (sens==true) moveAllFingers(-1,-1,-1,-1,OUVERT,-1,0); 
  if (sens==false) moveAllFingers(-1,-1,-1,-1,FERME,-1,0); 
}

// Detach tous les servo
void relax() {
 for (int j=0; j<nbServos; j++) {
  servos[j].detach();
 } 
}

void initialisation() {
  moveAllFingers(FERME,FERME,FERME,FERME,FERME,90,0);
}

void victoire() {
  Serial.println("Ouverture de la main !");
  moveAllFingers(FERME,OUVERT,OUVERT,FERME,FERME,90,0);
}

void attrappe() {
  Serial.println("Ouverture de la main !");
  moveAllFingers(FERME,OUVERT,OUVERT,FERME,FERME,90,0);
}


void mainOuverte() {
  Serial.println("Ouverture de la main !");
  moveAllFingers(OUVERT,OUVERT,OUVERT,OUVERT,OUVERT,90,0);
}

void mainFermee() {
  Serial.println("Fermeture de la main !");
  moveAllFingers(FERME,FERME,FERME,FERME,FERME,90,0);
}


//
// Configure le degré de rotation pour chacun des doigts de la main
// Le traitement pour chaque doit est ensuite géré dans la loop
// -1 pour ne pas toucher à la position d'un servo.
// 
void moveAllFingers(int pouce, int index, int majeur, int annulaire, int auriculaire, int poignet, int servospeed) {

  // Contrôle avec les bornes Min/Max pour chaque servo
 if (pouce!=-1) {
  if (pouce < servosPos[POUCE].minPos) pouce=servosPos[POUCE].minPos;
  if (pouce > servosPos[POUCE].maxPos) pouce=servosPos[POUCE].maxPos;
  servosPos[POUCE].destination = pouce;
  // Etablie une copie de l'état courrant du doigt vers la mémoire état de départ...
  servosPos[POUCE].startPos = servosPos[POUCE].curPos;    
 }

 if (index != -1) {
  if (index < servosPos[INDEX].minPos) index=servosPos[INDEX].minPos;
  if (index > servosPos[INDEX].maxPos) index=servosPos[INDEX].maxPos;
  servosPos[INDEX].destination = index;
  servosPos[INDEX].startPos = servosPos[INDEX].curPos;    
 }

 if (majeur !=-1) {
  if (majeur < servosPos[MAJEUR].minPos) majeur=servosPos[MAJEUR].minPos;
  if (majeur > servosPos[MAJEUR].maxPos) majeur=servosPos[MAJEUR].maxPos;
  servosPos[MAJEUR].destination = majeur; 
  servosPos[MAJEUR].startPos = servosPos[MAJEUR].curPos;    
 }

 if (annulaire !=-1) {
  if (annulaire < servosPos[ANNULAIRE].minPos) annulaire=servosPos[ANNULAIRE].minPos;
  if (annulaire > servosPos[ANNULAIRE].maxPos) annulaire=servosPos[ANNULAIRE].maxPos;  
  servosPos[ANNULAIRE].destination = annulaire;
  servosPos[ANNULAIRE].startPos = servosPos[ANNULAIRE].curPos;     
 }

 if (auriculaire !=-1) {
  if (auriculaire < servosPos[AURICULAIRE].minPos) auriculaire=servosPos[AURICULAIRE].minPos;
  if (auriculaire > servosPos[AURICULAIRE].maxPos) auriculaire=servosPos[AURICULAIRE].maxPos;    
  servosPos[AURICULAIRE].destination = auriculaire;
  servosPos[AURICULAIRE].startPos = servosPos[AURICULAIRE].curPos;    
 }

 if (poignet !=-1) {
  if (poignet < servosPos[POIGNET].minPos) poignet=servosPos[POIGNET].minPos;
  if (poignet > servosPos[POIGNET].maxPos) poignet=servosPos[POIGNET].maxPos;    
  servosPos[POIGNET].destination = poignet;
  servosPos[POIGNET].startPos = servosPos[POIGNET].curPos;  
 }
 
  // regle la vitesse (tps entre chaque deplacement )
  if (servospeed==0) G_servospeed=stdDelay; else G_servospeed=servospeed;

}

// -----------------------------------------------------------------
// Met les moteurs dans une position initiale au démarrage 
// en faisant en sorte de ne "rien casser"
// permet ensuite d'avoir un repère pour les mouvements
// ------------------------------------------------------------------
void initPosition() {
    int neutre=0;
    
    // met les servos à sa position Milieu entre ses bornes (90 degrés en théorie si Min=0 et max=180)
    // Position nécessitant à priori en moyenne le moins d'effort en déplacement
    // Car sans connaissance initiale impossible de déplacer le servo 
    // lentement vers cette position !
    for (int i=0;i<nbServos ;i++) {
      neutre=int((servosPos[i].maxPos-servosPos[i].minPos)/2);
      
      servos[i].write(neutre);
      servos[i].attach(servosPos[i].pin);

      servosPos[i].startPos = neutre;      
      servosPos[i].curPos = neutre;
      servosPos[i].destination = neutre;
      delay(50); // delai entre chaque mouvement pour ne pas trop tirer de courant d'un coup
      servos[i].detach();
    }   
}


/**
 * Mesure la capacité électrique présente sur une broches digitale
 *
 * Principe : Place la broche au 0v, puis compte le nombre de cycles requis avant que la broche ne commute.
 * Ce système tire parti du temps de charge d'un condensateur au travers d'une résistance de forte valeur (>1M ohms).
 *
 * @param measurePin Broche sur laquelle effectuer la mesure
 * @return Valeur comprise entre 0 (= pas de capacitance) et 255 (= "grosse" capacitance)
 *
 * Remarque : une résistance >1M ohms entre la broche et +VCC est obligatoire !
 */
uint8_t touch_measure(uint8_t measurePin){
  // Serial.print(" mesure ");
  noInterrupts();
   
  /* Registre bas-niveau, DDR = port de configuration, PORT = port de sortie, PIN = port d'entrée */
  uint8_t xport = digitalPinToPort(measurePin);
  volatile uint8_t *ddr = portModeRegister(xport);
  volatile uint8_t *port = portOutputRegister(xport);
  volatile uint8_t *pin = portInputRegister(xport);
 
  /* Résultat de la mesure, Bitmask de la broche à mesurer */
  uint8_t cycles, bitmask = digitalPinToBitMask(measurePin);
 
  /* Décharge la capacité en contact avec la broche */
  *port &= ~(bitmask);     // Place la broche à LOW
  *ddr |= bitmask;         // Place la broche en sortie
  delayMicroseconds(1000); // Attend pour être sur que la capacité est déchargé

   
  /* Place la broche en entrée, sans résistance de pull-up ! */
  /* (La résistance de >1M ohms externe servira de résistance de pull-up) */
  *ddr &= ~(bitmask);
 
  /* Mesure le nombre de cycles CPU requis avant que la broche ne commute */
  for(cycles = 0; cycles < 256; cycles=cycles+1){
    if (*pin & bitmask) break; // Si la broche a commuter on quitte la boucle
     // Serial.println(cycles);
  }

 //  Serial.print(" fin de mesure "); 
  /* Re-décharge la capacité en contact avec la broche
   * afin d'éviter tout parasitages d'une autre mesure sur une autre broche.
   * Dans le cas contraire il serait impossible de manipuler plus d'une touche "tactile" */
  *port &= ~(bitmask);
  *ddr |= bitmask;

 interrupts();
  /* Retourne le résultat */
  return cycles;
}



void sensor_touch() {

  // Une mesure toutes les 500 ms pour éviter de pb de stabilité...
  if ((millis()-oldtouchTimeStamp)>300) {
   oldtouchTimeStamp= millis() ;

    /* Test si la "touche" a été appuyé ou non */
   nbcycle=touch_measure(SENSOR_GAUCHE);
   // Serial.print(nbcycle);
    
    if(nbcycle > THRESHOLD_GAUCHE) {
      // Serial.print(1);
      //ledOn(LEDG);
      moveAllFingers(-1,-1,-1,-1,-1,servosPos[POIGNET].destination-5,0);
      // servosPos[POIGNET].destination = servosPos[POIGNET].destination-5;
      // Serial.println(servosPos[POIGNET].destination);
    }   
    else
    {
       // Serial.print("0");
       //ledOff(LEDG);
    }
    // Serial.println(touch_measure(i), DEC);

 
   nbcycle=touch_measure(SENSOR_DROIT);
   // Serial.print(nbcycle);
    
    if(nbcycle > THRESHOLD_DROIT) {
       // Serial.print(1);
      //ledOn(LEDD);
       moveAllFingers(-1,-1,-1,-1,-1,servosPos[POIGNET].destination+5,0);
       // servosPos[POIGNET].destination = servosPos[POIGNET].destination+5;  
       // Serial.println(servosPos[POIGNET].destination);     
    }   
    else
    {
      // Serial.print("0");
      //ledOff(LEDD);
    }

  } 
}


// Gere le bouton en push successif / 1 push allume / 1 push éteind
void changeState() {
  // Inverse l'état
  // La pullup n'elimine pas tous les rebonds
  // on va considérer le changement sur un interval de temps (10ms mini entre 2 changements)
  if ((millis()-lastinterupt_millid)> 500) {state=!state;lastinterupt_millid=millis();}

  // en fonction de l'état allume ou éteind
  if (state) {
      commande='d';
      ledOn(LEDD);
  } else {
    commande='s';
    ledOff(LEDD);
  }
   Serial.println(state);
}


// Allume la led tant que bouton maintenu poussé
void changeLed() {
 if (digitalRead (POUSSG) == HIGH && stateg==false && (millis()-lastinterupt_millig)> 500) {
   ledOn(LEDG);
   commande='+';
   stateg=true;
   lastinterupt_millig=millis();
 }  else {
    stateg=false;
    ledOff(LEDG); // end of switchPressed
   
 }  
}


void ledOn(int pinLed) {
   digitalWrite(pinLed, LOW); 
}


void ledOff(int pinLed) {
   digitalWrite(pinLed, HIGH);
}
