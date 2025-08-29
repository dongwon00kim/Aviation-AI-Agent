# FSX FSLabs A320 Guide

**Source:** FSX FSLabs A320 Guide.pdf

**Converted:** Aviation Document Processing System

---

## FSX GUIDE FS LABS A320

By Chuck

LAST UPDATED: 04/10/2018

1

## TABLE OF CONTENTS

- PART 1 -INTRODUCTION
- PART 2 -COCKPIT LAYOUT
- PART 3 -FLIGHT PLAN &amp; PRE-START
- PART 4 -START-UP PROCEDURE
- PART 5 -TAXI
- PART 6 -TAKEOFF, CLIMB &amp; CRUISE
- PART 7 -AUTOPILOT
- PART 8 -PROTECTION SYSTEMS
- PART 9 -APPROACH &amp; LANDING

Special thanks to Paul "Goldwolf" Whittingham for creating the guide icons.

2

A320

INTRODUCTION

-

PART 1

The Airbus  A320 family consists  of short-  to  medium-range, narrow-body,  commercial passenger twin-engine jet airliners manufactured by Airbus. The family includes the A318, A319, A320 and A321, as well as the ACJ business jet. Its first flight took place in 1987, therefore it is still a fairly young jet by aviation standards. The A320 family pioneered the  use  of  digital fly-by-wire flight  control  systems,  as well  as side-stick controls, in commercial aircraft. There has been a continuous improvement process since introduction.

Other improvements over older aircraft designs included a streamlined and more structured cockpit  ergonomically  speaking.  It  was  a  drastic  change  from  the  cockpits  of  its  direct competitor,  the  Boeing  737.  Most  switches  are  logically  placed  and  easy  to  access.  The addition of multiple system monitoring pages allowed a much better and user-friendly way for the pilot to monitor the state of various systems. The A320 has a great level of automation, and at some point you might feel that you are more some sort of 'systems operator' instead of  an  actual  pilot.  This  automation  can  be  a  blessing  or  a  curse  if  someone  is  not  trained properly to know the inner workings of the plane.

The Airbus design philosophy is based on four "Golden Rules" (used to be more, but they cut them down recently):

- Fly, navigate, and communicate, in that order
- Use the correct level of automation for the task at hand.
- Know your Flight Mode Annunciator at all times.
- If things on automation are not going as expected, take over immediately.

Overall, the eternal Boeing vs Airbus rivalry can be summed up like this:

Boeing focuses  on the pilot having  more  authority  on  the  aircraft,  while  Airbus  focuses  on system  automation  to  reduce  pilot  workload  and  minimize  the  risk  of  human  error.  Both approaches are quite different and offer different solutions to the same problem: how to fly.

In December 2010, Airbus announced a new generation of the A320 family, the A320neo with a  new  engine  option. The  A320neo  offers  new,  more  efficient  engines,  combined  with airframe improvements and the addition of winglets, named sharklets by Airbus.

A320 first flight in 1987

A320 Neo

A320

## PART 1 -INTRODUCTION

Flight Sim Labs offers two engine variants of the A320 'X' :  the  IAE and the CFM engines.

## CFM 56 (CFM56-5-B4):

CFM International is a joint venture between GE Aviation, a division of General Electric and Safran Aircraft Engines (formerly known as SNECMA), a division of Safran. The 'CFM 56 ' product line is derived from the  two  parent companies' commercial  engine  designations: GE's CF6 and SNECMA's M56. The CFM engine is equipped with a clamshell door type thrust reverser and uses N1 (fan speed) as its thrust reference on the ECAM (Electronic Centralised Aircraft Monitor).

## IAE V2500 (V2527-A5):

'International Aero Engine' (IAE) is a joint venture engine consortium for the  V2500  engine  program  between  Pratt  &amp;  Whitney,  Rolls-Royce, Japanese  Aero  Engines  Corporation  (Kawasaki  Heavy  Industries,  IHI, Mitsubishi  Heavy  Industries)  and  MTU  Aero  Engines.  The  IAE  engine  is equipped  with  a cascade  type  thrust  reverser and  uses  EPR  (Engine Pressure Ratio) as its thrust reference on the ECAM.

The CFM and IAE engines are different. The IAE engine has a longer startup time,  is noisier, is more fuel/oil efficient, has a more effective reverse thrust and has a higher idle thrust (more braking needed during taxi). The CFM  engine  is  quieter,  starts  quicker,  has  a  lower  idle  thrust,  higher reliability but also higher fuel and oil consumption.

CFM Engine

IAE Engine

A320

INTRODUCTION

-

PART 1

## EPR OR N1? WHAT? WHY? HOW?!?

You  may  be  wondering … but  why  would  different  engine  manufacturers  use  different  units  for power settings?

Pratt &amp; Whitney and Rolls-Royce use the Engine Pressure Ratio (EPR) for engines like the IAE V2500 , while GE Aviation (General Electric) uses the engine Fan Speed (N1) for engines like the CFM 56. This difference originates from the way the two companies want the pilot to define his thrust reference.

EPR is defined as the ratio between the pressure at the engine outlet and the engine inlet, and is dependent on the prevailing atmospheric conditions as pressure is affected by temperature and aircraft altitude.

- This is a somewhat more accurate indication of thrust reference since it's the result of simple physics: Thrust = Pressure x Area of Application.
- No matter the condition of the engine, a given EPR in the same atmospheric conditions is guaranteed to deliver the same amount of thrust.
- EPR relies on two pitot probes, and they are susceptible to foreign object damage, such as insects, icing, clogging … which can lead to faulty EPR readings. In multi-spool engines, there is also an issue of stability in control of thrust since filtering of noise from sensors delays response time.

N1 is defined as the speed of the engine compressor or fan, which is independent of the prevailing local atmospheric conditions.

- The N1 sensors are not prone to failure, are more reliable and provide a much better response time. The measurement of speed is a lot more accurate, which allows for excellent stability in control. The N readings do not fluctuate with atmospheric variations, unlike EPR. For this reason, when penetrating a turbulent region in flight, N1 values are used as reference, even if EPR readings are available.
- N1 is a less accurate indication of thrust since it does not take into account engine degradation, which can generate less thrust for the same N1 . However, the presence of an N1 indication can allow the crew to recognize performance degradation.

Check out 'The Flying Engineer'

website for more information:

http://theflyingengineer.com/flightdeck/cockpit-design-epr-vs-n1-indication/

5

## TUTORIAL STRUCTURE

Before you  even step foot in your virtual cockpit, you need to know where you are, where you are going, how you will get there, what you need to get there. This document is structured like a short tutorial flight.

## The flight tutorial is structured as follows:

- Familiarize yourself with the cockpit layout
- Plan your flight
- Determine the flight route, fuel &amp; cargo loads
- Spawn the aircraft and set it in a Cold &amp; Dark state
- Provide aircraft with power
- Begin navigation system alignment phase
- Program the FMGC (Flight Management &amp; Guidance Computer)
- Start -up the aircraft and make it ready for flight
- Taxi
- Takeoff
- Climb and cruise
- Introduction to autopilot and flight control laws
- Approach and land

A320

INTRODUCTION

-

PART 1

BEST RESOURCES

## DISCLAIMER: Do not use this guide for real life flying. I mean it.

Airbus Driver Website

http://www.airbusdriver.net/

Blackbox711 Youtube Channel

https://www.youtube.com/channel/UCe9fggL9PwEqSyMDrlLubVw

Blackbox711 Basic Training Playlist:

https://www.youtube.com/watch?v=E-PsdxhEs-s&amp;list=PL24XRTIr2OjIe7PvRwS50Lf74nZFUeE9x

Blackbox711 Advanced Training Playlist:

https://www.youtube.com/watch?v=ts1aoPdSGNY&amp;list=PL24XRTIr2OjIHo36UtqEp5GCge9u\_wkFW

A320

## PART 2 -COCKPIT LAYOUT

A320

## PART 2 -COCKPIT LAYOUT

Front Flight Deck

9

A320

## PART 2 -COCKPIT LAYOUT

Cockpit Window Handle

10

A320

COCKPIT LAYOUT

-

PART 2

Thumb Rest dimple

Nose Wheel Steering Tiller (used to steer aircraft on the ground)

Side Stick

Pedal Disconnect Button

Takeover Priority Switch Disconnects Autopilot

A320

## PART 2 -COCKPIT LAYOUT

Flood Light

Controls

12

A320

COCKPIT LAYOUT

-

PART 2

AUTO LAND Light

Master Caution Light

Level 2 Cautions

Chronometer Button

Master Warning Light

Level 3 Warnings

Side Stick Priority Light

13

A320

COCKPIT LAYOUT

-

PART 2

Data Display Buttons

CSTR: Flight Plan Constraints

WPT: Waypoints

VOR.D: VHF Omnidirectional Range / Doppler

NDB: Non-Directional Beacon

ARPT: Airport

Barometric

Reference

Barometric Unit Selector

(Black Circle)

Barometric

Setting Selector

Flight Director Switch

ND (Navigation Display) Mode Selector Rose ILS Rose VOR Rose NAV ARC NAV-Weather Radar PLAN

ND (Navigation Display)

Range Selector (nm)

VOR/ADF (VHF Omnidirectional  Range/

Automated Direction Finder) Selector 1 &amp; 2

EFIS (Electronic Flight Instrument System) Control Panel Note 1 : The EFIS is a flight deck instrument display system that displays flight data electronically rather than electromechanically. An EFIS normally consists of a primary flight display ( PFD ), multi-function display ( MFD ), and an Electronic Centralized Aircraft Monitoring ( ECAM ) display. Note 2 : The complex electromechanical attitude director indicator (ADI) and horizontal situation indicator (HSI) were the first candidates for replacement by EFIS.

ILS (Instrument Landing

System) Switch

FCU (Flight Control Unit) Panel

14

A320

COCKPIT LAYOUT

-

PART 2

Flight Director Display Mode Indicator

Flight Director Display Mode

HDG V/S: Heading - Vertical Speed

TRK FPA: Track  -Flight Path Angle

Autopilot Heading/Track Window

Autopilot Speed/Mach Window

Autopilot Speed/Mach Unit Selector

Autopilot Speed/Mach Value Selector

Autopilot Heading/Track Selector

Autopilot LOC (Localiser) Switch

Autopilot 1 &amp; 2 Engage Buttons

Autothrottle

Engage Button

15

A320

COCKPIT LAYOUT

-

PART 2

Autopilot Altitude Window

EXPED (Expedite) Autopilot Mode Button (Maximum Vertical Gradient)

Autopilot V/S / FPA (Vertical Speed / Flight Path Angle) Window

## Metric Altitude Button

Autopilot Vertical Speed / Flight Path Angle Value Selector Rotated : Changes value Pushed : Airplane levels off Pulled : Vertical Speed Engages

APPR (Approach) Autopilot Mode Button

Autopilot Altitude Value Selector Inner : Altitude Change Outer : Altitude Change Scale (100 vs 1000 ft)

16

A320

## PART 2 -COCKPIT LAYOUT

PFD (Primary Flight Display)

Brightness Control

PFD/ND Transfer Switch

ND (Navigation Display) Brightness Control

GPWS

-

G/S (Ground Proximity

Warning System

-

Glide Slope)

Indicator &amp; Test Button

Foot Warmer Switch

Console/Floor Lighting

Selector

Loudspeaker

Volume Knob

Calibrated Airspeed

Indicator (kts)

Heading and Track Indicator

Flight Mode Annunciations

Bank Angle Scale

Vertical Speed

Indicator (x1000 ft/s)

Altitude Indicator (ft)

Attitude Indicator

Barometric Pressure

(inches of Hg or HPa)

PFD (PRIMARY FLIGHT DISPLAY)

Ground Speed (kts)

True Airspeed (kts)

ND Mode shown: ROSE NAV

ND (NAVIGATION DISPLAY)

17

A320

COCKPIT LAYOUT

-

PART 2

ECAM (Engine Centralized Aircraft Monitoring) (Boeing Equivalent: EICAS )

Upper ECAM Display Unit (DU)

## EWD (Engine Warning Display)

Displays engine system warnings and indications

Lower ECAM Display Unit (DU)

## System Display page

Displays system synoptics (a synopsis of various system statuses)

