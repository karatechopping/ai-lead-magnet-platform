# Operational Details for AI Lead Magnet Platform

This document provides detailed information about the operational aspects of the AI Lead Magnet Platform, including business model, hosting requirements, front-end access, and integration capabilities.

## Table of Contents
1. [Platform Architecture Overview](#platform-architecture-overview)
2. [Business Owner Experience](#business-owner-experience)
3. [Lead Capture and Data Management](#lead-capture-and-data-management)
4. [Hosting and Infrastructure](#hosting-and-infrastructure)
5. [Front-End Access](#front-end-access)
6. [Payment Processing](#payment-processing)
7. [Implementation Checklist](#implementation-checklist)

## Platform Architecture Overview

The AI Lead Magnet Platform operates as a multi-tenant SaaS application:

```
                                 ┌─────────────────┐
                                 │                 │
                                 │  Your Platform  │
                                 │                 │
                                 └────────┬────────┘
                                          │
                                          ▼
                 ┌───────────────────────────────────────────┐
                 │                                           │
                 │           Platform Server                 │
                 │                                           │
┌────────────────┴───────────┐   ┌───────────────┴──────────┐
│                            │   │                          │
│  Business Owner Interface  │   │  Admin Dashboard         │
│                            │   │                          │
└────────────┬───────────────┘   └──────────────┬───────────┘
             │                                  │
             ▼                                  ▼
┌────────────────────────┐        ┌───────────────────────┐
│                        │        │                       │
│  Lead Magnet Creation  │        │  Analytics & Billing  │
│                        │        │                       │
└────────────┬───────────┘        └───────────┬───────────┘
             │                                │
             └──────────────┬────────────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │                   │
                  │  Database & APIs  │
                  │                   │
                  └─────────┬─────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                 Business Websites                       │
│                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ Business A  │    │ Business B  │    │ Business C  │  │
│  │ Website     │    │ Website     │    │ Website     │  │
│  │             │    │             │    │             │  │
│  │ [Embed      │    │ [Embed      │    │ [Embed      │  │
│  │  Script]    │    │  Script]    │    │  Script]    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Business Owner Experience

### Registration and Onboarding
1. Business owners visit your platform website
2. They create an account (email/password or OAuth)
3. They complete a brief onboarding process
4. They're directed to the lead magnet creation process

### Lead Magnet Creation Process
1. The business owner engages with the conversational assessment
2. The system recommends appropriate lead magnet types
3. The owner selects and customizes their lead magnet
4. The system builds the lead magnet
5. The owner reviews and approves the lead magnet

### Embedding Process
1. After approval, the system generates a unique JavaScript snippet
2. The snippet is displayed in the interface and emailed to the owner
3. The owner can access it anytime from their dashboard
4. The owner (or their developer) adds the snippet to their website

Example snippet:
```html
<!-- AI Lead Magnet by YourPlatform -->
<script src="https://yourdomain.com/embed/business_id/lead_magnet_id.js"></script>
<button class="ai-lead-magnet-trigger" data-magnet-id="lead_magnet_id">
  Take Our Quiz
</button>
```

### Dashboard Access
Business owners can log in to their dashboard to:
1. View lead magnet performance
2. Access leads captured
3. Modify lead magnet settings
4. Create additional lead magnets
5. Manage billing and subscription

## Lead Capture and Data Management

### Data Collection
All lead magnets include lead capture functionality:
1. Contact information (name, email, phone)
2. Custom fields based on business needs
3. Quiz/assessment responses
4. Interaction data

### Data Storage
1. All data is stored in your MongoDB database
2. Organized by business tenant
3. Encrypted at rest
4. Compliant with data protection regulations

### CRM Integration Options
The platform supports these integration methods:

1. **Direct API Integration** (Phase 2)
   - HubSpot
   - Salesforce
   - Mailchimp
   - ActiveCampaign
   - Others via custom integration

2. **Webhook Support** (Phase 2)
   - Real-time data pushing to any system
   - Customizable data mapping

3. **Manual Export** (Phase 1)
   - CSV export
   - JSON export
   - Excel export

### Email Notification
1. Business owners receive email notifications for new leads
2. Customizable notification settings
3. Daily/weekly summary options

## Hosting and Infrastructure

### Server Requirements
For initial deployment (Phase 1):
- Hetzner CX11 VPS ($7/month)
- 2GB RAM
- 20GB SSD
- 1 vCPU
- Ubuntu 22.04

For scaling (Phase 2+):
- Hetzner CX21/CX31 ($15-30/month)
- 4-8GB RAM
- 40-80GB SSD
- 2-4 vCPUs

### Resource Allocation
All resources are shared across tenants:
1. Each business's lead magnets run on your server
2. AI processing uses your OpenAI API key
3. Database storage uses your MongoDB instance
4. All costs are borne by you (the platform owner)

### Scaling Considerations
As your user base grows:
1. Implement caching for common AI responses
2. Use a CDN for static assets
3. Consider horizontal scaling with load balancing
4. Implement database sharding for larger datasets

## Front-End Access

### Domain Setup
1. Purchase a domain for your platform (e.g., aileadmagnet.com)
2. Configure DNS records to point to your server IP
3. Set up SSL certificates using Let's Encrypt (included in deployment instructions)

### Access Points
After deployment, these are the main access points:

1. **Your Admin Dashboard**:
   - URL: `https://yourdomain.com/admin`
   - Alternative: `http://your-server-ip/admin`
   - Login with your admin credentials
   - Manage all aspects of the platform

2. **Business Owner Portal**:
   - URL: `https://yourdomain.com`
   - Business owners register and log in here
   - They create and manage their lead magnets

3. **API Endpoints**:
   - Base URL: `https://yourdomain.com/api`
   - Used by the JavaScript embeds
   - Secured with API keys

### SSL Configuration
The deployment instructions include setting up SSL with Let's Encrypt:
```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## Payment Processing

### Integration Options
The current design doesn't include payment processing, but here are recommended options to implement:

1. **Stripe Integration**:
   - Easy to implement
   - Supports subscriptions and one-time payments
   - Handles international payments
   - Reasonable fees (2.9% + $0.30 per transaction)

2. **PayPal Integration**:
   - Widely recognized
   - Good for international businesses
   - Higher fees for some transaction types

### Subscription Models
Recommended pricing structures:

1. **Tiered Subscription**:
   - Basic: $29/month (1 lead magnet, basic features)
   - Professional: $79/month (3 lead magnets, all features)
   - Agency: $199/month (10 lead magnets, white labeling)

2. **Usage-Based Pricing**:
   - Base fee: $19/month
   - Per lead captured: $0.50-1.00
   - Cap options to prevent surprise bills

### Implementation Priority
Payment processing should be implemented:
- Before public launch
- After core functionality is stable
- With thorough testing of the billing cycle

## Implementation Checklist

Use this checklist to ensure all operational aspects are addressed:

### Initial Setup
- [ ] Purchase domain name
- [ ] Set up Hetzner VPS
- [ ] Deploy application using deployment instructions
- [ ] Configure SSL certificates
- [ ] Set up admin account

### Business Owner Experience
- [ ] Test registration process
- [ ] Verify lead magnet creation workflow
- [ ] Test embedding process on sample websites
- [ ] Verify dashboard functionality

### Lead Capture
- [ ] Test lead capture forms
- [ ] Verify data storage in database
- [ ] Test export functionality
- [ ] Implement basic email notifications

### Front-End
- [ ] Verify all access points work correctly
- [ ] Test responsive design on mobile devices
- [ ] Ensure proper error handling
- [ ] Implement basic analytics

### Future Enhancements
- [ ] Integrate payment processing
- [ ] Implement CRM integrations
- [ ] Add advanced analytics
- [ ] Develop white-labeling options

This checklist will help ensure all operational aspects are properly implemented before launching the platform.
