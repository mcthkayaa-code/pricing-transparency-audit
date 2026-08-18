SOURCE EVIDENCE FILE (Krea official documentation, Mintlify docs site)
URL: https://www.krea.ai/docs/developers/job-lifecycle
Accessed: 2026-08-09
Method: curl static fetch of the page's clean-markdown variant (Mintlify serves a .md version of every docs page at the same path + .md; content matches the rendered page), User-Agent=Chrome/124, Accept-Language: en-US,en;q=0.9
Archive: https://web.archive.org/web/20260809180525/https://www.krea.ai/docs/developers/job-lifecycle

> ## Documentation Index
> Fetch the complete documentation index at: https://www.krea.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Job Lifecycle

> Understand each Krea job state from creation to completion, including polling patterns, retries, and practical error-handling strategies.

## Overview

All generation requests follow the same basic lifecycle:

<img className="w-full mx-auto dark:hidden" src="https://mintcdn.com/krea/ZLw3hmlHm50-cthl/images/job-status.svg?fit=max&auto=format&n=ZLw3hmlHm50-cthl&q=85&s=6cbb1b15fcde8ed4c7d7d84c2637d5c6" alt="Job lifecycle diagram" width="569" height="239" data-path="images/job-status.svg" />

<img className="w-full mx-auto dark:block hidden" src="https://mintcdn.com/krea/ZLw3hmlHm50-cthl/images/job-status-dark.svg?fit=max&auto=format&n=ZLw3hmlHm50-cthl&q=85&s=cc4c42010e1f9fb4688263f83705e37d" alt="Job lifecycle diagram" width="569" height="239" data-path="images/job-status-dark.svg" />

### Job States

<span className="text-sm font-bold text-blue-900 dark:text-blue-100 font-mono bg-blue-100 dark:bg-blue-900/30 border border-blue-300 dark:border-blue-600 px-1.5 py-0.5 rounded mr-1">queued</span> Job is waiting in the queue to be processed

<span className="text-sm font-bold text-blue-900 dark:text-blue-100 font-mono bg-blue-100 dark:bg-blue-900/30 border border-blue-300 dark:border-blue-600 px-1.5 py-0.5 rounded mr-1">backlogged</span> Job is waiting behind your current concurrency limit

<span className="text-sm font-bold text-blue-900 dark:text-blue-100 font-mono bg-blue-100 dark:bg-blue-900/30 border border-blue-300 dark:border-blue-600 px-1.5 py-0.5 rounded mr-1">scheduled</span> Job has been accepted and scheduled for processing

<span className="text-sm font-bold text-amber-900 dark:text-amber-100 font-mono bg-amber-100 dark:bg-amber-900/30 border border-amber-300 dark:border-amber-600 px-1.5 py-0.5 rounded mr-1">processing</span> Job is actively being processed by a worker

<span className="text-sm font-bold text-amber-900 dark:text-amber-100 font-mono bg-amber-100 dark:bg-amber-900/30 border border-amber-300 dark:border-amber-600 px-1.5 py-0.5 rounded mr-1">sampling</span> Job is generating output samples

<span className="text-sm font-bold text-amber-900 dark:text-amber-100 font-mono bg-amber-100 dark:bg-amber-900/30 border border-amber-300 dark:border-amber-600 px-1.5 py-0.5 rounded mr-1">intermediate-complete</span> Job has an intermediate result and may continue processing

<span className="text-sm font-bold text-green-900 dark:text-green-100 font-mono bg-green-100 dark:bg-green-900/30 border border-green-300 dark:border-green-600 px-1.5 py-0.5 rounded mr-1">completed</span> Job finished successfully, result available in `result.urls`

<span className="text-sm font-bold text-red-900 dark:text-red-100 font-mono bg-red-100 dark:bg-red-900/30 border border-red-300 dark:border-red-600 px-1.5 py-0.5 rounded mr-1">failed</span> Job failed due to an error, details in `result.error`

