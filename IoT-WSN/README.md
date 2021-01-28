Contiki OS for the Internet Of things 
=====================================

# INTRODUCTION
The Internet of Things is considered to be the next big opportunity, and challenge, for the Internet engi neering community, users of technology, companies and society as a whole. It involves connecting embedded devices such as sensors, home appliances, weather stations and even toys to Internet Protocol (IP) based networks. The number of IP-enabled embedded devices is increasing rapidly, and although hard to estimate, will surely outnumber the number of personal computers (PCs) and servers in the future. With the advances made over the past decade in microcontroller, low-power radio, battery and microelectronic technology, the trend in the industry is for smart embedded devices (called smart objects) to become IP-enabled, and an integral part of the latest services on the Internet. These services are no longer cyber, just including data created by humans, but are to become very connected to the physical world aroung us by including sensor data, the monitoring and control of machines, and other kinds of physical context. We call this latest frontier of the
Internet, consisting of wireless low-power embedded devices, the Wireless Embedded Internet. Applications that this new frontier of the Internet enable are critical to the sustainability, efficiency and safety of society and include home and building automation, healthcare, energy efficiency, smart grids and environmental monitoring to name just a few. Standards for the Internet are set by the Internet Engineering Task Force (IETF). A new set of IETF standard for IPV6 over low-power wireless area networks (6lowPAN) will be a key technology for the Wireless Embedded Internet. Originally WPAN stood wireless Personal area network, a term inherited from IEEE 802.15.4, which is no longer descriptive for the wide range of applications for 6LoWPAN. extracted from 6LoWPAN The Wireless Embedded Internet book introduction [2].

## Course content 
In this assignment, 6LowPAN technologies is used through Contiki Operating System for the Internet Of Things (IoT) for learning to implement IoT applications and to build complete tools chain in collaborative projects. In first section, COOJA Wireless Sensor Network (WSN) simulator is used to present basic examples of WSN in which are discussed main constraints and characteristics of IoT technologies. Next section focuses on building a complete tool chain for developing and deploying a Contiki OS application on native and microcontroller platform in a collaborative projects. Patch, Makefile and deployment script are studied over Linux tools. Finally, the two last section concerns a Broadcast Network Chatting project which uses Shell Contiki application and 6LoWPAN broadcast mechanisms over RPL routing protocol.

 
Prerequirements
---------------

### VirtualBox Installation

