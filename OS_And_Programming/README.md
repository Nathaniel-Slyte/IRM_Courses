# Operating Systems and Programming

This document is divided in 3 sections. 

- The Introduction (FAQ) has the most frequently asked questions I received the last few weeks regarding this lesson.
- The Table Of Contents shows the lesson's plan and what you will be be doing
- The Bibliography has some resources that you should watch before coming to class

## Introduction (FAQ)

**Why a lesson about OS and Programming** 

> Because Operating Systems are going to be you primary tool for a lot of projects. A good understating of your tools will save you from a lot of trouble (and headache). Regarding Programming, most of you will be writing some sort of code in the future or at the very least use some sort of software.
>
> However, knowing how to program and a good understanding of OSs are strongly tied, as you will see.

**What is the required entry level ?**

> The lesson is aimed at beginners, but please don't overlook the bibliography.

**Can I use a mac?**

> For Mac Users, OSX will work for the most of the class. It will be indicated when a workshop will not work on Macintosh 

# Table Of Contents

## Part 1: Operating Systems

### I) Introduction

- Brief history of Operating Systems
- What is an Operating system
- What are the different kinds of OS ?

### II) Hardware

- Interruptions, CPU & registries and its interations with RAM
- RAM topology
- Boot sequence

### III) Base Concepts of an OS

- Process
- Files
- Syscalls

### IV) Linux

- Kernel and its different parts
- 'Everything is a file'
- Mounts

### V) Daily Usage

- The command line.
- Systemd

## Part 2: C/Python programming

### I) Introduction

- Links with Operating Systems
- What is `compilation` ?

### II) C 

- Memory manipulation, pointers
- Structures, using syscalls
- Compilation in-depth: dynamic linking
- Error Management with `errno`
- Inter Process Communications: The hard way

### III) Python

- Links with C
- Using pip, and modules
- File manipulation
- Object Oriented Programming
- Inter Process Communication: The easy way

## Bibliography

> Try to watch and understand as much as you can, try not to tunnel-vision on a single resource

> Ben Eater's Playlist on the 8 bit computer, you will see this again in the Electronics lesson, but it's a must-see.
>
> https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU

> Linux File System structure. It can be difficult to wrap your head around it when coming from Windows, take time to understand.
>
> https://www.youtube.com/watch?v=HbgzrKJvDRw

> Quick lesson about compilation. A.k.a the base of how to make a program. The video is a bit technical, but try to get the gist of it.
>
> https://www.youtube.com/watch?v=N2y6csonII4

> Process and memory map. **Absolutely fundamental, please watch with attention**
>
> The `8 Basic lsof Commands Every Sysadmin Needs to Know` video is a bit more practical and showcases a lot of useful commands.
>
> https://www.youtube.com/playlist?list=PLtK75qxsQaMKLUENMaPlD_O2qS8ZBGjuy
>
> https://www.youtube.com/watch?v=qlH4-oHnBb8

> Detailed Bash. See part 1 to 8 and 19 (Timestamp: 2:31:14)
>
> https://www.youtube.com/watch?v=e7BufAVwDiM

For C and Python, you have plenty tutorials online, from Open Classroom to Tutorials Point, However they sometimes don't cover all the essentials, and to be on the same page I'll link you:

> C/Python by freeCodeCamp. Very in-depth, they sometimes spend too much time on some details but are very good. (If you end up skipping things, please look the "pointers" part)
>
>  You'll have to install and figure out how to compile a program in C on linux. Use this video to get started: https://www.youtube.com/watch?v=lrx5dcB_4Oo

>  Also, the C video uses "CodeBlocks" for developing C programs. I encourage you to try out other text editors lke Atom or VsCode and do the compilig by hand using the video above as a starting point.
>
> https://www.youtube.com/watch?v=KJgsSFOSQv0 For the C lesson
>
> https://www.youtube.com/watch?v=rfscVS0vtbw For the Python

> Inria's C PDF lesson (in french). (Skip the gdb part)
>
> https://www.rocq.inria.fr/secret/Anne.Canteaut/COURS_C/cours.pdf

> The Python Official Website has a lot of resources to learn
>
> https://wiki.python.org/moin/BeginnersGuide/Programmers
>
> https://docs.python.org/3/tutorial/

## Other References

To go further I recommend you:

`Modern Operating Systems`: https://github.com/smellslikekeenspirit/an-askreddit-list-of-compsci-books/blob/master/Modern%20Operating%20Systems%204th%20Edition--Andrew%20Tanenbaum.pdf or in the DVIC Library for a hardcover version

`Efficient Python` That an be found in the DVIC Library

`Computer System Architecture` https://www.pdfdrive.com/computer-system-architecture-morris-mano-third-edition-e31004022.html