A320

COCKPIT LAYOUT

-

PART 2

N1 (Fan Speed/Low Pressure Compressor Speed) Indication (%RPM)

EGT (Exhaust Gas Temperature) Indication (deg C)

N2 (High Pressure Compressor Speed) Indication (%RPM)

Fuel Flow Indication (kg/hour)

ISIS (Integrated Standby

Instrument System) Indicator

Terrain Map Display on ND

page button

FOB (Fuel On Board) Quantity (kg)

Thrust Limit Mode

Actual Flap/Slat

Position Indicator

Memo/Failure

Information Window

Memo/Failure

Information Window

19

A320

## PART 2 -COCKPIT LAYOUT

Digital Distance &amp; Radio

Magnetic Indicator

Total Air Temperature

(TAT) (deg C)

Static Air Temperature

(SAT) (deg C)

Clock

Fuel Used (kg)

Oil Quantity (Qt)

Oil Pressure (PSI)

Oil Temperature (deg C)

N1 Vibration Level

N2 Vibration Level

Gross Weight

20

A320

COCKPIT LAYOUT

-

PART 2

AUTO/BRK switches

Arms required braking/deceleration rate

- LO : Selected for landing (low intensity)
- MED : Selected for landing (medium intensity)
- MAX : Selected for takeoff (maximum intensity)

Note

: Blue (ON) light is for positive arming, Green (DECEL) light is when actual airplane deceleration corresponds to 80 % of selected rate.

Landing Gear Lever

UP: Gear UP

DOWN: Gear DOWN

Left-Click and Drag to move Lever

Brake Accumulator Pressure Indicator

Left &amp; Right Brake Pressure Indicators

Landing Gear Indicator Light UNLK (Red): Gear is not locked in selected position. Green : Gear is locked down.

Clock

Landing Gear Brake Fan switch For cooling brakes

Anti-Skid (A/SKID) and Nosewheel Steering (N/W STRG) Switch

21

A320

## PART 2 -COCKPIT LAYOUT

Pedestal

A320

## PART 2 -COCKPIT LAYOUT

Air Data (or ADIRU, Air Data Inertial Reference Unit) Selector CAPT 3 :  ADR 3 (Air Data Reference) replaces ADR 1. NORM : ADR 1 supplies data to PFD 1, ND1 and RMI/DOR DME. ADR 2 supplies data to PFD2 and ND 2. F/O 3 : ADR 3 (Air Data Reference) replaces ADR 2.

ATT HDG (Attitude Heading) Selector CAPT 3 :  IR (Inertial Reference) 3 replaces IR 1 NORM : IR 1 supplies data to PFD 1, ND1 and RMI/DOR DME. IR 2 supplies data to PFD2 and ND 2. F/O 3 : IR 3 replaces IR 2

EIS DMC (Electronic Instrument System, Display Management Computer) Selector CAPT 3 :  DMC 3 replaces DMC 1 NORM : DMC 1 supplies data to PFD 1, ND 1 &amp; upper ECAM display. DMC 2 supplies data to PFD 2, ND2 &amp; lower ECAM display. F/O 3 : DMC 3 replaces DMC 2.

FMS (Flight Management System) MCDU (Multifunction Control Display Unit)

- An FMS is a specialized computer system that automates a wide variety of in-flight  tasks,  reducing the workload on the flight crew to the point that modern  civilian  aircraft  no  longer  carry flight  engineers or navigators.  A primary function is in-flight management of the flight plan.
- The FMS is controlled through the MCDU physical interface.
- The FMS sends the flight plan for display to the Electronic Flight Instrument System ( EFIS ), Navigation Display ( ND ), or Multifunction Display ( MFD ).

ECAM (Electronic Centralized Aircraft Monitoring) /ND Transfer Selector CAPT :  Transfers SD (System Display) to Captain's ND (Navigation Display) NORM : SD appears on lower ECAM display

- F/O : Transfers SD to First Officer's ND.

23

A320

COCKPIT LAYOUT

-

PART 2

TO (Takeoff) Configuration Button

Simulates takeoff power application to trigger a warning if the airplane is not properly

configured for takeoff.

ECAM Upper Display

Brightness Control

ECAM Lower Display

Brightness Control

CLR (Clear) Button

Clears error messages on EWD.

STS (Status) Button

System Status Page is displayed on lower ECAM display.

RCL (Recall) Button

Recalls warning and caution messages that have been

suppressed with CLR key.

Emergency Cancel Key

Cancels aural warnings, MASTER WARN lights and caution messages.

System Page (System Display, SD) Keys

Toggles system pages on ECAM displays.

ENG

:  Engines page

BLEED

:  Bleed Air Systems page

PRESS

:  Cabin Air Pressure page

ELEC

:  Electrical Systems page

HYD

: Hydraulic Systems page

FUEL

: Fuel Systems page

APU

: Auxiliary Power Unit page

COND

: Air Conditioning page

DOOR

: Door status page

WHEEL

: Wheel brake page

F/CTL

:  Flight Controls page

STS

: Status page

ALL

: All system pages displayed in succession

24

A320

COCKPIT LAYOUT

-

PART 2

System Page (System Display, SD) ENG :  Engines page BLEED :  Bleed Air Systems page

A320

COCKPIT LAYOUT

-

PART 2

System Page (System Display, SD) PRESS :  Cabin Air Pressure page ELEC :  Electrical Systems page

A320

## PART 2 -COCKPIT LAYOUT

System Page (System Display, SD) HYD : Hydraulic Systems page FUEL : Fuel Systems page

A320

COCKPIT LAYOUT

-

PART 2

System Page (System Display, SD) APU : Auxiliary Power Unit page COND : Air Conditioning page

A320

COCKPIT LAYOUT

-

PART 2

System Page (System Display, SD) DOOR : Door status page WHEEL : Wheel brake page

A320

COCKPIT LAYOUT

-

PART 2

System Page (System Display, SD) F/CTL :  Flight Controls page STS : Status page ALL : All system pages displayed in succession

## A320

COCKPIT LAYOUT

-

PART 2

Throttle

Autothrottle Disconnect Button

Thrust Reverser Lever

Throttle Detents TOGA : Takeoff / Go Around FLX/MCT :  Max Continuous Thrust CL : Max Climb Thrust IDLE :  Idle Thrust REV IDLE : Reversed Idle Thrust

Note: FLEX is the standard takeoff thrust setting  used  on  Airbus  aircraft.  FLEX  means that the aircraft uses reduced thrust on takeoff in  order  to  reduce noise,  prevent engine wear and prolong engine life. 'Flexible temperature' means that the engine controller will force the engine to behave as if outside air temperature was higher than it really is, causing  the  engines  to  generate  less  thrust since higher air temperatures diminish an aeroengine's thrust generating capabilities. FLEX is also  known  in  other  companies  as 'Assumed Temperature Derate ', 'Assumed Temperature Thrust Reduction' or 'Reduced Takeoff Thrust' or 'Factored Takeoff Thrust' .

Stabilizer Pitch Trim Wheel

Stabilizer Pitch Trim Position Scale

Full Reverse Throttle Range

Throttle Scale (in degrees)

Engine Master (ENG MASTER) Switch

- Right-Click and HOLD to UNLOCK/PULL switch up
- Left-Click to MOVE switch FWD (MASTER) or AFT (OFF)

Engine Mode Selector CRANK : Engine cranks without ignition NORM : Continuous Ignition when engine is running IGN/START : Continuous Ignition if ENG MASTER switch is ON and N2 is at IDLE or greater

Engine Fire / Fault light

31

A320

COCKPIT LAYOUT

-

PART 2

The Thrust Reverser lever can be moved by pressing and holding the 'Throttle (decrease quickly)' control mapped to your joystick. Make sure that the 'Repeat' slider is set fully to the right. The default key binding is 'F2'.

Take note that the Reverse Thrust lever can only be engaged if your throttle is at IDLE. The reason for that is a mechanical stopper that prevents you from engaging thrust reversers at high throttle settings.

A320

## PART 2 -COCKPIT LAYOUT

Radio Panel

Audio Control Panel

Main Panel &amp; Control Pedestal

Integral Brightness Control

Main Panel Flood lights

Brightness Control

DFDR (Digital Flight Data

Recorder) Event Flag Button

AIDS (Aircraft Integrated

Data System) Print Button

Control Pedestal Flood

33

lights Brightness Control

A320

## PART 2 -COCKPIT LAYOUT

Weather Radar Control Panel

Speed Brake / Ground Spoiler

Arming Lever

TCAS/ATC (Traffic Alert &amp;

Collision Avoidance System / Air

Traffic Controller) Control Panel

Flaps Control Lever

Settings: 0, 1, 2, 3, FULL

34

A320

COCKPIT LAYOUT

-

PART 2

## FLAPS &amp; SLATS

Flaps and slats are deployed with the Flaps lever. Flaps and slats are used to create additional lift at low speeds.

## SPEED BRAKES &amp; GROUND SPOILERS

The  speed  brake  and  ground  spoiler  system, however, will be automatically deployed only if certain conditions are respected (see next page).  A 'spoiler' is  the  physical  panel,  while the 'speed brake' and 'ground spoiler' expressions are functions of these spoilers. Simply  put,  spoiler  panels  have  either  speed brake  or  ground  spoiler  functions.  The  speed brake function is used to bleed off speed while in  the  air,  while  the  ground  spoiler  is  used  to 'dump' lift once you landed and need to bleed off lift as soon as possible.

Speed brakes can be actuated in the air while in certain conditions but they can't be actuated on the ground.

Ground  spoilers  can  only  be  actuated  on  the ground (which is why you need to 'arm' them first  while  in  the  air)  and  will  only  actuated  if certain conditions are met.

A320

COCKPIT LAYOUT

-

PART 2

A320

## PART 2 -COCKPIT LAYOUT

Cockpit Door Control

Rudder Trim Indicator (deg)

Rudder Trim Control

Rudder Trim Reset Button

Parking Brake

(shown in OFF position)

Emergency Landing

Gear Extension Lever

37

A320

COCKPIT LAYOUT

-

PART 2

Overhead Panel

38

A320

## PART 2 -COCKPIT LAYOUT

ADIRS (Air Data Inertial

Reference System) Panel

Flight Control Panel

Evacuation &amp; Emergency

Electrical Panel

GPWS (Ground Proximity

Warning) Panel

Flight Recorder Panel

Oxygen Panel

Miscellaneous Panel

Fire Detection &amp; Protection Panel

Hydraulics Panel

Fuel Panel

Electrical Panel

Air Conditioning Panel

Anti-Ice &amp; Heating Panel

Cabin Pressure Panel

Lights Panel

APU

Panel

Lights Panel

Audio Panel

Radio Panel

Flight Control Panel

Ventilation Panel

Engine Manual Start Panel

Miscellaneous Panel

A320

## PART 2 -COCKPIT LAYOUT

High Altitude

Landing

Pushbutton

Rain Repellant

Button

Ground Mechanic

Communication Button

Forward &amp; Aft Call

Light Button (for flight attendants)

Windshield

Wiper Control

Emergency Call

Button

GPWS (Ground Proximity

Warning System) Mode Selector

RCDR (Cockpit Voice

Recorder) Control Panel

Crew Oxygen Supply

Pushbutton

Passenger Oxygen Supply ON light

Oxygen Mask Door Manual

Control Pushbutton

40

A320

## PART 2 -COCKPIT LAYOUT

PACK (Pneumatic Air

Conditioning Kit) Flow Selector

PACK 1 (Pneumatic Air

Conditioning Kit) Pushbutton

Engine 1 Bleed Pushbutton

Engine 1 &amp; 2 Anti-Ice Pushbuttons

Wing Anti-Ice Pushbutton

Beacon Lights Control Switch

Strobe Lights Control Switch

Runway Turn OFF Lights

Control Switch

Ram Air Inlet Valve Control Pushbutton

Landing Lights Control Switch

Cockpit, Forward Cabin and Aft Cabin

Air Temperature Controls

APU Bleed Pushbutton

Engine 2 Bleed Pushbutton

Probe/Window Heat

Control pushbutton

Navigation &amp; Logo Lights Control Switch

1: Light set 1 ON / 2: Light set 2 ON

OFF: Lights OFF

