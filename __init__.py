from .context_nodes import PrepareLatentSchedule, IterativeSampler, CalculateLatentFrames

NODE_CLASS_MAPPINGS = {
    "PrepareLatentSchedule": PrepareLatentSchedule,
    "IterativeSampler": IterativeSampler,
    "CalculateLatentFrames": CalculateLatentFrames,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PrepareLatentSchedule": "Sliding Window Options",
    "IterativeSampler": "KSampler (Sliding Window)",
    "CalculateLatentFrames": "Calculate Context & Limits",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("---✅ Context Processor Nodes: Loaded")