* Download the Virtual Hard Drive (VHD) [https://s3.dvic.devinci.fr/public/InstantContiki2.6.zip](https://s3.dvic.devinci.fr/public/InstantContiki2.6.zip)
* Create a new virtual machine and configure it properly (number of CPU, RAM memory, etc).
* Add your user to the group user's virtual box for USB right access. 

```sudo usermod -a -G vboxusers $USER```

* Start the virtual machine and install the guest additional drivers

**password : user**


# COOJA WSN simulator
Simulators are required during the development of new network algorithms at large scale. In this section, you must test two pre-configured simulations to understand main WSN problematic which is energy consumption impact of data routing on each node.

## Data collector algorithm
Firstly, load the simulation located in /examples/collect/example−collect−views.csc. COOJA simulator
is composed of several main windows :

* Network window shows spatial distribution of nodes which can be moved to build real network topology use case. On views section, click on *radio traffic* to show network exchanges.
* Mote output window shows all print outputs of all nodes which is really useful to debug yours programs.
* Sensor data collect window is a dedicated window for node behaviour analysis.


On Node Control panel, click on *Send command* to nodes then on *Start collect* and wait some seconds.

### Questions

* Explain what is the purpose of this algorithm based on Power and Sensors panel results.
* Try to change algorithm parameters in Node control and explain the impact of your changes. 
* Finally, go to Serial console and send help command to the node. What is printed ? 
* What is the command ps ? 
* Explain HOW is implemented the collect data algorithm after reading node outputs when you have sent commands to nodes ?

This preliminary simulation shows how can be simulated Wireless Sensor Network behaviour and what
are the available tools to debug it. Next simulation shows more complex applications using web services and web server on nodes with external stimulations by a real network of your Linux Network Interface.

## COAP RestFul services and WEB Server

Contiki OS is a really lightweight system which includes web server and web services applications.  HTTP is not efficient on Wireless Sensor Network due to its verbosity. A new protocol is defined by IETF in order to replace HTTP by COAP which is an adapted HTTP based binary compression. In this
simulation, you will run a web server node on border-router (WSN access point) and a client-server COAP nodes.

* Load simulation located in */examples/er−rest−example/server−client.csc*. 
* Start the simulation and explain the network activity between the three nodes. Deduces their roles.
* In a new console tab, go to */examples/er−rest−example/*, executes the following command to connect your Linux to the simulated WSN : *make connect-router-cooja*
* Check your linux network interfaces with *ifconfig -a*
* Ping your border edge router with *ping6 aaaa::0212:7401:0001:0101*
* Try to connect with a web browser *http://[aaaa::0212:7401:0001:0101]* 
*  What is the contained informations ?

An important debugging tools in WSN development is the traffic analysis that can be realized by tcpdump or wireshark. 
* Explain what is a SLIP network interface and capture some packets of it.

This section presents you some useful tools for developing WSN projects like simulation, external stimulus analysis by real network and network traffic monitoring. All of this requirements will help you in your project development of the below section.

# Contiki OS 
Contiki OS is a highly modular Kernel Operating system for Internet Of Things. The concern of this
assignment is to discover, compile and run basic Contiki applications for understanding the several steps required to build your future application of the last assignment.

Contiki OS source code is composed by five main folders :

* */core/* contains every kernel files with its 6lowPAN stack.
* */cpu/* contains all procedures depending of CPU targets (AVR).
* */platform/* contains every driver files for development boards (atmega128rfa1).
* */apps/* contains Contiki OS applications.
* */examples/* contains projects composed of Contiki applications.

During compilation steps, a set of hierarchical makefile are called to build final file hierarchy to compile project according to configurations e.g. target, applications, network configuration, etc.  The purpose of this second assignment is to prepare a complete tool chain for building an hello word
example application. Final result has to be composed of a makefile to generate a new project in /examples/ built on minimal-net and avr-atmega128rfa1 platform. Sometimes in collaborative project, patches have to be generated for diffusing bug corrections or proposal add-ons on other authors’s files. Finally, you will be evaluated on your capacity to write a patch for adding your project to a Contiki source code folder. 

Your assignment result must contain :

* *README* file to present briefly your work by using Contiki coding style 2 .
* *AUTHOR* file written with Contiki coding style.
* *install.sh* file which copies all YOUR files in a new contiki source code folder with proper right access.
* *build.sh* file which builds your project for minimal-net and avr-atmega128rfa1 platform.
* *patch.diff* called in *install.sh* to add corrected lines in existing contiki files
* *src* folder which contains all your project hierarchy

For evaluating yourself, you can uncompress a new contiki folder and run ./install.sh YourNewContiki-Folder. If installation is success, YourNewContikiFolder must contain all files of your src folder at the good hierarchical place. Finally, *./build.sh* compiles your project for the both platform and runs minimal-net instance of your project.

## Tool chain and first compilation
For beginning, you will create a first application helloword with your first Contiki makefile as below.  This makefile is run by the Linux command make all TARGET=minimal-net with proper execution right access (*chmod 755 yourfile*).

### my Makefile in /example/myproject/
``` make
CONTIKI=../..

all: yourmainfile

# Add your application
APPS+=Apps1
APPS+=Apps2

# Set compilation optimization parameter
CFLAGS+=-Os

# Add your project config file which contains global parameters
CFLAGS+=-DPROJECTCONFH=\”project-conf.h\”

# Include Contiki makefile
include $(CONTIKI)/Makefile.include
```

### my project.c in /example/mymainproject/ 
``` C
#include <stdio.h>
#include ”contiki.h”

PROCESS(helloworld_process,”Helloworld process”);
AUTOSTART_PROCESSES(&helloworld_process);

PROCESS_THREAD(helloworld_process,ev,data)
{
PROCESS_BEGIN();
printf(”Hello,world!\n”);
PROCESS_END();
}
```

If you are success in building this helloword application, you can start it by ./your program and see the shell output : Hello world !

Now, you can develop and compile your application on X86 system, but we are interested in porting it to the micro-controller avr-atmega128rfa1. Programming of AVR micro-controller is done thanks to a JTAG interface mkII properly connected to the main board stk600 on which are plugged the micro-controller child card as illustrated below.

![alt text](https://s3.dvic.devinci.fr/public/InstantContikihardware.png "Stk600")

Loading your program to the AVR target (previously compiled for it) is composed of several steps :

* Cleaning : *make clean && rm -rf obj\** 
* Compilation : *make all TARGET=avr-atmega128rfa1*
* Check your application size : *avr-size -C –mcu=atmega128rfa1 your_file*
* Prepare flash image : *avr-objcopy -O ihex -R .eeprom -R .fuse -R .signature your file your file.hex*
* Loading : *avrdude -p atmega128rfa1 -c jtag2 -P usb -Uflash:w:your file.hex*

Congratulation, you have loaded your first program on the micro-controller but you cannot see it running yet ! Now, you have to use the *serial-shell* application of Contiki to connect your computer on the serial interface of the micro-controller and see your : Hello world !

## Contiki OS applications

Contiki OS has a lot of applications such  webserver, telnet, ftp, erbium, etc which can be included in your project. This applications are standalone or required some developments. To include an application, refer to your makefile in which global variable *APPS* defines all built-in applications.

In this section, we will learn how to create your Contiki OS application helloworld. Firstly, you must create a new folder *myapps* in */apps/* in which you must add a new file *Makefile.myapps*. This file defines all files which have to be compiled for your application, see below the example :

``` make
myapps_src = myfile1.c myfile2.c etc
```

* Write a helloworld function in */apps/yourapps/helloworld.c*
* Call this function in your main file /example/myproject/my_project.c
* Try to compile your project and fix issues !

**/example/myproject/my_project.c**

``` C
#include <stdio.h>
#include ”contiki.h”
#include ”helloworld.h”

PROCESS(helloworld_process,”Helloworld process”);
AUTOSTART_PROCESSES(&helloworld_process);

PROCESS_THREAD(helloworld_process,ev,data)
{
PROCESS_BEGIN();
helloworld();
PROCESS_END();
}
```

**/example/myproject/Makefile**

``` make
CONTIKI=../..

all: myproject
APPS+=yourapps
CFLAGS+=-Os
include$(CONTIKI)/Makefile.include
```
**/apps/yourapps/hello world.c**
``` C
#include <stdio.h>
#include ”contiki.h”

void helloworld(){
printf(”Helloworld!\n”);
};
```
**/apps/yourapps/Makefile.yourapps**
``` make
yourapps_src = hello_world.c
```

### Point of Interests
The encapsulation of your functions in application modules is usefull in terms of code reusability, debugging and maintenance. Hence your application can be based on other contiki applications and be used by other ones. Everyone will benefit of other's bug fix and new functionnalities **if everyone ensures retro-compatibility**. Similarly hardware components and kernel operations are encapsulated in modules independent modules that you can link thanks to the makefile (*/cpu/*, */platform/*, */core*/). Hence if someone creates its own electronic board, it just has to develop the different drivers in a new folder in */platform/* in order to ensure cross-compilation for the different contiki apps.

## Shell application
We are interested in using the *serial-shell* application to send commands and receive
output messages on the serial interface with the GtkTerm software (*sudo apt-get install gtkterm*) or any other serial clients.

Firstly, you must add the *serial-shell* application to your *APPS* global variable of your Makefile. Try to compile and run it on minimal-net platform. This application redirects the IO of your program to the IO of the platform. On minimal-net platform, printf is already redirect by your compiler to Linux IO system. On your avr-atmega128rfa1 target, the IO of your program is redirected to the serial interface of the micro-controller. Firstly, you must connect microcontroler RXD/TXD to PD2/PD3 pins on STK600 boards to route serial interface to the micro-controller UART connector by a wire (see on figure 3).
Unfortunately, these development boards are not directly compatible with current implementation
of Contiki serial driver for Atmega128rfa1. Some changes have to be realized to connect properly GtkTerm with the micro-controller. You must change baudrate connection from USART_BAUD_57600 to
USART_BAUD_19200 in main file of avr-atmega128rfa1 platform.

## Build a patch

Because you have changed some files which are not part of your project, you will need to save your modifications in a *patch file*. Hence you will be able to integrate automatically these modifications in future works, as illustrated below, thanks to an installation procedure.The following command will compare and save the difference between two folder :

``` bash
diff −crB contiki−ori/ contiki−2.6−modified/ >> patch.diff
```

This patch can apply to an original contiki folder with the following command :

``` bash
patch --dry-run -p1 -i patch.diff
```

![alt text](https://s3.dvic.devinci.fr/public/InstantContikipatch.png "Patch example")

## Create installation procedure
Create an installation script *install.sh* which : 
* Unzip an original contiki folder
* Apply the patch to this contiki folder
* Copy all of your files in their proper locations
* Try to compile

## Fix a bug

At this point, when a printf is executed in your program, the output is redirected through the serial line interface. However there is two other contiki bugs to fix : 

* In order to send commands from your computer to contiki through the serial line interface, you will need to add (or to replace by) the following lines in main file of avr-atmega128rfa1 platform and invert 0x0a with 0x0d in file *contiki/core/dev/serial-line.c* beucause of the window and linux different implementations of the end char. 
``` C
rs232_init (RS232_PORT_1, USART_BAUD_19200, USART_PARITY_NONE| USART_STOP_BITS_1|USART_DATA_BITS_8);
rs232_set_input (RS232_PORT_1, serial_line_input_byte);
rs232_redirect_stdout (RS232_PORT_1);
```

* There is a last bug in core/dev/leds.c of Contiki OS kernel files, clock delay() function is called but it is not implemented. You have to remove this function call.

* Update your patch and test your installation procedure



## Shell implementation

Shell is the simplest interface in order to communicate with an operating system kernel. You have to install contiki's one by adding *serial-shell* in your contiki application list in the *APPS* variable of your *Makefile* and add following function calls in your application. 
``` C
#include <stdio.h>
#include ”contiki.h”
#include ”dev/serial−line.h”
#include ”shell.h”
#include ”serial−shell.h”
#include ”helloworld.h”

PROCESS(helloworld_process,”Helloworld_process”);
AUTOSTART_PROCESSES(&helloworld_process);
PROCESS_THREAD(helloworld_process,ev,data)
{
PROCESS_BEGIN ( ) ;
serial_line_init ();
serial_shell_init ();

reboot_init ();
power_init ();
ps_init ();
ping_init ();
hello_world ();
PROCESS_END ( ) ;
}
```
After a global recompilation, you should be able to access it through your serial line interface as below : 
``` bash
255.255 : Contiki >.
```
* Try to use standard commands like help, etc. What is the purpose of ps command ? 
* Read some example of command implementation in */apps/shell/*
* Implement your own shell command *setname USER_NAME* in your apps folder. This command must store the username in a global variable of your application. 
* Compile and test it !

## Project : distributed communication network 

The **distributed communication network project** consists of a distributed communication networks between all nodes based on 6lowPAN RPL routing protocol. 

* What is 6lowPAN accord ing to IPV6 ? What is the main purpose of RPL according to other routing protocol ? 
* Activate IPV6 module and its routing protocol by setting the global variable *UIP_CONF_IPV6=1* in your project Makefile.
* Read the simple broadcast message example in file : */examples/ipv6/simple-udp-rpl/broadcast-example.c*. 
* Implement a shell command *send MY_MESSAGE* in your contiki applications in order to send an UDP packet which contain in payload: {”username” : ”USER_NAME”, ”msg” : ”THE_MESSAGE”}. 
* Implement an UDP listener function which print every messages recevied with the following format : * USER_NAME> THE_MESSAGE with a prompt return.

Finally and furthermore, you can explore more advance Contiki OS applications such as the webserver
application in order to create a chatting website with HTML rendering on your node

* Update your installation procedure
* Try it !

# References
[1] Adam Dunkels Jean-Philippe Vasseur. Interconnecting Smart Objects with IP - The Next Internet. Rich Adams, 2010.

[2] Carsten Bormann Zach Shelby. 6lowPAN The Wireless Embedded Internet. Wiley-Blackwell, 2009.

[3] Contiki OS official documentation. http://contiki.sourceforge.net/docs/2.6/