APU (Auxiliary Power Unit) Master Switch

Wing Lights Control Switch

APU (Auxiliary Power Unit) Start Switch

Nose Lights Control Switch

41

Crossbleed

Selector Valve

A320

COCKPIT LAYOUT

-

PART 2

PACK 2 (Pneumatic Air

Conditioning Kit) Pushbutton

Ditching Switch

LDG ELEV Mode Selector

Cabin Pressure Mode

Select Pushbutton

Manual Vertical Speed (V/S)

Target Valve Control Switch

Ice Indicator &amp; Standby

Compass Light Control Switch

Overhead Integral

Lighting Control Switch

Seatbelt Sign Light

Control Switch

No Smoking Sign Light

Control Switch

Dome Light Control Switch

FWD Cargo Fire Smoke Detected and Discharge Light

Cargo Fire Agent Discharge Switch

Hot Air Pressure Regulating

Valve Pushbutton

Annunciator Light

Control Switch

Emergency Exit Light Control Switch &amp; Indicator

Cargo Hot Air Pressure

Regulating Valve Pushbutton

Aft Isolation Valve pushbutton

Cargo Temperature Control

Cargo Compartment

Smoke Test Button

Cargo Fire Agent Discharge

Switch

AFT Cargo Fire Smoke

Detected and Discharge Light

Cabin Ventilation Fans

Pushbutton

Ventilation Extract

Pushbutton

Ventilation Blower Pushbutton

Engine 1 &amp; 2 Manual Start Pushbuttons

Rain Repellant Pushbutton

Windshield Wiper Control

42

A320

## PART 2 -COCKPIT LAYOUT

Evacuation Alert Command Switch

ELAC 1 (Elevator &amp; Aileron Computer) Switch

Evacuation Horn Shut Off

SEC 1 (Spoiler &amp; Elevator

Computer) Switch

FAC 1 (Flight Augmentation

Computer) Switch

RAT (Ram Air Turbine)

Emergency Electrical

&amp; Emergency

Generator Fault Light

Power RAT Manual

Switch

Emergency

Generator

Test

Generator 1

Line Switch

CAPT &amp; PURS

Evacuation Alert

IDG 1 (Integrated

Drive Generator)

Galley &amp; Cabin Electrical Switch

Battery 1 Voltage

Battery 1 Pushbutton

Battery 2 Pushbutton

Battery 2 Voltage

AC Essential Bus

Feed Pushbutton

Generator 1

APU

Generator

Bus Tie

Pushbutton

External

Power

IDG 2 (Integrated

Drive Generator)

43

Generator 2

A320

COCKPIT LAYOUT

-

PART 2

Engine 1 Hydraulic

Pump Pushbutton

Left Fuel Tank

Pump 1 Pushbutton

Left Fuel Tank Pump 2 Pushbutton

Center Fuel Tank Pump 1 Pushbutton

Fuel Pump Mode AUTO Selection Switch

Center Fuel Tank Pump 2 Pushbutton

Right Fuel Tank Pump 1 Pushbutton

Right Fuel Tank Pump 2 Pushbutton

ELAC 2 (Elevator &amp; Aileron Computer) Switch

SEC 2 (Spoiler &amp; Elevator Computer) Switch

SEC 3 (Spoiler &amp; Elevator Computer) Switch

FAC 2 (Flight Augmentation Computer) Switch

RAT (Ram Air Turbine) Manual Extension Switch

Blue Hydraulic

System Electrical

Pump Pushbutton

PTU (Power Transfer

Unit) Pushbutton

Engine 2 Hydraulic

Pump Pushbutton

Radio Panel

Yellow Hydraulic System

Electrical Pump Pushbutton

44

A320

## PART 2 -COCKPIT LAYOUT

ADR 1, 3 &amp; 2 (Air Data

Reference) Fault Lights

IR 1, 3 &amp; 2 (Inertial Reference)

Status Lights (ALIGN/FAULT)

IR 1, 3 &amp; 2 (Inertial Reference) Mode Reference

Pushbuttons

OFF

: Deactivates ADIRU (Air Data Inertial Reference Unit)

NAV

:  Full Inertial Data

ATT

:  Attitude and Heading data only

ADIRS (Air Data Inertial Reference System) Data Display Window

Engine Fire

Test Button

Engine 1 Agent 1  Switch

Engine 1 Fire Light &amp; Switch

Engine 1 Agent 2  Switch

APU (Auxiliary Power Unit) Agent Switch

APU Fire Light &amp; Switch

APU Fire Test Button

Engine 2 Agent 1 Switch

Engine 2 Fire Light &amp; Switch

Engine 2 Agent 2 Switch

Engine Fire Test Button

45

A320

COCKPIT LAYOUT

-

PART 2

Fuse Panel

Circuit Breakers

Captain Reading

Light Control Knob

46

A320

COCKPIT LAYOUT

-

PART 2

Lavatory Toilet Occupied Light

Audio Switching Control

Maintenance Oxygen

Timer switch

Service Interphone

Override Switch

Hydraulic System Blue

Pump Override switch

APU (Auxiliary Power

Unit) Test Switch

APU (Auxiliary Power

Unit) Reset Switch

Data Loading Selector Panel

Avionics Compartment

Light Switch

Engine 1 &amp; 2 FADEC

Ground Power Switches

Green (G), Blue (B) &amp; Yellow (Y)

Hydraulic System Leak Measurement

Valve Test Switches

Flight Officer Reading

Light Control Knob

47

A320

## PART 2 -COCKPIT LAYOUT

Wing Light

Right Landing Light

Logo Light

Upper Beacon Light

Lower Beacon Light

- Landing Lights: used to illuminate runway during landing
- Runway Turnoff Lights: used to aid the crew in seeing the turn in the taxiway/runway
- Taxi Lights: used to illuminate area in front of nosewheel during taxi
- Beacon (Anti-Collision) Lights: flashing red light used to prevent collisions and warn others that aircraft is active and engines are running
- Navigation (Position) Lights: red, green and white lights help you know the direction of an aircraft (red is on the left, green on the right, white on the tail).
- Strobe (Anti-Collision) Lights: pulsating white lights used when aircraft enters a runway in use to increase visibility
- Wing Lights: used to check wing at night (i.e. verify if there is ice accumulation on the wing)
- Logo Light: used to illuminate the airline's logo painted on the tail

Left Landing Light

A320

COCKPIT LAYOUT

-

PART 2

Taxi Light

Runway Turnoff Lights

Takeoff Light

Navigation (Red) Light

Strobe (Flashing White Light)

Navigation (Green) Light

Strobe (Flashing White Light)

Navigation (White) Light

Strobe (Flashing White Light)

49

## PLANNING THE FLIGHT

In real life, you cannot just fly an A320 wherever and whenever you please. Just like on land, the sky is littered with an intricate network of waypoints and aerial highways. Therefore, it is necessary to plan your flight route and to determine how much fuel you will need to carry in order to reach your destination.

In  order  to  do  this,  we  will  use  a  tool  called 'Online Flight Planner' available here: http://onlineflightplanner.org/

There are a number of fuel planners available online. These estimates may or may not be very accurate. There are specific charts created by Airbus to come up with accurate fuel estimates which are unfortunately not available to the public. Therefore, for the sake of simplicity we will just use a rule of thumb that's good enough for the purpose of this tutorial.

A320

FLIGHT PLAN &amp; PRE-START

-

PART 3

## PLANNING THE FLIGHT

Today's flight will start from AMSTERDAM-SCHIPHOL (EHAM) and our destination will be LONDON-HEATHROW (EGLL).

Using the 'Online Flight Planner' available here: http://onlineflightplanner.org/  we will enter the Departure airport (EHAM), the Destination airport (EGLL) and the AIRAC Cycle desired (we will use the AIRAC cycle 1609 as explained on the next page).

Click on CREATE PLAN to generate a flight plan.

Airbus A320

Choose your fuel units: KGs in our case

51

Click CREATE PLAN

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## PLANNING THE FLIGHT

In aviation,  an Aeronautical Information Publication (or AIP ) is defined by  the International Civil Aviation Organization as a publication issued by or with the authority of a state and containing aeronautical information of a lasting character essential to air navigation. It is designed to be a manual containing thorough details of regulations, procedures and other information pertinent to flying aircraft in the particular country to which it relates. It is usually issued by or on behalf of the respective civil aviation administration. AIPs are kept up-to-date by regular revision on a fixed cycle. For operationally significant changes in information, the cycle known as the AIRAC (Aeronautical Information Regulation And Control) cycle is used: revisions are produced every 56 days (double AIRAC cycle) or every 28 days (single AIRAC cycle). These changes are received well in advance so that users of the aeronautical data can update their flight management systems (FMS). (Source: https://en.wikipedia.org/wiki/Aeronautical\_Information\_Publication )

In  other  words,  some  Youtube  tutorials  might  show  you flight  routes  with  certain  waypoints  that  got  changed  with  more  recent  AIRAC  updates.  Some  waypoints  or  even  airports  may not  exist  anymore. Therefore, you have two options:

1. Plan your flight using the default AIRAC cycle programmed in the FMGC when it was first released by FS Labs during late August (period 09) 20 16 (AIRAC cycle 1609 ), which is what we will do for this tutorial. This option is free and simple if you fly alone. However, if you fly with online ATCs in multiplayer that use the latest AIRAC database, you should go for the second option.
2. Plan  your  flight  using  the  latest  AIRAC  cycle.  You  will  need  to  update  your  AIRAC,  SID  and  STAR  database  by  using  a  paid  subscription  service  called ' Navigraph ', which  is  available  here https://www.navigraph.com/FmsDataManualInstall.aspx .

## PLANNING THE FLIGHT

## FUEL

For a flight of approx. 200 nm ,  fuel  planning can  be  estimated with the following formula:

## Imperial Units

Fuel for flight = (Number of 100 nm legs) x (2200 lbs)

= 2 x 2200 lbs = 4400 lbs

Reserve Fuel = 5500 lbs

Total (Block) Fuel = Fuel for Flight + Reserve Fuel = 9900 lbs Metric Units

Fuel for flight = (Number of 100 nm legs) x (1000 kg)

= 2 x 1000 kg = 2000 kg

Reserve Fuel =

2500 kg

Total (Block) Fuel = Fuel for Flight + Reserve Fuel = 4500 kg

## FLIGHT ROUTE

The flight route we will take is:

EHAM SID GORLO UL980 XAMAN L980 LOGAN STAR EGLL

## Write this route down.

But what does it all mean? Here is a breakdown of this route:

- Depart from Schiphol Airport (EHAM)
- Follow the SID (Standard Instrument Departure) route from EHAM to GORLO
- Navigate to GORLO VOR
- Follow UL980 airway
- Navigate to XAMAN VOR
- Follow L980 airway
- Navigate to LOGAN VOR
- Follow the STAR (Standard Terminal Arrival Route) from LOGAN to EGLL
- Land at Heathrow Airport (EGLL)

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## WHAT IS A SID AND A STAR ?

A SID (Standard Instrument Departure) is a small initial route which leads an aircraft  from  the  runway  they've  just  taken  off  from  to  the  first  point  in his/her intended route. An airport usually has a lot of aircraft departing from it's  runways. To save confusion (and for safety), a busy airport will publish standard  routes  from  it's  runways  to  the  various  routes  away  from  that airport.  This  way  a  controller  can  be  sure  that  even  if  a  steady  stream  of aircraft is leaving the airport they will all be following in a nice neat line, one behind the other (that's the idea anyhow!).

Standard routes are the preferred method to fly from airport to airport. This is why we use a flight plan generator. Arriving at an airport is just the same. The STARs (STandard  Arrival  Routes)  are  also  published  in  chart  form  and allow  you  to  fly  into  an  airport  using  standard  procedures.  This  way,  less communication  is  again  needed  with  the  controllers  as  (once  you  have declared your intention or been given a route to fly by name) the controller and you both know exactly how you are going to approach the airport. The end of the STAR route will normally leave your aircraft at a position where controllers can give you final instructions to set you up for a landing.

SIDs  and  STARs  are  quite  similar  to  highways;  they  have  speed  limits  and altitude restrictions at certain waypoints to make sure the air traffic is flying safely  and  on  the  same  trajectory.  The  FMGC  (Flight  Management  &amp; Guidance Computer) will automatically try to respect these restrictions.

