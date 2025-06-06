# 🧪 OrangeHRM User Management Test Suite (Playwright - Python)

This project automates the testing of the **User Management workflow** in the **Admin module** of OrangeHRM using **Playwright with Python**.

## ✅ Test Scenarios Covered

- Navigate to Admin Module
- Add a New User
- Search the Newly Created User
- Edit all Possible User Details
- Validate Updated Details
- Delete the User
- Additional validations: Search deleted user, form validations, duplicate entries

---

## 🚀 Project Setup

### 📁 Prerequisites
Ensure the following are installed:

- **Python** ≥ 3.8
- **pip**
- **Playwright for Python version-1.52.0**

---

### ⚙️ Installation Steps

```bash
# 1. Clone the repository or download the folder
git clone https://github.com/your-repo/orangehrm-user-tests.git
cd orangehrm-user-tests

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install
