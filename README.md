# VeriVue - AI-Powered Video Fact-Checker

## **Project Overview**
VeriVue is an AI-powered application designed to fact-check videos in real-time and provide summaries of false claims. It also integrates a chatbot for further insights and user queries.

---

## **Features**
1. **Fact-Checking System**: Analyzes video content and identifies incorrect claims.
2. **Summary Generation**: Provides a summary of the video.
3. **Chatbot Integration**: Laravel-based chatbot with serverless inference.
4. **Scalable Deployment**: Flask and Laravel apps deployed on Vultr Kubernetes.

---

## **Project Architecture**
### 1. **Flask Backend**:
   - Handles video uploads and fact-checking logic.
   - Exposed on port `5000`.

### 2. **Laravel Frontend**:
   - User interface for video uploads and chatbot.
   - Exposed on port `8000`.

---

## **Deployment Details**
- **Backend External IP**: `http://139.84.132.84:5000`
- **Frontend Web App**: [http://139.84.132.85:8000](http://139.84.132.85:8000)

---

## **How to Use the App**
1. Visit the frontend web app.
2. Upload a video for fact-checking.
3. Use the chatbot for further information.

---

## **Installation (For Local Development)**
### Prerequisites:
- Docker
- Kubernetes
- Python 3.8
- Node.js and NPM (for Laravel)

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/verivue-project.git