In other words, you can see SIDs and STARs like road junctions in the sky that lead  to  other  waypoints  and  airways  from or to  your  desired  airport. One airport has many SIDs and STARs.

Typically,  SIDs  and  STARs  are  provided  by  the  ATC  (Air  Traffic  Controller). Since we're doing a tutorial, I will just give you the SID and STAR to plug in the FMGC.

54

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## PLANNING THE APPROACH  - STAR

These charts are for the STAR (Standard Terminal  Arrival  Route)  from  LOGAN  to  EGLL. We intend to:

1. Come from LOGAN waypoint
2. Fly  from  LOGAN  towards  the  BIG1E  arrival route.
3. Follow the STAR (BIG1E -&gt; KOPUL -&gt; TANET &gt; DET -&gt; BIG)
4. Select an AIF (Approach Initial Fix) from the FMGC  database  (in  our  case  CI27L)  and follow  the  approach  towards  the  runway, guided by the EGLL airport's ILS (Instrumented Landing System).
5. Land  at  Heathrow  (EGLL)  on runway  27L (orientation: 270 Left)

A320

FLIGHT PLAN &amp; PRE-START

-

PART 3

## PLANNING THE FLIGHT - SUMMARY

So there it is! This is more or less all the information you need to plan your flight!

Flight Plan Input to FMGC

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## MCDU/FMGC IN A NUTSHELL

Most of the aircraft setup and flight planning will be done with the help of the MCDU, which encompasses various systems such as the FMGC system.

MCDU : Multifunction Control Display Unit

## MAIN MENU page:

- FMGC -&gt; Flight Management &amp; Guidance Computer
- Fundamental component of a modern airliner's avionics. The FMGC is a component of  the  FMGS  (Flight  Management  &amp;  Guidance  System),  which  is  a  specialized computer  system  that  automates  a  wide  variety  of  in-flight  tasks,  reducing  the workload  on  the  flight  crew  to  the  point  that  modern  civilian  aircraft  no  longer carry flight engineers or navigators. A primary function is in-flight management of the  flight  plan.  All  FMS  contain  a  navigation  database.  The  navigation  database contains the elements from which the flight plan is constructed. The FMGS sends the  flight plan  for  display  to  the Electronic  Flight  Instrument  System (EFIS), Navigation Display (ND), or Multifunction Display (MFD).
- ATSU -&gt; Air Traffic Services Unit, not fully simulated
- Digital  datalink  system  for  transmission  of  short  messages  between  aircraft  and ground stations via airband radio or satellite.
- OPTIONS -&gt; Setup various aircraft options
- Allows  you  to  change  fuel  loads,  payloads,  ground  carts  for  power  and  air,  door controls, cabin lights or pushback controls. This is a fictional custom interface built by FS Labs as a tool for you to work with.
- Allows  you  to  configure  aircraft  equipment  installed  on  your  current  airframe, customize various parameters like display parameters, unit system, ADIRUS alignment  time,  setup  cold  &amp;  dark  and  other  panel  states,  and  configuration  of aircraft malfunctions/failures.
- FAILURES -&gt; Flight Simulation Failures
- Allows  you  to  configure  various  aircraft  malfunctions  and  failures  for  training purposes (i.e. engine flameout).

Note: The FMGC and ATSU menus only appear if the aircraft is powered on.

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## MCDU/FMGC IN A NUTSHELL

- FMGC -&gt; Flight Management &amp; Guidance Computer
- DIR : 'Direct to' page modifies the flight plan by creating a direct leg from the aircraft's present position to any selected waypoint
- PROG : 'Progress' page displays dynamic flight information and data related to the primary flight plan
- PERF : 'Performance' page provides performance data, speeds and various vertical predictions associated with each flight phase
- INIT : Initialization pages INIT A (flight plan initialization, departure point, etc.) and INIT B (zero fuel CG, zero fuel weight, block fuel)
- DATA : navigation data index page
- F-PLN : displays flight plan data
- RAD NAV : 'Radio Navigation' page displays NAVAIDS (navigation aids like VOR beacons, NDBs, etc.) tuned by the FMGS or selected by the pilot
- FUEL PRED : fuel and time prediction information and fuel management data
- SEC F-PLN : displays secondary flight plan data
- ATC COMM : displays the ATSU (Air Traffic Service Unit) menu
- AIRPORT : displays the F-PLN page, which includes the next airport along the current flight plan
- MCDU MENU : view the main menu page (see previous page)
- ARROWS (SLEW KEYS) : Cycles through previous and next page of selected FMGC page
- BRT : Brightens MCDU page
- DIM : Dims MCDU page
- CLR : Used to clear message or data from the scratchpad or a data field
- OVFY : Overfly key enables the pilot to change the transition from a fly-by to a fly-over, and vice-versa.

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## SPAWN COLD &amp; DARK

In  FSX,  you  will  generally  spawn  with  your  engines  running.  A 'cold &amp; dark' start-up  means  that  your  aircraft  is  in  an  unpowered  state  with  engines  and every other system off. Here is the procedure to spawn in such a state:

1. Spawn like you normally would at Gate F6 in EHAM (departure airport) in the ' AirCreation  Trike Ultralight' .  Press  and  hold 'CTRL+SHIFT+F 1 ' to automatically shut down the aircraft
2. Replace Trike Ultralight by the FS Labs A320
- a) Press ALT to open FSX menu
- b) Click on 'Aircraft', and then 'Select Aircraft'
- c) Select 'Flight Sim Labs' tab and choose desired A320
- d) Click 'OK'
- e) Aircraft should be set to Cold and Dark configuration as shown

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## SPAWN COLD &amp; DARK

In  FSX,  you  will  generally  spawn  with  your  engines  running.  A 'cold &amp; dark' start-up  means  that  your  aircraft  is  in  an  unpowered  state  with  engines  and every other system off. Here is the procedure to spawn in such a state:

1. Spawn like you normally would at Gate F6 in EHAM (departure airport) in the ' AirCreation  Trike Ultralight' .  Press  and  hold 'CTRL+SHIFT+F 1 ' to automatically shut down the aircraft
2. Replace Trike Ultralight by the FS Labs A320
- a) Press ALT to open FSX menu
- b) Click on 'Aircraft', and then 'Select Aircraft'
- c) Select 'Flight Sim Labs' tab and choose desired A320
- d) Click 'OK'
- e) Aircraft should be set to Cold and Dark configuration as shown

2d

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## POWER UP AIRCRAFT

3. On Overhead panel, press the BAT 1 and BAT 2 switches to set battery power
4. Go on MCDU main menu to install wheel chocks, connect ground power unit (GPU)  to the aircraft
- a) Power up FMGC by pressing and holding the BRT button on the MCDU
- b) Select OPTIONS menu
- c) Select 'EXT CTRLS' (External Controls) menu
- d) Make sure the GPU (Ground Power Unit), Air Starter, GND A/C and GND CHOCKS all display 'CONNECT', which means that they are currently all disconnected.
- e) Click on the 'GPU -CONNECT' LSK to set ground power. The MCDU will then display 'GPU DISCONNECT'.
- f) Click on the 'GND CHOCKS -CONNECT' LSK to set chocks. The MCDU will then display 'GND CHOCKS DISCONNECT'.
- g) Return to main MCDU MENU
5. On Overhead panel, confirm that the 'EXT PWR' indication is illuminated
6. Click on the 'EXT PWR' switch to power the aircraft

5

6a

## GPU : Ground Power Unit

Air Starter : External pressurized air used for engine start GND A/C : External air conditioning to the aircraft to control cabin temperature

GND Chocks :  places chocks around the nose and main gear

4e

4f

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## START ADIRS ALIGNMENT

7. Engage Parking Brake (aircraft movement can screw up your navigation system alignment) by right-clicking on the handle to pull it and set it to the ON position. Note that left clicking the handle sets it to OFF while right clicking sets it to ON.
8. On  Overhead  panel,  set  ADIRS  System  1  (Air  Data  Inertial Reference  System)  switch  to  NAV.    The 'ON BAT' caution will illuminate  during  the ADIRU's self-test  phase,  then extinguish once the self-test is complete.
9. Repeat step 8  for ADIRS System 2.
10. Repeat step 8 for ADIRS System 3.

NOTE:  This  alignment  phase  usually  takes  between  7  and  10 minutes. ADIRS alignment is complete once a full PFD (Primary Flight Display) and ND (Navigation Display) are displayed on your display units. Alignment time remaining is displayed on the EWD (Engine Warning Display) on the upper ECAM display once you cleared  the  EWD  caution  messages  using  the 'CLR' button  on the MCDU.

8

9

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -UNITS &amp; TILLER SETUP

11. Go on MCDU main menu and set aircraft fuel weight units to your desired system (lbs or kg) and set desired aircraft tiller axis options. We will choose KGs and a single-axis tiller setup (meaning that you do  not  want  to  assign  any  separate  joystick  axis  for  the  tiller  and want  to  use  the  simpler 'RUDDER PEDAL DISCONNECT' button mapped to the 'Comma' key by default in order to use nosewheel steering).
- a) Select MCDU OPTIONS page
- b) Select UNITS page
- c) Click on LSK next to 'WEIGHT LBS/KG' to switch the weight unit system to KG as shown.
- d) Click on LSK next to 'RETURN' to return to the OPTIONS menu
- e) Cycle to OPTIONS page 3/3 using the arrow slew keys
- f) Select the CONTROLS page
- g) Select RUDDER PEDALS page
- h) Make sure PEDALS CONTROL NWS is ON and the PEDALS DISC BTN STICKY is ON.

11c

- i) Return to main MCDU MENU

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -DATA

12. Go on FMGC (Flight Management &amp; Guidance Computer) and initialize your flight plan
- a) Press the DATA page button
- b) Select 'A/C STATUS' menu
- c) Check that engine type and active navigation database are correct (we will assume that they are).

## D IFRIP

NOTE: We will prepare the MCDU using the ' DIFRIP ' flow. DIFRIP is just an acronym to help you remember what to initialize and in what order.

D: DATA

- I: INIT
- F: F-PLN (Flight Plan)
- R: RADIOS
- I: INIT ZFG/ZFWCG
- P: PERFORMANCE

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -INIT A

## D I FRIP

13. Go on FMGC (Flight Management &amp; Guidance Computer) and initialize your flight plan in the INIT A page
- a) Press the INIT page button
- b) Type 'EHAM/EGLL' on the MCDU keypad and select LSK next to FROM/TO since we spawned at Schiphol Airport (EHAM) and intend to land at Heathrow (EGLL)
- c) Type 'EGKK' (Gatwick Airport) on the MCDU keypad and select LSK next to ALTN/CO RTE (Alternate / Company Route) in order to set an alternate destination (legally required).
- d) Type your flight number (i.e. Flight No. AFR106) on the MCDU keypad and select LSK next to FLR NBR
- e) Type '30' on MCDU keypad and select LSK next to COST INDEX (cost index is generally given to you by the airline company, so you shouldn't really care about it within the scope of this simulation)
- f) Set cruising altitude to FL240 (24000 ft ) by typing '240' on the MCDU keypad and selecting CRZ FL/TEMP.

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -FLIGHT PLAN

## DI F RIP

NOTE: Flight Plan = EHAM SID GORLO UL980 XAMAN L980 LOGAN STAR EGLL SID: GORL2N                                                 STAR: BIG1E

15. Go on FMGC (Flight Management &amp; Guidance Computer) and set flight waypoints and airways
- a) Cycle the list of waypoints towards GORLO using the arrow slew UP key
- b) Select GORLO
- c) Click on AIRWAYS to set up airway followed after GORLO waypoint
- d) Type 'UL980' on the MCDU keypad and click on the LSK next to the VIA space on the left column (AIRWAYS) to set your next Airway.
- e) Type 'XAMAN' on the MCDU keypad and click on the LSK next to the squared line on the right column (WAYPOINTS) to set your next Waypoint to XAMAN.
- f) Enter remaining Airways and Waypoints as shown in steps d) and e) to complete the flight (L980, LOGAN). See picture to see the final result. We will enter the approach to Heathrow later while in the air.
- g) Click on the LSK next to 'TMPY INSERT' to insert flight plan.

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -FLIGHT PLAN

