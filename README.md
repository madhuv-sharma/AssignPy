# AssignPy <img>
<br><i>Kurius SE Hackathon Project - Brain Canada Foundation </br></i>
<div align = "center">
  <img align="center" src= "https://github.com/madhuv-sharma/AssignPy/blob/main/logoassignpylong.png" width='610'>
  <p></p>
  <p>Assignment Made Easy ;)</p>
</div>

___

<div align = "center">
  <img align="center" src= "https://github.com/madhuv-sharma/AssignPy/blob/main/MdLogo.png" >
  <p></p>
  <p>Brain Canada is a national non-profit organization that plays a unique and invaluable role as the national convenor of those who support and advance brain research. Our vision is to understand the brain in health and illness, to improve lives and achieve societal impact. We achieve our vision by Increasing the scale and scope of funding to accelerate the pace of Canadian brain research, creating a collective commitment to brain research across the public, private and voluntary sectors, and delivering transformative, original and outstanding research programs.
  </p>
</div>


## *The Problem Statement*: 
Brain Canada receives hundreds of applications in various types and areas of brain research. Each application needs to be randomly assigned to three expert reviewers. Assignment rules: application type, area of research or keywords for each applicant must match or closely match those of reviewers (excluding those with conflict of interest). Currently, Brain Canada uses as Excel model to match each applicant to a reviewer. This is quite tedious and can generate erroneous results that need to be manually corrected - potentially increases assignment bias. The development of a program/automation process to improve the randomization process and generate a march percentage would be very helpful for Brain Canada's research Programs. It should include some level of flexibility to add rules for specific Programs (e.g., the use of keywords or including the level of expertise as criteria). It should also allow CSV or Excel data importing from both the applicant forms and the reviewer forms. 
## [*AssignPy* GitHub Repository](https://github.com/madhuv-sharma/AssignPy)

### Short Description

___


### How to Use The Application
<table>
  <tr><td>Home Page</td><td>Registeration Page</td><td>Login Page</td></tr>
  <tr><td><img src= "https://github.com/madhuv-sharma/AssignPy/blob/main/MainPage.png" ></td><td><img src= "https://github.com/madhuv-sharma/AssignPy/blob/main/Register.png" ></td><td><img src= "https://github.com/madhuv-sharma/AssignPy/blob/main/Login.png" ></td></tr>
  <tr><td>This is the very first page that you encounter as soon as you run the Python File. This is the root page of the program and therefore one shouldn't close this window. </td><td>Using this page you can Register a new user. After you have entered your details a .txt file is created in the folder with all the credentials.</td><td>A function now checks the credentials against the input provided by the user and gives an output accordingly. </td></tr>
</table>

___

### Challenges We Encountered
<div>
  <img align='left' src="https://media3.giphy.com/media/l2YWFxG9GxXk8A7w4/giphy.gif?cid=ecf05e47cqpuzxgw3zhivi0ur3sxw4388yb4dyhanpm7tu5g&rid=giphy.gif&ct=g" width="300"> 
  <dl><dt><h3>- Incorporating the whole code in the Tkinter GUI</h3></dt><dt><h3>- Coming up with an optimal scoring system</h3> </dt> <p>Type of Research is for 20 pts (if primary matches then 20 pts and for secondary 10 otherwise Zero)</p><p> On the other hand, Research Area for 50 pts (The result can take any value between Zero to 50)</p><p> And Keywords are for 30 pts(Similarly,The result can take any value between Zero to 30 )</p></ul>
</div>

___

### Our Proud Accomplishment - Scoring Mechanism
For calculating the percentage we are using *Levenshtein Distance Algorithm*. In information theory, linguistics, and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. 
**We are using a threshold value as 5 edits. In simple words if can change word A->B in less than or equal to five “edits” (which can be replacement, addition or deletion) then they are essentially the same.**

___

### What We've Learned

___

### Future Project Extension
- Ability to enter a rubriks from the GUI itself
- Making the GUI easier to navigate 
- Integrating MySQL to have a database with all the information (Students,Reviewer,Passwords,etc.)

___

### Built with
- Python
- Tkinter (Python Module)
___

### Sources
