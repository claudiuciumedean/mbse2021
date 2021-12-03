# MBSE2021


# Simulator operation

The simulator is organized into three main parts:
\begin{itemize}
    \item The \texttt{Simulation\_Manager.py} file, which is the main file and orchestrates the whole simulation;
    \item The \texttt{Simulation\_Constants.py} file, which includes the complete parameter list of the simulator;
    \item The components files (i.e. \texttt{World.py}, \texttt{Coordinates.py}, \texttt{Area.py}, \texttt{Person.py}, \texttt{Wearable.py}), implementing the system's components.
\end{itemize}
\noindent
When the \texttt{Simulation\_Manager.py} is executed, the simulation starts. The 2D world with the moving people is generated and kept updated throughout the entire run, while the bottom plot keeps track of how many people are healthy, infected, recovered or dead. Moreover, the logged data are printed on the output terminal, and at the same time written in the CSV file. The simulation terminates when the script is manually stopped or when the number of simulated days reaches its predetermined value.