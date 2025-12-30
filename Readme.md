# **EngageTruth**

##### 

##### EngageTruth is a behavior-based engagement analysis system designed to detect manipulation on Instagram by analyzing how users interact with content rather than relying on surface-level popularity metrics.

##### 

##### Unlike traditional analytics tools that focus on follower counts or total likes, EngageTruth evaluates engagement patterns over time and assigns an explainable manipulation risk score.

##### 

### **1. Problem Statement**

##### 

##### Social media popularity is no longer a reliable indicator of influence. Many Instagram pages artificially inflate followers, likes, and comments using paid or coordinated engagement services. This creates a false sense of credibility and misleads users, brands, and advertisers.

##### 

##### Most existing tools display only raw metrics such as follower count or total likes—numbers that are easy to manipulate. They fail to analyze behavioral patterns that distinguish organic engagement from artificial activity.

##### 

##### EngageTruth addresses this gap by evaluating engagement behavior instead of raw numbers.

##### 

### **2. What “Fake Engagement” Means in This Project**

##### 

##### In this project, fake engagement does not refer to bots or spam accounts directly.

##### Fake engagement is defined as unnatural behavioral patterns that do not align with how real users typically interact with content, such as:

##### Sudden follower growth without proportional engagement

##### Extremely low or abnormally high engagement rates

##### Repetitive or templated comments

##### Inconsistent interaction patterns across posts

##### The focus is on probability of manipulation, not absolute identification.

##### 

### **3. Why Existing Solutions Are Not Enough**

##### 

##### Most analytics platforms focus on quantitative metrics:

##### 

##### Followers

##### Likes

##### Views

##### These metrics can be artificially boosted and do not reflect audience authenticity. Very few systems analyze behavioral signals such as engagement consistency, proportionality, or growth patterns.

##### 

##### This allows manipulated pages to appear legitimate despite poor audience quality.

##### 

### **4. Goal of the Project**

##### 

##### The goal of EngageTruth is to build a transparent, behavior-based engagement analysis system that:

##### Evaluates public Instagram data

##### Detects abnormal engagement behavior

##### Assigns a clear and explainable risk score

##### Helps users judge whether popularity is organic or manipulated

##### 

### **5. Methodology**



##### Engagement Rate Calculation

##### Engagement rate is calculated as:

##### (avg likes + avg comments) / total followers

##### This helps determine whether audience interaction aligns with the page’s size.

##### 

### **6. Instagram Behavioral Signals**

##### 

##### EngageTruth currently analyzes the following Instagram signals:

##### 

* ##### Engagement rate anomalies
* ##### Sudden follower growth spikes
* ##### Repetitive comment patterns (comment analysis is performed only when comments are publicly accessible; restricted comments are safely skipped to comply with platform limitations)
* ##### Engagement inconsistency across recent posts

##### 

### **7. Scoring System**

##### 

##### Each suspicious signal contributes predefined risk points.

##### The final risk score is capped at 100.

##### 

##### Risk Score Interpretation

##### 

* ##### 0–30 → Likely genuine
* ##### 31–60 → Suspicious
* ##### 61–100 → High probability of engagement manipulation

##### The score represents likelihood, not certainty.



#### **Engagement Anomaly Rule**

* ##### Engagement rate below 1% indicates inactive or artificial audiences
* ##### Engagement rate above 15% may indicate engagement boosting
* ##### Both cases contribute to the risk score.

##### 

### **8. Assumptions \& Limitations**

##### 

##### Only publicly available Instagram data is analyzed

##### Private profiles and restricted analytics are not accessed

##### No bot identification is performed

##### Results indicate probability, not definitive proof

##### 

### **9. Ethical Considerations**

##### 

##### EngageTruth is designed as a decision-support tool, not a labeling system.

##### It does not accuse or defame creators

##### No personal data is collected or stored

##### Final judgment is left to the user

##### 

### **10. Why a Rule-Based Approach?**

##### 

##### Instead of using machine learning models that require large labeled datasets, EngageTruth uses rule-based behavioral analysis.

##### This approach ensures:

* ##### Transparency
* ##### Explain ability
* ##### Easy validation of each risk score
* ##### Clear reasoning behind every verdict

##### 

### **11. Web Interface**

##### 

##### The project includes a lightweight web interface built with HTML, CSS, and JavaScript, connected to a FastAPI backend.

##### The UI:

##### 

* ##### Accepts an Instagram username
* ##### Displays real-time analysis
* ##### Shows engagement metrics and risk verdict
* ##### Uses loading states and smooth reveal animations for clarity

##### 

### **12. Sample Output**



##### --- EngageTruth Analysis Report ---

##### username: example\_page

##### followers: 12,000

##### engagement rate: 0.8%

##### risk score: 70

##### final verdict: high manipulation risk

##### --------------------------------

##### 

### **13. Future Scope**

##### 

##### Planned enhancements include:

* ##### Telegram channel analysis
* ##### Machine learning-based pattern learning
* ##### Chrome extension support
* ##### Creator-side dashboards
* ##### Multi-platform engagement analysis
* ##### Scoring refinement using real-world feedback

##### 

### **14. Naming Explanation**

##### 

##### The name EngageTruth represents the idea of revealing the truth behind engagement numbers by analyzing how users actually interact with content, rather than trusting visible popularity metrics.