## DI F RIP

NOTE: Flight Plan = EHAM SID GORLO UL980 XAMAN L980 LOGAN STAR EGLL SID: GORL2N                                                 STAR: BIG1E

15. Go on FMGC (Flight Management &amp; Guidance Computer) and set flight waypoints and airways
- h) Cycle the list of waypoints towards the arrival airport EGLL using the arrow slew UP/DOWN keys
- i) Select EGLL
- j) Click on ARRIVAL to set up our arrival approach
- k) Select ILS 27L as our landing runway
- l) Select STAR (Standard Terminal Arrival Route) for BIG1E as determined when we generated our flight plan.
- m) Click on the LSK next to 'TMPY INSERT' to insert flight plan.
8. by setting the ILS27L runway we will use for our approach via the F-PLN page, the ILS frequency
9. NOTE: (109.50, course 271)  and course are automatically set in the RAD NAV page.

15l

15j

15m

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -FLIGHT PLAN

## DI F RIP

NOTE: Flight Plan = EHAM SID GORLO UL980 XAMAN L980 LOGAN STAR EGLL SID: GORL2N                                                 STAR: BIG1E

16. Go on FMGC (Flight Management &amp; Guidance Computer) and verify all waypoints and any look for any discontinuity
- a) Cycle the list of waypoints towards the arrival airport EGLL using the arrow slew UP/DOWN keys
- b) If there is a route discontinuity between a waypoint and a SID or STAR, you would need to find the F-PLN DISCONTINUITY section, click CLR on the MCDU keypad and click on the LSK next to the F-PLN DISCONTINUITY line. This is not the case in this tutorial, so you can skip that step

## This is what a route discontinuity would look like (between SANDY and ALESO)

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -INIT B (SET FUEL)

NOTE: Remember our fuel calculations of earlier:

Reserve  Fuel = 2500 kg

Total (Block) Fuel = Fuel for Flight + Reserve Fuel = 4500 kg

18. Go to MCDU Main Menu and set fuel payload
- a) Click on MCDU MENU
- b) Select OPTIONS
- c) Select FUEL
- d) Type '4500' on the MCDU keypad (since we need 4500 kgs)
- e) Click on 'TOTAL' menu to set fuel payload
- f) Ta-dah! The aircraft fuel load is now properly set in the sim instead of having to go through the FSX main menu
- g) Click on the LSK next to 'RETURN' to return to the OPTIONS menu
- h) Select PAYLOAD
- i) Write down the ZFW (Zero Fuel Weight) value and ZFW CG (center of gravity), which are 57.0 (57.0 tons, which is 57,000 kg, or 114,000 lbs) and 27.3 % .

DIFR I P

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -INIT B

## DIFR I P

19. Go on FMGC (Flight Management &amp; Guidance Computer) and initialize your Zero Fuel Weight, CG and Fuel parameters
- a) Press the INIT page button and click on the arrow slew RIGHT key to access the INIT B page
- b) On the MCDU keypad, type '57.0/27.3' and click on the LSK next to ZFW/ZFWCG to enter the zero fuel weight (57.0 tons) and the zero fuel weight center of gravity (27.3 %) determined in the previous page with the PAYLOAD page in the OPTIONS menu.
- c) On the MCDU keypad,  type '4.5' on MCDU keypad and click on the LSK next to BLOCK to enter the total fuel quantity (Block) required for the flight determined by Fuel Planner tool (4.5 tons of fuel, or 4500 kg)
- d) And there you have it, your fuel predictions are now initialized.

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -PERFORMANCE

## DIFRI P

20. Go to MCDU Main Menu and find out gross weight in order to set takeoff trim setting

- a) Click on MCDU MENU
- b) Select OPTIONS
- c) Select PAYLOAD
- d) Write down the GW CG (Gross Weight Center of Gravity) value, which is 27.1%
21. Go on FMGC (Flight Management &amp; Guidance Computer) and set performance parameters
- a) Press the PERF page button
- b) Check TAKEOFF TRIM scale on the throttle using the GWCG found earlier (27.1 %). We obtain a takeoff trim of  approx. 0.5 deg UP.
- c) Type '1/UP0.5' on MCDU keypad and select LSK next to 'FLAPS/THS' to set takeoff flaps to 1 degree with a takeoff horizontal stabilizer trim of 0.5 degrees nose up.
- d) Click twice on the LSKs next to V1, VR and V2 to automatically calculate and enter your V speeds.
- e) Observe the resulting V1, VR and V2 speeds resulting of this flap setting and current aircraft weight: V1 is the Decision Speed (minimum airspeed in the takeoff, following a failure of the critical engine at VEF, at which the pilot can continue the takeoff with only the remaining engines), VR is the rotation speed (airspeed at which the pilot initiates rotation to obtain the scheduled takeoff performance), and V2 is Takeoff Safety Speed (minimum safe airspeed in the second segment of a climb following an engine failure at 35 ft AGL).

V1 Speed is 134 kts

VR Speed is 134 kts

V2 Speed is 135 kts

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## FMGC SETUP -PERFORMANCE

## DIFRI P

22. Go on FMGC (Flight Management &amp; Guidance Computer) and set remaining performance parameters (FLEX TO TEMP)

- a) Type '58' on MCDU keypad and click on the LSK next to 'FLEX TO TEMP' to set your FLEX temperature in order to limit your engines' thrust to 58 degrees C.
- b) Verify that the TRANS ALT (transition altitude) is set to 3,000 ft (transition altitude would be 18,000 ft in North America, and 3,000 ft in Europe). Correct it if necessary.
- c) Type '1500/3000' on the MCDU keypad and click on the LSK next to THR RED/ACC (Thrust Reduction/Acceleration Height) to set valid Thrust Reduction (1500 ft) and Acceleration (3000 ft) Heights in ft.
- d) Type '1500' on the MCDU keypad and click on the LSK next to ENG OUT ACC (Engine Out Acceleration Height)

NOTE: THR RED/ACC and ENG OUT ACC Values are automatically generated.  You could leave them as is if you wanted to.

A FLEX takeoff, or 'flexible temperature' takeoff  is  a  fancy  way  of saying that the engine is de-rated during takeoff. De-rating means that the aircraft uses reduced thrust on takeoff in order to  reduce engine  wear,  prolong  engine  life,  reduce  fuel  consumption,  and more importantly comply with  noise  reduction  and  runway  safety requirements.

'Flexible temperature' means  that  the  engine  controller  will  force the engine to behave as if outside air temperature was higher than it really is, causing the engines to generate less thrust since higher air temperatures diminish an aeroengine's thrust generating capabilities. Therefore, the 'FLEX TO TEMP' field of 58 deg C in the PERF page is the pilot telling the engine to behave as if the outside air  temperature  was  58  deg  C,  which  will  result  in  less  thrust,  less noise, and less fuel consumption.

FLEX/De-rating  is  also  known  in  other  companies  as 'Assumed Temperature Derate ', 'Assumed Temperature Thrust Reduction' or 'Reduced Takeoff Thrust' or 'Factored Takeoff Thrust' .

## FMGC SETUP -PERFORMANCE

DIFRI P

## NOTE:

The Thrust Reduction and Engine Out Acceleration Heights are automatically generated, but can be modified. These heights may seem like plugging random numbers in a computer at first, but there is a valid reason for that. Special heights for Thrust Reduction/Acceleration Height, and OEI Acceleration more often than not are dependent on whether there  is  a  NAP  (Noise  Abatement  Procedure),  or  if  there  are  some  company  SOP (Standard Operating Procedure) for other factors like terrain clearance. You can consult Jeppesen charts to see  what  these  Noise  Abatement  procedures  are  for  a  particular  airport.  If  no  particular  procedures  are listed, you can follow the standard procedures in the following document:

ICAO Document 8168, Vol 1, Section 7 - Noise Abatement Procedures

Link: http://www.chcheli.com/sites/default/files/icao\_doc\_8168\_vol\_1.pdf

Like  I  said  before,  the  main  wear  on  engines,  especially  turbine  engines,  is  heat.  If  you  reduce  heat,  the engine will have greater longevity. This is why takeoff power is often time limited and a height established that thrust is reduced. The difference between takeoff thrust and climb thrust may only be a few percent, but the lowering of EGT (Exhaust Gas Temperature) reduces heat and extends engine life significantly.  Acceleration Height is the altitude above ground level (AGL) that a pilot accelerates the aircraft by reducing the aircraft's pitch, to allow acceleration to a speed safe enough to raise flaps and slats, and then reach  the  desired  climb  speed.  The  thrust  reduction  height  is  where  the  transition  from  takeoff  to  climb thrust takes place.

Acceleration  Height (3,000  ft  in  our  case)  is  when  the  nose  is  to  be  lowered  to  allow  the  aircraft  to accelerate.  When  the  aircraft  starts  accelerating  is  when  the  flight  crew  will  retract  flaps  as  per  the schedule. Our value was taken directly from the Jeppesen document.

Thrust Reduction Height (1,500 ft in our case) is when the autothrottle will decrease the engine power to the preselected  climb  thrust;  thereby  reducing  engine  wear  and  tear. Both  may  occur  simultaneously  or  at differing heights above ground level.  Both can be configured in the CDU. Our value was taken directly from the Jeppesen document. If no such value was specified, then we'd have to use 800 ft as the minimal value as per the ICAO document.

EO  ACCEL  HT (1,500 ft in our case) is is the safe altitude that  you  can  lower  the  nose  and start accelerating the  aircraft  in  the  event  of  an  engine  failure.  It  is  based  mainly  on  company  SOP  or  a prescribed  procedure  (EO SID,  as  an  example),  which,  unless  someone  gave  you  one,  you  wouldn't  know what the SOP value is.  For the purposes of the sim, you can just leave it at 1,500 ft. Some UK pilots add the airport elevation to this value.

76

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## AUTOPILOT SETUP

23. Set QNH mode to desired unit system (hPa in our case)
24. Set both FD (Flight Director) switches  ON (illuminated)
25. Set ND (Navigation Display) mode to NAV
26. Set ND range scale to 10 nm
27. Set all ADF/VOR switches to VOR
28. Set FCU (Flight Control Unit) mode to HDG V/S
29. As per EHAM SID Chart, set Initial Altitude (FL060, or 6,000 ft) on FCU panel by rotating ALTITUDE knob on glareshield until Altitude is set to 6,000 ft )

Flight Plan on ND (Navigation Display)

A320

## PART 3 -FLIGHT PLAN &amp; PRE-START

## CABIN PRESSURE &amp; DOORS SETUP

30. On overhead panel, make sure that CREW SUPPLY and PASSENGER oxygen switches are ON (dark)
31. Verify  that  all  doors  are  closed  by  monitoring  the  DOOR  SD (System Description) page
32. If  any  door  is  still  open,  go  in  MCDU  MENU  -&gt;  OPTIONS  -&gt; DOORS and shut remaining doors.

A320

START-UP PROCEDURE

-

PART 4

ENGINE START-UP

APU

AUXILIARY

POWER UNIT

GROUND

POWER  CART

AIR PRESSURE

CART

ENGINE

(RUNNING)

ENGINE MASTER SWITCH

&amp;

THROTTLE POSITION

ENGINE

SELECTION

SWITCH

APU GENERATOR

APU BLEED AIR

EXTERNAL POWER

EXTERNAL AIR

ENGINE GENERATOR

(ENGINE CROSS-START)

ENGINE BLEED

(ENGINE CROSS-START)

MASTER SWITCH ON &amp; THROTTLE AT IDLE

FUEL STARTER VALVE CONTROLS FUEL FLOW

CONTROLLED BY FADEC

SELECTION SWITCH

-

IGNITION START

IGNITION CONTROLLED BY FADEC

FUEL

IGNITION

ELECTRICAL POWER

AIR PRESSURE

ENGINE START

A320

## PART 4 -START-UP PROCEDURE

## ENGINE START-UP

1. On  the  Pedestal,  select  APU  (Auxiliary  Power  Unit)  SD page to monitor APU parameters.
2. On  Overhead  Panel,  press  on  the  APU  MASTER  SW pushbutton
3. When APU MASTER SW light is ON, press the APU START pushbutton to start the APU.
4. Once APU start cycle is finished, the APU AVAIL light will illuminate.