<span className="text-sm font-bold text-gray-900 dark:text-gray-100 font-mono bg-gray-100 dark:bg-gray-900/30 border border-gray-300 dark:border-gray-600 px-1.5 py-0.5 rounded mr-1">cancelled</span> Job was cancelled by the user or system

### Failures & Cancellation

**Jobs can fail** for several reasons:

* API errors from the generation service
* Invalid parameters or unsupported configurations
* Content moderation (NSFW filtering)
* Automatic timeout detection (3 minutes for hosted tools, 2 hours for external providers)

**To cancel a job:** Send a `DELETE` request to `/jobs/{id}`. Note: Jobs can only be canceled while they have a status of <span className="text-sm font-bold text-blue-900 dark:text-blue-100 font-mono bg-blue-100 dark:bg-blue-900/30 border border-blue-300 dark:border-blue-600 px-1.5 py-0.5 rounded mr-1">queued</span> or <span className="text-sm font-bold text-amber-900 dark:text-amber-100 font-mono bg-amber-100 dark:bg-amber-900/30 border border-amber-300 dark:border-amber-600 px-1.5 py-0.5 rounded mr-1">processing</span>.

<Check>
  **Important:** Failed and cancelled jobs are not billed. You only pay for completed jobs.
</Check>

### Checking Job Status

Poll for job status using a `GET` request to `/jobs/{id}`. Recommended practices:

* Poll every 2-5 seconds while job is pending (`backlogged`, `queued`, `scheduled`, `processing`, `sampling`, or `intermediate-complete`)
* Use exponential backoff for longer-running jobs
* Stop polling when status is <span className="text-sm font-bold text-green-900 dark:text-green-100 font-mono bg-green-100 dark:bg-green-900/30 border border-green-300 dark:border-green-600 px-1.5 py-0.5 rounded mr-1">completed</span>, <span className="text-sm font-bold text-red-900 dark:text-red-100 font-mono bg-red-100 dark:bg-red-900/30 border border-red-300 dark:border-red-600 px-1.5 py-0.5 rounded mr-1">failed</span>, or <span className="text-sm font-bold text-gray-900 dark:text-gray-100 font-mono bg-gray-100 dark:bg-gray-900/30 border border-gray-300 dark:border-gray-600 px-1.5 py-0.5 rounded mr-1">cancelled</span>
* Some jobs may include preview images in responses during <span className="text-sm font-bold text-amber-900 dark:text-amber-100 font-mono bg-amber-100 dark:bg-amber-900/30 border border-amber-300 dark:border-amber-600 px-1.5 py-0.5 rounded mr-1">processing</span>

**Example polling implementation:**

<CodeGroup>
  ```javascript Node.js theme={null}
  // npm install @krea-ai/sdk
  import { Krea } from "@krea-ai/sdk";

  const krea = new Krea({ apiKey: process.env.KREA_API_KEY });

  async function waitForJob(jobId) {
    const job = await krea.jobs.wait(jobId, { intervalMs: 2000 });
    return job.result;
  }
  ```

  ```python Python theme={null}
  import time

  def wait_for_job(job_id):
      while True:
          response = requests.get(
              f"{API_BASE}/jobs/{job_id}",
              headers={"Authorization": f"Bearer {API_TOKEN}"}
          )
          job = response.json()

          if job["status"] == "completed":
              return job["result"]
          if job["status"] in ("failed", "cancelled"):
              raise Exception(f"Job {job['status']}: {job.get('result', {}).get('error')}")

          print(f"Status: {job['status']}")
          time.sleep(2)
  ```
</CodeGroup>

## Next Steps

<CardGroup cols={2}>
  <Card title="Webhooks" icon="bell" href="/docs/developers/webhooks">
    Receive notifications when jobs complete
  </Card>

  <Card title="Rate Limits" icon="gauge" href="/docs/developers/rate-limits">
    Understand API limits by plan tier
  </Card>

  <Card title="Model APIs" icon="book-open" href="/docs/api-reference/image/flux">
    Explore all available endpoints and parameters
  </Card>

  <Card title="API Keys & Billing" icon="key" href="/docs/developers/api-keys-and-billing">
    Create and manage your API keys
  </Card>
</CardGroup>
