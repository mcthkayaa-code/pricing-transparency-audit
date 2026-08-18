SOURCE EVIDENCE FILE (Krea official documentation, Mintlify docs site)
URL: https://www.krea.ai/docs/user-guide/help-and-support/refunds-and-billing
Accessed: 2026-08-09
Method: curl static fetch of the page's clean-markdown variant (Mintlify serves a .md version of every docs page at the same path + .md; content matches the rendered page), User-Agent=Chrome/124, Accept-Language: en-US,en;q=0.9
Archive: https://web.archive.org/web/20260809180348/https://www.krea.ai/docs/user-guide/help-and-support/refunds-and-billing

> ## Documentation Index
> Fetch the complete documentation index at: https://www.krea.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Refunds and Billing

> Find clear answers about refunds, invoices, failed payments, and billing timelines so you can resolve Krea subscription issues quickly.

## Requesting a Refund

### Eligibility Requirements

To be eligible for a refund, you must meet the following criteria:

* **Active subscription**: You must have an active paid subscription
* **Usage limit**: To be eligible for a refund, workspace usage must be below 650 compute units and must have less than 20 generations for the current month.
* **Timing**: Refund requests are typically processed for recent charges

### How to Request a Refund

1. **Open the Stripe Customer Portal**

* Log in to your [Krea.ai](https://Krea.ai) account
* Go to the [Billing](https://www.krea.ai/settings/billing) page
* Click the "Manage Subscription" button to open the Stripe customer portal

2. **Cancel and Receive Your Refund**

* When you cancel your subscription in the Stripe portal, our system will automatically check your workspace for refund eligibility based on the criteria listed above.
* If you are eligible, you will be automatically offered a refund during the cancellation flow — no extra steps needed.

### Refund Processing Time

* You will receive an email confirmation shortly after requesting a refund
* Refunds typically take 5-10 business days to appear in your account
* The exact timing depends on your payment provider and bank

## Common Billing Issues

### Failed Payment Attempts

If you're experiencing failed payment attempts:

1. **Check Card Details**

* Verify your card information is correct
* Ensure your card hasn't expired
* Check that you have sufficient funds

2. **Contact Your Bank**

* Some banks may block international transactions
* Verify that online/recurring payments are enabled

3. **Try Alternative Payment Method**

* If issues persist, try using a different card
* Consider using an alternative payment method
  * We support Credit/Debit Cards, Google Pay, US Bank Accounts, Amazon Pay and Cash App Pay

### Duplicate or Unexpected Charges

If you see duplicate charges:

1. **Check Your Subscription Status**

* Visit your [Billing](https://www.krea.ai/settings/billing) page to view your billing and subscription details
* Verify you don't have multiple active subscriptions
  * This could be due to having a team plan and a personal plan

2. **Review Recent Transactions**

* Sometimes pending charges may appear as duplicates
* Wait 24-48 hours for transactions to settle

3. **Make sure your past payments went through**

* Sometimes payments for past months fail so we attempt to charge your card multiple times
* Monthly plans charge every month, and if a payment fails the month before, that invoice stays outstanding until it's paid
* If you get charged twice in a month, your payments might've been overdue from prior months

### Auto-Renewal Information

**Important**: All paid subscriptions are set to **auto-renew by default**.

* Subscriptions renew on the same date each month
* You will be charged the subscription amount automatically
* To prevent auto-renewal, you must manually cancel your subscription

***

## Frequently Asked Questions

### Q: I accidentally subscribed to an annual plan when I only wanted a monthly plan

You can switch from an annual plan to a monthly one. The change is scheduled and will take effect at the end of your current annual billing period. To switch, go to the [Pricing page](https://krea.ai/pricing), make sure the monthly toggle is selected, and choose your desired plan.

<img src="https://mintcdn.com/krea/SiD9ytqYemIrqCv7/images/plans-ss.png?fit=max&auto=format&n=SiD9ytqYemIrqCv7&q=85&s=fec3ce7d03e0a458be98d878449a3a64" alt="plans-ss.png" width="3130" height="1550" data-path="images/plans-ss.png" />

### I was charged but can't access premium features

1. Log out and log back in to refresh your account status
2. Clear your browser cache
3. Ensure you're using the same email address associated with your subscription
4. Sometimes it may take 12-24 hours for your account status change to be reflected in our systems. If it takes longer, reach out to [help@krea.ai](mailto:help@krea.ai).

### Why was my payment unsuccessful?

Common reasons include:

* Insufficient funds
* Expired card
* Bank blocking international transactions
* Incorrect card information

### How do I update my payment method?

1. Go to your Account Details page
2. Navigate to the Billing section
3. Click "Update Payment Method"
4. Enter your new payment information

### Q: How do I add a VAT number/Tax ID for invoicing?

**A:**

1. Go to your [Account Settings](https://krea.ai/settings) page
2. Navigate to Stripe by clicking "Update Subscription" or any alternate method
3. Once in Stripe, scroll until you see Billing Information, then click "Update Information"

<img src="https://mintcdn.com/krea/SiD9ytqYemIrqCv7/images/stripe-billing-info.png?fit=max&auto=format&n=SiD9ytqYemIrqCv7&q=85&s=087ba0c2bae9f9c94caf4c92719766d6" alt="stripe-billing-info.png" width="2040" height="566" data-path="images/stripe-billing-info.png" />

4. From there, scroll until you see "Tax ID", then you should be able to add whatever you need

<img src="https://mintcdn.com/krea/SiD9ytqYemIrqCv7/images/tax-id.png?fit=max&auto=format&n=SiD9ytqYemIrqCv7&q=85&s=184d9c9b98311e12efa89bf2cb54e0c9" alt="tax-id.png" width="822" height="694" data-path="images/tax-id.png" />
