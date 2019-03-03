# OCR_Parsing
It was unclear if I was allowed to use Jupyter Notebooks to implement the solution to the problem, hence I built two different solutions. My preferred method is the BusinessCardParser.ipnyb.  However, if this file is not acceptable please use BusinessCardParser.py.    
## BusinessCardParser.ipynb (Prefered Method)
 Jupyter notebooks (.ipynb files) are a browser based interactive coding platform.  To utilize the software download the Anaconda Data Science Platform here https://www.anaconda.com/distribution/.  Once loaded you can launch a web browser from the command line with the command:
 > $ jupyter notebooks

  Once you launch the local browser navigate to the location of BusinessCardParser.ipynb and open the file. Once the notebook opens, select Cell -> Run All.  At the top of the notebook you will see a "Show/Hide Code" button.  Click this button to hide the code for a simple interface. 
  
  A GUI will appear on the screen where you can input the OCR results.  Once you have inputted them,  click the green 'Get Contact Info' button and your results will print to the screen. 
  
# BusinessCardParser.py
BusinessCardParser.py is designed to be run from the command line on a computer with Python version 3.4 or higher installed.  To run the program simply navigate to the correct folder and run the following from the command line.

>  $ python BusinessCardParser.py

Once the program loads you will be prompted to input the OCR results ONE LINE AT A TIME.  Simply input the text and press enter.  When you have entered all lines from the results, press enter without inputting text, and the results will print to the console.  
