# Week 1 Task – Django REST Framework Core Concepts

**Internship**: Perpex – Django Full Stack Internship  
**Week**: 1  
**Developer**: Uggina Tejaswini  
**Topic**: Authentication, Authorization, and HTTP Response Codes in DRF

---

# Description : 

This repository contains detailed notes and examples based on my Week 1 learning task for the Django REST Framework (DRF) module. The focus is on understanding and applying:

- 🔐 Authentication (Who are you?)
- ✅ Authorization (Are you allowed?)
- 📤 HTTP Response Status Codes
- ⚙️ Core REST API Principles

This serves as a foundation for building secure, scalable RESTful APIs using Django and DRF.

---

 1.Authentication in DRF

**Authentication** is the process of identifying the user before allowing access to protected resources.

 Types of Authentication:

 1. SessionAuthentication : Cookie-based auth for browser sessions  
 2. BasicAuthentication   : Base64-encoded username:password          
 3. TokenAuthentication   : Token passed in headers (`Authorization`) 
 4. JWTAuthentication     : Stateless, secure token-based auth        
 5. CustomAuthentication  : Developer-defined logic for custom needs  

2. Authorization
   Authorization controls what an authenticated user is allowed to do.

      DRF uses permission classes such as:
      
      * AllowAny
      
      * IsAuthenticated
      
      * IsAdminUser
      
      * IsAuthenticatedOrReadOnly
      
      * Custom permissions (e.g., IsOwnerOrReadOnly)
3.  REST API principles:

   1. Resource-Based Architecture
    
   2.Use of Standard HTTP Methods
    
   3.Stateless Communication
    
   4.Uniform Interface
    
   5.Representations (JSON/XML)
    
   6. Content Negotiation
    
   7. Client-Server Separation
    
   8. Layered System

