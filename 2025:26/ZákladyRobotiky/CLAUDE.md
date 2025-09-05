# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Czech educational robotics curriculum called "Základy elektrotechniky a robotiky" (Electronics and Robotics Fundamentals) designed for children aged 9-13. The course is theory-focused, using simulation tools rather than physical hardware, with students taking home project plans and code instead of built devices.

## Repository Structure

The repository contains a 35-week curriculum organized into 8 blocks:

- `01_teorie-zaklady/` - Theory and electronics fundamentals (weeks 1-5)
- `02_simulator-intro/` - Tinkercad simulator introduction (weeks 6-10) 
- `03_arduino-logika/` - Arduino programming basics (weeks 11-13)
- `04_3d-model-sim/` - 3D modeling and printing (weeks 14-15)
- `05_senzory/` - Sensors in simulation (weeks 16-20)
- `06_male-projekty/` - Small projects (weeks 21-27)
- `07_rocni-projekt/` - Annual project development (weeks 28-32)
- `08_final-test-prezentace/` - Final presentations (weeks 33-35)

Each directory contains a markdown file with lesson plans and objectives for that curriculum block.

## Key Educational Tools

The curriculum uses these simulation and design tools:
- **Tinkercad Circuits** - Primary Arduino simulation environment with Python programming support
- **Arduino Labs** - Python-based Arduino programming (Arduino Cloud)
- **Falstad Circuit Simulator** - Physics visualization and component demonstration
- **RoboBlocky** - Visual programming for robots
- **Open Roberta** - Robot programming platform with real hardware integration
- **Python IDLE/Thonny** - Python development environment
- **MicroPython** - Python for microcontrollers
- **CircuitPython** - Adafruit's Python for embedded systems
- **Tinkercad 3D & Fusion 360** - 3D modeling
- **Cura, PrusaSlicer** - 3D printing preparation

## Content Guidelines

When working with this educational content:

1. **Language**: All content is in Czech. Maintain Czech language for lesson materials and student-facing content.

2. **Age Appropriateness**: Content targets 9-13 year olds. Keep explanations simple, visual, and engaging.

3. **Safety Focus**: Electronics safety is emphasized throughout. Always include safety considerations in practical exercises.

4. **Simulation-First Approach**: Physical hardware is minimal. Focus on simulation tools and virtual environments for learning.

5. **Project Documentation**: Students receive detailed project plans, component lists, commented Python code, and step-by-step instructions for home construction.

6. **Python-First Programming**: The curriculum uses Python as the primary programming language, including MicroPython and CircuitPython for Arduino/microcontroller programming, making it more accessible and readable for young learners.

## Curriculum Philosophy

- Theory foundation before practical application
- Safe learning environment through simulation
- Student ownership of project designs and code
- Progressive complexity from basic circuits to complete robotics projects
- Emphasis on understanding physics principles behind electronics