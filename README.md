<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="images/icon.png" alt="Logo" width="80" height="80">
  <h3 align="center">Dan's Plotter</h3>
  <p align="center">
    Multi-graph plotter
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
  * [Parser](#parser)
* [Contributing](#contributing)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This was a homework assignment given in Cyber Class, to plot a graph given a function using eval in python.

### Built With
Both of these editors were used in the creation of this project:
* [Pycharm](https://www.jetbrains.com/pycharm/)
* [Atom Editor](https://atom.io/)


<!-- GETTING STARTED -->
## Getting Started

Download the file, open in pycharm, and run.

### Prerequisites
Needed to run:
* [Pycharm](https://www.jetbrains.com/pycharm/)
* [3.x Python](https://www.python.org/downloads/)

<!-- USAGE EXAMPLES -->
## Usage

### Options
 * Amount of graphs (int)
 * f(x) =  The graph (string)
 * Custom range: y/N (default n)
 * Use scaling: Zoom Out/In (y/N)
### Parser
The parser built in to this plotter can parse things like:
5cos(5x)9(-4x+1) => 5\*cos(5\*(x))\*9\*(-4\*(x)+1)
(2x-1)(1-2x)     => (2\*(x)-1)\*(1-2\*(x))
 
Examples of valid input are (firs image before scaling option was added):
<img src="https://github.com/IMakeBotsForYou/python_graph_plotter/blob/main/images/graph_example1.png?raw=true" alt="ex1">
<img src="https://github.com/IMakeBotsForYou/python_graph_plotter/blob/main/images/fixed_graph_2.png?raw=true" alt="ex2">
<img src="https://github.com/IMakeBotsForYou/python_graph_plotter/blob/main/images/graph_example3.png?raw=true" alt="ex3">

<!-- ROADMAP -->
## Roadmap

<!-- See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues). -->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
