SOURCE EVIDENCE FILE (Krea official documentation, Mintlify docs site)
URL: https://www.krea.ai/docs/user-guide/features/model-overview
Accessed: 2026-08-09
Method: curl static fetch of the page's clean-markdown variant (Mintlify serves a .md version of every docs page at the same path + .md; content matches the rendered page), User-Agent=Chrome/124, Accept-Language: en-US,en;q=0.9
Archive: https://web.archive.org/web/20260809180406/https://www.krea.ai/docs/user-guide/features/model-overview

> ## Documentation Index
> Fetch the complete documentation index at: https://www.krea.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Overview

> Compare every Krea image and video model by speed, quality tier, credit cost, and best use case so you can pick the right one for each creative job.

<Tip>
  The table below gives you a full tour of every image generation model available on Krea, organized into four categories: Fast Models, Intelligent Models, Quality Models, and Legacy Models.

  Each entry tells you what the model does, what kinds of tasks it handles well, how it scores on speed (rated out of 3), and roughly how many credits you'll spend per generation.

  Think of it as your cheat sheet for picking the right tool for the job, whether you're rapidly sketching out concepts on a tight credit budget or chasing the highest possible quality for a final deliverable.
</Tip>

# Fast Models

| Model                                             | Description                                                                                                                                                      | Best For                                           | Speed | Credits |
| :------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- | :---- | :------ |
| [Krea 1](/docs/user-guide/features/krea-1)             | Most creative model with LoRAs. Excels at artistic photorealism. Realistic textures.                                                                             | Artistic photorealism, <br />LoRA styles           | 3/3   | 6       |
| [Krea 2 Turbo](/docs/user-guide/features/krea-2-turbo) | Fastest Krea 2 model, optimized for rapid prompt and style iteration.                                                                                            | Expressive illustration, <br />quick Krea 2 drafts | 3/3   | 2       |
| Flux 2 Klein                                      | A lightweight 4 billion parameter version of Flux 2, optimized for speed while maintaining quality. Supports up to 2K resolution.                                |                                                    |       |         |
| [Qwen 2512](/docs/user-guide/features/qwen2512)        | Latest Qwen model with enhanced human realism, finer natural detail for landscapes and textures, and improved text rendering with better layout and composition. | Human portraits, landscapes, <br />text rendering  | 2/3   | 9       |
| [Flux](/docs/user-guide/features/flux)                 | Best model for LoRAs. Fastest model. Highly customizable, less realistic colors and textures.                                                                    | LoRA customization, <br />fast iteration           | 3/3   | 5       |
| [Z Image](/docs/user-guide/features/z-image)           | Cheapest model. Medium quality photorealism at a budget. Realistic textures.                                                                                     | Budget photorealism, <br />quick drafts            | 3/3   | 3       |

# Intelligent Models

| Model                                                   | Description                                                                                                                                  | Best For                                | Speed | Credits |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- | :---- | :------ |
| [Nano Banana](/docs/user-guide/features/nano-banana)         | Smart model optimized for precise prompt adherence. Best for most tasks.                                                                     | General use, precise prompt following   | 3/3   | \~30    |
| [Nano Banana Pro](/docs/user-guide/features/nano-banana-pro) | Smartest model. World's best prompt adherence. Best model for complex tasks and image editing.                                               | Complex tasks, image editing            | 2/3   | \~100   |
| [Nano Banana 2](/docs/user-guide/features/nano-banana-2)     | Google's latest flash image model (also known as Gemini 3.1 Flash Image) optimized for fast generation with support for up to 4K resolution. | Fast high-res generation, 4K output     | 2/3   | \~50    |
| [Seedream 5 Lite](/docs/user-guide/features/seedream-5-lite) | Latest high-quality model from ByteDance with deep thinking, web search capabilities, and up to 14 style images.                             | Deep thinking, multi-style generation   | 2/3   | \~30    |
| [ChatGPT 1.5](/docs/user-guide/features/chat-gpt-1-5)        | Smartest model. Excellent prompt following. Best for complex diagrams, characters, and image editing.                                        | Complex diagrams, characters, editing   | 1/3   | \~150   |
| ChatGPT Image                                           | Older ChatGPT image model. Intelligent prompt adherence with sharp semi-realistic output.                                                    | Semi-realistic output, prompt adherence | 1/3   | \~200   |

# Quality Models

