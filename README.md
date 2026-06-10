# Cloud Resume in Azure

CRAz it is another approach of the cloud resume challenge with Azure.

It begins with an implementation on-premises with a framework-free frontend (plain HTML, simple CSS, vanilla JS), evolves into a backend with API on the computer, and ultimately deploys to the cloud, Azure using serverless services, IaC, and CI/CD.

## Tech Stack

|Layer|Name|Description|
|----|-----------|-----|
|Frontend|HTLM, CSS, JS|Resume, UI, visit counter|
|Backend|Python, FastAPI, Uvicorn| API endpoint, visit counter|
|Storage|LocalStorage,SQLite| Visit Tracking|
|Cloud|Azure|Hosting, API server|


## Roadmap
### Phase A : Local implementation
#### Step 1 : Frontend development
- HTML : 
    - build the resumer
    - implement : header, main, footer, aside semantic elements
- CSS  : 
    - design the layout
    - troubleshoot issue on position items in center by using Flexbox Model
- JS   : 
    - capture the visit and display the number of visit
    - troubleshoot issue on saving number of visit by using LocalStorage

#### Step 2 : Backend development
- Python : 
    - set up the web server 
    - build APIs for check GET, POST request
    - build API for counting visit
    - Troubleshoot the CORS Errors | Cross Origin Request Sharing Errors
- Database :
    - set up SQLite database to store visit per user

### Phase B : Cloud implementation

#### Step 3 : Migrate code Entra/Azure cloud 

#### Step 4 : Deployment and Distribution

### Step 5 : Testing

