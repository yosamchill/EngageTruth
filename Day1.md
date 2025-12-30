## **DAY 1 – THINKING \& DESIGN NOTES**

##### 

### **project idea**

##### fake engagement detector for instagram and telegram pages using behavior-based signals instead of raw numbers.

##### 

### **what problem i am solving**

##### many social media pages artificially inflate followers, likes, and views. follower count alone cannot be trusted to judge credibility.

##### 

### **what i mean by fake engagement**

##### fake engagement means unnatural interaction patterns such as:

##### sudden follower growth without matching likes

##### repeated comments

##### abnormal engagement timing

##### inconsistent views on telegram

##### this project does not try to identify bots. it focuses on behavior.

##### signals chosen for instagram (reasoning)

##### engagement rate: low engagement despite high followers indicates fake or inactive audience

##### follower spikes: organic growth is gradual, sudden spikes are suspicious

##### comment repetition: paid comments are often templated

##### like velocity: real users engage over time, not instantly

##### inconsistency across posts: manipulation is often uneven

##### signals chosen for telegram (reasoning)

##### views vs subscribers ratio: real channels have stable ratios

##### forward to view ratio: forwards show real interest

##### view spikes without subscriber growth indicate paid views

##### dead subscribers show inflated subscriber count

##### calculation logic (rough)

##### engagement rate = (avg likes + avg comments) / followers

##### engagement < 1% → suspicious

##### engagement > 15% → possible boosting

##### risk score is created by adding points from multiple signals.

##### 

### **why rule-based instead of machine learning**



##### ml requires large labeled datasets which are difficult to obtain. rule-based analysis is transparent, explainable, and easier to justify in interviews.

##### ethical thinking

##### this system should not defame creators. it only provides a probability score, not a final judgment.

##### 

### **future ideas (for later)**

##### 

##### ml refinement

##### chrome extension

##### real-time monitoring

##### more platforms





## **day 2 summary :**

##### successfully extracted instagram public engagement data

##### calculated engagement rate

##### defined engagement anomaly threshold





## **day 3:** 

##### converted engagement rate into risk points and implemented final verdict logic.



## **day 4:** 

##### implemented follower history tracking and multi-signal risk scoring.



## **day 5:** 

##### implemented comment repetition detection using public comment text. added graceful handling for instagram comment access restrictions to prevent system failure.



## **day 6:** 

##### finalized output formatting, handled edge cases, and prepared project for resume and linkedin presentation.