| Model        | Description                                                                                                                  | Best For                               | Speed | Credits |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------- | :---- | :------ |
| Recraft V4   | Sharp, detailed images from Recraft with Standard and Pro modes.                                                             | Sharp detail, graphic design           | 2/3   | \~30    |
| Seedream 4   | Latest high-quality model from ByteDance with flexible resolution support.                                                   | Flexible resolution, quality output    | 2/3   | 25      |
| Seedream 4.5 | Quality 4K model optimized for vibrant photorealism.                                                                         | Vibrant photorealism, 4K               | 2/3   | \~30    |
| Flux 2       | FLUX.2 \[dev] from Black Forest Labs. Enhanced realism and crisper text generation.                                          | Realism, text generation               | 3/3   | 20      |
| Flux 2 Pro   | Medium quality model by Black Forest with stable visuals.                                                                    | Stable, consistent visuals             | 2/3   | \~60    |
| Flux 2 Flex  | BFL's next generation model, excelling at rendering text and fine details.                                                   | Text rendering, fine detail            | 2/3   | \~200   |
| Flux 2 Max   | Frontier model by Black Forest Labs. Most capable Flux 2 model.                                                              | Highest quality Flux output            | 2/3   | \~400   |
| Wan 2.2      | Cinematic outputs with crisp textures and realistic color palette, but weak diversity and structure.                         | Cinematic, crisp textures              | 1/3   | \~30    |
| Qwen         | Semi-realistic model with great text generation and prompt adherence. Capable of following long and highly detailed prompts. | Long detailed prompts, text generation | 2/3   | 9       |
| Kling O1     | Kling Omni image model with support for up to 10 reference images with tags.                                                 | Multi-reference image generation       | 2/3   | 20      |

<TryInKrea href="https://www.krea.ai/models" title="Browse all AI models in Krea" description="Every image and video model available in Krea, in one place." />

<a href="https://www.krea.ai/models" className="not-prose group my-6 flex items-center justify-between gap-4 rounded-xl border border-gray-200 dark:border-gray-800 px-5 py-4 no-underline transition-colors hover:border-gray-300 dark:hover:border-gray-700">
  <div>
    <div className="font-semibold text-gray-900 dark:text-gray-100">Browse all AI models in Krea</div>
    <div className="mt-0.5 text-sm text-gray-500 dark:text-gray-400">Every image and video model available in Krea, in one place.</div>
  </div>

  <span aria-hidden="true" className="text-gray-400 transition-transform group-hover:translate-x-0.5 dark:text-gray-500">→</span>
</a>

## 4. Legacy Models

| Model              | Description                                                                                              | Best For                                | Speed | Credits |
| :----------------- | :------------------------------------------------------------------------------------------------------- | :-------------------------------------- | :---- | :------ |
| Flux Kontext       | Frontier model designed for image editing. Capable of advanced reasoning and style transfer.             | Image editing, style transfer           | 3/3   | 9       |
| Flux Kontext Pro   | Frontier model designed for image editing. Capable of advanced reasoning and style transfer.             | Advanced image editing, style transfer  | 2/3   | \~30    |
| Imagen 4 Ultra     | Google's best image model. Excellent prompt adherence. Capable of producing a wide range of subjects.    | Wide subject range, high quality        | 2/3   | \~45    |
| Imagen 4 Fast      | Google's fastest image model. Excellent prompt adherence. Capable of producing a wide range of subjects. | Fast Google-quality output              | 2/3   | 15      |
| Imagen 4           | Google's best image model. Excellent prompt adherence. Capable of producing a wide range of subjects.    | General high-quality generation         | 1/3   | \~30    |
| Runway Gen-4       | Cinematic image model with references. Best at combining multiple characters into a single image.        | Multi-character scenes, cinematic style | 1/3   | \~40    |
| Ideogram 3.0       | Highly aesthetic, general-purpose model. Excels at flat and graphic styles.                              | Flat design, graphic styles             | 2/3   | \~55    |
| Flux 1.1 Pro       | Advanced yet efficient model from Black Forest Labs.                                                     | Efficient advanced generation           | 2/3   | \~30    |
| Flux 1.1 Pro Ultra | Black Forest Lab's highest quality text to image model.                                                  | Highest quality BFL output              | 2/3   | \~45    |
| Imagen 3           | Google's previous generation image model.                                                                | Legacy Google generation                | 1/3   | \~30    |
| Flux.1 Krea        | Distilled and open sourced version of Krea 1. Better at text rendering and anatomy.                      | Text rendering, anatomy, open source    | 3/3   | 5       |
