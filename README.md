🔩 BOLTED LAP JOINT DESIGN MODEL

This project is part of the " FOSSEE Fellowship " under the ' Osdag Project ' . 
It involves developing and testing a Python module for the " design of bolted lap joints "  in structural steel elements. 
The goal is to ensure that the joint can withstand a specified tensile force and complies with the " IS 800:2007 " code.

------------------------------------------------------------------------------------------------------------------------

📌 Objective

Design a bolted lap joint connecting two steel plates with given dimensions and tensile force, ensuring that:
- The number of bolts is ≥ 2 for any load between 0 and 100 kN
- The joint complies with IS 800:2007 design recommendations
- The efficiency of the connection is ≤ 1 and > 0

------------------------------------------------------------------------------------------------------------------------

📁 Project Structure

bolted_lap_joint/ 
    ├── bolted_lap_joint_design.py # Main design logic 
    ├── is800_2007.py # Clause implementations from IS 800:2007 
    ├── test_bolted_lap_joint_design.py # PyTest test cases 
    ├── requirements.txt # Python dependencies 
    ├── README.md # Project overview and usage 
    └── .gitignore # Git ignore file


------------------------------------------------------------------------------------------------------------------------

⚙️ How It Works

The function `design_lap_joint(P, w, t1, t2)` computes an optimal design for:
- Bolt size and grade
- Number of bolts
- Plate dimensions and joint geometry
- Connection strength and efficiency

It ensures:
- Minimum of 2 bolts for safety
- Safe shear and bearing capacities
- Validations against "IS 800:2007" standards

------------------------------------------------------------------------------------------------------------------------

🧪 Unit Testing with PyTest

Tested across:
- Tensile Loads**: from 0 to 100 kN
- Plate Thicknesses: [6, 8, 10, 12, 16, 20, 24] mm

✅ Sample Tests
- Validates structure of the returned dictionary
- Checks efficiency is between 0 and 1
- Ensures ≥2 bolts are used
- Catches invalid/unrealistic inputs

------------------------------------------------------------------------------------------------------------------------

📦 Installation [Terminal]

Clone the repository
    git clone https://github.com/Comrade-1729/Bolted_Lap_Joint_Design.git


Navigate into the folder
    cd bolted_lap_joint

(Optional) Create virtual environment
    python -m venv venv
    source venv/bin/activate   # or venv\Scripts\activate on Windows

Install dependencies
    pip install -r requirements.txt

------------------------------------------------------------------------------------------------------------------------

🚀 Run the Code 
    python bolted_lap_joint_design.py

🧪 Run the Tests 
    pytest test_bolted_lap_joint_design.py

📚 Standards Followed
    IS 800:2007 – General Construction in Steel — Code of Practice

Functions implemented from:
    Clause 10.3.3 (Shear Capacity of Bolts)
    Clause 10.3.4 (Bearing Capacity of Bolts)

------------------------------------------------------------------------------------------------------------------------

📜 Author & Fellowship
Developed by Ishaan Shanker Srivastava as part of the FOSSEE Fellowship 2025, under the guidance of the Osdag team.

------------------------------------------------------------------------------------------------------------------------
