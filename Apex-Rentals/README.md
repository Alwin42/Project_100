# APEX-RENTALS

A sophisticated car rental platform offering seamless booking experiences with enterprise-grade security and premium vehicle collections.

## ✨ Overview

This premium car rental system delivers a luxury booking experience while maintaining robust security measures to protect both vehicle owners and renters. The platform features passwordless authentication, comprehensive identity verification, and an extensive fleet ranging from vintage classics to modern supercars.

## 🎯 Key Features

### 1. **Email-Based OTP Authentication**
- Passwordless login system for enhanced security and user convenience
- One-Time Password (OTP) delivery via email
- Seamless authentication flow without the hassle of password management
- Secure session management

### 2. **Diverse Vehicle Collection**
- **Vintage Cars**: Classic automobiles for nostalgic experiences
- **Classic Cars**: Timeless vehicles with enduring appeal
- **Modern Cars**: Latest models with cutting-edge technology
- **Luxury Cars**: Premium vehicles for distinguished occasions
- **Sports Cars**: High-performance vehicles for thrill-seekers
- **SUVs & Sedans**: Practical options for various needs

### 3. **Identity Verification System**
- Browse-before-book functionality - users can explore vehicles without registration
- Mandatory admin verification of user IDs before booking privileges are granted
- Multi-step verification process ensuring legitimate renters
- Document upload and validation system
- Real-time verification status tracking

### 4. **Vehicle Owner Security**
- Comprehensive renter background verification
- Admin-approved bookings only
- Secure payment processing
- Damage protection protocols
- Insurance verification requirements
- Rental agreement digital signing

### 5. **Automated Account Management**
- Automatic cleanup of unverified accounts after specified inactive period
- Removal of accounts pending admin approval beyond timeout threshold
- Database optimization through inactive user purging
- Notification system before account deletion
- Maintains system efficiency and data integrity

### 6. **Premium User Experience**
- Luxurious, modern interface design
- High-quality vehicle imagery and 360° views
- Smooth animations and transitions
- Responsive design for all devices
- Intuitive navigation and booking flow
- Dark/light theme options
- Premium typography and color schemes

## 🔐 Security Features

- Email OTP authentication (no password storage vulnerabilities)
- Admin verification gate before booking access
- Encrypted data transmission
- Secure payment gateway integration
- Regular security audits
- GDPR-compliant data handling
- Automated inactive account cleanup

## 🚀 User Journey

1. **Discovery Phase**: Browse vehicles without registration
2. **Registration**: Sign up using email-based OTP
3. **Verification**: Upload identification documents
4. **Admin Review**: Wait for administrator approval
5. **Booking Access**: Receive booking privileges upon approval
6. **Rental**: Book premium vehicles with confidence

## 📋 Account Status Types

- **Guest**: Can browse vehicles only
- **Pending Verification**: Registered but awaiting admin approval
- **Verified**: Full booking access granted
- **Inactive**: Subject to automatic deletion
- **Suspended**: Temporarily restricted access

## ⚙️ Admin Dashboard

- User verification management
- Document review and approval
- Vehicle inventory management
- Booking oversight
- User activity monitoring
- Automated cleanup configuration
- Analytics and reporting

## 🎨 Design Philosophy

The platform embraces a premium aesthetic with:
- Clean, minimalist layouts
- High-resolution imagery
- Sophisticated color palettes
- Smooth micro-interactions
- Professional typography
- Luxury brand positioning

## 🛠️ Technical Stack

- Frontend: Vue.js
- Backend: Python Django framework
- Database: Sqlite3



## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Alwin42/Project_100/tree/main/Apex-Rentals
# Navigate to project directory
cd Apex-Rentals

# Navigate to frontend directory 
cd frontend

# Install dependencies
npm install


# Start the application
npm run dev

# Go back to root directory
cd ..

# Navigate backend 
cd backend


# Activate venv/ virtual environment
python -m venv venv
source venv/bin/activate

# Install Dependencies
pip install Django 

# Run the backend
python manage.py runserver


```


## 📝 Usage

### For Users
1. Visit the platform and browse available vehicles
2. Register using your email address
3. Enter the OTP sent to your email
4. Upload required identification documents
5. Wait for admin verification
6. Once approved, start booking premium vehicles

### For Admins
1. Access admin dashboard
2. Review pending user verifications
3. Approve or reject ID documents
4. Manage vehicle inventory
5. Monitor booking activities
6. Configure automated cleanup settings


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

