# water-quality-and-water-level-detection
## 📌 Project Overview  
Groundwater and drinking water quality assessment is critical in both rural and urban areas.  
This project uses Machine Learning to evaluate water quality from measurable parameters and stores prediction results in SQLite database for future analysis.

The system predicts:
- **Good Water**
- **Bad / Contaminated Water**

## ⭐ Features  
✔ Random Forest ML model using scikit-learn  
✔ Predicts water quality with probability  
✔ Stores results in SQLite database  
✔ Multiple input parameters  
✔ Modular Python code (ML + DB separation)  
✔ Architecture & flowchart diagrams included  
✔ Fully ready for GitHub / CTS GenC submission  

## 🛠 Technology Stack  
**Programming Language:** Python  
**ML Library:** scikit-learn  
**Database:** SQLite  
**Other Libraries:** numpy, joblib, matplotlib  

## 🧠 Core ML Concepts  
This project demonstrates:  
- Supervised Learning  
- Binary Classification  
- Feature Engineering  
- Probability-based predictions  
- Persistence using SQLite database  
- Random Forest model interpretation  

## 🏗 Architecture Diagram    

              +----------------------+
              |  User Input Module   |
              +----------+-----------+
                         |
                         v
              +----------------------+
              |   ML Model (RF)      |
              +----------------------+
                         |
                         v
              +----------------------+
              |  Prediction Engine   |
              +----------------------+
                         |
                         v
              +----------------------+
              | SQLite Database      |
              +----------------------+

## 📊 Dataset Details  
Training dataset contains 6 sample rows of:  
- pH  
- Turbidity  
- Conductivity  
- Temperature  
- Label (1 = Good, 0 = Bad)

## 🤖 Model Used  
**Random Forest Classifier**  
- n_estimators = 60  
- Handles non-linear decision boundaries  
- Robust, fast, and accurate for small datasets  
- Provides prediction probabilities
  
## Real-world Applications
Borewell monitoring systems
Village/municipal water testing
IoT water sensor systems
Drinking water safety scoring
Industrial water filtration checks
## Advantages
✔ Lightweight and fast
✔ Works offline (SQLite)
✔ Extendable dataset
✔ High accuracy due to Random Forest
✔ Good academic/industry relevance
## Limitations
✘ Small demo dataset
✘ No real-time sensor integration (can be added)
✘ Only binary classification (can be extended to 4-class: Excellent, Good, Moderate, Contaminated)