Note:  You  do  not  need  to  press  the  APU  GEN  pushbutton

5. Press the APU BLEED pushbutton since it is active by default.

81

## A320

## PART 4 -START-UP PROCEDURE

## ENGINE START-UP

6. On  the  Pedestal,  select  the  ENG  SD  page  to  monitor engine parameters.
7. Press  all  fuel  pump  pushbuttons  to  extinguish  the  OFF lights
8. Set Engine Selection switch to IGN START
9. Make sure throttle is set to IDLE.
10. Right  click  and  hold  on  ENG  2  Master  Switch  to  pull  it, then left click to push it forward. Engine 2 (right engine) will then start.

Note: You do not need to press the GEN 2 pushbutton since it is active by default.

A320

## PART 4 -START-UP PROCEDURE

## ENGINE START-UP

11. Engine 2 will reach IDLE once N2 reaches approx. 59 % and N1 reaches 18 %.
12. Right click and hold on ENG 1 Master Switch to pull it, then left click to push it forward. Engine 1 (left engine) will then start
13. Engine 1 will reach IDLE once N2 reaches approx. 59 % and N1 reaches 18 %.
14.  Set the Engine Selection switch to NORM

A320

START-UP PROCEDURE

-

PART 4

A320

## PART 4 -START-UP PROCEDURE

## ENGINE START-UP

15. Press the 'EXT PWR' switch to turn off ground power
16. On  Overhead  panel,  confirm  that  the 'EXT PWR' indication  changes from 'ON' to 'AVAIL'
17. Disconnect ground power cart and remove chocks via the MCDU
- a) Select OPTIONS menu
- b) Select 'EXT CTRLS' (External Controls) menu
- c) Make sure the GPU (Ground Power Unit) and GND CHOCKS all display 'CONNECT', which means that they are currently all connected.
- d) Click on the 'GPU -DISCONNECT' LSK to remove ground power. The MCDU will then display 'GPU CONNECT'.
- e) Click on the 'GND CHOCKS -DISCONNECT' LSK to remove chocks. The MCDU will then display 'GND CHOCKS CONNECT'.
- f) Return to main MCDU MENU

A320

## PART 4 -START-UP PROCEDURE

## ENGINE START-UP

18. PACK FLOW (Pneumatic Air Conditioning Kit) switch -NORMAL
19. Probe/Window Heat Control pushbutton -ON
20. Engine Anti-Ice / Wing Anti-Ice pushbuttons -As Required
21. APU BLEED switch -OFF
22. APU Master switch -OFF

22b

86

A320

## PART 4 -START-UP PROCEDURE

## COMPLETE PRE-FLIGHT

23. Set Nose Light switch -TAXI
24. Set Runway Turnoff Lights switch -ON
25. Set Landing Light switches -ON
26. Set Beacon Anti-Collision Light switch -ON
27. Set Strobe Position Lights switch -ON
28. Set Navigation &amp; Logo Lights switch -1 (lights set 1 ON)
29. Set Signs -Emergency Lights switch - ON
30. Set Transponder switch -AUTO
31. Set Transponder ALT RPTG (Altitude Reporting) switch -ON
32. Set Transponder frequency to 7000 (VFR standard squawk code for most of European airspace, or 1200 if in North America) by pressing CLR on the keypad and then 7000
33. Set TCAS (Traffic Collision and Avoidance System) selector to TA/RA (Traffic Advisory/Resolution Advisory) using right-click.
34. On  Weather  Radar  panel,  set  PWS  (Predictive  Windshear  System) switch to AUTO

A320

## PART 4 -START-UP PROCEDURE

## COMPLETE PRE-FLIGHT

35. In real life, you would set PACK 1 and PACK 2 pushbuttons to OFF to ensure maximal engine performance during takeoff and prolong engine life, but we don't need to in this tutorial.
36. Press the AUTO BRK (Autobrake) -MAX pushbutton to arm  the  autobrake  system  in  the  event  of  a  rejected takeoff
37. Press the TO CONFIG button on the central pedestal to check normal takeoff configuration on the upper ECAM display.  We  see  in  cyan  what  corrective  actions  we need to take. We see that the signs (seat belts and no smoking lights) need to be set to ON, that we need to arm the speed brake, and that the flaps are not set in takeoff position.
38. Set SEAT BELTS sign light to ON and NO SMOKING sign light to AUTO
39. Arm Speed Brake by pulling (right-clicking) on it in the ARMED position.
40. Set Flaps lever to 1 as specified in the FMGC
41. Press  the  TO  CONFIG  button  again  and  confirm  that everything is set for takeoff.

A320

## PART 4 -START-UP PROCEDURE

## COMPLETE PRE-FLIGHT

35. In real life, you would set PACK 1 and PACK 2 pushbuttons to OFF to ensure maximal engine performance during takeoff and prolong engine life, but we don't need to in this tutorial.
36. Press the AUTO BRK (Autobrake) -MAX pushbutton to arm  the  autobrake  system  in  the  event  of  a  rejected takeoff
37. Press the TO CONFIG button on the central pedestal to check normal takeoff configuration on the upper ECAM display. We see in cyan what corrective actions we need to  take.  We  see  that  the  signs  (seat  belts  and  no smoking lights) need to be set to ON, that we need to arm the speed brake, and that the flaps are not set in takeoff position.
38. Set SEAT BELTS sign light to ON and NO SMOKING sign light to AUTO
39. Arm Speed Brake by pulling (right-clicking) on it in the ARMED position.
40. Set Flaps lever to 1 as specified in the FMGC
41. Press  the  TO  CONFIG  button  again  and  confirm  that everything is set for takeoff.

A320

TAXI

-

PART 5

## PUSHBACK

1. Set Nosewheel Steering Pin via the MCDU
- a) Select OPTIONS menu &gt; 'EXT CTRLS' (External Controls)
- b) Make sure the NWS PIN displays 'SET', which means that it is currently removed.
- c) Click on the 'NWS PIN' LSK to set nosewheel steering pin. The MCDU will then display 'NWS PIN REMOVE', and the 'NW STRG DISC' amber caution will illuminate on the upper ECAM display.
- d) Return to main MCDU MENU
2. Release parking brake
3. Set Anti-Skid and Nosewheel Steering (A/SKID &amp; N/W STRG) switch to ON (UP)
4. Begin Pushback by holding SHIFT and P to initiate pushback. Once you have enough room to steer the aircraft away from the gate, hold SHIFT and P a second time to stop the push.
5. Remove Nosewheel Steering Pin via the MCDU once pushback is complete as shown in step 1). The MCDU will then display 'NWS PIN SET' and the 'NW STRG DISC' amber caution will extinguish on the upper ECAM display

A320

TAXI

-

PART 5

PUSHBACK

A320

TAXI

-

PART 5

## TAXI

Unless you use a program called FSUIPC, we will assume that you cannot map a joystick axis to your nosewheel  steering  tiller.  Therefore,  in  order  to  steer  the  aircraft,  Flight  Sim  Labs  programmed  a 'Rudder Disconnect' keyboard  command that  allows  you to  use your  rudder pedals like a  tiller.  By default, this keyboard command is 'Comma' .  You can modify it by pressing ALT, then going in AddOns-&gt; FSLabs-&gt;Keyboard Commands.

## When you press RUDDER DISCONNECT key (Comma) a first time:

Your rudder pedals will control the nosewheel steering, not the rudder.

Nosewheel range up to +/- 75 degrees turn. Rudder doesn't physically  move,  but  nosewheel    does move.

## When you press RUDDER DISCONNECT key (Comma) a second time:

Your rudder pedals will control the both the rudder and the nosewheel steering.

Nosewheel range up to +/- 6 degrees turn. Rudder and NWS both move, but with less range.

## Pedal Disconnect Button.

Used to disconnect rudder pedals from nosewheel steering system in order to do rudder pedal checks.

A320

## PART 5 -TAXI

## TAXI

- Our Flight Number is AFR106 and we spawned at gate F6.
- After  we  performed  pushback  from  Gate  F6,  we  would  typically  contact the tower for guidance by saying 'AFR 106, requesting taxi. '
- The tower would then grant you taxi clearance by saying 'AFR 106, taxi to holding position N5 Runway 09 via taxiways Alpha 16 (A16), Bravo (B).
- This means that we will follow the A16 line, then go to B, then turn right to N5 and hold there until we get our clearance for takeoff.
- Throttle  up  to  maximum  40  %  N1  and  maintain  a  taxi  speed  of  15  kts maximum. Slow down to a maximum of 10 kts before making a 90 deg turn.

A320

TAXI

-

PART 5

Check signs to follow the taxi route towards the holding point (N5)

A320

TAXI

-

PART 5

95

A320

## PART 6 -TAKEOFF, CLIMB &amp; CRUISE

## TAKEOFF

1. Line up on the runway and make sure parking brake is disengaged.
2. Click on the F/CTL menu and make sure your control surfaces respond to pitch, roll and rudder input. If your rudder doesn't move, it means that you need to press the 'RUDDER DISCONNECT' key (comma).
3. Set Nose Light switch -TAKEOFF (T.O.)
4. Press and hold pedal brakes.
5. Throttle up until engines reach 50 % N1 and stabilize
6. Throttle up to FLEX/MCT power for a normal takeoff or TO/GA for a max power takeoff. You should hear a 'click' when you hear the detent. Autothrottle will then engage automatically.
7. Rotate smoothly and continuously when reaching VR (134 kts) until reaching 15 degrees of pitch angle
8. Follow the Flight Director (15 deg pitch)
9. Raise landing gear by left-clicking the landing gear lever and dragging it to the UP position

3

6b

A320

## PART 6 -TAKEOFF, CLIMB &amp; CRUISE

TAKEOFF

A320

## PART 6 -TAKEOFF, CLIMB &amp; CRUISE

## CLIMB

1. When  reaching  an  altitude  of  100  ft,  you  can  engage  autopilot  by pressing the 'AP 1 ' button on the FCU. Your aircraft will now follow the 'green line' on  your  navigation  display  automatically.  Since  our  SID trajectory demands a sharp turn after takeoff, I would advise hand flying the aircraft first by following the flight directory lines on the PFD, and when you are in a straight line segment then engage autopilot.
2. When 'LVR CLIMB' indication  flashes  on  your  PFD,  throttle  back  to CLIMB. You should hear a 'click' when detent is reached. The indication will change to 'THR CLB' on your PFD.
3. To confirm that you have a normal climb, make sure you see THR CLB, CLB  and  NAV  all  displayed  in  green  on  your  FMA  (Flight  Mode Annunciator).

A320

## PART 6 -TAKEOFF, CLIMB &amp; CRUISE

## CLIMB

4. Once you pass transition altitude (3000 ft in Europe, 18000 ft in the US), right click on the Barometric Pressure knob to switch barometric pressure to STANDARD pressure in order to use flight levels as a reference. This means you will be using a standard barometric pressure of 1013, which is also used by other aircraft in the airspace instead of a local one given by an Air Traffic Controller. If pilots don't use a 'standard' barometric pressure, different aircraft may collide in flight since they don't use the same pressure to define their current altitude. This is why higher altitudes are defined as 'flight levels' (i.e. FL250 would be 25000 ft).

Transition Altitude (U.S. system)

STD means that you are using standard barometric reference

99

## A320

## PART 6 -TAKEOFF, CLIMB &amp; CRUISE

## CLIMB

