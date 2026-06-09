# The KaziPad
A 3x3 macropad with a rotary encoder, and OLED screen, reprogrammable to meet the needs of anyone.
<img width="995" height="660" alt="image" src="https://github.com/user-attachments/assets/e68adb58-7db9-407b-8118-36ef382ac9b0" />

## What is This?

It is a custom macropad powered by a **Seeed XIAO RP2040** microcontroller and **KMK Firmware**, allowing it to be fully customizable and compact.

Have you ever felt like you need more keys, want a little hack station, or simply just love pressing buttons?

Well, then the **KaziPad** is for you!

### Features:
- 3x3 Matrix for 9 beautiful sounding keys
- One Rotary Encoder that you can twist and press to your hearts desire
- One .91" OLED Screen to display whatever you wish
- Custom PCB to eliminate the need for messy wires
- A 3D printed Case for accessibility and ease
- Custom KMK Firmware which allows easy reprogramming

## Custom PCB
Schematic

<img width="930" height="647" alt="image" src="https://github.com/user-attachments/assets/7929933f-c34a-495a-bafd-58e466485657" />

PCB

<img width="581" height="542" alt="image" src="https://github.com/user-attachments/assets/91268e79-ae46-4bdc-a142-e4ff189b88d0" />

3D Model

<img width="798" height="726" alt="image" src="https://github.com/user-attachments/assets/033a8947-5234-41be-93d7-c4e1f41ef7aa" />

Made With Kicad

## 3D Printable Case

Top Plate of Case

<img width="947" height="568" alt="image" src="https://github.com/user-attachments/assets/d12934ea-53e9-438c-ac5d-47b06bc2adbb" />

Bottom Plate of Case

<img width="857" height="568" alt="image" src="https://github.com/user-attachments/assets/55b7b107-ab32-4d91-a6bb-c745b2a21093" />

Made With Autodesk Fusion 360

## Preset Functions:

(My custom firmware comes with this included, but feel free to change it to better meet your needs!)

### Rotary Encoder:

|Turn Left | Turn Right | Press |
|----|-----|-----|
|Volume Up | Volume Down | Toggle Layers |


### Keys Base Layer:

|Col1 | Col2 | Col3|
|----|----|----|
|Ctrl + C | Ctrl + V | Ctrl + X |
|Ctrl + A | Ctrl + F | Ctrl + Z |
|Left Arrow| Up Arrow | Right Arrow|

### Keys Numpad Layer:

|Col1 | Col2 | Col3|
|----|----|----|
|7 | 8 | 9 |
|4 | 5 | 6 |
|1 | 2 | 3 |

## How To Use:
- Download CircuitPython and KMK onto your Seeed XIAO RP2040
- Drag and Drop the `main.py` file from the firmware onto your Seeed XIAO RP2040
- Save, and click away!

## How Does It Work?

- PCB and Schematic - The keys are wired in a 3x3 matrix which limits the amount of pins used in order to save space for for other components. After all the connections were established, I began laid each component out and wired them. The final **KaziPad** PCB that you see today is actually V4 of the PCB due to my wish to make it smaller and more aesthetically pleasing. It was designed with **Kicad**, an entirely free PCB designing program.
- Case - The Case is made up of two parts, a top plate, and a bottom plate. The bottom plate is where the PCB will sit, so the dimensions had to accomodate that. Additionally, each key, the OLED display, and the microcontroller are meant to be visible from the top plate, which meant I spent countless time measuring distances and ensuring accuracy. It was designed with **Autodesk Fusion 360**, a free 3D designing software for noncommercial use.
- Firmware - The KMK firmware was created based off of the [KMK Docs](https://github.com/KMKfw/kmk_firmware/tree/main), however, I was unable to test it since I do not have the physical **KaziPad** yet.

## What I Learned:
- How to design start to finish my own project
- How to design my own schematics and import footprints based on real world parts
- How to properly arrange my components on a PCB and wire them accordingly
- How to design 3D objects from scratch
- How to interpret Docs effectively in order to turn my knowledge into code
- How to ask for help when I need it from my Hack Club Community

The **KaziPad** was created for [Stardance](https://stardance.hackclub.com/home), a free online summer program.

## BOM
(A fully itemized list of all the components necessary to make a **KaziPad**!)

|Quantity | Item|
|---------|----------------|
|x1 | Custom PCB |
|x1 | 3d Printed Case (Top + Bottom)|
|x1 | Seeed XIAO RP2040|
|x1 | .91 inch OLED Display|
|x1 | EC11 Rotary encoder|
|x9 | MX-Style Switches|
|x9 | White blank DSA keycaps|
|x9 | White blank DSA keycaps|
|x9 | Through-hole 1N4148 Diodes|
|x4 | M3x16mm screws|
|x4 | M3x5mx4mm heatset inserts|



## My Takeaways

This is the first ever project I've ever fully designed, and I am very proud of it. I learned a lot of new skills that are applicable to just about everything I will do in the future.
