> For the complete documentation index, see [llms.txt](https://guide.plusai.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://guide.plusai.com/other/live-snapshots/free-and-paid-plans.md).

# Free and paid plans

## Snapshot limits

On the free plan, there is a limit of 5 Snapshots per organization. You can upgrade to a paid plan to unlock 25 Snapshots. If you or your team needs more than 25 Snapshots, [contact us](/help/contact-us.md).

#### What Snapshots count toward this limit?

All Snapshots taken in your organization count toward this limit, including Snapshots in Personal and [Team](/other/live-snapshots/drafts-and-team-spaces.md) folders, as well as Snapshots set to manual refresh.

Deleted Snapshots do not count toward this limit.

There are no limits on the number of times you can use Snapshots on Pages or the number of Pages you can create.

#### What happens when my org reaches the limit?

No one in the organization will be able to take new Snapshots.&#x20;

## Snapshot refresh rates

On the free plan, you can set Snapshots to automatically refresh every day or every 6 hours. You can upgrade to a paid plan to unlock hourly or 15 minute refresh rates.&#x20;

Snapshots can always be manually refreshed as often as desired, by anyone in your org.

## Upgrading to a plan

{% hint style="info" %}
Currently, only the owner of the organization can upgrade to a paid plan and manage an existing plan. If you're not the owner, contact them to make the upgrade.
{% endhint %}

The owner of the organization can pay to upgrade to a paid plan at any time from the Settings page in the Plus app.

#### How do I upgrade to a higher tier?

The organization owner can upgrade to a higher tier at any time from the Settings page in the Plus app. Click "Manage plan" to make the change.&#x20;

You'll be immediately billed for the difference between the cost of the two plans, pro-rated based on how many days remain in your billing cycle.

#### **Is there a discount for an annual plan?**

Currently, only monthly billing plans are available.

**What if I need more than the paid plans offer?**

[Contact us](/help/contact-us.md) to tell us about what you need.

## Downgrading and cancelling

{% hint style="info" %}
This also describes what happens if you previously had access to higher Snapshot limits as part of our beta program.
{% endhint %}

When your organization downgrades to a lower tier (or free) plan, you will no longer be able to take new Snapshots beyond the new plan limit. You will also not be able to set any Snapshots to the more frequent refresh rates.&#x20;

#### **How do I cancel a paid plan?**

The organization owner can cancel a paid plan at any time from the Settings page in the Plus app.&#x20;

**What happens to my Snapshots beyond the limit?**

While you won't be able to take new Snapshots, existing Snapshots will remain in your organization.&#x20;

## Need help?

{% content-ref url="/pages/4f9xPe0HHKsSjo1babmp" %}
[Contact us](/help/contact-us.md)
{% endcontent-ref %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://guide.plusai.com/other/live-snapshots/free-and-paid-plans.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
