# ComfyUI WAN Sliding Window
![Tested ENV](https://img.shields.io/badge/Tested%20ENV:-lightgrey)
![Python 3.12.x](https://img.shields.io/badge/Python-3.12.x-76B900) 
![NVIDIA RTX Driver Release 580](https://img.shields.io/badge/RTX%20Driver-R580%20U1%20(580.88)-76B900)
![Pytorch Ver 2.9.0.dev20250807+cu129](https://img.shields.io/badge/Pytorch-2.9.0.dev+cu129-76B900)
![Cuda Ver 12.9](https://img.shields.io/badge/Cuda-12.9-76B900)
![Platform Windows](https://img.shields.io/badge/Platform-Windows-76B900)

# WIP

This set of nodes provides a powerful sliding window or "tiling" technique for processing long WAN videos and animations in ComfyUI. It allows you to break the job into smaller, overlapping chunks and seamlessly blending them back together. 

Created these for my own experiments, and I'm sharing them so you can play with them and build amazing things too!

## 🛠️ Installation

Follow these simple steps to get the node up and running in your ComfyUI environment.

### Step 1. Clone the Repository

First, you need to clone this repository into your `ComfyUI/custom_nodes/` directory.

Open your terminal or command prompt and navigate to your ComfyUI installation folder.

**For a standard PC installation:**
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/PixWizardry/ComfyUI_Sliding_Window
```

### Step 2: Restart ComfyUI

After the repository has been successfully cloned, make sure to restart ComfyUI. This will allow it to recognize and load the new custom node.

---

### ✨ Available Nodes

Here is a breakdown of the nodes included in this package and what they do.

#### **Sliding Window Options**
This is the starting point for setting up your sliding window. It defines the "schedule" for how the sampler will process your animation in chunks.

*   **What it does:** Takes your full latent and creates a plan for processing it in smaller, overlapping segments.
*   **Key Inputs:**
    *   `latent_image`: The entire latent sequence you want to process.
    *   `context_length`: The number of frames in each processing window. Think of this as the size of each chunk.
    *   `context_overlap`: The number of frames that overlap between consecutive windows. This is crucial for creating a smooth blend.
    *   `fuse_method`: The shape of the blending window for the overlapping frames. Different methods provide different blending smoothness:
        *   `linear`: A standard, trapezoidal cross-fade.
        *   `pyramid`: A triangular blend, often smoother than linear.
        *   `gaussian`: A very soft, gradual blend shaped like a bell curve.
        *   `cubic`: A smooth "S-curve" blend.
        *   `None`: No Smoothing, Recommended

#### **KSampler (Sliding Window)**
This is the main workhorse and has two modes of operation, giving you flexibility in your workflows.

*   **What it does:** It process an animation chunk-by-chunk using the Sliding Window Options.
*   **Operating Modes:**
    *   **1. Sliding Window Mode (with `latent_schedule`):** This is the advanced mode. Connect the `Sliding Window Options` node here. The sampler will iteratively work through each window, denoise it, and/or blend it with the others according to your settings.
    *   **2. Legacy Mode (with `latent_image_optional`):** If you connect a latent directly to this input, the node will behave just like the standard ComfyUI KSampler (Advanced), processing the entire latent at once. This is useful for shorter animations or for when you don't need the sliding window functionality.

#### **Calculate Context & Limits**
This is a handy utility node designed to prevent errors and make setup easier.

*   **What it does:** It helps you calculate the correct number of latent frames based on your desired final video length and ensures your context length settings are valid.
*   **Key Inputs & Outputs:**
    *   **Inputs:**
        *   `pixel_frames`: The total number of frames in your final video.
        *   `context_length_cap`: The maximum context length your model can handle (e.g., its native training size).
        *   `rifle_length_cap`: A specific cap for architectural limits of other nodes you might be using, like a RoPE patcher.
    *   **Outputs:**
        *   `total_latent_frames`: The correct number of latent frames that corresponds to your pixel frames.
        *   `capped_context_length`: A "safe" context length to use in the `PrepareLatentSchedule` node, ensuring it doesn't exceed the total number of frames available.
        *   `capped_rifle_rope_length`: A "safe" value to use for other specialized nodes, preventing potential errors.


Licensed under the GNU Affero General Public License v3.0
