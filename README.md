# Requests Walmart Auth Project

For getting started with the [Walmart Affiliate Marketplace (REST) API](https://walmart.io/docs/affiliate/) and the python `requests-walmart-auth` library.


## Requirements

- Python 3.7+
- requests-walmart-auth ~= 1.0.0

## Install

Run `scripts/install`.

This installs a set of known-good dependencies from `requirements.txt.lock`.

## Getting Started

### 0. Create an account

A `walmart.com` account is required to access the developer APIs. A new account can be created here:

[Create Your Walmart Account](https://www.walmart.com/account/signup)

### 1. Login to Walmart.io

Navigate to [https://walmart.io](https://walmart.io) and [login to your account](https://www.walmart.com/account/login?response_type=code&client_id=46aaf693-6f92-4492-9a86-02036be7882a&redirect_uri=https://walmart.io/auth&scope=/identity/user/basic_profile)

### 2. Navigate to Dashboard > Applications

From the top-right corner of the page, click your user profile then click [Dashboard](https://walmart.io/userdashboard)

### 3. Create new Web Application

Click [Create Application](https://walmart.io/form-create-application) to request access to the developer APIs.

The `Application's type` should be `Web Application`.

Fill in the rest of the information, then click `Submit Form`. You will be returned to the Dashboard, and should see your application in the `Applications` list.

### 4. Generate SSH keys

SSH keys are required for authentication. To generate keys, run `scripts/generate-keys`.

The following files are created:

- `secrets/private_key.pem`
- `secrets/public_key.pem`
- `secrets/rsa_key_pair`

### 5. Upload public key

From the [Applications](https://walmart.io/userdashboard/applicationAdmin) tab, locate the application and click `Upload/Update public key`.

`Environment Type` should be `Production`.

Copy-paste the contents of `secrets/public_key.pem` WITHOUT THE HEADER AND FOOTER LINES into the `Public Key` field, then click `Upload Key`.

If the upload is successful, your application is assigned a production `consumer_id` and `key_version`.

### 6. Update consumer_id, key_version

In [__main__.py](__main__.py), edit `CONSUMER_ID` and `KEY_VERSION` to match those of the application.

To test authentication, run `scripts/start`. If authentication fails, the error message from the API server is displayed.

## References

- [walmart.io](https://walmart.io)
- [Walmart Affiliate Marketplace API](https://walmart.io/docs/affiliate/)