5. Once you have sufficient airspeed (green -S on the speed tape, for « slat &amp; flaps retraction speed », set flaps to UP by right-clicking the flaps lever
6. Set Nose Light switch -OFF
7. Set Runway Turnoff Lights switch -OFF
8. Set Landing Light switches -OFF
9. Set Beacon Anti-Collision Light switch -ON
10. Set Strobe Position Lights switch -AUTO
11. Set Navigation &amp; Logo Lights switch -1
12. Seat Belt signs light switch -OFF
13. You will reach your 'TOP OF CLIMB' point at a blue arrow on your navigation display

A320

## PART 6 -TAKEOFF, CLIMB &amp; CRUISE

## CLIMB

14. We will now begin our climb to our cruising altitude of 24000 ft. Set the ALTITUDE knob on the FCU (Flight Control Unit) to 24000.
15. Pull the autopilot ALTITUDE set knob (right click) to select this cruising target altitude for the autopilot. It will override the altitude target of the FMGS.
16. Set the autopilot Vertical Speed knob on the FCU to 2200 feet per minute (typical climb rate). This will ensure a smooth climb and make the passengers not feel like they're about to puke while riding a roller coaster.
17. You will reach your 'TOP OF CLIMB' point at a blue arrow on your navigation display for your cruising altitude (24000 ft)

Takeoff

The orange dot means that the FMGS is managing this parameter. Managed mode is achieved by pushing the parameter knob (give control back to the aircraft).

No Orange dot means that the autopilot is trying to maintain your selected parameter. Selected mode is achieved by pulling the parameter knob ('my aircraft', you have control over the aircraft).

A320

AUTOPILOT

-

PART 7

## Introduction to Autopilot

Many newcomers in the flight simulation world have this idea that on the A320, the autopilot is the answer to EVERYTHING. And I mean: e-v-e-r-y-t-h-i-n-g. Spoiler alert: it's not. The autopilot is a tool to help you fly to reduce your workload, not a tool to replace the pilot.

Now, why am I saying this? Because some people's knowledge of the autopilot system is summed up in 'hit AP, then go watch an episode of Mayday while the aircraft does all the work' .  However, there are times where the autopilot can disconnect by itself (i.e. during major turbulence, or when the autopilot is trying to follow a flight profile (SID or STAR) that exceeds safety limitations like bank or pitch angles). The autopilot isn't smart: it will put you in dangerous situations if you ask him to. This is why you need to constantly to be able to fly the aircraft manually if need be.

The autopilot should be seen as a system that can make your life easier. This is why you need to be familiar with its capabilities and be able to read what the FMA (flight mode annunciator) is telling you.

## Autopilot and Auto-Throttle

The autopilot is separated in three main components: the flight director, the autopilot itself and the auto-thrust system. Aircraft pitch and attitude will  help  maintain  the  aircraft  on  a  certain  flight  path.  The  throttle  will help maintain the aircraft on a certain speed. Depending on the phase of flight  (takeoff,  climb,  cruise,  descent, final approach, etc.), the autopilot will  react  differently.  During  a  climb,  the  AP  will  want  to  maintain  the best, most fuel-efficient climb to save fuel. During a descent, the AP will want to slow down in order to approach the runway in a low-speed highlift configuration. The Auto-Thrust system will control the engines for you. Take note that when auto-throttle is engaged, the physical throttles will not move but the engines will respond to autopilot thrust commands.

Managed mode  means  the  autopilot  follows  the  flight  management  system  plan. Selected means  the  pilot  chooses  the  parameter  (speed,  heading  or  altitude  for example), overriding the FMC. Some axes can be managed while others are selected. Autopilot and autothrottle will be affected depending on what mode is active

The AP has two channels: A and B. This is  why  you need to be  careful when  setting  values  on  the  MCP  (Main  Control  Panel)  by  making  sure there are no conflicting AP commands on both the Captain and the First Officer's side.

A320

## PART 7 -AUTOPILOT

Autopilot Parameter Selectors

Tip: When pulling a knob, it's YOUR aircraft (selected input will drive autopilot). When pushing a knob, the FMGS takes over (managed aircraft flight plan will drive autopilot).

- SPD MACH:  Change over airspeed unit (IAS (indicated airspeed) vs Mach), usually used above FL260, or 26000 ft

Note: These speed, heading, altitude and vertical speed autopilot commands  can  be  combined  together.  It  is  very  important  to  know whether  you  set  them  in 'managed' (the  FMGS  flight  plan  restrictions drive the autopilot) or 'selected' (your selected value drives the autopilot) mode. 'Managed' mode  will  display  an  orange  circle. 'Selected' mode will have no circle.

- METRIC ALT: Toggles altitude unit system (metric vs imperial)
- SPEED Selector: When pulled, autopilot and auto-throttle will set the aircraft at the selected speed. When pushed, autopilot and auto-throttle will set the aircraft at the managed speed of the FMGS (flight plan).
- HEADING Selector: When pulled, autopilot and auto-throttle will set the aircraft at the selected heading. When pushed, autopilot and auto-throttle will set the aircraft at the managed heading of the FMGS (flight plan).
- ALTITUDE Selector: When pulled, autopilot and auto-throttle will set the aircraft at the selected altitude. When pushed, autopilot and auto-throttle will set the aircraft at the managed altitude of the FMGS (flight plan). Note that the autopilot will not go below waypoint altitude restrictions (in magenta on PFD altitude tape) in managed mode, while in selected mode it will ignore such restrictions (i.e. if you get clearance from an Air Traffic Controller).
- VERTICAL SPEED Selector: When pulled, aircraft will follow vertical speed selected. When pushed, aircraft will level off.

A320

AUTOPILOT

-

PART 7

## Autopilot, Flight Director &amp; Autothrottle Selectors

- Autothrottle (A/THR) ARM Switch : Arms A/T for engagement. Autothrottle engages automatically.
- Flight Director (FD) Switch: Arms flight director
- AP 1/2: Engages autopilot in selected mode.

## Autoflight -Vertical Modes

- EXPED: Engages EXPED mode to reach the altitude window with maximum vertical gradient.

## Autoflight -Lateral Modes

.

- LOC:  Tracks VHF Ominidirectional Range (VOR) localizer. Aircraft will only be controlled laterally. Used in case the ILS system is unserviceable.
- NOTE: LS is not an autopilot mode. Pressing this button displays ILS (Instrumented Landing System) information on the PFD.

## Autoflight -Vertical + Lateral Mode

- APPR: Tracks localizer and glideslope during approach. Aircraft will be controlled laterally and vertically.

## FMA (Flight Mode Annunciator)

The FMA displays the status of the auto-throttle, vertical mode, lateral mode, and autopilot systems.

First row is for ENGAGED systems, second row if for ARMED systems, third row is for reminders.

| 1: Autothrust                                                                                            | 2: Vertical                                                                                          | 3: Lateral                                                | 5: Autopilot                                |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|---------------------------------------------|
| TOGA : autothrust armed, throttle at TOGA (Takeoff Go- Around) detent                                    | SRS : Speed Reference System used for takeoff and go-around                                          | RWY : Runway mode                                         | AP : Autopilot Command Engaged              |
| FLX 42 : Autothrust armed, throttle at FLC/MCT detent                                                    | ALT/ALT* : Altitude Hold/Capture mode                                                                | RWY TRK : Runway Track mode                               | FD : Flight Director Engaged (no autopilot) |
| MCT : Single Engine - Autorthust armed, most forward lever at MCT (Max Continuous Thrust) detent         | ALT CRZ/CST : Altitude hold of the cruise flight level / altitude constraint hold                    | GA TRK : Go Around Track mode                             | A/THR : Autothrottle engaged                |
| CLB : Autothrust armed, throttle at CLB (Climb) detent                                                   | V/S : Vertical Speed Mode                                                                            | TRACK : Track mode                                        |                                             |
| IDLE : Auto thrust armed, IDLE power commanded                                                           | CLB : Climb mode                                                                                     | HDG : Heading mode                                        |                                             |
| ASYM : Asymmetric thrust (autothrust armed but both levers in different positions)                       | DES : Descent mode                                                                                   | NAV : Navigation mode                                     |                                             |
| A. FLOOR: Autothrust engaged while in Alpha Floor conditions                                             | OP CLB/DES : Open Climb or Descent mode. FCU selected altitude is higher/lower than actual altitude. | LOC/LOC* : Localizer track/capture mode                   |                                             |
| TOGA LK : TOGA lock is engaged following alpha floor engagement.                                         | EXP CLB/DES : Expedite mode in climb or descent                                                      | APP NAV : Approach Navigation mode                        |                                             |
| THR LK : Thrust locked at last known position (A/THR failure or disconnect)                              | G/S : Glide slope mode                                                                               |                                                           |                                             |
| MANTOGA/FLX/MCT/THR : Autothrust armed, at least one throttle is at TOGA/FLX/MCT/Above CLB detent.       | FINAL : Final mode (non precision approach)                                                          |                                                           |                                             |
| THR MCT/CLB/LVR/IDLE : Thrust mode active at MCT/CLIMB/Undetermined Lever Position/Minimum Thrust detent | FPA :Flight Path Angle mode                                                                          |                                                           |                                             |
| SPEED : Autothrust armed in SPEED mode                                                                   | LAND : Landing mode engaged below 400 ft AGL                                                         | LAND : Landing mode engaged below 400 ft AGL              |                                             |
| MACH : Autothrust armed in MACH mode                                                                     | FLARE : Flare mode                                                                                   | FLARE : Flare mode                                        |                                             |
| LVR CLB/MCT : Request to set thrust levers in CLB or MCT detents.                                        | ROLL OUT : Roll out mode (Autoland)                                                                  | ROLL OUT : Roll out mode (Autoland)                       |                                             |
| LVR ASYM : Request to set both thrust levers in same position/detent.                                    | FINAL APP : Final approach mode during a Non-ILS approach                                            | FINAL APP : Final approach mode during a Non-ILS approach | 106                                         |

## FLIGHT ENVELOPE PROTECTION

You will often hear people mention 'Normal Law' or 'Alternate Law' .  These  flight  control  laws  are  basically  sets  of  automated protections  applied to  your flight  control surfaces that will prevent your aircraft from doing unsafe manoeuvers or exceed limitations.  Normal Law is always active unless you start pulling circuit breakers. Flight Control Law changes happen automatically.  Here is a great link to the Airbus Flight Control Laws: http://www.airbusdriver.net/airbus\_fltlaws.htm

## FLIGHT CONTROL LAWS

| NORMAL LAW                                                                                                                                                                                                                            | ALTERNATE LAW                                                                                                                                                                                                                                                                          | ABNORMAL ALTERNATE LAW                                                                                                                                                                                                   | DIRECT LAW                                                                                                                                                                                                                                                                                                                                      | MECHANICAL BACKUP                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Normal operating configuration of the system. Airplane cannot be stalled in this law. Covers 3-axis control, flight envelope protection and load alleviation with 3 modes according to phase of flight (Ground, Flight or Flare Mode) | Activated by the aircraft if multiple failures of redundant systems occur.. Airplane can be stalled in this law. Reduced protections in comparison to Normal Law with 3 modes according to phase of flight (Ground, Flight or Flare Mode). ALTN LAW: PROT LOST caution message on ECAM | Activated by the aircraft if it enters an unusual attitude, allowing recovery from the unusual attitude. Pitch law becomes Alternate without protections, while Roll law becomes Direct law with mechanical yaw control. | Lowest level of computer flight control and occurs with certain multiple failures. Activated when landing gear is down while flying in alternate law. Pilot control inputs are transmitted unmodified to the control surfaces, providing a direct relationship between sidestick and control surface. USE MAN PITCH TRIM caution message on PFD | In case of a complete loss of electrical flight control signals, the aircraft can be temporarily controlled by mechanical mode. Pitch control is achieved through the horizontal stabilizer by using the manual trim wheel, lateral control is accomplished using the rudder pedals (requires hydraulic power). MAN PITCH TRIM ONLY caution message on PFD |
| PROTECTIONS • High AoA Protection • Load Factor Limitation • Pitch Attitude Protection • High Speed Protection • Flight Augmentation (Yaw) • Bank Angle Protection • Alpha Floor                                                      | PROTECTIONS • Low Speed Stability • Load Factor Limitation • High Speed Stability • Yaw Damping Only                                                                                                                                                                                   | PROTECTIONS • Load Factor Limitation • Yaw Damping Only                                                                                                                                                                  | PROTECTIONS • None                                                                                                                                                                                                                                                                                                                              | PROTECTIONS • None                                                                                                                                                                                                                                                                                                                                         |

107

A320

## PART 8 -PROTECTION SYSTEMS

## FLIGHT ENVELOPE PROTECTION

There  are  seven  flight  control  computers:  the  3  SEC's  (Spoiler  Elevator  Computers),  the  2  ELAC's (Elevator Aileron Computers) and 2 FAC's (Flight Augmentation Computers.

## Their uses:

ELAC = Normal elevator and stabilizer control. Aileron control.

SEC = Spoiler control. Standby elevator and stabilizer control

FAC = Electrical Rudder control.

It is through these seven computers and their associated software that programs like Alpha Floor and speed &amp; attitude protection work. If one or more of those computers fail or are switched off, you may lose some of the protections, thereby going into alternate or direct law. But if all seven fail or there is a complete electrical failure or if you switch all seven off, then you are in mechanical reversion. At that point you only have cable operated rudder and cable operated stabilizer trim available for control. The sidestick would be so much useless plastic because you need at least one of those computers running for it to work.

Great link on Flight Control Laws: https://www.scribd.com/doc/64148571/Airbus-A320-Flight-Controls-Laws

A320

## PART 8 -PROTECTION SYSTEMS

As an example, we can 'simulate' a change in flight control laws by forcing the aircraft to power off certain flight computers with the switches shown last page. Here are some tests I did just for fun to illustrate this point:

## TEST 1: ELAC 1 and ELAC 2 off = ALTERNATE LAW

## TEST 2: ELAC 1 and ELAC 2 off  and landing gear deployed = DIRECT LAW

## TEST 3: ALL ELAC, FAC &amp; SEC switches OFF = MECHANICAL BACKUP

A320

## FLIGHT ENVELOPE PROTECTION - NORMAL LAW

Normal Law is the normal operation of flight control systems. In theory, you should always be operating  with  normal  law  unless  something  breaks  in  the  aircraft  due  to  a  malfunction. Normal  Law  covers  the  Flight  Envelope  Protection  and  Load  Alleviation.  Load  Alleviation  is provided  by  dedicated  accumulators  to  help  move  the  ailerons  and  spoilers  4  and  5  very rapidly to alleviate the load on the wings during turbulence.

Normal Law has a set of protections that work in conjunction with the flight control computers.

## 1. High AoA Protection

- When angle of attack (AoA ) exceeds a certain angle, the elevator control changes to the 'Alpha Protection' mode in which the AoA is proportional to sidestick deflection. Alpha Max cannot be exceeded by the pilot even with full aft sidestick deflection

## 2. Load Factor Limitation

- Keeps pilot from exceeding g-loads in all configurations

## 3. Pitch Attitude Protection

- Pitch limited to +30 deg / - 15 deg

## 4. High Speed Protection

- Prevents exceedance of Vmo/Mmo (Maximum Operating Speed/Mach) by inducing a pitch up load factor demand, which cannot be overridden by the pilot
5. Flight Augmentation (Yaw)
- Controls yaw damper

## 6. Bank Angle Protection

- Bank angle limited to 67 deg

## 7. Low Energy Warning

- 'Speed, speed!' aural warning warns the pilot in low energy states that require immediate throttle input. Available in Flaps Config 2, 3 or Full between 200 0 ft and 100 ft RA (radar altimeter) when TOGA (Takeoff Go-Around) is not selected.

## 8. Alpha Floor

- Predictive function of the autothrust system. It activates based on the current trend if it predicts thrust will be required. Is normally available from immediately after takeoff throughout the flight down 100 feet RA in flaps configuration 1 or greater.
- As an example, if the aircraft starts stalling, the auto-thrust system will automatically set the engines to TOGA in order to keep the aircraft flying.

A320

## PART 9 -APPROACH &amp; LANDING

## PLANNING DESCENT

So, you've finally made it all the way up to your cruising altitude? Congrats! Now, we have a bit of planning to do.

First, let's introduce you to the ILS (Instrument Landing System).  This  system  exists  to  guide  you  during  your approach.

- The  Localizer  is  generally  an  array  of  antennas  that will  give  you a lateral reference to the center of the runway.
- The  Glide  Slope  station  will  help  you  determine  the descent  speed  you  need  in  order  to  not  smack  the runway in a smoldering ball of fire.

A320

## PART 9 -APPROACH &amp; LANDING

## PLANNING DESCENT

These charts are for the STAR (Standard Terminal Arrival  Route)  from  LOGAN  to  EGLL.  We  intend to:

1. Come from LOGAN waypoint
2. Fly  from  LOGAN  towards  the  BIG1E  arrival route.
3. Follow the STAR (BIG1E -&gt; KOPUL -&gt; TANET &gt; DET -&gt; BIG)
4. Select an AIF (Approach Initial Fix) from the FMC database (in our case CI27L) and follow the approach towards the runway, guided by the  EGLL airport's ILS  (Instrument  Landing System).
5. Land  at  Heathrow  (EGLL)  on runway  27L (orientation: 270 Left)

A320

## PART 9 -APPROACH &amp; LANDING

## PLANNING DESCENT

## Final Approach Course: 271

This  is  the  heading  you  will  take  when approaching for final landing.

## Minimums in BARO:  277

This  is  the  minimum 'decision altitude' (DA) during landing. If you go lower than 277  ft,  you  are  committed  to  land  no matter  what  happens.  Above  277  ft,  you can still miss your approach and go around.

## ILS Frequency: 109.50 MHz

This  is  the  ILS  system  frequency  you  will track to guide your aircraft for landing.

## Missed Approach Standby

## Frequency: 113.60 MHz

VOR 'LONDON' (LON)  will  be  the  beacon we will track in case we miss our approach and have to go around.

## Missed Approach Procedure

In case we miss our approach, the procedure is to climb straight ahead. When passing  1080  ft,  we  climb  LEFT  on heading 149 to 2000 ft. When passing VOR beacon D6.0 LON, we must climb to 3000 ft and wait for instructions from the tower.

## Transition Level &amp; Transition Altitude

The transition altitude is the altitude at or below which the vertical position of an aircraft is controlled  by  reference  to  altitudes  (6000  ft  on chart).  The  transition  level  is  the  lowest  flight level available for use above the transition altitude.  Our  transition  level  is  defined 'by ATC' (Air  Traffic  Controller).  In  that  case,  a  rule  of thumb is to add 1000 ft to the transition altitude which give us FL070, or 7000 ft.

Here is a great link to know how to read these charts properly:

https://community.infinite-flight.com/t/howto-read-an-approach-chart/8952

A320

## PART 9 -APPROACH &amp; LANDING

## PLANNING DESCENT

1. We have already selected in our FMC our Arrival runway as ILS27L and our arrival STAR 'BIG 1 E' and our Initial Approach Fix 'CI 27 L' at  the  beginning.  Normally,  we  do  this  before  we  begin  our approach. See the 'FMGC SETUP -FLIGHT PLAN' section.
2. Go  on    FMGS  PERFORMANCE  page  on  the  MCDU  to  set  FMGC parameters for your approach and arrival
3. Click on 'NEXT PHASE' until you reach the 'APPR' (approach) page
4. Set QNH (barometric pressure) setting to 1030 by typing ' 1030 ' on MCDU keypad and clicking on LSK next to QNH
5. Set temperature to 15 deg C by typing ' 15 ' on MCDU keypad and clicking on LSK next to TEMP
6. Set  magnetic  heading  and  wind  correction  to  271  and  5  kts  by typing ' 271/05 ' on MCDU keypad and clicking on LSK next to MAG WIND
7. Set Transition Level to FL070 and by typing ' 70 ' on MCDU keypad and clicking on LSK next to TRANS FL
8. Set  MINIMUMS  (Decision  Height)  to  277  ft  by  typing ' 277 ' on MCDU keypad and clicking on LSK next to 'DH'
9. Verify that LDG CONF (Landing Configuration) flaps setting is set to FULL.
10. Set AUTOBRAKE to LO

A320

## PART 9 -APPROACH &amp; LANDING

## PLANNING DESCENT

11. On FCU (Flight Control Unit), set Final Descent Altitude to 2000 ft. The aircraft will not start descending yet because it hasn't reached the Top of Descent point, represented with a white arrow.
12. Go in the PERFORMANCE page of the FMGC to monitor your flight progress. You can monitor your distance to the Top of Climb for instance.
13. Go in the PROGRESS page of the FMGC and select the 'REPORT' page to make sure that you have enough distance to perform your approach at a 3 deg glide slope. You can use the following rule of thumb: Required Descent Distance = (Altitude x 3)/1000 + (10 nm for deceleration) = (24000 x 3)/1000 + 10 = 72 + 10 = 82 nm

A320

## PART 9 -APPROACH &amp; LANDING

## DESCENT &amp; APPROACH

1. Once you reach the Top of Descent point, set ALTITUDE knob to 2000 ft and press it (left click) to engage a 'managed mode' descent.
2. Once our descent profile is initiated, click on the 'STD' BARO button to set barometric pressure instead of standard pressure. In our case, we will assume the tower told us to leave the barometric pressure at 1030 hPa.
3. When reaching FL100, set LANDING LIGHTS to ON and SEAT BELTS light to ON.

A320

## PART 9 -APPROACH &amp; LANDING

## SECURING APPROACH

1. Before you reach the last waypoint of the STAR (BIG), the tower should be able to clear us for open descent to 2000 ft.
2. Once you fly over the Deceleration Point (can be monitored on the Navigation Display or the DECEL menu in the 'F -PLN' FMGC page), your aircraft will start losing speed and will begin your approach.
3. Once you crossed the Deceleration Point, open up the PERF page on your FMGC and click two times on the LSK next to 'ACTIVATE APPR PHASE'.

117

A320

## PART 9 -APPROACH &amp; LANDING

## SECURING APPROACH

4. Press the 'LS' button to show ILS information on the PFD.
5. Once you are at least 25 nm from ILS approach (a bit before Approach Fix CI27L), press the 'APPR' autopilot mode to arm both LOC (Localizer) and G/S (Glide Slope) modes.
6. Press the 'AP2' button to arm the Autoland autopilot mode (this mode requires a second autopilot channel).
7. Set Navigation Display mode to LS to check for localizer and glide slope.
8. When LOC (localizer) is captured, the PFD will indicate in green that the 'LOC' autopilot mode is active.
9. Set Flaps lever to 1
10. Set Navigation Display mode back to NAV
11. When glide slope is captured,/the PFD will indicate in green that the 'G/S' autopilot mode is active.
12. Set Flaps lever to 2
13. Once localizer (lateral guidance) and glide slope (vertical guidance) are both captured, you can now set your autopilot altitude to the Go-Around Altitude of 3000 .

4

5

6

118

A320

## PART 9 -APPROACH &amp; LANDING

## FINAL APPROACH

1. Once you are at 1500 ft on final approach, set landing gear down.
2. Set flaps to FULL.
3. Arm Speed Brake
4. Set all lights ON
5. The Autoland will use three autopilot modes.
- When flying at 400 ft, the autopilot will switch to LAND mode in order to set the aircraft in a proper altitude and attitude to flare properly.
- When flying at 50 ft, the autopilot will switch to FLARE mode in order to flare the aircraft to have a smooth touchdown.
- On touchdown, the autopilot will switch to ROLLOUT mode. This mode will keep the aircraft on the runway centerline.

Another procedure is to disconnect both Autopilot AP1 and AP2 switches and the Autothrottle switch just before landing and follow the flight director to the runway by flying manually.

ILS Information Frequency Distance to ILS

3 Armed (UP)

A320

## PART 9 -APPROACH &amp; LANDING

## LANDING

1. When you hear an audio cue 'MINIMUM', this means you have reached your minimal decision altitude. You are now committed to land.
2. At 20 ft, pull up slightly to reduce rate of descent
3. At 10 ft, throttle back to IDLE
4. On touchdown, push the nose into the ground to improve adherence with the runway and maximize braking (the Autobrake system will already brake for you)

Glide Slope Captured

Localizer Captured

A320

## PART 9 -APPROACH &amp; LANDING

121

## A320

## PART 9 -APPROACH &amp; LANDING

## LANDING

5. Press and hold 'F2' ('Throttle decrease quickly' binding) to deploy thrust reversers until you slow down enough to vacate the runway safely.

The Thrust Reverser lever can be moved by pressing and holding the 'Throttle (decrease quickly)' control mapped to your joystick. Make sure that the 'Repeat' slider is set fully to the right. The default key binding is 'F2'.

Take note that the Reverse Thrust lever can only be engaged if your throttle is at IDLE. The reason for that is a mechanical stopper that prevents you from engaging thrust reversers at high throttle settings.

## PART 9 -APPROACH &amp; LANDING

124