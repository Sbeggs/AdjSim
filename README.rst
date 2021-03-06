AdjSim Simulation Framework
===========================

|Build Status| |Coverage Status| |License: GPL v3|

    Designed and developed by Sever Topan

Navigation
----------

1. `Feature Abstract <#Features>`__
2. `Installation Instructions <INSTALL.md>`__
3. `Tutorial <tutorial/tutorial.ipynb>`__
4. `Class Documentation <https://severtopan.github.io/AdjSim/>`__

Features
--------

Engine
~~~~~~

At its core, AdjSim is an agent-based modelling engine. It allows users
to define simulation environments through which agents interact through
ability casting and timestep iteration. The framework is targeted
towards agents that behave intelligently, for example a bacterium
chasing down food. However, the framework is extremely flexible - from
enabling physics simulation to defining an environment in which
`Conway's Game of
Life <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>`__ plays
out! AdjSim aims to be a foundational architecture on top of which
reinforcement learning can be built.

Graphical Simulation Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simulation can be viewed in real time as it unfolds, with graphics
are rendered and animated using PyQt5. Below are four of the distinct
examples packadged with AdjSim, ranging from bacteria to moon system
simulation.

+-------------------+------------------------+
| |Bacteria Demo|   | |Predator Prey Demo|   |
+===================+========================+
| |GOL Demo|        | |Jupiter Demo|         |
+-------------------+------------------------+

Post Simulation Analysis Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agent properties can be marked for tracking during simulation, allowing
for viewing the results of these values once the simulation completes.
For example, we can track the population of each different type of
agent, or the efficacy of the agent's ability to meet its intelligence
module-defined goals.

\| |QLearning Graph|\ \| |Predator Prey Graph| \|
\|:-------------:\|:-------------:\|

Intelligence Module
~~~~~~~~~~~~~~~~~~~

Perhaps the most computationally interesting aspect of AdjSim lies in
its intelligence module. It allows agents to set goals (for example, the
goal of a bacterium may be to maximize its calories), and assess its
actions in terms of its ability to meet its goals. This allows the
agents to learn which actions are best used in a given situation.
Currently the intelligence module implements
`Q-Learning <https://en.wikipedia.org/wiki/Q-learning>`__, but more
advanced reinforcement learning techniques are coming soon!

.. |Build Status| image:: https://travis-ci.org/SeverTopan/AdjSim.svg?branch=master
   :target: https://travis-ci.org/SeverTopan/AdjSim
.. |Coverage Status| image:: https://coveralls.io/repos/github/SeverTopan/AdjSim/badge.svg?branch=master
   :target: https://coveralls.io/github/SeverTopan/AdjSim?branch=master
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
.. |Bacteria Demo| image:: https://raw.githubusercontent.com/SeverTopan/AdjSim/master/gallery/images/readme_bacteria.png
.. |Predator Prey Demo| image:: https://raw.githubusercontent.com/SeverTopan/AdjSim/master/gallery/images/readme_predator_prey.png
.. |GOL Demo| image:: https://raw.githubusercontent.com/SeverTopan/AdjSim/master/gallery/images/readme_game_of_life.png
.. |Jupiter Demo| image:: https://raw.githubusercontent.com/SeverTopan/AdjSim/master/gallery/images/readme_jupiter_moon_system.png
.. |QLearning Graph| image:: https://raw.githubusercontent.com/SeverTopan/AdjSim/master/gallery/images/readme_individual_learning.png
.. |Predator Prey Graph| image:: https://raw.githubusercontent.com/SeverTopan/AdjSim/master/gallery/images/readme_predator_prey_population.png
